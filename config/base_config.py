# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：
# 1. 不得用于任何商业用途。
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。
# 3. 不得进行大规模爬取或对平台造成运营干扰。
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。
# 5. 不得用于任何非法或不当的用途。
#
# 详细许可条款请参阅项目根目录下的LICENSE文件。
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。

# 基础配置
PLATFORM = "bili"  # 平台，xhs | dy | ks | bili | wb | tieba | zhihu
KEYWORDS = "编程副业,编程兼职"  # 关键词搜索配置，以英文逗号分隔
LOGIN_TYPE = "qrcode"  # qrcode or phone or cookie
COOKIES = "__ac_nonce=0688b44fa0039ad95c6bd; __ac_signature=_02B4Z6wo00f016x0NRAAAIDChXCrbZti.s-sVDGAAIOe16; enter_pc_once=1; UIFID_TEMP=ecb38e5e86f1f8799c3256ca6c3446710d152cd7b76a2f92ca888d379e861b9ee14c7187491d24ad18524ea139cfbcf91ce65ed6f3e33762fa0811391e641a8b5eba6233837c38a12d499939762a09ad; x-web-secsdk-uid=2bde654e-726b-4254-b591-b2e01c23ba3a; douyin.com; device_web_cpu_core=10; device_web_memory_size=8; hevc_supported=true; dy_swidth=1920; dy_sheight=1080; fpk1=U2FsdGVkX188HbMnNmmWalooJfkxqZ9zF4AMw5FmGPxmhbQgcKrat/c+Wkgw1q6F6th5pUoTNtyDdEyBNCtvgQ==; fpk2=ce69b851c4edc7eebfb3998aa94a7157; s_v_web_id=verify_mdr933v2_uo2uLmqe_SvPF_4m2G_8XCO_c8S3tbjEFySs; volume_info=%7B%22volume%22%3A0.6%2C%22isMute%22%3Atrue%7D; my_rd=2; ttwid=1%7CN9rzYHfMMwgkzo-phCn4s_gSaSglcIPKSGQJPktKTn4%7C1753957630%7C7203c1daf1dd603c11df78c56e2472e76de4ab3f8bbdc5df215da00a8b1ab4e7; bd_ticket_guard_client_web_domain=2; __security_mc_1_s_sdk_crypt_sdk=471f394c-4c5e-83f2; passport_csrf_token=7de7531d0946b3f7e002291b4f451a61; passport_csrf_token_default=7de7531d0946b3f7e002291b4f451a61; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f273d343734363332303c36303234272927676c715a75776a716a666a69273f2763646976602778; bit_env=qfco_mTFcxjJRyaXumBiVD7e_poNoKyqmJXlfEb1O6yQ7OwmXs4luXcnla7EWK6GNeg_1vUJIFjlZ1Qz7oBnjLZxX1SaF-hfxC80xkNNAzzJTr3bbnffyh9Q8TxnKG37oBVx1NuInHAa9gOdL_79SzlWQpmEqHeeXEC1iTQ_gfqld2ltLwOrb0w0CJYvR_1DlkRvP5bPeX_yLrynHsBQveNY3d-hJp7G4oLom6uWpEnfR3onroUNrCzkAwmBB6o9jmuXfBycfUQ8R1Uq3YVX__QQAai3notx21OIzBiMpD0J4LcSgDU0XuDAsBZpGwiRYAUUp2MNWbJuWQeVL-BAwbfPQ6aCarDPoC47DnWCvbEIHWYi0P-zOGMW6IPdaJuI5Q02ZYGrR9UB-w6yXBhy7m512NAA4S4Mc80GLnLkg2c_W0mQUG3C2Ii9qlnc4y9EquFP_MwVvm0hJ9_txXPe-XxV6kKyROrDd4UAeSviYimJbdO8RhINKCrcTrM8u6eo3urvBVE8WJLjq3bO0WNP33vM3QN2vdGtwwVeWyuJM8U%3D; gulu_source_res=eyJwX2luIjoiNWRiODg4ZDk2OWY5MmIyYmRkNjBkMTk5NjFmM2EzM2M0MDE5MTQ4NjExYzMyZGJjNzllZGE3NTdkNTBmMGQwMyJ9; passport_auth_mix_state=gkaob3m1pdn6qet2uii56lks3npk89fk; passport_mfa_token=Cjfy8zWg7RPiybTyreSS4%2FrWJUpn9yhljUdhot5vF4TsOUsgP4Xl5t%2F%2BL8fgbckPvveNVWZLZ6wvGkoKPAAAAAAAAAAAAABPTOtMohU9tuzMNwMHSA09bhx5xxLemMyNZlTYWNqqZgxliiOKzqJuHBtZDnhuZiJGzxDEm%2FgNGPax0WwgAiIBA8v7PFY%3D; d_ticket=dedef5ce8d77d973b2ccb90534ab112f7fa1c; passport_assist_user=CkFdBvRES48_xl5Uf-IX8DetdsRvXbOoRK5lqgDdRzvwhcWj0NDoPl6kgauECy5znLFY6xOP5tJaprILdg9Ksgr2BRpKCjwAAAAAAAAAAAAAT0yiYvKy0CT2Xz9Lk0gzanyXE3Kz7aTOiFClLYvHqg2fD73M7PODQ14IbRQJ7e-uZaIQ15v4DRiJr9ZUIAEiAQMTa7Cc; n_mh=otXlj-oj4tnP7SY9y2P3icONy6k9W4Ff3avoKIpPhB0; passport_auth_status=6cfe8e4cac69ccf86bce25506d9ce053%2C; passport_auth_status_ss=6cfe8e4cac69ccf86bce25506d9ce053%2C; sid_guard=71c8e56a3c0a4ffed9798c98b58fc2e7%7C1753957671%7C5183999%7CMon%2C+29-Sep-2025+10%3A27%3A50+GMT; uid_tt=d611a2734862b09b8ae600f7037db7aa; uid_tt_ss=d611a2734862b09b8ae600f7037db7aa; sid_tt=71c8e56a3c0a4ffed9798c98b58fc2e7; sessionid=71c8e56a3c0a4ffed9798c98b58fc2e7; sessionid_ss=71c8e56a3c0a4ffed9798c98b58fc2e7; session_tlb_tag=sttt%7C3%7CccjlajwKT_7ZeYyYtY_C5_________-wRcnzxExu4jA9PfH8qoxNLE6Pv-KS91Se7H3q3Bt8vIA%3D; is_staff_user=false; sid_ucp_v1=1.0.0-KDY1ZjllZDc1ZTk4OTM5ZTMyMWU1Njg5NzNiYjczMTBiYjAwNWY1ZjEKIQiXsfC_wfSRBhCniq3EBhjvMSAMMPGBhvIFOAJA8QdIBBoCbGYiIDcxYzhlNTZhM2MwYTRmZmVkOTc5OGM5OGI1OGZjMmU3; ssid_ucp_v1=1.0.0-KDY1ZjllZDc1ZTk4OTM5ZTMyMWU1Njg5NzNiYjczMTBiYjAwNWY1ZjEKIQiXsfC_wfSRBhCniq3EBhjvMSAMMPGBhvIFOAJA8QdIBBoCbGYiIDcxYzhlNTZhM2MwYTRmZmVkOTc5OGM5OGI1OGZjMmU3; login_time=1753957671099; biz_trace_id=3bfe97a3; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=9870b57988175aefb237b6e0af86b558; __security_mc_1_s_sdk_sign_data_key_web_protect=02bceabe-40e0-81c5; __security_mc_1_s_sdk_cert_key=bbc69325-4cf7-b97d; __security_server_data_status=1; UIFID=ecb38e5e86f1f8799c3256ca6c3446710d152cd7b76a2f92ca888d379e861b9ee14c7187491d24ad18524ea139cfbcf9848ba37cba1acddb9fab27de1f6c08d7707a9c976db38db392fc824ff0653bb039fc648e3fef1eddf07d82140dfcd79da35df72da76bc4ab76f53d50d46296348ebb8ee4647be92290c95f568da023012b1db4a02f09ba739dc3847f6f53eb9de400bc84d749e2db19d25c714462c2a9; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A10%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A150%7D%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA1Y2SiOKSFHL2jTYWrx7yeE_OgyOBN0unwRNAO8lcCcJkpzLJANCd7rECbxyS5UZY%2F1753977600000%2F0%2F1753957672418%2F0%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRmRiWkNVM0xPUThpVzRtSHdKSFphVXN5NkJDVjlFSG5SWnpDcHV1WGYvdjhqR0N3OXU2UnUyV2VuQk16RWVySlVhVzRyVE9BLzlQZmpGQytxTHVONmc9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; odin_tt=741bd92feb120fd313f176f0d824cffdae7bbc9efd519ff8a9784b40384e5d341479ef365a5bfc3690db47a4566c677d1201216fec31f21241c040520b6e8798"
CRAWLER_TYPE = (
    "search"  # 爬取类型，search(关键词搜索) | detail(帖子详情)| creator(创作者主页数据)
)
# 是否开启 IP 代理
ENABLE_IP_PROXY = False

