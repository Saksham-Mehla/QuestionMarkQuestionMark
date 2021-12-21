from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('about', __name__)

@bp.route('/about')
def info():
    return render_template('about.html', title="About Me")