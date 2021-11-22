from selenium import webdriver
import time

def get_driver():
  #Set options to make browser easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://titan22.com/account/login?return_url=%2Faccount")
  return driver

# Scraping the static text of the website
def main():
  driver = get_driver()
  driver.find_element(by="id", value="CustomerEmail").send_keys("app7flask@gmail.com")
  time.sleep(2)
  driver.find_element(by="id", value="CustomerPassword").send_keys()
  time.sleep(2)


print(main())
