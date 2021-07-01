from bs4 import BeautifulSoup
from selenium import webdriver
import csv
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("start-maximized")
url = r"https://hi.krishnakosh.org/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4%B5%E0%A4%A8_%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%B5_%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF_155_%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%8B%E0%A4%95_1-23"

driver = webdriver.Chrome(options=options, executable_path=r'./chromedriver')
driver.get(url)


filename = "./data/Hindi.txt"
with open(filename, 'a') as txtfile:

    for i in range(155, 315):
        if i != 0:
            driver.find_element_by_xpath('//img[@alt="Next.png"]').click()

        html = driver.page_source

        soup = BeautifulSoup(html, "html.parser")
        body = soup.find_all('tbody')[5].findChildren('tr')[
            0].findChildren(recursive=False)[1].findChildren(recursive=False)
        for ele in body:
            if ele.name != 'div':
                txtfile.write(ele.text)
        print(i)
