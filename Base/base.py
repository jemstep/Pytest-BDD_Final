# import os
#
# import pytest
# from selenium import webdriver
#
#
# class Base:
#
#     @pytest.fixture(autouse=True)
#     def set_up(self):
#         print("Initiating Chrome driver")
#         currentDirectory = os.getcwd()
#         print(currentDirectory)
#         url = 'https://citiwealthbuilderqa.jemstep.com/'
#
#         self.driver = webdriver.Chrome(executable_path=currentDirectory+"/chromedriver.exe")
#         print("-----------------------------------------")
#         print("Test is started")
#         self.driver.implicitly_wait(10)
#         self.driver.get(url)
#         self.driver.maximize_window()
#
#         yield self.driver
#         if self.driver is not None:
#             print("-----------------------------------------")
#             print("Tests is finished")
#             self.driver.close()
#             self.driver.quit()
