# -*- coding: utf-8 -*-

import os

# **は可変長引数。辞書にまとめられる
# *の場合tupleになる
def run(**args):

	print "[*] In dirlister module."
	files = os.listdir(".")

	return str(files)