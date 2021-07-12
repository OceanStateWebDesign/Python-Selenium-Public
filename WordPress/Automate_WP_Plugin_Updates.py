from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#Variables
fp = webdriver.FirefoxProfile()
driver = webdriver.Firefox(fp)
url =" https://example/wp-login.php"
updatepage = "https://example.com/wp-admin/update-core.php"
username = "admin"
password = "password"

#Start Actions

#Login as Admin
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

sleep(5)

#Navigate to Updates Page
driver.get(updatepage)
#Click the Plugins 'select all' checkbox
elem = driver.find_element_by_xpath("//*[@id='plugins-select-all']").click()

elem = driver.find_element_by_xpath("//*[@id='upgrade-plugins']")
elem.send_keys(Keys.RETURN)

driver.close()
