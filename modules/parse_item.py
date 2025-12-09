import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)


def search_tag(block: str, name: str) -> str | None:
    elements = driver.find_elements(By.XPATH, block)

    for el in elements:
        try:
            for inner in el.find_elements(By.XPATH, "./div/div"):

                element1 = inner.find_element(By.XPATH, ".//span")
                element2 = inner.find_element(By.XPATH, ".//span[position() = 2]")
                if element1.get_attribute('innerText').strip().find(name) != -1:
                    if element2.find_elements(By.XPATH, ".//a"):
                        return element2.find_element(By.XPATH, ".//a").get_attribute('innerText')
                    else:
                        return element2.get_attribute('innerText') if element2 else None
        except Exception as e:
            print(f"Error with block: {block}, name: {name}, Exception: {str(e)}")
            return None

    return None


def collect_chars(block: str) -> dict | None:
    characteristics = {}

    try:

        for element in driver.find_elements(By.XPATH, block):
            element1 = element.find_element(By.XPATH, ".//div/div/span")
            element2 = element.find_element(By.XPATH, ".//div/div/span[position()=2]")

            characteristics[element1.get_attribute("innerText").strip()] = element2.get_attribute("innerText").strip()
    except NoSuchElementException as e:
        pass
    return characteristics


def get_item(url: str):
    driver.get(url)
    time.sleep(1)

    element = driver.find_elements(By.XPATH, "//input[@class='quick-search-input']")

    if element:
        element = element[1]
        if element.is_displayed() and element.is_enabled():
            element.send_keys("Apple iPhone 15 128GB Black")
        else:
            print("Element is not Clickable")

    element = driver.find_element(
        By.XPATH, "//*[contains(@class, 'search-form') and contains(@class, 'header-search-form')]"
                  "/form/input[position()=2]",
    )
    if element:
        element.submit()

    try:
        element = driver.find_element(By.XPATH, "//div[@class='br-pp-imadds']/div/a")
        if element:
            element.click()
    except NoSuchElementException:
        return None

    try:
        driver.find_element(By.XPATH, "//*[@class='br-prs-button']").click()
    except ElementClickInterceptedException:
        pass

    try:
        title = driver.find_element(By.XPATH, "//*[@id='br-pr-1']/h1").get_attribute("innerText").strip()
    except NoSuchElementException as e:#
        title = None

    colour = search_tag("//div[@class='br-pr-chr-item']", "Колір")

    memory = search_tag("//div[@class='br-pr-chr-item']", "Вбудована")

    try:
        price = driver.find_element(By.XPATH, "//*[@class='price-wrapper']/span").text
    except NoSuchElementException as e:
        price = None


    try:
        action_price = driver.find_element(By.XPATH, "//span[@class='red-price']").text
    except NoSuchElementException as e:
        action_price = None

    try:
        photos = driver.find_elements(By.XPATH, "//*[@class='slick-track']/div/img")
        links = [photo.get_attribute("src") for photo in photos]
    except NoSuchElementException as e:
        links = []

    try:
        code = driver.find_element(By.XPATH, "//span[@class='br-pr-code-val']").get_attribute("innerText").strip()
    except NoSuchElementException as e:
        code = None

    try:
        reviews_count = driver.find_element(By.XPATH, "//a[@href='#reviews-list' and @class='scroll-to-element']/span")
        reviews_count = reviews_count.text
    except NoSuchElementException as e:
        reviews_count = 0

    screen_size = search_tag("//div[@class='br-pr-chr-item']", "Діагональ екрану")
    screen_power = search_tag("//div[@class='br-pr-chr-item']", "Роздільна здатність екрану")

    characteristics = collect_chars("//div[@class='br-pr-chr-item']")

    driver.quit()

    return {
        "title": title,
        "colour": colour,
        "memory": memory,
        "price": price,
        "action_price": action_price,
        "photo_links": links,
        "code": code,
        "reviews_count": reviews_count,
        "screen_size": screen_size,
        "screen_power": screen_power,
        "characteristics": characteristics,
    }
