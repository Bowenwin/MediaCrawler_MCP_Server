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
MYSQL_HOST=localhost     # Database host
MYSQL_PORT=3306         # Optional: Database port (defaults to 3306 if not specified)
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=your_database
```