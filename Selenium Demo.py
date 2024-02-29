from selenium import webdriver
import time

from selenium.webdriver.common.by import By


# Function to verify page title
def verify_page_title(driver, expected_title):
    actual_title = driver.title
    assert actual_title == expected_title, f"Expected title: {expected_title}, but found: {actual_title}"


# Function to verify text on the page
def verify_text_on_page(driver, expected_text):
    page_text = driver.find_element(By.TAG_NAME, "h3").text

    assert page_text == expected_text, f"Expected text: {expected_text}, but found: {page_text}"


# Function to verify checkboxes status
def verify_checkboxes(driver, checkbox1_status, checkbox2_status):
    checkbox1 = driver.find_element(By.XPATH, "//input[@type='checkbox'][1]")
    checkbox2 = driver.find_element(By.XPATH, "//input[@type='checkbox'][2]")
    assert checkbox1.is_selected() == checkbox1_status, f"Checkbox 1 is not checked as expected"
    assert checkbox2.is_selected() == checkbox2_status, f"Checkbox 2 is not checked as expected"


# Function to upload a file
def upload_file(driver, file_path):
    upload_button = driver.find_element(By.ID,"file-upload")
    upload_button.send_keys(file_path)
    driver.find_element(By.ID,"file-submit").click()


# Launching the browser
driver = webdriver.Chrome()
driver.maximize_window()
# Task 1: Verify page title
driver.get("http://the-internet.herokuapp.com/")
verify_page_title(driver, "The Internet")

# Task 2: Click on Checkboxes link and verify text and checkbox status
driver.find_element(By.XPATH, "//a[@href='/checkboxes']").click()
verify_text_on_page(driver, "Checkboxes")
verify_checkboxes(driver, False, True)

# Task 3: Navigate back to home page
driver.back()

# Task 4: Click on File Upload link and upload a file
driver.find_element(By.XPATH, "//a[@href='/upload']").click()
upload_file(driver,"/Users/piyush/Documents/Python Project.pdf")

time.sleep(5)
