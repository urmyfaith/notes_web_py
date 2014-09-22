# -*- coding:utf-8 -*-
import web

db = web.database(dbn='mysql', user='root', pw='283017', db='tododb')

render = web.template.render('templates/')

urls = ( 
    '/', 'index' ,  #处理URL:/
    '/add', 'add'   #处理URL：/add
)
class index: 
    def GET(self):
        todos = db.select('todo')#查询数据库
        return render.index(todos)#使用模版显示数据
class add:
    def POST(self):
        i = web.input()#获得输入
        title_value=i.title;#根据名称得到输入的值
        if title_value!='': 
            n = db.insert('todo',title=title_value)#插入数据库
        raise web.seeother('/')#网址跳转 
if __name__ == "__main__": 
    app = web.application(urls, globals()) 
    app.run()
