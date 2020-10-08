from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://play2048.co/')

while True:
    try:
        board = driver.find_element_by_xpath('/html/body')
        board.send_keys(Keys.UP)
        board.send_keys(Keys.RIGHT)
        board.send_keys(Keys.DOWN)
        board.send_keys(Keys.LEFT)
    except KeyboardInterrupt:
        break