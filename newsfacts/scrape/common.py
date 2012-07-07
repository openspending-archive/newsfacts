from lxml import html
from lxml.cssselect import CSSSelector

def fetch_page(session, url, **kw):
    response = session.get(url, **kw)
    doc = html.document_fromstring(response.content.decode('utf-8'))
    css = lambda sel: CSSSelector(sel)(doc)
    return doc, css
