from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, views'
        ' FROM post p'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('index.html', posts=posts, title="Posts")