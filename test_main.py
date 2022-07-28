import main
from selenium.webdriver.common.by import By

g = main.Guvi_Project()
url = 'https://www.zenclass.in/'

def test_Login():
    g.Log_in('email', 'password')
    assert g.driver.current_url == 'https://www.zenclass.in/class'

def test_Query():
    g.Creat_query()
    assert g.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/span').text == 'Guvi Python AT – 1 &2 Automation Project'
    driver.close()