# 代理IP池数量
IP_PROXY_POOL_COUNT = 2

# 代理IP提供商名称
IP_PROXY_PROVIDER_NAME = "kuaidaili"

# 设置为True不会打开浏览器（无头浏览器）
# 设置False会打开一个浏览器
# 小红书如果一直扫码登录不通过，打开浏览器手动过一下滑动验证码
# 抖音如果一直提示失败，打开浏览器看下是否扫码登录之后出现了手机号验证，如果出现了手动过一下再试。
HEADLESS = False

# 是否保存登录状态
SAVE_LOGIN_STATE = True

# ==================== CDP (Chrome DevTools Protocol) 配置 ====================
# 是否启用CDP模式 - 使用用户现有的Chrome/Edge浏览器进行爬取，提供更好的反检测能力
# 启用后将自动检测并启动用户的Chrome/Edge浏览器，通过CDP协议进行控制
# 这种方式使用真实的浏览器环境，包括用户的扩展、Cookie和设置，大大降低被检测的风险
ENABLE_CDP_MODE = False

# CDP调试端口，用于与浏览器通信
# 如果端口被占用，系统会自动尝试下一个可用端口
CDP_DEBUG_PORT = 9222

# 自定义浏览器路径（可选）
# 如果为空，系统会自动检测Chrome/Edge的安装路径
# Windows示例: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
# macOS示例: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CUSTOM_BROWSER_PATH = ""

