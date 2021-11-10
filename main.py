from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os


def write_message():
    # Replace below path with the absolute path
    # to chromedriver in your computer
    path = r'C:\Users\andrz\Downloads\chromedriver.exe'  # path to your chromedriver
    file_available = os.path.isfile(path)
    print(file_available)
    if file_available:
        driver = webdriver.Chrome(executable_path=path)

        driver.get("https://web.whatsapp.com/")

        wait = WebDriverWait(driver, 500)

        # Define Friend and Message
        target = '"THE NAME OF YOUR WHATSAPP CONTACT"'
        my_message_list = ["The first message", "The second message?", "The third message", "it's just a list"]

        # Find Friend Contact
        x_arg = '//span[contains(@title,' + target + ')]'
        group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        group_title.click()

        # Find Message Input Field
        inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

        # Send Message
        for phrase in my_message_list:
            input_box.send_keys(phrase + Keys.ENTER)
            time.sleep(1)


if __name__ == "__main__":
    write_message()
