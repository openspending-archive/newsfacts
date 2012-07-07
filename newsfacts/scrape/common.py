from lxml import html
from lxml.cssselect import CSSSelector

def fetch_page(session, url, **kw):
    response = session.get(url, **kw)
    doc = html.document_fromstring(response.content.decode('utf-8'))
    css = lambda sel: CSSSelector(sel)(doc)
    return doc, css

def drop_tag(doc, tag_name):
    for t in doc.findall(".//" + tag_name):
        t.drop_tag()

def drop_tree(doc, tag_name):
    for t in doc.findall(".//" + tag_name):
        t.drop_tree()

def cleanup_body(text):
    doc = html.fromstring("<div>%s</div>" % text)
    drop_tag(doc, 'a')
    drop_tag(doc, 'h1')
    drop_tag(doc, 'h2')
    drop_tree(doc, 'script')
    drop_tree(doc, 'iframe')
    drop_tree(doc, 'canvas')
    drop_tree(doc, 'img')
    drop_tree(doc, '*[@class="caption"]')
    return html.tostring(doc)
