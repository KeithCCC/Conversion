from flask import Flask, render_template, request, make_response, redirect
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, RadioField, SelectField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import validators

app = Flask(__name__)

app.secret_key = 'development key'
Bootstrap(app)

class mainform(Form):
    Entry  = StringField('Enter data here', [validators.required()])
    submit = SubmitField('Submit')

@app.route("/", methods=['GET', 'POST'])
def index():
    form = mainform()
    result_text='result here'
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('index.html', form=form, result=result_text)

@app.route("/success")
def Success():
    return 'Success'

if __name__ == '__main__':
    app.run(debug=True)
