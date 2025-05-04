from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
PROMISED_DOWN = 10
PROMISED_UP = 5
X_USERNAME = 'USERNAME'
X_PASSWORD = 'PASSWORD'
class InternetSpeedTwitterBot :
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.chrome_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        print(r'''-------------------------------------------------------------------------------------------------------------
              --------------------------------------------VISITING SPEEDTEST SITE---------------------------------------------------
              --------------------------------------------------------------------------------------------------------------''')
        self.driver.get('https://www.speedtest.net/')

        # Depending on your location, you might need to accept the GDPR pop-up.
        accept_button = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        accept_button.click()

        print(r'''-------------------------------------------------------------------------------------------------------------
              --------------------------------------------GETTING SPEED DATA---------------------------------------------------
              --------------------------------------------------------------------------------------------------------------''')
        time.sleep(3)
        click_go = self.driver.find_element(By.CSS_SELECTOR, '.start-text')
        click_go.click()
        time.sleep(30)
        self.down = self.driver.find_element(By.XPATH,
                                           value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]').text
        self.up = self.driver.find_element(By.XPATH,
                                             value='/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(r'''-------------------------------------------------------------------------------------------------------------''')
        print(f'Data Speed Fetched Sucessfully Download Speed:{self.down}, Upload Speed:{self.up}')
        print(r'''-------------------------------------------------------------------------------------------------------------''')
        

    def tweet_at_provider(self):
        print(r'''-------------------------------------------------------------------------------------------------------------
            --------------------------------------------VISITING X SIGN-IN PAGE---------------------------------------------------
            --------------------------------------------------------------------------------------------------------------''')
        self.driver.get('https://x.com/login')
        
        # Wait for email input to be present
        email_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'))
        )
        email_input.send_keys(X_USERNAME)
        email_input.send_keys(Keys.ENTER)

        # Wait for password input to be present
        password_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))
        )
        password_input.send_keys(X_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        
        print(r'''-------------------------------------------------------------------------------------------------------------
            --------------------------------------------SIGNED-IN SUCESSFULLY---------------------------------------------------
            --------------------------------------------------------------------------------------------------------------''')

        # Wait until the element is visible and clickable
        tweet_input_box = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='tweetTextarea_0']"))
        )

        print('-------------------------------------------------------------------------------------------------------------')
        print("writing post...")
        print('-------------------------------------------------------------------------------------------------------------')

        Content = f"Hey internet provider , Why is my internet speed {self.down}down/{self.up}up when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up"
        tweet_input_box.send_keys(Content)
        tweet_button = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        tweet_button.click()
        print(r'''-------------------------------------------------------------------------------------------------------------
            --------------------------------------------TWEET-ED SUCESSFULLY---------------------------------------------------
            --------------------------------------------------------------------------------------------------------------''')

if __name__ == '__main__':
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()
