Em đã kết hợp `Selenium` để xử lý các trang web động và `BeautifulSoup` để bóc tách, trích xuất dữ liệu từ HTML. 

Ngoài ra, để tránh bị chặn bởi lỗi 429, em đã dùng thư viện `time` tạo khoảng nghỉ giữa các yêu cầu, giúp quá trình crawl ổn định hơn.

<aside>
💡

Lưu ý

- Để **đơn giản hóa** và giúp mọi người dễ hình dung luồng xử lý chính, em đã **ẩn đi các lệnh** `time.sleep()` trong phần giải thích code
</aside>


Em sẽ chia bài toán crawl data ra thành các phần nhỏ để mọi người có thể hiểu lối tư duy và hướng làm của em

### Task 1: Vào website TopCV

Để điều khiển trình duyệt, em sử dụng **ChromeDriver** để `Selenium` tương tác với Google Chrome. 

Vì TopCV là một trang web công khai không yêu cầu đăng nhập, việc truy cập ban đầu rất đơn giản, chỉ cần thực thi lệnh `.get()` để tải trang

```python
driver = webdriver.Chrome()
url = 'https://www.topcv.vn/'
driver.get(url)
```

### Task 2: Search loại Job muốn Crawl

Khi muốn tăng tác với các vật thể, em sẽ sử dụng lệnh `.find_element()` để xác định vị trí vật thể

> *Thực chất ở đây để ngắn gọn code thì có thể dùng luôn `.find_element(By.ID, 'keyword')`*
> 

→ Từ đó chọn các lệnh tương tác phù hợp

```python
finding = 'Data Analyst'

search = driver.find_element(By.XPATH, '//*[@id="keyword"]')
search.send_keys(finding) 
search.send_keys(Keys.RETURN) 
```

### Task 3: Mở URLs của từng tin tuyển dụng

Sau khi tìm kiếm, trang kết quả sẽ hiển thị một danh sách nhiều tin tuyển dụng. Nhiệm vụ ở bước này là lấy link (URL) chi tiết của từng tin đó và lưu lại.

**FUNCTION 1: Trích xuất toàn bộ URL trong 1 trang** 

Cách tiếp cận của em khá tương tự Task 2, nhưng có hai điểm khác biệt chính:

- **Sử dụng `find_elements()`:** vì có nhiều tin tuyển dụng cần lấy, em sử dụng phương thức `find_elements()`  để tìm **tất cả** các phần tử khớp với điều kiện và trả về một List URL
- **Định vị bằng `CLASS`:** em nhận thấy mỗi tin tuyển dụng trên trang đều được bao bọc trong một khối HTML có chung một `class` nên sử dụng `By.CSS_SELECTOR` để định vị.

> *Trong trường hợp này, có thể dùng `.find_element(By.CLASS, '')` nhưng sẽ dễ bị lỗi data trích xuất do các `class` được tái sử dụng chung trên trang*
> 

```python
def get_job_url() : 
    job_links = driver.find_elements(By.CSS_SELECTOR, ".job-item-search-result")
    job_list = []

    for job in job_links:
        a = job.find_element(By.CSS_SELECTOR, ".title a")
        full_url = a.get_attribute('href')
        # trimmed_url = full_url.split('.html')[0]
        job_list.append(full_url)

    return job_list
```

**FUNCTION 2: Trích xuất URL trong toàn bộ trang** 

Dữ liệu tuyển dụng thường được chia thành nhiều trang. Để có thể thu thập toàn bộ thông tin mà không bỏ sót, scraper cần có khả năng tự động chuyển qua các trang tiếp theo.

Em tạo một vòng lặp (`while loop`) để liên tục thực hiện chu trình sau:

1. **Thu thập dữ liệu trang hiện tại:** gọi lại hàm `get_job_url()` 
2. **Tìm nút Next:** dùng `try-except` để tìm kiếm nút Next nếu trang không có nút Next → tức là trang cuối cùng →  `break` ngắt vòng lặp

```python
def get_url_allpage():    
    URL_all_page = []

    while True:
        URL_one_page = get_job_url()
        URL_all_page += URL_one_page

        next_buttons = driver.find_elements(By.CSS_SELECTOR, "a[rel='next']")       
        if not next_buttons:
            break  

        next_button = next_buttons[0]
        driver.execute_script("arguments[0].click();", next_button)
        sleep(3)
        
    return URL_all_page
```

### Task 4: Crawl Data + extract vào file CSV

