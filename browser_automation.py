from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui as pg

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
target = "Lokesh"
msg = "Hi"
x_arg = f'//span[contains(@title, "{target}")]'

try:
    target = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    target.click()

    time.sleep(1)
    pg.typewrite(msg)
    pg.press('enter')
    time.sleep(1)
    

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()