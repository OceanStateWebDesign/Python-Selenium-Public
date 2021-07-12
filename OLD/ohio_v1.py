import os
import string
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import date
from datetime import datetime, timedelta
from PyPDF2 import PdfFileReader

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
#countyfile =
#agencyfile =
#Start Actions

#For each County in file
for county in range(1):
	for agency in range(1):

		driver.get(url)

		#Start Search Date
		elem = driver.find_element_by_name("Parameters.CrashStartDate")
		#elem.click()
		sleep(1)
		elem.clear()
		sleep(1)
		elem.send_keys(startdate.strftime("%m/%d/%Y"))

		#End Search Date
		elem = driver.find_element_by_name("Parameters.CrashEndDate")
		#elem.click()
		sleep(1)
		elem.clear()
		sleep(2)
		elem.send_keys(enddate.strftime("%m/%d/%Y"))
		sleep(1)

	#Select County from Dropdown
	elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/form/div/div/div[2]/div[3]/div[2]/div[2]/select/option[8]")
	sleep(1)
	elem.click();
	sleep(2)

	#Select Agency from Dropdown
	#elem  driver.find.element_by_xpath("/html")
	#sleep(1)
	#elem.click()
	#sleep(2)

	#CAPTCHA Code - 3rd party code goes here
	elem = driver.find_element_by_xpath("//*[@id='txtCaptcha']")
	elem.click();
	sleep(6)

	#Click the Search Button
	elem = driver.find_element_by_name("btnSearch")
	elem.send_keys(Keys.RETURN)

	sleep(2)

	#Download Results
	for report in driver.find_elements_by_xpath("//*[contains(@id, 'btn')] "):

		sleep(1)
		report.click()
		sleep(5)

#I think i can remove the code below becuase auto pdf download now?
#		another_window = list(set(driver.window_handles) - {driver.current_window_handle})[0]
#		driver.switch_to.window(another_window);
#		sleep(2);
#		driver.close();
#		driver.switch_to.window(default_handle);

		with open('/home/regor/Downloads/GetReport', 'rb') as pdf:

			enddate = date.today()
			search1 = "ERROR" + '\n' + "5"
			reader = PdfFileReader(pdf)
			contents = reader.getPage(0).extractText().split('\n ')[4]
			pass

			if search1 in contents:
				print("The PDF has Property Damage Only '5' - NOT Saving")
				os.remove('/home/regor/Downloads/GetReport')

			else:
				print("The PDF Passes Checks -> Saving and creating Master PDF")
				os.rename('/home/regor/Downloads/GetReport', './'+enddate.strftime("%m-%d-%Y"+'.pdf'))

