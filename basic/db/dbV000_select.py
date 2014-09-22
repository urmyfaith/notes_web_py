import web

db = web.database(dbn='mysql', user='root', pw='283017', db='tododb')

render = web.template.render('templates/')

urls = ( 
    '/', 'index' ,
)
class index: 
    def GET(self):
        todos = db.select('todo')
        return render.index(todos)      
if __name__ == "__main__": 
    app = web.application(urls, globals()) 
    app.run()
