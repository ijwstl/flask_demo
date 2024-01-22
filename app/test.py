# -*- coding: utf-8 -*-

"""
@author: ijwstl
@contact: asiaw159753@outlook.com
@software: Pycharm
@version: 1.0.0
@file: test.py
@time: 10/12/2023 12:39 AM
"""
import os
import shutil

from PIL import Image

from typing import List


def icns2ico(path: str) -> None:
    """
    @description:

    ------------------
    @params:

    ------------------
    @return:

    """
    icns_files = os.listdir(path)
    all_ico_file_path = path.replace("icns_file", "ico_file")
    for icns_file in icns_files:
        os.system(f"icnsutil test {os.path.join(path, icns_file)}")
        os.system(f"icnsutil extract {os.path.join(path, icns_file)}")

        export_file_path = os.path.join(path, os.path.basename(icns_file) + ".export")

        if not os.path.exists(export_file_path):
            continue

        png_file_path = os.path.join(export_file_path, "256x256.png")
        ico_file_path = os.path.join(export_file_path, f"{icns_file}.ico")
        if os.path.exists(png_file_path):
            logo = Image.open(png_file_path)
            logo.save(ico_file_path, format='ICO')

            shutil.move(ico_file_path, all_ico_file_path)
            shutil.rmtree(export_file_path)


if __name__ == '__main__':
    icns2ico(r"C:\Users\wangqi\Downloads\icns_file")