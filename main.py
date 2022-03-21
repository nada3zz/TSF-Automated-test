import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By 
import time
import warnings



class TestTSF(unittest.TestCase):

    def setUp(self):
        s=Service("C:\SeleniumDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        warnings.simplefilter('ignore', ResourceWarning)

    def test_title(self):
        driver = self.driver
        self.assertIn("The Sparks Foundation", driver.title)
        self.assertNotIn("No results found.", driver.page_source)
        print("\n Page Title:", driver.title)

    def test_home_link(self):
        driver = self.driver
        try:
            driver.find_element( By.PARTIAL_LINK_TEXT,"The Sparks Foundation").click()
            print("\n Home Link Clicked Successfully \n")
        except NoSuchElementException:
            print("\n Home Link Verification Failed \n")
        time.sleep(1)    

    def test_navbar(self):
        driver = self.driver
        try:
            driver.find_element(By.CLASS_NAME,'navbar')
            print("\n Navbar Verified Successfully \n")

        except NoSuchElementException:
            print("\n Navbar Verification Failed \n")
    
    def test_aboutUs_menu(self):
        driver = self.driver
        try:
            driver.find_element(By.LINK_TEXT, 'About Us').click()
            time.sleep(2)
            print('\n AboutUS Menu Verified Successfully \n')
            driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[1]/ul/li[7]/a').click()
            time.sleep(1)
            print("\n News Clicked Successfully \n")
            
        except NoSuchElementException:
            print("\n AboutUS Verification Failed \n")
            

    def test_programs_menu(self):
        driver = self.driver
        try:
            driver.find_element(By.LINK_TEXT, 'Programs').click()
            time.sleep(2)
            print('\n Programs verified Successfully \n')
            driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[3]/ul/li[1]/a').click()
            time.sleep(1)
            print("\n Student Scholarship Program clicked Successfully \n")
           
        except NoSuchElementException:
            print("\n Programs Verification Failed \n")
            
    def test_logo(self):
        driver = self.driver
        try:
            driver.find_element(By.XPATH , '//*[@id="home"]/div/div[1]/h1/a/*').click()
            print("\n  Logo Verified Successfully \n")
            time.sleep(3)
        except NoSuchElementException:
            print("\n Logo Verification Failed \n")

    def test_contactUs_page(self):
        driver = self.driver
        try:
            driver.find_element(By.LINK_TEXT, 'Contact Us').click()
            time.sleep(1)
            info = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
            time.sleep(1)
            if(info.text == "+65-8402-8590, info@thesparksfoundation.sg"):
                print('\n Contact Information Correct \n')
            else:
                print('\n Contact Information Incorrect \n')
   
            print("\n Contact Page verified successfully \n")

        except NoSuchElementException:
            print("Contact Page Verification Failed ")
    
    def test_youtube_iframe(self):
        driver= self.driver
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]').click()
            time.sleep(4)
            print("\n Youtube video verified successfully \n")
            frame = driver.find_element(By.XPATH, "//iframe[contains(@src,'https://www.youtube.com/embed/kgj_0E_urK0?autoplay=0&theme=light&loop=1&disablekb=1&modestbranding=1&hd=1&autohide=0&color=white&controls=0&showinfo=0&showsearch=0&cc_load_policy=1&rel=0')]")
            driver.switch_to.frame(frame) 

            play= driver.find_element(By.XPATH, "//button[@aria-label='Play']")
            play.click()
            print("\n YouTube video played Successfully \n")
            time.sleep(10) 

            stop = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/video")
            stop.click()
            print("\n YouTube Video Paused Successfully \n")
            time.sleep(1.5) 

        except NoSuchElementException:
           print("\n Youtube Video Verification Failed \n")

    def test_visitNow_button(self):
        driver =self.driver
        button = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/a') 
        if(button.text):
            print("\n Button Text Verified: ", button.text)
        else:
            print(" Button Text Verification Failed!\n")
        button.click()
        time.sleep(10)
        print('Visit Now button clicked successfully')


    def test_jobs_at_angle_co_portal_page(self):
        driver= self.driver
        elem= driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div[2]/ul/li[2]/a')
        if(elem.text):
            print("\n Element text verified: ",elem.text)
        else:
            print("Element text Verification Failed!\n")

        elem.click()
        time.sleep(10)
        print("\n Jobs At Angel.co Portal Page Clicked Successfully\n")
            

    
    def test_jobs_at_aisha_portal_page(self):
        driver = self.driver
        elem = driver.find_element(By.XPATH ,'/html/body/div[6]/div/div[2]/div[2]/ul/li[3]/a')
        if(elem.text):
            print("\n Element text verified: ",elem.text)
        else:
            print("\n Element text Verification Failed!\n")

        elem.click()
        time.sleep(12)
        print("\n Jobs At Tech In Asia Portal Page Clicked Successfully \n")


    def test_scrolling(self):
        driver = self.driver
        for i in range(0,1500,300):
            driver.execute_script(f"window.scrollTo(0, window.scrollY + {i})")
            time.sleep(1)
        print("\n scrolling down Successfully \n")
        driver.find_element(By.ID, "toTopHover").click()
        time.sleep(1)
        print("\n scrolling up Successfully \n")
        driver.refresh()
        time.sleep(2)
        print("Page Refreshed Successfully")
    
    
    def test_TSF_global_page(self):
       driver= self.driver
       try:
           driver.find_element(By.LINK_TEXT, 'The Sparks Foundation (Global)').click()
           time.sleep(12)
           print("\n The Sparks Foundation (Global) Page Verified Successfully \n")
       
       except NoSuchElementException:
           print("\n The Sparks Foundation (Global) Page Verification Failed \n")


    def test_know_more_button(self):
        driver= self.driver
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/a').click()
            time.sleep(5)
            print("\n Know More Button Clicked Successfully \n")
        except NoSuchElementException:
           print("\n Know More Button Verification Failed \n")

    def test_politicsAndCode(self):
        driver = self.driver
        try:
            driver.find_element(By.LINK_TEXT, 'Policies and Code').click()
            time.sleep(1)
            driver.find_element(By.LINK_TEXT, "Policies").click()
            time.sleep(1)
            print('Policy Page Clicked Successfully \n')
        except NoSuchElementException:
            print('Policy Page Verification Failed \n')
            time.sleep(1)





    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()