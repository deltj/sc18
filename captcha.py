import urllib2
from bs4 import BeautifulSoup
import base64
from fontTools.ttLib import TTFont as ttfont


from simpleeval import simple_eval

if __name__ == "__main__":
    # get captcha page
    url = "https://hidden-island-93990.squarectf.com/ea6c95c6d0ff24545cad"
    headers = { 'User-Agent' : 'Mozilla/5.0' }
    request = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(request)
    print(response)
    html = response.read()

    # scrape base64 TTF data
    soup = BeautifulSoup(html, "html.parser")
    s = soup.select("style")
    encodedfontdata = s[0].text
    start = encodedfontdata.find("base64") + 7
    end = encodedfontdata.find("==") + 2
    encodedfontdata = encodedfontdata[start:end]
    #print(encodedfontdata)

    # decode TTF
    fontdata = base64.b64decode(encodedfontdata)
    fontfile = open("font.ttf", "w")
    fontfile.write(fontdata)
    fontfile.close()
    font = ttfont("font.ttf")
    font.saveXML("font.xml")
    #font = ttfont(fontdata)
    glyphs = font.getGlyphSet()

    # scrape encoded expression
    p = soup.select("p")
    encoded_expression = p[0].text
    print(encoded_expression)

    #for c in encoded_expression:
    #    g = glyphs.get(c)
    #    print(g)


