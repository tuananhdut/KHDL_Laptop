from CrawlData import CrawlData
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import requests
from Config import Config

class CellphoneCrawlData(CrawlData):
    DOMAIN = Config["CELLPHONE"]["DOMAIN"]
    DETAIL_LINK_FILE = Config["CELLPHONE"]["DETAIL_LINK_FILE"]
    RAW_DATA_FILE = Config["CELLPHONE"]["RAW_DATA_FILE"]

    def get_detail_links(self):
        self.driver.get(f"{self.DOMAIN}/laptop.html")
        sleep(2)

        # click btn load more to show all available products
        load_more_btn = self.driver.find_element(By.CSS_SELECTOR, ".btn-show-more.btn-load-more.cta-xem-san-pham")
        try:
            while load_more_btn is not None:
                self._closePopup()
                self.driver.execute_script("window.scrollTo({ left: 0, top: 1* document.body.scrollHeight / 4, behavior: 'smooth'});")
                sleep(0.5)
                self._closePopup()
                self.driver.execute_script("window.scrollTo({ left: 0, top: 2* document.body.scrollHeight / 4, behavior: 'smooth'});")
                sleep(0.5)
                self._closePopup()
                load_more_btn = self.driver.find_element(By.CSS_SELECTOR, ".btn-show-more.btn-load-more.cta-xem-san-pham")
                load_more_btn.click()
                print("Clicked load more")
                sleep(3)
        except Exception:
            pass

        # get detail links
        soup = BeautifulSoup(self.driver.page_source, features="html.parser")
        link_details = []
        for a in soup.select(".item-product > .item-product__box-img > a"):
            link_details.append(a.get('href'))

        return link_details
    
    def get_info(self, link):
        self.driver.get(link)
        sleep(1)
        soup = BeautifulSoup(self.driver.page_source, features="html.parser")
        data = {}
        data["Title"] = soup.select_one(".box-name__box-product-name h1").get_text().strip().replace("\n", "") if soup.select_one(".box-name__box-product-name h1") else None
        data["Description"] = soup.select_one(".box-name__box-product-name p").get_text() if soup.select_one(".box-name__box-product-name p") else None
        data['Price sale'] = soup.select_one('.box-info__box-price .special-price').get_text() if soup.select_one('.box-info__box-price .special-price') else None
        data['Price origin'] = soup.select_one('.box-info__box-price .old-price').get_text() if soup.select_one('.box-info__box-price .old-price') else None
        for item in soup.select(".modal-content .box-table tr"):
            th = item.select("th")
            key = th[0].get_text()
            value = th[1].get_text()
            data[key] = value
        data['url'] = link.replace("\n", "")
        return data

    def _closePopup(self):
        try:
            closeBtn = self.driver.find_element(By.CSS_SELECTOR, ".subscriber-popup-close i#btn-close")
            if closeBtn:
                closeBtn.click()
        except Exception:
            pass

if __name__ == "__main__":
    crawler = CellphoneCrawlData()
    crawler.exec()