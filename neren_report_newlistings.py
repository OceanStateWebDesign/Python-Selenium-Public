import os
import string
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep
from datetime import date
from datetime import datetime, timedelta
from PyPDF2 import PdfFileReader
from twocaptcha import TwoCaptcha
import urllib

#Variables
mime_types = "application/pdf,application/vnd.adobe.xfdf,application/vnd.fdf,application/vnd.adobe.xdp+xml"
fp = webdriver.FirefoxProfile()
fp.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
fp.set_preference("pdfjs.disabled", True)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf,application/x-pdf")
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, firefox_profile=fp)
default_handle = driver.current_window_handle
url = "https://www.neren.com/search?class=Residential&ListDateRelDategte=-1&sortOption=created%20desc"
x = range(21)

#
#Start Actions
#

driver.get(url)

sleep(1)

for i in x:

	try:
	  elem = driver.find_element_by_xpath("/html/body/main/div[1]/div/div/div/div[1]/div[1]/article[" + format(i) + "]/div[1]/div[2]/div[2]/div[1]/span[1]")
	  f = open("listing_db.txt")

	  if elem.text not in f.read():
	    print("New Listing Found!")

	    with open("listing_db.txt", "a") as text_file:
	         print(elem.text, file= text_file)
	         print(elem.text)



	except:
	  print(i)
