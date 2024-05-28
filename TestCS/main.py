# Author: oneelsons

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = ""
browser.get(url)


# Logical construct for simplified method creation
def element(xpath, bol, key):
    if bol == 1:
        browser.find_element(By.XPATH, xpath).click()
    elif bol == 0:
        browser.find_element(By.XPATH, xpath).send_keys(key)


def sleep(sec):
    time.sleep(sec)


def main():
    # Accepting cookies and log in
    element('//*[@id="cookies"]', 1)
    element('/html/body/div[2]/div/div[2]/div/div/div/form/table/tbody/tr[1]/td/input', 0, 'login')
    element('/html/body/div[2]/div/div[2]/div/div/div/form/table/tbody/tr[2]/td/input', 0, 'password')
    element('/html/body/div[2]/div/div[2]/div/div/div/form/table/tbody/tr[4]/td/input', 1)

    # Cycle for n times repetition of entering questions into the website
    for j in range(100):
        element('/html/body/div[5]/div[3]/form/div/div[3]/div[1]/div[1]/div[2]/a', 1)
        sleep(3)

        # Accepting cookies
        try:
            element('//*[@id="cookies"]', 1)
        except Exception as e:
            pass

        # Opening the document to read and write questions
        with open('Questions.txt', 'r+', encoding='utf8') as file:
            str1 = file.readline()  # Read first line
            element('/html/body/div[5]/div[3]/form/div/div/div[4]/div/div/span', 1)
            element('/html/body/div[5]/div[3]/form/div/div/div[4]/div/div/span', 1)
            element('/html/body/div[5]/div[3]/form/div/div/div[2]/div/textarea', 0, str1)

            # Insert the answers into the fields
            element('/html/body/div[5]/div[3]/form/div/div/div[3]/div/div[2]/input[2]', 0, 'Никогда - 1')
            element('/html/body/div[5]/div[3]/form/div/div/div[3]/div/div[3]/input[2]', 0, 'Редко - 2')
            element('/html/body/div[5]/div[3]/form/div/div/div[3]/div/div[4]/input[2]', 0, 'Иногда - 3')
            element('/html/body/div[5]/div[3]/form/div/div/div[3]/div/div[5]/input[2]', 0, 'Чаще всего - 4')
            element('/html/body/div[5]/div[3]/form/div/div/div[3]/div/div[6]/input[2]', 0, 'Очень часто - 5')

            # Right answer
            element('//*[@id="ans_6"]', 1)

            # Clearing a used string
            d = file.readlines()
            file.seek(0)
            for i in d:
                if i != "1 line":
                    file.write(i)
            file.truncate()
            sleep(3)
        element('/html/body/div[5]/div[3]/form/div/div/div[6]/div/button', 1)
        sleep(3)

    sleep(15)
    browser.close()


if __name__ == "__main__":
    main()
