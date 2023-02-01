class ImageOpenError(Exception):
    """图像打开错误异常类

    :param exc: 原始异常
    """

    def __init__(self, exc):
        self.exc = exc
        # 调用异常父类方法，初始化错误信息
        super().__init__(f'Image open error: {self.exc}')
