from Headervalidation import *
from selenium.webdriver.common.by import By

def test_header_click(setup):
    driver = setup
    driver.get("https://www.guvi.in/")
    driver.find_element(By.ID, "login-btn").click()
    print("navigated to Guvi login page")
    driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("ashikait06@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("Positive@25")
    time.sleep(5)
    driver.find_element(By.XPATH,"//main[@class='index relative']//div[2]//div[@class='⭐️rwl3jt-0 navbar py-2 px-0']//div[4]//a[text()='Courses']").click()
    time.sleep(5)