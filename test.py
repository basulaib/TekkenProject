from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import datetime

now = datetime.datetime.now()

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path='D:/Downloads/chromedriver.exe', options=options)
driver.get('http://rbnorway.org/t7-frame-data/')
pars = driver.find_elements_by_tag_name('p')
link = driver.find_elements_by_link_text('S2')
for y in link:
    y.click()
    #driver.get(y.get_attribute('href'))
    print(driver.current_url)
    # heading = driver.find_elements_by_tag_name('h3')
    # #print(heading[0].text)
    # #print(heading[1].text)
    # title = driver.find_element_by_class_name('title')
    # print(title.text)
    # print(now)
    # print()
    # trs = driver.find_elements(By.TAG_NAME, "tr")
    # n = 1
    # for i in trs:
    #     tds = i.find_elements(By.TAG_NAME, "td")
    #     print(n, end=" ")
    #     for j in range(0, 8):
    #         print(tds[j].text, end=" ")
    #     print()
    #     n += 1
    # # driver.save_screenshot('C:\\Users\\Abu\\Desktop\\headless.png')
if __name__ == "__main__":
    pass