# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：
# 1. 不得用于任何商业用途。
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。
# 3. 不得进行大规模爬取或对平台造成运营干扰。
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。
# 5. 不得用于任何非法或不当的用途。
# 详细许可条款请参阅项目根目录下的LICENSE文件。
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。


import os
from typing import Optional

from mcp.server.fastmcp import FastMCP

import config
import db
from base.base_crawler import AbstractCrawler
from media_platform.bilibili import BilibiliCrawler
from media_platform.douyin import DouYinCrawler
from media_platform.kuaishou import KuaishouCrawler
from media_platform.tieba import TieBaCrawler
from media_platform.weibo import WeiboCrawler
from media_platform.xhs import XiaoHongShuCrawler
from media_platform.zhihu import ZhihuCrawler

mcp = FastMCP("MediaCrawler_MCP_Server")


def set_config(crawler_type: str, platform: str, keywords: str = None, video_id: list = None, creator_id: list = None):
    """
    Set configuration based on crawler type and platform
    """
    
    # Get system settings from environment variables
    crawler_max_notes_count = int(os.getenv("CRAWLER_MAX_NOTES_COUNT", "20"))
    max_concurrency_num = int(os.getenv("MAX_CONCURRENCY_NUM", "4"))
    enable_get_comments = os.getenv("ENABLE_GET_COMMENTS", "True").lower() == "true"
    mysql_db_pwd = os.getenv("MYSQL_DB_PWD", "1234567")
    mysql_db_user = os.getenv("MYSQL_DB_USER", "localhost")
    mysql_db_host = os.getenv("MYSQL_DB_HOST", "127.0.0.1")
    mysql_db_port = int(os.getenv("MYSQL_DB_PORT", 3306))
    mysql_db_name = os.getenv("MYSQL_DB_NAME", "Test")

    # Set common system configurations
    config.CRAWLER_MAX_NOTES_COUNT = crawler_max_notes_count
    config.MAX_CONCURRENCY_NUM = max_concurrency_num
    config.ENABLE_GET_COMMENTS = enable_get_comments
    config.MYSQL_DB_PWD = mysql_db_pwd
    config.MYSQL_DB_USER = mysql_db_user
    config.MYSQL_DB_HOST = mysql_db_host
    config.MYSQL_DB_PORT = mysql_db_port
    config.MYSQL_DB_NAME = mysql_db_name
    

    # Set platform-specific configurations based on crawler type
    if crawler_type == "search":
        # Search mode only needs keywords
        config.KEYWORDS = keywords
            
    elif crawler_type == "detail":
        # Detail mode needs video_id for specific platform
        if platform == "xhs":
            config.XHS_SPECIFIED_NOTE_URL_LIST = video_id
        elif platform == "dy":
            config.DY_SPECIFIED_ID_LIST= video_id
        elif platform == "ks":
            config.KS_SPECIFIED_ID_LIST = video_id
        elif platform == "bili":
            config.BILI_SPECIFIED_ID_LIST = video_id
        elif platform == "wb":
            config.WEIBO_SPECIFIED_ID_LIST = video_id
            
    elif crawler_type == "creator":
        # Creator mode needs creator_id for specific platform
        if platform == "xhs":
            config.XHS_CREATOR_ID_LIST = creator_id
        elif platform == "dy":
            config.DY_CREATOR_ID_LIST = creator_id
        elif platform == "ks":
            config.KS_CREATOR_ID_LIST = creator_id
        elif platform == "bili":
            config.BILI_CREATOR_ID_LIST = creator_id
        elif platform == "wb":
            config.WEIBO_CREATOR_ID_LIST = creator_id

