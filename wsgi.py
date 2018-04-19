from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import FloatField, SubmitField
from wtforms.validators import InputRequired, DataRequired

application = Flask(__name__)
application.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(application)
moment = Moment(application)


class NameForm(Form):
    valeur1 = FloatField('valeur 1 : ', validators=[InputRequired("Entrez un nombre")])
    valeur2 = FloatField('valeur 2 : ', validators=[InputRequired("Entrez un nombre")])
    submit = SubmitField('Calculer')


@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@application.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@application.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        value_format= "{:.2f}".format(form.valeur1.data / form.valeur2.data)
        session['result'] = value_format
        return redirect(url_for('index'))
    return render_template('index.html', form=form, result=session.get('result'))


if __name__ == '__main__':
    application.run()
