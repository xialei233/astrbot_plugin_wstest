# 导入必要的API模块
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger  # 使用AstrBot统一的日志接口

# 注册插件信息：插件标识、作者、描述、版本（仓库地址可选）
@register("hello_reply", "YourName", "接收/hello指令回复你也好的插件", "1.0.0")
class HelloReplyPlugin(Star):
    """核心插件类，必须继承Star基类"""
    def __init__(self, context: Context):
        # 初始化父类，传入上下文对象（包含AstrBot核心组件）
        super().__init__(context)
        logger.info("【你也好插件】已初始化完成")

    # 注册/hello指令的处理函数
    @filter.command("hello")  # 指令名对应/hello触发
    async def hello_handler(self, event: AstrMessageEvent):
        """处理/hello指令，回复固定内容你也好"""
        # 记录日志（方便调试）
        sender_name = event.get_sender_name()
        logger.info(f"【你也好插件】收到{sender_name}发送的/hello指令")
        
        # 核心逻辑：回复"你也好"
        yield event.plain_result("你也好")

    async def terminate(self):
        """插件卸载/停用时执行的销毁方法（可选）"""
        logger.info("【你也好插件】已卸载")
