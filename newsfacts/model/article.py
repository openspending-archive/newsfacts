
from newsfacts.core import db

class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.Unicode)
    title = db.Column(db.Unicode)
    link = db.Column(db.Unicode)
    source = db.Column(db.Unicode)
    feed = db.Column(db.Unicode)
    author = db.Column(db.Unicode)
    attribution = db.Column(db.Unicode)
    body = db.Column(db.Unicode)
    date = db.Column(db.DateTime)

    @classmethod
    def by_key(cls, key):
        return cls.query.filter_by(key=key).first()

    @classmethod
    def store(cls, data):
        article = cls.by_key(data.get('key'))
        if article is None:
            article = cls()
        article.key = data.get('key')
        article.source = data.get('source')
        article.feed = data.get('feed')
        article.link = data.get('link')
        article.title = data.get('title')
        article.date = data.get('date')
        article.body = data.get('body')
        article.author = data.get('author')
        article.attribution = data.get('attribution')
        db.session.add(article)
        db.session.flush()


