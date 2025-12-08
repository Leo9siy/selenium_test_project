import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)

def get_item(url):
    driver.get(url)
    time.sleep(1)

    element = driver.find_elements(By.CSS_SELECTOR, "input.quick-search-input")

    if element:
        element = element[1]
        if element.is_displayed() and element.is_enabled():
            element.send_keys("Apple iPhone 15 128GB Black")
        else:
            print("Элемент не доступен для клика.")

    element = driver.find_elements(By.CSS_SELECTOR, ".search-form.header-search-form > form > input:nth-child(2)")

    if element[1]:
        element[1].click()

    element = driver.find_elements(By.CSS_SELECTOR, "div.br-pp-imadds > div > a")
    element[0].click()

    title = driver.find_element(By.CSS_SELECTOR, "h1.main-title").text
    colour = driver.find_element(By.CSS_SELECTOR, "div.series-item.series-color.current > a > ul > li > div").get_attribute("style")

    memory = driver.find_element(By.CSS_SELECTOR, ".br-pr-chr-item > div > div > span:nth-of-type(2) > a").text
    price = driver.find_element(By.CSS_SELECTOR, ".price-wrapper > span").text

    action_price = driver.find_element(By.CSS_SELECTOR, ".red-price")
    if action_price:
        action_price = action_price.text

    photos = driver.find_elements(By.CSS_SELECTOR, ".slick-track > div > img")
    links = [photo.get_attribute("src") for photo in photos]

    code = driver.find_element(By.CSS_SELECTOR, "span.br-pr-code-val").text


    elements = driver.find_elements(By.CSS_SELECTOR, 'a[href="#reviews-list"].scroll-to-element > span')
    reviews_count = element[0].text if elements else 0

    screen_size = driver.find_element(By.CSS_SELECTOR, "div.br-pr-chr > .br-pr-chr-item:nth-child(2) > div > div > span > a").text
    screen_power = driver.find_element(By.CSS_SELECTOR, "div.br-pr-chr > .br-pr-chr-item:nth-child(3) > div > div > span > a").text


    characteristic = {}
    for element in driver.find_elements(By.CSS_SELECTOR, ".br-pr-chr-item > div > div"):
        characteristic[element.find_element(By.CSS_SELECTOR, "span:first-of-type").text] =\
            element.find_element(By.CSS_SELECTOR, "span:nth-of-type(2)").text

    return {
        "title": title,
        "colour": colour,
        "memory": memory,
        "price": price,
        "action_price": action_price,
        "links": links,
        "code": code,
        "reviews_count": reviews_count,
        "screen_size": screen_size,
        "screen_power": screen_power,
        "characteristic": characteristic
    }

print(get_item("https://brain.com.ua/ukr/"))
