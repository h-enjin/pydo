#!/usr/bin/python2
# -*- coding:utf-8 -*-

## TODO:TODOリストを作成する
## TODOリストとして、「内容/完了フラグ」を基本

import csv,sys

def showTodo():
	print "list選択しました"
	csvfile = "data.csv"
	f = open(csvfile, "r")
	reader = csv.reader(f)

	for row in reader:
		print row

	f.close()

def selectMenu():
	exit_flg = True

	print "メニューです"
	print "終了：exit\n現在のTODO：list"
	while exit_flg:
		print "入力してください"
		input_line = sys.stdin.readline()

		if input_line == "list\n":
			showTodo()
		elif input_line == "exit\n":
			exit_flg = False

if __name__ == "__main__":
	selectMenu()
	print "終了します"
