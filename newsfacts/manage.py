from flaskext.script import Manager

from newsfacts.core import app, db
from newsfacts.model import *

manager = Manager(app)

@manager.command
def scrape():
    pass

if __name__ == '__main__':
    manager.run()