# CDP模式下是否启用无头模式
# 注意：即使设置为True，某些反检测功能在无头模式下可能效果不佳
CDP_HEADLESS = False

# 浏览器启动超时时间（秒）
BROWSER_LAUNCH_TIMEOUT = 30

# 是否在程序结束时自动关闭浏览器
# 设置为False可以保持浏览器运行，便于调试
AUTO_CLOSE_BROWSER = True

# 数据保存类型选项配置,支持四种类型：csv、db、json、sqlite, 最好保存到DB，有排重的功能。
SAVE_DATA_OPTION = "json"  # csv or db or json or sqlite

# 用户浏览器缓存的浏览器文件配置
USER_DATA_DIR = "%s_user_data_dir"  # %s will be replaced by platform name

# 爬取开始页数 默认从第一页开始
START_PAGE = 1

# 爬取视频/帖子的数量控制
CRAWLER_MAX_NOTES_COUNT = 2

# 并发爬虫数量控制
MAX_CONCURRENCY_NUM = 1

# 是否开启爬媒体模式（包含图片或视频资源），默认不开启爬媒体
ENABLE_GET_MEIDAS = False

# 是否开启爬评论模式, 默认开启爬评论
ENABLE_GET_COMMENTS = True

# 爬取一级评论的数量控制(单视频/帖子)
CRAWLER_MAX_COMMENTS_COUNT_SINGLENOTES = 2

# 是否开启爬二级评论模式, 默认不开启爬二级评论
# 老版本项目使用了 db, 则需参考 schema/tables.sql line 287 增加表字段
ENABLE_GET_SUB_COMMENTS = False

# 词云相关
# 是否开启生成评论词云图
ENABLE_GET_WORDCLOUD = False
# 自定义词语及其分组
# 添加规则：xx:yy 其中xx为自定义添加的词组，yy为将xx该词组分到的组名。
CUSTOM_WORDS = {
    "零几": "年份",  # 将“零几”识别为一个整体
    "高频词": "专业术语",  # 示例自定义词
}

# 停用(禁用)词文件路径
STOP_WORDS_FILE = "./docs/hit_stopwords.txt"

# 中文字体文件路径
FONT_PATH = "./docs/STZHONGS.TTF"

# 爬取间隔时间
CRAWLER_MAX_SLEEP_SEC = 2

from .bilibili_config import *
from .xhs_config import *
from .dy_config import *
from .ks_config import *
from .weibo_config import *
from .tieba_config import *
from .zhihu_config import *
