# -*- coding: UTF-8 -*-
'''
download photo from http://unsample.net/
photo is actually get from unsplash.com 
'''
import selenium
from time import sleep

def get_chromebrowser():
    #set download directory
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
    options.add_experimental_option('prefs', prefs)

    chrome_browser = webdriver.Chrome('F:\KeepVid_Vir\chromedriver.exe')
    chrome_browser.maximize_window()
    return chrome_browser

'''
http://unsample.net/  download 1080P width
'''
if __name__ == '__main__':
    driver = get_chromebrowser()

    while(True):
        try:
            driver.get('http://unsample.net/')
            break
        except selenium.common.exceptions.TimeoutException:
            sleep(2)
        finally:
            print 'waiting for http://unsample.net/'
    sleep(2)

    for i in range(0,100):
        submit = driver.find_element_by_id('submit-btn')
        submit.click()
        sleep(12)
        print 'downloaded %d time'%i

    print 'Download completed!'




