from flask import Blueprint, request, redirect, url_for
from flask import render_template, flash

from newsfacts.core import db
from newsfacts.model import Article

from newsfacts.scrape.common import cleanup_body

section = Blueprint('extract', __name__)

@section.route('extract', methods=['GET'])
def view():
    import random
    rand = random.randrange(0, Article.query.count()) 
    article = Article.query[rand]
    body = cleanup_body(article.body)
    return render_template('extract/view.html', 
            article=article,
            body=body)

