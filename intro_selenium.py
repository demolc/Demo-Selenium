from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://ludivinecrepin.fr/selenium/intro.html")

# find_element retourne le premier tag trouvé
body = driver.find_element(By.TAG_NAME, 'body')

# find_elements retourne une liste de tags trouvés
inputs = driver.find_elements(By.TAG_NAME, 'input')


# par id ou xpath
input_user = driver.find_element(By.ID, 'user')
input_msg = driver.find_element(By.XPATH, '/html/body/form/input[2]')


# attends que le button soit présent sur la page
wait = WebDriverWait(driver, timeout=2)
btn = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'button')))


input_user.send_keys('toto')
input_msg.send_keys('hello')
input_submit = driver.find_element(By.XPATH, '//*[@id="send"]')
input_submit.click()

driver.close()
driver.quit()


