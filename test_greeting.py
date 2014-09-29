from selenium import webdriver
driver = webdriver.Firefox()
def test_greeting():
	driver.get("http://192.168.1.192")
	my_text = driver.find_element_by_id("greeting").text
	assert my_text == "Welcome to Ha's Home"
