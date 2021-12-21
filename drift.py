from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('drift', __name__)

@bp.route('/drift')
def car():
    return render_template('drift.html', title="Drift")