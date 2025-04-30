from lxml import html, etree

def prettyprint_html(element, **kwargs):
    html_str = html.tostring(doc = element, pretty_print=True, **kwargs)
    print(html_str.decode(), end='')

def prettyprint_xml(element, **kwargs):
    xml = etree.tostring(element, pretty_print=True, **kwargs)
    print(xml.decode(), end='')