from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('tikitaka', __name__)

@bp.route('/tikitaka')
def football():
    return render_template('tikitaka.html', title="TikiTaka")