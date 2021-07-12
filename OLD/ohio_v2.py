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
url = "https://ohtrafficdata.dps.ohio.gov/CrashRetrieval"
startdate = date.today() - timedelta(days=11)
enddate = date.today() - timedelta(days=1)
countyfile = open('counties.txt')
#agencyfile = open('agencies.txt')
solver = TwoCaptcha('09fd33978408d2c34d665d037e79e20a')

#Start Actions

#For each County in file
for county in countyfile:
#	for agency in range(1):

	driver.get(url)

	#Start Search Date
	elem = driver.find_element_by_name("Parameters.CrashStartDate")
	elem.clear()
	sleep(1)
	elem.send_keys(startdate.strftime("%m/%d/%Y"))

	#End Search Date
	elem = driver.find_element_by_name("Parameters.CrashEndDate")
	elem.click()
	sleep(2)
	elem.clear()
	sleep(3)
	elem.send_keys(enddate.strftime("%m/%d/%Y"))
	sleep(2)

	#Select County from Dropdown
	elem = driver.find_element_by_xpath(county)
	sleep(2)
	elem.click();
	sleep(2)

	#Select Agency from Dropdown
	#elem  driver.find.element_by_xpath("/html")
	#sleep(1)
	#elem.click()
	#sleep(2)

	#Set window size + scroll to bottom  + screenshot
	driver.set_window_size(800, 600)
	driver.execute_script("window.scrollTo(0, 700);")
	driver.save_screenshot("./captcha.png")
	sleep(3)

	#Get Captcha Result
	capimg = solver.normal(file='./captcha.png')
	capimg.split(" ");
	sleep(10)
	#print(capimg)

	#CAPTCHA Code - 3rd party code goes here
	elem = driver.find_element_by_xpath("//*[@id='txtCaptcha']")
	elem.click();
	sleep(2)
	elem.send_keys(capimg)
	sleep(10)
	os.remove('./captcha.png')

	#Click the Search Button
	elem = driver.find_element_by_name("btnSearch")
	elem.send_keys(Keys.RETURN)

	sleep(3)

	#Download Results
	for report in driver.find_elements_by_xpath("//*[contains(@id, 'btn')] "):

		sleep(3)
		report.click()
		sleep(7)


		with open('/home/regor/Downloads/GetReport', 'rb') as pdf:

			enddate = date.today()
			search1 = "ERROR" + '\n' + "5"
			reader = PdfFileReader(pdf)
			contents = reader.getPage(0).extractText().split('\n ')[4]
			pass

			if search1 in contents:
				print("The PDF has Property Damage Only '5' - NOT Saving")
				sleep(1)
				os.remove('/home/regor/Downloads/GetReport')
				sleep(2)

			else:
				print("The PDF Passes Checks -> Saving and creating Master PDF")
				os.rename('/home/regor/Downloads/GetReport', './'+enddate.strftime("%m-%d-%Y"+'.pdf'))
				sleep(4)
