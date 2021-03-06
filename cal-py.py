#!/usr/bin/python2
# -*- coding:utf-8 -*-

## TODO:TODOリストを作成する
## TODOリストとして、「内容/完了フラグ」を基本

import sqlite3,sys

def showAllTodo():
	db_connecter = sqlite3.connect("data.db")
	cursor = db_connecter.cursor()
	cursor.execute("select todo,flg from todo_list")
	
	result = cursor.fetchall()

	print "==TODO Lists=="
	for row in result:
		if row[1] == "true":
			print u"✓ " + row[0]
		else:
			print u"・" + row[0]
	
	print ""

	cursor.close()
	db_connecter.close()

def showTodo():
	db_connecter = sqlite3.connect("data.db")
	cursor = db_connecter.cursor()
	cursor.execute("select todo,flg from todo_list where flg='false'")
	
	result = cursor.fetchall()

	print "==TODO Lists=="
	for row in result:
		print row[0]
	
	print ""

	cursor.close()
	db_connecter.close()

def addTodo():
	db_connecter = sqlite3.connect("data.db")

	print "TODO追加します"
	mes = sys.stdin.readline().split("\n")

	sql = "insert into todo_list values ('" + mes[0] +  "', 'false')"
	db_connecter.execute(sql)

	db_connecter.commit()
	db_connecter.close()
	print "追加しました！\n"

def selectMenu():
	# ループ終了フラグ
	exit_flg = True

	while exit_flg:
		print "--MENU--\nadd:TODO追加\nlist:TODO表示\nall:TODO全て表示\nexit:終了"
		# メニュー選択
		menu = sys.stdin.readline().split("\n")
		input_menu = menu[0]

		if input_menu == "add":
			addTodo()
		elif input_menu == "all":
			showAllTodo()
		elif input_menu == "list":
			showTodo()
		elif input_menu == "exit":
			exit_flg = False

if __name__ == "__main__":
	selectMenu()

	print "終了します"
