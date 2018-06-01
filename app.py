from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DABATASE_URI ']= 'mysql://root:@127.0.0.1/news'
db = SQLAlchemy(app)

class File(db.Model):
    id = db.Column(db.Integer)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer)
    content = db.Column(db.Text)




class Category(db.Model):
    id = db.Column(db.Integer)
    name = db.Column(db.String(80))


@app.route('/')
def index():
    title = []
    path = r'/home/shiyanlou/files'
    for filesname in os.listdir(path):
        file =  os.path.join(path,filesname)
        with open(file, 'r') as f:
            c = json.loads(f.read())
            title.append(c['title'])
    return render_template('index.html', title=title)

@app.route('/files/<filename>')
def file(filename):
    path = r'/home/shiyanlou/files'
    file = os.path.join(path, filename) + '.json'
    with open(file, 'r') as f:
        content = json.loads(f.read())
    return render_template('file.html', content = content)

if __name__ == '__main__':
    app.run()
