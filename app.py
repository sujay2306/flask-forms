from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = "MYSECRETKEY"

class InfoForm(FlaskForm):
    title = StringField("what should be the title")
    submit = SubmitField("Submit")

@app.route('/', methods=['Get', 'Post'])
def index():
    title = False

    form = InfoForm()

    if form.validate_on_submit():
        #extracting the value 
        title = form.title.data
        form.title.data = ""
    return render_template('home.html',form=form,title=title)


if __name__ == '__main__':
    app.run(debug=True)