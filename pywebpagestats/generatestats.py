import requests
from bs4 import BeautifulSoup
import pandas as pd

def getstats(url):
    # Collect and parse first page
    page = requests.get(url=url)
    # print(page.text)
    listoftags = [
	"a",
	"abbr",
	"address",
	"area",
	"article",
	"aside",
	"audio",
	"b",
	"base",
	"bdi",
	"bdo",
	"blockquote",
	"body",
	"br",
	"button",
	"canvas",
	"caption",
	"cite",
	"code",
	"col",
	"colgroup",
	"data",
	"datalist",
	"dd",
	"del",
	"details",
	"dfn",
	"dialog",
	"div",
	"dl",
	"dt",
	"em",
	"embed",
	"fieldset",
	"figcaption",
	"figure",
	"footer",
	"form",
	"h1",
	"h2",
	"h3",
	"h4",
	"h5",
	"h6",
	"head",
	"header",
	"hgroup",
	"hr",
	"html",
	"i",
	"iframe",
	"img",
	"input",
	"ins",
	"kbd",
	"keygen",
	"label",
	"legend",
	"li",
	"link",
	"main",
	"map",
	"mark",
	"math",
	"menu",
	"menuitem",
	"meta",
	"meter",
	"nav",
	"noscript",
	"object",
	"ol",
	"optgroup",
	"option",
	"output",
	"p",
	"param",
	"picture",
	"pre",
	"progress",
	"q",
	"rb",
	"rp",
	"rt",
	"rtc",
	"ruby",
	"s",
	"samp",
	"script",
	"section",
	"select",
	"slot",
	"small",
	"source",
	"span",
	"strong",
	"style",
	"sub",
	"summary",
	"sup",
	"svg",
	"table",
	"tbody",
	"td",
	"template",
	"textarea",
	"tfoot",
	"th",
	"thead",
	"time",
	"title",
	"tr",
	"track",
	"u",
	"ul",
	"var",
	"video",
	"wbr"
]
    soup = BeautifulSoup(page.text, 'html.parser')

    tagstats = {}

    for tag in listoftags:
        tagstats[tag] = len(soup.findAll(tag))
        print("Number Of " + tag + " tags :- " + str(tagstats[tag]))

     # images = soup.findAll('img')
    # videos = soup.findAll('video')
    # divs = soup.findAll('div')
    # print(soup.contents)
    # print("Number Of Images :- " + str(len(images)))
    # print("Number Of Videos :- " + str(len(videos)))
    # print("Number Of Divs :- " + str(len(divs)))

def getDataframe():
	dataframe = pd.DataFrame.from_dict(tagstats, orient='index', columns=['Tag Name', 'Count'])
	dataframe.head()

getstats("https://www.ibm.com")