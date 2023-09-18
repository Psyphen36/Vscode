import time
from plyer import notification
from topNews import top_Stories


newsItems = top_Stories()
def notifier():
    title = ''
    message = ''
    for newsItem in newsItems:
        title = newsItem['title']
        message = newsItem['description']
    
    return title, message

title, message = notifier()

notification.notify(title = title, message = message, timeout = 2)

time.sleep(15)