
from Headervalidation import *
from selenium.webdriver.common.by import By

def test_parent_element(setup):
     try:
        driver = setup
        driver.get("https://www.guvi.in/")
        starting_element_xpath = "//a[text()='Courses']"
        starting_element = driver.find_element(By.XPATH, starting_element_xpath)
        #finding the parent element
        parent_xpath = "./parent::*"
        parent_element = starting_element.find_element(By.XPATH, parent_xpath)
        print("value: ",parent_element.text)
        #XPATH another format
        driver.find_element(By.XPATH,"//main[@class='index relative']//div[2]//div[@class='⭐️rwl3jt-0 navbar py-2 px-0']//div[4]//a[text()='Courses']").click()
        print("success")
        time.sleep(2)

     except Exception as e:
         print(f"\n An unexpected error occurred: {e}")

def test_first_child_element(setup):
    try:
        driver = setup
        driver.get("https://www.guvi.in/")
        time.sleep(2)
        xpath = "//div[@id='resources']"
        starting_element = driver.find_element(By.XPATH, xpath)
        parent_xpath = "./parent::*"
        parent_element = starting_element.find_element(By.XPATH, parent_xpath)
        #first child
        first_child_xpath = "./*[1]"
        first_child_element = parent_element.find_element(By.XPATH, first_child_xpath)
        print("first child:",first_child_element.text)
        print("success")
    except Exception as e:
        print(f"\n An unexpected error occurred: {e}")

def test_preceding_elements(setup):
        driver = setup
        driver.get("https://www.guvi.in/")
        time.sleep(2)
        driver.find_element(By.XPATH,"//main[@class='index relative']//div[2]//div[@class='⭐️rwl3jt-0 navbar py-2 px-0']//div[4]//div[@id='liveclasses']").click()
        REFERENCE_XPATH = "//div[@id='liveclasses']"
        #preceding siblings
        preceding_sibling_xpath = f"{REFERENCE_XPATH}/preceding-sibling::*"
        preceding_siblings = driver.find_elements(By.XPATH, preceding_sibling_xpath)
        for element in preceding_siblings:
            print(f"Tag Name: {element.tag_name}, Text Value: {element.text}")
        print("success")
        time.sleep(2)


def test_siblings_elements(setup):
        driver = setup
        driver.get("https://www.guvi.in/")
        driver.find_element(By.XPATH,"//main[@class='index relative']//div[2]//div[@class='⭐️rwl3jt-0 navbar py-2 px-0']//div[4]//div[@id='practices']").click()
        time.sleep(2)
        descendants = driver.find_element(By.XPATH,"//div[@class='⭐️rwl3jt-0 invisible absolute mt-2 z-50 flex w-full flex-col bg-white py-1 text-gray-800 shadow-xl group-hover:visible dropdownPractice']//ul[1]//li[1]//a")
        span_descendants = descendants.find_elements(By.CSS_SELECTOR, "*")
        print("Descendants found using XPath:")
        for element in span_descendants:
            print(f"Tag Name: {element.tag_name}, Text Value: {element.text}")
        print("success")
        time.sleep(2)


def test_parent_axis(setup):
        driver = setup
        driver.get("https://www.guvi.in/")
        axis_parent_node ="//a[@href='/sign-in/']//parent::div"
        element = driver.find_element(By.XPATH, axis_parent_node)
        print("Parent axis node:", element.tag_name)
        driver.find_element(By.LINK_TEXT, "Login").click()
        print("navigated to Guvi login page")
        print("success")
        time.sleep(2)

def test_parent_element_href_click(setup):
        driver = setup
        driver.get("https://www.guvi.in/")
        time.sleep(2)
        href_parent_xpath = "//a[@href='/register/']/parent::*"
        element = driver.find_element(By.XPATH,href_parent_xpath)
        print("Parent element of attribute href:",element.tag_name)
        driver.find_element(By.XPATH,"//main[@class='index relative']//div[2]//div[@class='⭐️rwl3jt-0 navbar py-2 px-0']//div[5]//div[@class='⭐️rawbli-0 flex gap-1 hover:bg-transparent focus:bg-white']//a[@href='/register/']").click()
        print("success")
        time.sleep(2)