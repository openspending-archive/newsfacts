from lxml import html
from datetime import datetime

from newsfacts.scrape.common import fetch_page

def stringify(p):
    del p.attrib['style']
    del p.attrib['class']
    return html.tostring(p)

def get_article(session, entry):
    doc, css = fetch_page(session, entry.link)
    body = '\n'.join([stringify(p) for p in css('.ap_para')])
    date_ = datetime.strptime(css('.ap_dt_stmp').pop().text, '%b. %d, %Y')
    by_line = css('.ap_by')
    author = by_line.pop().text if len(by_line) else ''
    article = {
        'title': css('.ap_head').pop().text,
        'author': author,
        'link': entry.link,
        'key': entry.id,
        'date': date_,
        'attribution': css('#CopyrightLine').pop().xpath('string()'),
        'body': body
        }
    return article

