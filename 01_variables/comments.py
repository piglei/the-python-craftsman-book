# -*- coding: utf-8 -*-


def resize_image(image, size):
    """将图片缩放为指定尺寸，并返回新的图片。

    该函数将使用 Pilot 模块读取文件对象，然后调用 .resize() 方法将其缩放为指定尺寸。

    但由于 Pilot 模块自身限制，这个函数不能很好的处理尺寸过大的文件，当文件大小
    超过 5MB 时，resize() 方法的性能就会因为内存分配问题急剧下降，详见 Pilot 模块的
    Issue #007。因此，对于超过 5MB 的图片文件，请使用 resize_big_image() 替代，后者
    基于 Pillow 模块开发，很好的解决了内存分配问题，性能更好。

    :param image: 图片文件对象
    :param size: 包含宽高的元组：（width, height）
    :return: 新图片对象
    """


def resize_image(image, size):
    """将图片缩放为指定尺寸，并返回新的图片。

    注意：当文件超过 5MB 时，请使用 resize_big_image()

    :param image: 图片文件对象
    :param size: 包含宽高的元组：（width, height）
    :return: 新图片对象
    """