Đây là bước cuối cùng và cũng là bước cốt lõi của quá trình thu thập dữ liệu. Với danh sách URL đã có từ các bước trước, em sẽ thực hiện một quy trình tự động để "đọc" nội dung của từng trang.

> TopCV
> 

Em sẽ chia 1 page tuyển dụng ra làm 4 section nhỏ cho việc extract thông tin

1. header_div: phần header trên cùng
2. company_div: phần thông tin công ty ở góc trên bên phải
3. skill_div: đây là phần khoanh đỏ ở phía dưới company_div nhưng do em chỉ extract mỗi **Skills** nên gọi là skill_div
4. detail_div: phần chi tiết tuyển dụng

![image.png](attachment:971171ec-9815-4e98-ad4f-fe04ba8882c7:image.png)

Luồng xử lý được thực hiện như sau:

- **Tạo vòng lặp:** một vòng lặp `for` được tạo để duyệt qua từng URL trong danh sách đã thu thập.
- **Tải trang và Phân tích HTML:** em dùng`Selenium`để truy cập và tải toàn bộ nội dung của trang tuyển dụng. Rồi, em tải HTML Doc bằng `BeautifulSoup` để dễ dàng extract thông tin.
- **Trích xuất các trường thông tin:** cuối cùng, em sử dụng `.find()` và `.find_all()` để định vị chính xác các trường thông tin cần thiết.

Vì phần skill_div thường không phải lúc nào thông tin cũng cố định mà có thể thay đổi tùy theo Nhà Tuyển dụng

> Hướng xử lý
> 
1. Vòng lặp `for` và xét từng mục trong skill_div 
2. Crawl data ở mục nào có **title** là “*Kỹ năng cần có*” và “*Kỹ năng nên có*” 

> Full Thông tin
> 

![image.png](attachment:62c87e05-9ff1-4c70-9233-dcb6e66c4787:image.png)

> Thiếu thông tin
> 

![image.png](attachment:0ea9db32-eab4-4d24-94f7-f3eccb64330b:image.png)

> Code
> 

```python
for i in range(len(URL)):

    driver.get(URL[i])
    page_source = BeautifulSoup(driver.page_source, "html.parser")

    header_div = page_source.find('div', class_="job-detail__info") 
    # 1.1 Title
    job_title_div = header_div.find_all('h1', class_="job-detail__info--title")
    job_title = job_title_div[0].get_text().strip()
    # 1.2 Salary
    salary_div = header_div.find_all('div', class_="job-detail__info--section-content-value")
    salary = salary_div[0].get_text().strip()
    # 1.3 Place
    place = salary_div[1].get_text().strip()
    # 1.4 YOE
    yoe = salary_div[2].get_text().strip()

    # 2. Company Info
    company_div = page_source.find('div', class_="job-detail__box--right job-detail__company")
    company_name_div = company_div.find_all('div', class_="company-name")
    company_name = company_name_div[0].get_text().strip()
    company_no_emp = company_div.find_all('div', class_="company-value")[0].get_text().strip()
    company_industry = company_div.find_all('div', class_="company-value")[1].get_text().strip()

    # 3. Skills
    require_skill_div = ''
    add_skill_div = ''

    skill_div = page_source.find('div', class_="job-detail__box--right job-detail__body-right--item job-detail__body-right--box-category")
    if skill_div:
        titles = skill_div.find_all('div', class_="box-title")
        skill_tags = skill_div.find_all('div', class_="box-category-tags")

        for idx, title_tag in enumerate(titles):
            title_text = title_tag.get_text()

            skill_content = skill_tags[idx].get_text()

            if title_text == "Kỹ năng cần có":
                require_skill_div = skill_content
            elif title_text == "Kỹ năng nên có":
                add_skill_div = skill_content

    # 4. Job Detail
    detail_div = page_source.find_all('div', class_="job-description__item")
    job_description = detail_div[0].get_text().strip()
    job_requirement = detail_div[1].get_text().strip()
    job_benefit = detail_div[2].get_text().strip()
    job_schedule = detail_div[4].get_text().strip()
```

Dữ liệu được lưu vào file CSV bằng thư viện `csv` của Python. Em có dùng thêm encoding ‘utf-8’ để tránh bị lỗi khi upload ngôn ngữ Tiếng Việt lên

```python
with open('output2.csv', 'w', newline='', encoding='utf-8-sig') as file_output:
    headers = [
		# ...
    ]
    writer = csv.DictWriter(file_output, delimiter=',', lineterminator='\n', fieldnames=headers)
    writer.writeheader()
    
    writer.writerow({
		# ...
        })
```

## 2.2 Transform
