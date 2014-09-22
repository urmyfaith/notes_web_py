import web
from web import form

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form(
    form.Textbox('username'),
    form.Password('password'),
    form.Button('Login'),
    ) 

class index: 
    def GET(self): 
        form = myform()
        return  form.render()
if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
