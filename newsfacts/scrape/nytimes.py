from datetime import datetime
from lxml import html

from newsfacts.scrape.common import fetch_page

def get_article(session, entry):
    if 'pheedo_origlink' not in entry:
        return
    link = entry['pheedo_origlink']
    url = link.rsplit('?', 1)[0] + '?pagewanted=print'
    doc, css = fetch_page(session, url, headers={'Referer': link})
    date = css('.timestamp')
    if not len(date):
        return
    date_text = date.pop().text.strip()
    try:
        date = datetime.strptime(date_text, '%B %d, %Y')
    except ValueError:
        date = datetime.strptime(date_text, '%B %d, %Y,')
    headline = css('nyt_headline')
    if not len(headline):
        headline = css('h3.entry-title')
    author = css('nyt_byline')
    if not len(author):
        author = css('.byline')
    body = css('#articleBody')
    if not len(body):
        body = css('.entry-content')
    article = {
        'title': headline.pop().text,
        'author': author.pop().xpath('string()').strip(),
        'link': link,
        'id': link,
        'date': date,
        'attribution': '',
        'body': html.tostring(body.pop())
        }
    return article

