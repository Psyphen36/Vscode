import requests
import xml.etree.ElementTree as et

Rss_Url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

def Rss_request():
    resp = requests.get(Rss_Url)

    return resp.content


def Rss_Xml(rss):
    root = et.fromstring(rss)

    news_items = []

    for item in root.findall('./channel/item'):
        news = {}

        for child in item:
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
        news_items.append(news)

    return news_items


def top_Stories():
    rss = Rss_request()

    top_news = Rss_Xml(rss)

    return top_news

stories = top_Stories()

print(stories)
