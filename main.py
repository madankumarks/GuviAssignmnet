from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



class Guvi_Project:
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    # def __init__(self,username,password):
    #     self.username = username
    #     self.password = password
    #     self.driver = webdriver.Firefox()

    # A function to deffine login credentials
    def Log_in(self, username, password):
        self.username = username
        self.password = password
        driver = self.driver
        driver.get('https://www.zenclass.in/login')
        time.sleep(2)

    #using XPATH we assign the value of username, password to look and fill

        my_username = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input')
        my_username.send_keys(self.username)
        my_password = self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input')
        my_password.send_keys(self.password)
        my_password.send_keys(Keys.ENTER)
        time.sleep(2)

    #  creating the query
    def Creat_query(self):

    # define  query section
            query_section = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/nav/ul/div[6]')
            query_section.click()

            random_hover = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[1]')
            random_hover.click()

    #Creating new query
            new_query_button = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[1]/div[1]/button')
            new_query_button.click()
            time.sleep(2)

    # cancel button
            query_cancel_button = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section[3]/div[2]/button[1]')
            query_cancel_button.click()

    # In query create a new
            category_dropdown = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select')
            category_dropdown.click()
            time.sleep(2)
            category_dropdown_click = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select/option[2]')
            category_dropdown_click.click()

    # Selecting sub_category
            sub_category_dropdown = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select')
            sub_category_dropdown.click()
            time.sleep(2)
            sub_category_dropdown_click = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select/option[2]')
            sub_category_dropdown_click.click()

    #  language selection
            language_selection = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[4]/select')
            language_selection.click()
            time.sleep(1)
            language_selection_click = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[4]/select/option[2]')
            language_selection_click.click()

    #  query title details are entered
            query_title = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/div/input')
            query_title.send_keys('Guvi Python AT – 1 &2 Automation Project')

    # Query Description
            query_description = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/textarea')
            query_description.send_keys('This is a Project Test Code Running for the Python Automation – 1&2 Project Given by mentor Mr. Suman Gangopadhyay')

    # Creating the query
            create_query = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div/div/form/div[13]/div/button')
            create_query.click()





guvi = Guvi_Project()
guvi.Log_in('email', 'password')
guvi.Creat_query()