from datetime import datetime
from lxml import html

from newsfacts.scrape.common import fetch_page

def get_article(session, entry):
    if 'pheedo_origlink' not in entry:
        return
    link = entry['pheedo_origlink']
    if '_blog.' in link:
        return
    f, a = link.rsplit('/', 1)
    a = a.replace('_story.', '_print.')
    url = f + '/' + a
    doc, css = fetch_page(session, url)
    content = css('#content').pop()
    h1 = content.find('h1')
    title = h1.xpath('string()').strip()
    content.remove(h1)
    h3 = content.find('h3')
    time = h3.find('span')
    date = datetime.fromtimestamp(int(time.get('epochtime'))/1000)
    h3.remove(time)
    author = h3.xpath('string()').strip()
    content.remove(h3)
    body = html.tostring(content)
    article = {
        'title': title,
        'author': author,
        'link': link,
        'key': link,
        'date': date,
        'attribution': 'The Washington Post',
        'body': body
        }
    return article