class CrawlerFactory:
    CRAWLERS = {
        "xhs": XiaoHongShuCrawler,
        "dy": DouYinCrawler,
        "ks": KuaishouCrawler,
        "bili": BilibiliCrawler,
        "wb": WeiboCrawler,
        "tieba": TieBaCrawler,
        "zhihu": ZhihuCrawler,
    }

    @staticmethod
    def create_crawler(platform: str) -> AbstractCrawler:
        crawler_class = CrawlerFactory.CRAWLERS.get(platform)
        if not crawler_class:
            raise ValueError(
                "Invalid Media Platform Currently only supported xhs or dy or ks or bili ..."
            )
        return crawler_class()


crawler: Optional[AbstractCrawler] = None

@mcp.tool()
async def crawl_search(platform: str = config.PLATFORM, store_type: str = config.SAVE_DATA_OPTION, keywords: str = config.KEYWORDS) -> str:
    """Start the crawler for the media platform by keywords.
    
        args:
            platform (str): The media platform to crawl. You can choose from 'xhs', 'dy', 'ks', 'bili', 'wb', 'tieba', 'zhihu'.
            store_type (str): The storage type for data. You can choose from 'db', 'sqlite', 'json', 'csv'.
            keywords (str): The keywords to search for. This is only used in search mode.
    """
    global crawler
    config.PLATFORM = platform
    config.SAVE_DATA_OPTION = store_type
    config.KEYWORDS = keywords
    
    set_config(crawler_type="search", platform=platform, keywords=keywords)

    if store_type in ["db", "sqlite"]:          
        try:
            await db.init_db_table(store_type=store_type)
            await db.init_db()
        except Exception as e:
            return f"Error occurred: Database connection failed: {e}, Please check your database configuration or use another storage type."

    try:
        crawler = CrawlerFactory.create_crawler(platform=platform)
        await crawler.start()
        return "success to crawl"
    except Exception as e:
        return f"Error occurred: {e}"

@mcp.tool()
async def crawl_detail(platform: str = config.PLATFORM, store_type: str = config.SAVE_DATA_OPTION, video_id: list = []) -> str:
    """Start the crawler for the media platform by video ID.

        args:
            platform (str): The media platform to crawl. You can choose from 'xhs', 'dy', 'ks', 'bili', 'wb', 'tieba', 'zhihu'.
            store_type (str): The storage type for data. You can choose from 'db', 'sqlite', 'json', 'csv'.
            video_id (list): The video ID or URL to crawl details for.
    """
    global crawler
    config.PLATFORM = platform
    config.SAVE_DATA_OPTION = store_type
    
    set_config(crawler_type="detail", platform=platform, video_id=video_id)

    if store_type in ["db", "sqlite"]:          
        try:
            await db.init_db_table(store_type=store_type)
            await db.init_db()
        except Exception as e:
            return f"Error occurred: Database connection failed: {e}, Please check your database configuration or use another storage type."

    try:
        crawler = CrawlerFactory.create_crawler(platform=platform)
        await crawler.start()
        return "success to crawl"
    except Exception as e:
        return f"Error occurred: {e}"

@mcp.tool()
async def crawl_creator(platform: str = config.PLATFORM, store_type: str = config.SAVE_DATA_OPTION, creator_id: list = []) -> str:
    """Start the crawler for the media platform by creator id.
    
        args:
            platform (str): The media platform to crawl. You can choose from 'xhs', 'dy', 'ks', 'bili', 'wb', 'tieba', 'zhihu'.
            store_type (str): The storage type for data. You can choose from 'db', 'sqlite', 'json', 'csv'.
            creator_id (list): The creator ID to crawl.
    """
    global crawler
    config.PLATFORM = platform
    config.SAVE_DATA_OPTION = store_type
    
    set_config(crawler_type="creator", platform=platform, creator_id=creator_id)

    if store_type in ["db", "sqlite"]:          
        try:
            await db.init_db_table(store_type=store_type)
            await db.init_db()
        except Exception as e:
            return f"Error occurred: Database connection failed: {e}, Please check your database configuration or use another storage type."

    try:
        crawler = CrawlerFactory.create_crawler(platform=platform)
        await crawler.start()
        return "success to crawl"
    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == "__main__":
    mcp.run(transport='stdio')

