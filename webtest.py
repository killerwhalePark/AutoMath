"""Flask Login Example and instagram fallowing find"""

from flask import Flask, url_for, render_template, request, redirect, session, send_file
from flask_sqlalchemy import SQLAlchemy
import makepdf

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    """ Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password


@app.route('/', methods=['GET', 'POST'])
def home():
    """ Session control"""

    return render_template('index.html')



@app.route('/main', methods=['GET', 'POST'])
def main():

    data = []

    if request.method == 'GET':
        return render_template('main.html')
    else:
        name = request.form.get('Curri')
        if name != None:
            name = int(name)
            name1 = "math" + str(name) + '.html'
            data.append(name)
            return render_template(name1)
        else:
            lesson = int(request.form.get('lesson'))
            data.append(lesson)
            level = int(request.form.get('level'))
            data.append(level)
            questionnum = int(request.form.get('questionnum'))
            data.append(questionnum)

            print(data)

            makepdf.makepdf(1, data[0], data[1], data[2])

            file = 'result.pdf'
            return send_file(file)








@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.secret_key = "123"
    app.run()
