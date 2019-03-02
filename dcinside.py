#python code for dcinside
#2019.03.03 by ÄÚ³ª(aero1)
#delete posts and comment at www.dcinside.com

import time
from selenium import webdriver
browser=webdriver.Chrome("chromedriver.exe")
url="https://gallog.dcinside.com/aero1/comment?gno=2&p=1"
browser.get(url)

time.sleep(60) 
# at this moment login your account
# 1000: page number/2 that you want to delete.
for j in range(1, 1000):
    try:
	    url="https://gallog.dcinside.com/aero1/comment?gno=2&p=1"
	    browser.get(url)
	    a=browser.find_elements_by_class_name("btn_box")
	    b=len(a)
	    for i in range(1, b):
		    a[i].click()
		    time.sleep(0.70)
		    browser.switch_to_alert().accept()
		    time.sleep(0.22)
    except:
        pass

    try:
	    url="https://gallog.dcinside.com/aero1/comment?gno=2&p=2"
	    browser.get(url)
	    a=browser.find_elements_by_class_name("btn_box")
	    b=len(a)
	    for i in range(1, b):
		    a[i].click()
		    time.sleep(0.75)
		    browser.switch_to_alert().accept()
		    time.sleep(0.20)
    except:
        pass
