from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://ludivinecrepin.fr/selenium/")

# nous testons qu'au moins deux post sont affichés
# les données des posts peuvent changer
wait = WebDriverWait(browser, timeout=20)
post2 = wait.until(EC.presence_of_element_located((By.ID, 'post-2')))
titrepost1 = browser.find_element(By.XPATH, '/html/body/div[1]/h2').text

bouton = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="1"]')))
bouton.click()

returnBouton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/button')))
titre = browser.find_element(By.TAG_NAME, 'h2').text
# vérifier que titre et titrepost1 ont le même texte 
# pour être sûr que le bon post soit affiché

# retourner sur la liste
returnBouton.click()
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/button')))

browser.close()
browser.quit()
