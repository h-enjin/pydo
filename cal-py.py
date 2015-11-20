#!/usr/bin/python2
# -*- coding:utf-8 -*-

## TODO:TODOリストを作成する
## TODOリストとして、「内容/完了フラグ」を基本

import sqlite3,sys

if __name__ == "__main__":
	
	db_connecter = sqlite3.connect("data.db")

	sql = "insert into todo_list values ('1', 'test', 'false')"
	db_connecter.execute(sql)

	db_connecter.commit()
	db_connecter.close()

	print "終了します"
