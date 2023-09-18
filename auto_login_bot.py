from selenium import webdriver
import os

def startBot(username, password, url):
    path = '/home/anupam/chromedriver-linux64/chromedriver'
    
    driver = webdriver.Chrome(path)

    driver.get(url)

    driver.find_element_by_name(
        'id/class/name of username').send_keys(username)

    driver.find_element_by_name(
        'id/class/name of password').send_keys(password)

    driver.find_element_by_css_selector(
    'id/class/css selector of login button').click()

username = 'anupammishra87706@gmail.com'
password = 'psyphenmishra369'

url = 'https://www.typingclub.com/login.html'

startBot(username, password, url)
