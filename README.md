## 1. Cào dữ liệu
### 1.1 Driver chrome

* Nhóm đã chuẩn bị 2 driver (Window/Mac) cho chrome phiên bản 102 ở đường link: https://drive.google.com/open?id=1wbUZiWvLFbKEnOLG2UXrYFHSBzl5RR7y , download về thư mục `./driver_chrome/`
* Driver chrome hiện đã giải nén là giành cho Window.
* Nếu là MacOS thì giải nén file: `./driver_chrome/chromedriver_mac64.zip`
* Nếu thầy đang sử dụng chrome phiên bản khác 102 thì vào link sau để tải driver tương ứng với phiên bản chrome đang dùng: `https://chromedriver.chromium.org/downloads`
* NOTE: lưu ý không tải và sử dụng chrome phiên bản 103 (bản mới nhất tính tới thời điểm hiện tại), vì có 1 số issue liên quan đến Selenium. Link issue: `https://github.com/SeleniumHQ/selenium/issues/10799`

### 1.2 Cài đặt package

Cài đặt các package cần thiết
```
pip install -r requirements.txt
```

### 1.3 Điều chỉnh thông số cấu hình
Truy cập file `./crawl_code/Config.py` để chỉnh các thông số cấu hình
### 1.4 Cào dữ liệu
Chạy lệnh sau để cào dữ liệu:
```
cd crawl_code
python FptCrawlData.py
python CellphoneCrawlData.py
python PhilongCrawlData.py
```

## 2. Chạy file notebook (Cần cài đặt pandas, numpy, scikit-learn, eli5)
* Lưu ý:
    - Chỉ chạy code notebook ở phần 2.2 trở về sau
    - Cập nhật biến DATASET ở phần 3 thành đường dẫn đến file csv ở phần 2

