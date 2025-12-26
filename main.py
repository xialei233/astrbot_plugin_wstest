from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

# 注册插件信息：插件名、作者、描述、版本
@register("hello_cn", "YourName", "一个回复中文问候的插件", "1.0.0")
class MyHelloPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """插件初始化方法（异步），实例化后自动调用"""
        # 这里可以添加插件初始化逻辑，比如加载配置、连接数据库等
        logger.info("中文问候插件已初始化")

    # 注册指令：指令名为“你好”，对应触发消息为 /你好
    @filter.command("hello")
    async def hello_handler(self, event: AstrMessageEvent):
        """回复中文问候的指令，触发词：/你好"""
        # 获取发送者的用户名
        user_name = event.get_sender_name()
        # 构造回复消息：我很好 + 用户名 + 你呢？
        reply_msg = f"我很好{user_name}你呢？"
        # 记录日志（可选，方便调试）
        logger.info(f"回复用户 {user_name}：{reply_msg}")
        # 发送纯文本回复
        yield event.plain_result(reply_msg)

    async def terminate(self):
        """插件销毁方法（异步），卸载/停用时调用"""
        logger.info("中文问候插件已销毁")
