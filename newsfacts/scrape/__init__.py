import requests
import logging
import feedparser

from newsfacts.core import app, db

from newsfacts.scrape import nytimes
from newsfacts.scrape import wapo
from newsfacts.scrape import guardian
from newsfacts.scrape import ap

ARTICLE_PARSERS = {
    'nytimes': nytimes.get_article,
    'wapo': wapo.get_article,
    'guardian': guardian.get_article,
    'ap': ap.get_article
    }

log = logging.getLogger(__name__)

def fetch():
    feeds = app.config.get('FEEDS')
    for parser_name, url in feeds:
        parser = ARTICLE_PARSERS.get(parser_name)
        if parser is None:
            log.error("No such parser: %s", parser_name)
        try:
            fetch_feed(url, parser)
        except Exception, e:
            log.exception(e)

def fetch_feed(url, parser):
    session = requests.session()
    response = session.get(url)
    feed = feedparser.parse(response.content)
    for entry in feed.entries:
        try:
            article = parser(session, entry)
            if article is None:
                log.warn("No article for entry: %s", entry.link) 
                continue
            log.info("Loaded: %s", article.get('title'))
        except Exception, e:
            log.exception(e)



