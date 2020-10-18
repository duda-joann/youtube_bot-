from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


class YoutubeSearcher:

    def __init__(self, search_word: str) -> None:
        """
        params: search word - provide by user word, for which user need to  find a result in youtube
        """
        self.search_word = search_word
        chrome_options = Options()
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("user-data-dir=selenium")
        self.driver = webdriver.Chrome(options=chrome_options)

    def close_browser(self) -> None:
        """
        function to close browser
        """
        self.driver.close()

    def open_url(self) -> None:
        """
        function  opens a browser and  looking for  result for  user request and opening first met link
        :return: function return none
        """
        self.driver.get('https://www.youtube.com/')
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/ytd-app/ytd-popup-container/paper-dialog/'
                                            'yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/'
                                            'paper-button/yt-formatted-string'))).click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                    '#introAgreeButton>div.Vwe4Vb.MbhUzd'))).click()
        except:
                print(f'no alerts')

        search = self.driver.find_element_by_name("search_query")
        search.clear()
        search.send_keys(self.search_word)
        submit_button = self.driver.find_element_by_id("search-icon-legacy")
        submit_button.click()
        WebDriverWait(self.driver, 10).until(EC.element_located_to_be_selected((By.XPATH,'//*[@id="mouseover-overlay"]'))).click()


if __name__ == '__main__':
    b = "Led Zeppelin Immigrant Song"
    YoutubeSearcher(b).open_url()
