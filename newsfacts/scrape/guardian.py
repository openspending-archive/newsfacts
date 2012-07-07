from datetime import datetime
from lxml import html

from newsfacts.scrape.common import fetch_page

def get_article(session, entry):
    doc, css = fetch_page(session, entry.link)

    time = css('time')
    date_ = css('.date')
    if len(time):
        date = time.pop().get('datetime')
        try:
            date = datetime.strptime(date[:15], "%Y-%m-%dT%H:%M%Z")
        except ValueError:
            try:
                date = datetime.strptime(date[:15], "%Y-%m-%dT%H:%M")
            except ValueError:
                date = datetime.strptime(date[:15], "%Y-%m-%d")
    elif len(date_):
        date = date_.pop().text.split(' ', 1)[-1]
        try:
            date = datetime.strptime(date, "%d %B %Y")
        except ValueError:
            date = datetime.strptime(date, "%d %b %Y")
    body = css('#article-body-blocks')
    if not len(body):
        return None
    body = html.tostring(body.pop())
    author = css('a.contributor')
    author = author.pop().text.strip() if len(author) else ''
    article = {
        'title': css('h1').pop().text,
        'author': author,
        'link': entry.link,
        'key': entry.id,
        'date': date,
        'attribution': css('#copyright-links li').pop().xpath('string()'),
        'body': body
        }
    return article

