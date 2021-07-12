from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#Variables
fp = webdriver.FirefoxProfile()
driver = webdriver.Firefox(fp)
url = https://example.com/wp-login.php?
username = "test"
password = "pass"

#Start Actions

	#Navigate to site
	driver.get(url)
	#Find Name field
	elem = driver.find_element_by_name("log")
	elem.send_keys(username)
	#Find Email field
	elem = driver.find_element_by_name("pwd")
	elem.send_keys(password)
	#Submit Button
	elem = driver.find_element_by_name("wp-submit")
	elem.send_keys(Keys.RETURN)


sleep(10)
driver.close()
