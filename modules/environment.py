# -*- coding:utf-8 -*-

import os

def run(**args):
	print "[*] In environment modules."
	# environは環境変数を取得
	return str(os.environ)