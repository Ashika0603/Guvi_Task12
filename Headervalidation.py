from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


@pytest.fixture(scope="session")
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
    print("\nWebDriver closed.")

def headerValidation(setup):
    driver = setup
    driver.get("https://www.guvi.in/")
    starting_element_xpath = "//a[text()='Courses']"
    starting_element = driver.find_element(By.XPATH, starting_element_xpath)
    # finding the parent element
    parent_xpath = "./parent::*"
    parent_element = starting_element.find_element(By.XPATH, parent_xpath)
    print("value: ", parent_element.text)
    time.sleep(2)
    xpath = "//div[@id='resources']"
    starting_element = driver.find_element(By.XPATH, xpath)
    parent_xpath = "./parent::*"
    parent_element = starting_element.find_element(By.XPATH, parent_xpath)
    #first child
    first_child_xpath = "./*[1]"
    first_child_element = parent_element.find_element(By.XPATH, first_child_xpath)
    print("first child:", first_child_element.text)
    time.sleep(2)
    driver.find_element(By.XPATH,"//main[@class='index relative']//div[2]//div[@class='⭐️rwl3jt-0 navbar py-2 px-0']//div[4]//div[@id='practices']").click()
    time.sleep(2)
    descendants = driver.find_element(By.XPATH,"//div[@class='⭐️rwl3jt-0 invisible absolute mt-2 z-50 flex w-full flex-col bg-white py-1 text-gray-800 shadow-xl group-hover:visible dropdownPractice']//ul[1]//li[1]//a")
    span_descendants = descendants.find_elements(By.CSS_SELECTOR, "*")
    print("Descendants found using XPath:")
    for element in span_descendants:
        print(f"Tag Name: {element.tag_name}, Text Value: {element.text}")
    time.sleep(2)
    axis_parent_node = "//a[@href='/sign-in/']//parent::div"
    element = driver.find_element(By.XPATH, axis_parent_node)
    print("Parent axis node:", element.tag_name)
    driver.find_element(By.ID, "login-btn").click()
    print("navigated to Guvi login page")
    print("success")