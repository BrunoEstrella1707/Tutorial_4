from tutorial import app
from tutorial import db
from flask import render_template, redirect, url_for
from tutorial.models import Usuario
from tutorial.forms import FormularioDeNomes

@app.route('/', methods=['GET', 'POST'])
def page_home():
    form = FormularioDeNomes()
    if form.validate_on_submit():
        user = Usuario(
            nome = form.nome.data
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('page_home'))

    return render_template("home.html", form=form)


@app.route('/show')
def page_show():
    itens = Usuario.query.all()
    return render_template('show.html', itens=itens)
