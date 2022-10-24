from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos') #I'm following along with Jonathan's lecture below.
def r_show_dojos():
    return render_template("add_dojo.html", dojos = Dojo.get_all_dojos()) # This is what we will reference in the page itself. "dojos" will be a list of Dojo objects

@app.route('/dojos/add', methods=['POST'])
def f_add_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/ninjas')
def r_new_ninja():
    return render_template("add_ninja.html", dojos = Dojo.get_all_dojos())

@app.route('/ninjas/add', methods=['POST'])
def f_add_ninja():
    Ninja.save(request.form)
    id = request.form['dojo_id']
    return redirect(f'/dojos/{id}')

@app.route('/dojos/<int:id>')
def r_dojo_show(id):
    dictionary = {'id': id}
    return render_template("dojo_ninjas.html", dojo_ninjas = Dojo.get_dojo_with_ninjas(dictionary))

@app.route('/ninjas/edit/<int:id>')
def r_ninja_edit(id):
    dictionary = {'id': id}
    return render_template("edit_ninja.html", ninja = Ninja.get_one(dictionary))

@app.route('/ninjas/update', methods=['POST'])
def f_update_ninja():
    print(request.form)
    Ninja.update(request.form)
    id = request.form['dojo_id']
    return redirect(f'/dojos/{id}')

@app.route('/ninjas/destroy/<int:dojo_id>/<int:id>')
def r_ninja_destroy(dojo_id, id):
    dictionary = {'id': id}
    Ninja.destroy(dictionary)
    return redirect(f'/dojos/{dojo_id}')