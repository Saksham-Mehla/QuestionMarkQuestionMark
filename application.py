from flask import Flask, render_template
import os

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'DumbLifeForm.sqlite')
    )
        
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else: 
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    import db
    db.init_app(app)

    import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    import tikitaka
    app.register_blueprint(tikitaka.bp)

    import drift
    app.register_blueprint(drift.bp)

    import edit_create
    app.register_blueprint(edit_create.bp)

    import about
    app.register_blueprint(about.bp)

    return app