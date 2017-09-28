from flask import Flask, render_template, request, make_response, redirect
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, RadioField, SelectField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
from flask_wtf import Form

app = Flask(__name__)

app.secret_key = 'development key'
Bootstrap(app)

class mainform(Form):
    submit = SubmitField('Submit')

@app.route("/")
def index():
    form = mainform()
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
