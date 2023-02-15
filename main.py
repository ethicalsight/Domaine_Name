import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def main():
    driver = webdriver.Chrome()
    driver.get('https://www.hostpapa.com/orders/domains/step1')
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, 'domain_name'))
    )

    with open(sys.argv[1]) as f:
        for line in f.readlines():
            try:
                driver.find_element(By.NAME, 'domain_name').clear()
                driver.find_element(By.NAME, 'domain_name').send_keys(line.strip().replace("'", '')
                                                                      .replace('-', '').replace('&', 'and')
                                                                      .replace(',', '')
                                                                      .replace('|', '')
                                                                      .replace(' ', '')
                                                                      .replace('.', '')
                                                                      .replace('°', '') + '')
                driver.find_element(By.NAME, 'domain_name').send_keys(Keys.ENTER)
                driver.implicitly_wait(3)

                if len(driver.find_elements(By.NAME, 'action_doStep2')) > 0:
                    print(line)
                    driver.back()
                    driver.implicitly_wait(2)
                else:
                    continue

            except Exception as e:
                print(e)

    driver.close()


if __name__ == "__main__":
    main()