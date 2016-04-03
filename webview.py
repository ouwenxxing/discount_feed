#encoding=utf8
from selenium import webdriver

def crawl(keyword,link):
    try:
        browser = webdriver.Chrome()

        browser.get('{}{}'.format(link,keyword))

        browser.refresh()

        # result = browser.page_source
        items = []
        searchEleList = browser.find_elements_by_css_selector('div[class="search-list"]')
        for ele in searchEleList:
            time = ele.find_element_by_xpath('div[2]/div[3]/div[1]/span[5]').text
            if time.__contains__(' '):
                break
            title = ele.find_element_by_xpath('div[2]/div[1]/a').text
            left_a = ele.find_element_by_xpath('div[1]/a')
            link = left_a.get_attribute('href')
            img_node = left_a.find_element_by_xpath('img').get_attribute('outerHTML')
            item = {'title':title,'link':link,'img':img_node,'time':time}
            items.append(item)

    finally:
        browser.quit()
        print items.__len__()
        return items

