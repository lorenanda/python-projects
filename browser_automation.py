# A Python-Selenium script that automates opening a webpage in Chrome, closing a pop-up ad, filling in a text field, clicking on a submit button, and finally closing the window.

from selenium import webdriver

chrome_browser = webdriver.Chrome('chromedriver')
#print(chrome_browser)
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# check if some text is in the page
assert 'Selenium Easy Demo' in chrome_browser.title

# extract a button from the webpage
show_message_button = chrome_browser.find_element_by_class_name("btn-default")
#print(show_message_button.get_attribute("innerHTML"))

assert "Show Message" in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id("user-message")
user_button = chrome_browser.find_element_by_css_selector("#get-input > .btn")
print(user_button)
user_message.clear()

# close pop-up ad
popup_ad = chrome_browser.find_element_by_class_name("at4-close")
popup_ad.click()


# type in the text field
user_message.send_keys("testy test")

# click on the button
show_message_button.click()

output_message = chrome_browser.find_element_by_id("display")
assert "testy test" in output_message.text

# close the browser
chrome_browser.close()