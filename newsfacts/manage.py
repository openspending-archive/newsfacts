from flaskext.script import Manager

from newsfacts.core import app, db
from newsfacts.model import *
from newsfacts import web

manager = Manager(app)

@manager.command
def scrape():
    """ Update news articles from various sources. """
    from newsfacts.scrape import fetch
    fetch()

@manager.command
def createdb():
    """ Update news articles from various sources. """
    db.create_all()

if __name__ == '__main__':
    manager.run()
