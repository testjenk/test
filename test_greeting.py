from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://192.168.1.192")
my_text = driver.find_element_by_id("greeting")
print my_text
