# 🔥 MediaCrawler_MCP_Server - MCP for MediaCrawler 🕷️
## 🔗 MediaCrawler仓库地址
[https://github.com/NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler)
## 🔧  基于MediaCrawler改进
- **python版本**：所有包版本可用于python 3.13，以支持mcp的使用
- **mysql存储**：如表已经存在，初始化不会覆盖原有数据

✨ 更多设置（config）可见MediaCrawler仓库

## 🧰 可使用的MCP工具

1. **crawl_search(platform: str, store_type: str, keywords: str)** - Start the crawler for the media platform by keywords
2. **crawl_detail(platform: str, store_type: str, video_id: list):** - Start the crawler for the media platform by video ID
3. **crawl_creator(platform: str, store_type: str, creator_id: list)** - Start the crawler for the media platform by creator id.

## 📦 Python包安装
```shell
# 进入项目目录
cd MediaCrawler_MCP_Server

# 使用 uv sync 命令来保证 python 版本和相关依赖包的一致性
uv sync
```

## 🌐 浏览器驱动安装

```shell
# 安装浏览器驱动
uv run playwright install
```

## ⚙️ 设置

设置环境变量:
```shell
MYSQL_DB_HOST=localhost     # Database host
MYSQL_DB_PORT=3306         # Optional: Database port (defaults to 3306 if not specified)
MYSQL_DB_USER=your_username
MYSQL_DB_PWD=your_password
MYSQL_DB_NAME=your_database
CRAWLER_MAX_NOTES_COUNT=20 # number of notes you want to crawl
MAX_CONCURRENCY_NUM=1 # number of concurrent crawlers
ENABLE_GET_COMMENTS=true # crawl the comments or not
```

## 🚀 使用
添加至 `claude_desktop_config.json` or `cline_mcp_settings.json`

```json
"mediacrawler": {
      "disabled": false,
      "timeout": 600,
      "type": "stdio",
      "command": "uv",
      "args": [
        "--directory",
        "path/to/MediaCrawler_MCP_Server",
        "run",
        "main.py"
      ],
      "env": {
        "MYSQL_DB_HOST": "localhost",
        "MYSQL_DB_PORT": "3306",
        "MYSQL_DB_USER": "your_username",
        "MYSQL_DB_NAME": "your_database",
        "MYSQL_DB_PWD": "your_password",
        "CRAWLER_MAX_NOTES_COUNT": "20",
        "MAX_CONCURRENCY_NUM": "1",
        "ENABLE_GET_COMMENTS": "true"
      }
  }
```
## 🌰 例子

1. `帮我爬取b站视频资料，关键词为"钱"，存储模式为mysql。`
2. `帮我爬取b站视频号为BV1d54y1g7db,BV1Sz4y1U77N的视频存储模式为json。`
3. `帮我爬取b站up主视频资料，其id为20813884,存储模式为csv。`