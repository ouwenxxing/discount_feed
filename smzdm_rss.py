#encoding=utf8
from selenium import webdriver
import datetime
import PyRSS2Gen

try:
    browser = webdriver.Chrome()

    browser.get('http://search.smzdm.com/?c=home&s=电动牙刷')

    browser.refresh()

    rss = PyRSS2Gen.RSS2(
        title = "smzdm 电动牙刷 feed",
        link = "localhost/rss/smzdm.html",
        description = "szmdm 电动牙刷每天 feed",

        lastBuildDate = datetime.datetime.now(),
    )
    items = []
    # result = browser.page_source
    searchEleList = browser.find_elements_by_css_selector('div[class="search-list"]')
    for ele in searchEleList:
        title = ele.find_element_by_xpath('div[2]/div[1]/a').text
        left_a = ele.find_element_by_xpath('div[1]/a')
        link = left_a.get_attribute('href')
        img_node = left_a.find_element_by_xpath('img').get_attribute('outerHTML')
        item = PyRSS2Gen.RSSItem(
        title = title,
        link = link,
        description = title,
        guid = PyRSS2Gen.Guid(link),
        pubDate = datetime.datetime.now())
        items.append(item)

    rss.items = items

finally:
    browser.quit()
    rss.write_xml(open("smzdm2gen.xml", "w"),encoding="UTF-8")