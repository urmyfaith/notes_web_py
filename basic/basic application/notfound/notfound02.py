# -*- coding: cp936 -*-
import web

urls = (
    '/', 'index'
)

app =  web.application(urls, globals())
render = web.template.render('templates/')

def notfound():
    return web.notfound(render.notfound())
app.notfound = notfound


class index:
    def GET(self):
        return "hello zx!"


web.webapi.internalerror = web.debugerror
if __name__ == '__main__':
    app.run()

