# -*- coding: cp936 -*-
import web

render = web.template.render('templates/', cache=False)

urls = (
    '/(.*)', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self, code):
        web.header('Content-Type', 'text/xml')#通知接收端，发送文件类型是xml
        
        return render.response(code)

web.webapi.internalerror = web.debugerror
if __name__ == '__main__':
    app.run()
