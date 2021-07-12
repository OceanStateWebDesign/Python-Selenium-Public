import os
import string
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

driver = webdriver.Firefox(firefox_profile=fp)
default_handle = driver.current_window_handle
url = "https://fortress.wa.gov/wsp/collisionanalysistool/Query/SearchCriteria"
startdate = date.today() - timedelta(days=11)
enddate = date.today() - timedelta(days=1)
countyfile = open('counties.txt')
solver = TwoCaptcha('apikeygoeshere')

#
#Start Actions
#

driver.get(url)

#Send Start Date
startdate = driver.find_element_by_xpath("//*[@id='ColliDateStart']")
startdate.send_keys("1/25/21")

#Send End Date
enddate = driver.find_element_by_xpath("//*[@id='ColliDateEnd']")
enddate.send_keys("2/05/21")

#Click Statewide checkbox
statewide = driver.find_element_by_xpath("//*[@id='chkStatewide']").click()

#School Bus Involvement
sch = driver.find_element_by_xpath("//*[@id='lstSchoolBusesInvolved']")
sch.click()
sleep(2)
sch2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/fieldset[3]/div[1]/div[2]/div[3]/div[2]/select/option[2]").click()
sleep(3)

#Commercial Carrier Involvement
comm = driver.find_element_by_xpath("//*[@id='lstCommercialCarriersInvolved']")
comm.send_keys(Keys_DOWN)
comm.send_keys(Keys_DOWN)

sleep(2)
comm2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/fieldset[3]/div[1]/div[2]/div[3]/div[2]/select/option[3]").click()
sleep(3)

#click the search button
searchbutton = driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/div[3]/div/div[1]/input").click()
sleep(5)

#Click export to csv and download server side
csv = driver.find_element_by_xpath("//*[@id='lnkSummary']").click()


