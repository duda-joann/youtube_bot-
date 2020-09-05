from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



class YoutubeSearcher:

    def __init__(self, search_word: str) -> None:
        self.search_word = search_word

    def open_url(self) -> None:
        chrome_options =Options()
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("user-data-dir=selenium")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.youtube.com/')
        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/ytd-app/ytd-popup-container/paper-dialog/'
                                            'yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/'
                                            'paper-button/yt-formatted-string'))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                    '#introAgreeButton>div.Vwe4Vb.MbhUzd'))).click()
        except:
                print(f'no alerts')

        search = driver.find_element_by_name("search_query")
        search.clear()
        search.send_keys(self.search_word, Keys.RETURN)
        #submit_button = driver.find_element_by_id("search-icon-legacy")
        #driver.implicitly_wait(10)
       #ActionChains(driver).move_to_element(submit_button).click(submit_button).perform()
        #submit_button.click()


if __name__ == '__main__':
    b = "Led Zeppelin Immigrant Song"
    YoutubeSearcher(b).open_url()
