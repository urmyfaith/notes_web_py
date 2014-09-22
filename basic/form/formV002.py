import web
from web import form

urls = ('/', 'index')
app = web.application(urls, globals())

mytextbox = form.Form(
    form.Textbox('phonenumber',
                 size="12",
                 maxlength="12"),
    form.Textbox("firstname",
                 form.notnull, #put validators first followed by optional attributes
                 class_="textEntry", #gives a class name to the text box -- note the underscore
                 pre="pre", #directly before the text box
                 post="post", #directly after the text box
                 description="please enter your name", #describes field, defaults to form name ("firstname")
                 value="bob", #default value
                 id="nameid", #specify the id
                 ),
    )

class index: 
    def GET(self): 
        mTextbox = mytextbox()
        return  mTextbox.render()
if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
