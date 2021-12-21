from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from db import get_db

bp = Blueprint('edit_create', __name__)

@bp.route('/editor_ibjhrv87g4', methods=('GET', 'POST'))
def editor():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, views'
        ' FROM post p'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('editor.html', posts=posts, title="Editor")


@bp.route('/create_ibjhrv87g4', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body)'
                ' VALUES (?, ?)',
                (title, body)
            )
            db.commit()
            return redirect(url_for('edit_create.query'))

    return render_template('create.html', title='Create')


def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created'
        ' FROM post p '
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    return post

@bp.route('/<int:id>/update_ibjhrv87g4', methods=('GET', 'POST'))
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('edit_create.query'))

    return render_template('update.html', post=post, title='Edit')

@bp.route('/<int:id>/delete_ibjhrv87g4', methods=('POST',))
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('edit_create.editor'))


@bp.route('/query_ibjhrv87g4')
def query():
    return render_template('query.html', title="Query")
