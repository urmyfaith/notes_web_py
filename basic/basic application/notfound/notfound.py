# -*- coding: cp936 -*-
import web

urls = (
    '/', 'index',
    '/(^weixin)','notfound',
    '/weixin','weixin'
)

app =  web.application(urls, globals())

def notfound():
    return web.notfound("Sorry, the page you were looking for was not found.")

    # You can use template result like below, either is ok:
    #return web.notfound(render.notfound())
    #return web.notfound(str(render.notfound()))
#app.notfound = notfound


class index:
    def GET(self):
        return "hello zx!"
class weixin:
    def GET(self):
        return "weixin"

web.webapi.internalerror = web.debugerror
if __name__ == '__main__':
    app.run()

