from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://rbnorway.org/armor-king-t7-frames/')
print(driver.current_url)
if __name__ == "__main__":
    pass