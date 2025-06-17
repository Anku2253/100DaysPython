from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Your account details
SIMILAR_ACCOUNT = "arxsavage69"
USERNAME = "daring____devil1"
PASSWORD = "@Meatinsta"

class InstaFollower:
    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_option)
        self.wait = WebDriverWait(self.driver, 15)
        
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        
        # Login
        username = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username.send_keys(USERNAME)
        
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)
        
        # Dismiss popups
        self.dismiss_popup('//div[text()="Not now"]')  # Save login info
        self.dismiss_popup('//button[text()="Not Now"]')  # Notifications
        
    def dismiss_popup(self, xpath):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            time.sleep(2)
        except:
            pass
        
    def open_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(3)
        
        # Click followers button - more reliable locator
        followers_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f'a[href="/{SIMILAR_ACCOUNT}/followers/"]')
            )
        )
        followers_button.click()
        time.sleep(3)
        
    def scroll_and_follow(self):
        # Find the followers dialog
        dialog = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@role="dialog"]//div[contains(@style, "overflow: hidden")]')
            )
        )
        
        # Scroll and follow
        followed = 0
        scroll_attempts = 0
        
        while scroll_attempts < 5:  # Limit scroll attempts
            # Find all follow buttons in current view
            buttons = self.driver.find_elements(
                By.XPATH,
                '//div[@role="dialog"]//button[.//text()="Follow"]'
            )
            
            if not buttons:
                print("No follow buttons found, scrolling...")
                self.driver.execute_script(
                    "arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;",
                    dialog
                )
                time.sleep(random.uniform(2, 4))
                scroll_attempts += 1
                continue
            
            for button in buttons:
                try:
                    button.click()
                    followed += 1
                    print(f"Followed user {followed}")
                    time.sleep(random.uniform(3, 6))
                    
                    # Handle "Already Following" if appears
                    self.dismiss_popup('//button[text()="Cancel"]')
                    
                except Exception as e:
                    print(f"Couldn't follow: {e}")
                    continue
            
            # Scroll after processing current buttons
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;",
                dialog
            )
            time.sleep(random.uniform(2, 4))
            scroll_attempts += 1
        
        print(f"Finished! Followed {followed} users")

if __name__ == "__main__":
    bot = InstaFollower()
    bot.login()
    bot.open_followers()
    bot.scroll_and_follow()