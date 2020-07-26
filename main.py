import unittest
# import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, Chrome

class BuyFigsScrubs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")

    def test_check_scrub_top(self):
        driver = self.driver
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver = Chrome(options=opts)

        driver.get("https://www.wearfigs.com/pages/shop-products/womens-catarina-scrub-top")
        self.assertIn("Scrub", driver.title)
        assert "No results found." not in driver.page_source

        color = driver.find_element_by_xpath('''//*[@id="brunswick-root"]/div[1]/div[4]/div/div[2]
        /div/div[1]/div[2]/div/main/section[3]/div[2]/div/button[4]''')
        color.click()

        size = driver.find_element_by_xpath('''/html/body/div[1]/div[1]/div[4]/div/div[2]/div/
        div[1]/div[2]/div/main/section[4]/div[3]/div/button[2]''')
        size.click()
        
        add_to_bag = driver.find_element_by_xpath('''/html/body/div[1]/div[1]/div[4]/div/
        div[2]/div/div[1]/div[2]/div/main/section[6]/button''')
        add_to_bag.click()



    def tearDown(self):
        self.driver.close()

# class BuyFigsTop(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        
    
#     def test_check_scrub_bottom(self):
#         driver = self.driver
#         opts = ChromeOptions()
#         opts.add_experimental_option("detach", True)
#         driver = Chrome(options=opts)

#         driver.get("https://www.wearfigs.com/pages/shop-products/womens-zamora-scrub-pants")
#         self.assertIn("Scrub", driver.title)

#         assert "No results found." not in driver.page_source
    

#     def tearDown(self):
#         self.driver.close()


if __name__ == "__main__":
    unittest.main()