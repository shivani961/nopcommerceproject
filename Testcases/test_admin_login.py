import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from BasePages.Login_Admin_Page import Login_Admin_Page
from Utilities.read_properties import Read_Config
from Utilities.custom_logger import Log_Maker

class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username =Read_Config.get_username()
    password =Read_Config.get_password()
    invalid_username =Read_Config.get_invalid_username()
    logger = Log_Maker.log_gen()



    def test_title_verification(self,setup):
        self.logger.info("********* Test_01_Admin_Login ********")
        self.logger.info("********* verification of login page title ********")

        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title ="Your store. Login"
        if act_title == exp_title:
            self.logger.info("********* Title matched *********")
            assert True
            self.driver.close()
        else:
            self.logger.info("********* Title not matched ********")
            self.driver.save_screenshot(os.getcwd()+"\\test_Admin_login.png")
            self.driver.close()
            assert False
    def test_valid_admin_login(self,setup):
        self.logger.info("*********Test_01_Admin_Login********")
        self.logger.info("********* Testing valid admin login ********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        time.sleep(2)
        self.admin_lp.click_login()
        time.sleep(4)
        act_dashboard_text = self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/h1").text
        if act_dashboard_text == "Dashboard":
            self.logger.info("********* Test case passed Dashboard found ********")
            assert True
            self.driver.close()
        else:
            self.logger.info("********* Test case failed Not found ********")
            self.driver.save_screenshot(os.getcwd()+"\\valid_login.png")
            self.driver.close()
            assert False

    def test_invalid_admin_login(self,setup):
        self.logger.info("********* Test invalid login ********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self. invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        error_message = self.driver.find_element(By.XPATH,"//li").text
        if error_message == "No customer account found":
            self.logger.info("********* Test case passed  ********")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.getcwd()+"\\third.png")
            self.driver.close()
            assert False
