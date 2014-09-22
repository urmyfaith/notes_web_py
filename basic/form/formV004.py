# -*- coding: cp936 -*-
import web
from web import form

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

#表格
myform = form.Form( 
    form.Textbox("boe"), 
    form.Textbox("bax", 
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),#必须为数字
        form.Validator('Must be more than 5', lambda x:int(x)>5)),#必须大于5
    form.Textarea('moe'),
    form.Checkbox('curly'), 
    form.Dropdown('french', ['mustard', 'fries', 'wine'])) 

class index:
    # GET直接显示表格
    def GET(self): 
        form = myform()
        return render.formtest(form)

    #
    def POST(self): 
        form = myform() 
        if not form.validates(): #数据有效性检查
            return render.formtest(form)
            #无效数据的显示页面
            #将form作为参数，传入到模版formtest里去处理。
        
        else:#数据
            return "boe: %s, bax: %s" % (form.d.boe, form['bax'].value)

if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
