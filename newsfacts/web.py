from flask import render_template

from newsfacts.core import app, db
from newsfacts.views import extract

app.register_blueprint(extract.section, url_prefix='/')

@app.route('/')
def index():
    return render_template('index.html')
