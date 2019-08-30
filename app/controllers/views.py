from app import app
from app.form import TodoForm
from app.models import db
from flask import render_template, request, flash, redirect, url_for
import datetime

app.config['SECRET_KEY'] = '89af651d869493e77b115a89a2e5dc14'

@app.route('/', methods=['POST', 'GET'])
def home():
    form = TodoForm()
    if form.validate_on_submit():     
        formData={'todoName': request.form['listName'], 'date': datetime.datetime.now().strftime('%d %B, %Y')}
        if db.insert(formData) == True:
            flash(f'New todo item added')
        else:
            flash(f'Item not added')

    listData = db.showListItem()
    return render_template('home.html', form=form, listItems=listData)

@app.route('/delete/<id>')
def delete(id):
    db.deleteItem(id)
    flash(f'Item deleted')
    return redirect(url_for('home'))