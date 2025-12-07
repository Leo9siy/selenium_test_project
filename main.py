import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)

driver.get("https://brain.com.ua/ukr/")
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
memory = driver.find_element(By.CSS_SELECTOR, ".series-item.series-characteristic.current.on-mob > a").text
price = driver.find_element(By.CSS_SELECTOR, ".price-wrapper > span").text

action_price = driver.find_element(By.CSS_SELECTOR, ".red-price")
if action_price:
    action_price = action_price.text

photos = driver.find_elements(By.CSS_SELECTOR, ".slick-track > div > img")
links = [photo.get_attribute("src") for photo in photos]

code = driver.find_element(By.CSS_SELECTOR, "span.br-pr-code-val").text

reviews_count = driver.find_element(By.CSS_SELECTOR, "a['href=#reviews_list'] > span").text


screen_size = driver.find_element(By.CSS_SELECTOR, "div.br-pr-chr > .br-pr-chr-item:nth-child(2) > div > div > span > a").text
screen_power = driver.find_element(By.CSS_SELECTOR, "div.br-pr-chr > .br-pr-chr-item:nth-child(3) > div > div > span > a").text


characteristic = {}
for element in driver.find_elements(By.CSS_SELECTOR, ".br-pr-chr-item > div > div"):
    characteristic[element.find_element(By.CSS_SELECTOR, "span:first-of-type").text] =\
        element.find_element(By.CSS_SELECTOR, "span:nth-of-type(2)").text


time.sleep(30)


# -Полное название товара
# -Цвет
# -Объем памяти
# -Продавец
# -Цена обычная
# -Цена акционная (если есть)
# -Все фото товара. Здесь нужно собрать ссылки на фото и сохранить в список
# -Код товара
# -Кол-во отзывов
# -Серия
# -Диагональ экрана
# -Разрешение дисплея
# -Характеристики товара. Все характеристики на вкладке. Характеристики собрать как словарь


# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
time.sleep(200)