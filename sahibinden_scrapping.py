from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# The exact location of your browser webdriver
driver = webdriver.Chrome("C:/Users/Ahmet Guler/Desktop/chromedriver.exe")

driver.get("https://banaozel.sahibinden.com/ilan-ver/adim-1/?state=new")
sleep(15)


def process_done_check():
    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/main/div[1]/div[2]/'
                                      'div[1]/div[3]/div[1]/div[2]/div/section[6]/div/div[1]/ul')
        check = False
        return check

    except NoSuchElementException:
        check = True
        return check


vasita = driver.find_element(By.XPATH,
                             '/html/body/div[1]/div[1]/div[2]/main/div[1]/div[2]/div[1]/'
                             'div[3]/div[1]/div[2]/div/div[2]/span')
sleep(2)

vasita.click()
sleep(3)

ticari = driver.find_element(By.XPATH,
                             '/html/body/div[1]/div[1]/div[2]/main/div[1]/div[2]/div[1]/'
                             'div[3]/div[1]/div[2]/div/section[2]/div/div[1]/ul/li[5]')
sleep(2)

ticari.click()
sleep(2)

category_level_1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/main/div[1]/div[2]/'
                                                 'div[1]/div[3]/div[1]/div[2]/div/section[3]/div/div[1]/ul')
sleep(2)

ticari_contents = category_level_1.find_elements(By.TAG_NAME, 'li')
sleep(2)

for ticari_content in ticari_contents[0:3]:
    ticari_content.click()
    sleep(2)
    category_level_2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/main/div[1]/div[2]/'
                                                     'div[1]/div[3]/div[1]/div[2]/div/section[4]/div/div[1]/ul')
    brands = category_level_2.find_elements(By.TAG_NAME, 'li')[:-1]

    for brand in brands:
        brand.click()
        sleep(2)
        category_level_3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/main/div[1]/div[2]/div[1]/'
                                                         'div[3]/div[1]/div[2]/div/section[5]/div/div[1]/ul')
        series = category_level_3.find_elements(By.TAG_NAME, 'li')[:-1]

        for serial in series:
            serial.click()
            sleep(2)
            process_done = process_done_check()
            if process_done:
                print('Aracı Buldum')

            else:
                category_level_4 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/main/'
                                                                 'div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/'
                                                                 'div/section[6]/div/div[1]/ul')
                models = category_level_4.find_elements(By.TAG_NAME, 'li')[:-1]

                for model in models:
                    model.click()
                    print('Aracı Buldum')
                    sleep(2)

# ahmetguler.510.pk@gmail.com

print('Süreci Bitirdim!')
sleep(2)

driver.close()
