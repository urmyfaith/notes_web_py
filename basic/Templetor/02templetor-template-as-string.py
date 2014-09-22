import web 

urls = ( 
    '/(.*)', 'index' 
)
class index: 
    def GET(self,name): 
        i=web.input(name=None)
        template = "$def with (name)\nHello $name"
        hello = web.template.Template(template)
        return hello(name)

if __name__ == "__main__": 
    app = web.application(urls, globals()) 
    app.run()
