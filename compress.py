#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import logfile


class CompressPicture(object):
    """
        压缩图片文件
    """

    def __int__(self, base_width=1024):

        print("Compressing, base_width")
        self.base_width = base_width

    def compress_ratio(self, w, h):
        """
        计算图片压缩比
        :param w: 图片宽度
        :param h: 图片高度
        :return: 压缩比
        """
        if w < h:
            w, h = h, w
        # 计算压缩比
        return 1 if w <= self.base_width else self.base_width / w

