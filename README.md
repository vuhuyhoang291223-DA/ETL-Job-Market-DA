# ETL-Job-Market-DA
[Full ETL process to find out what is needed in the Data Analyst Job Market in Vietnam]

Khi thị trường Data Analyst ngày càng cạnh tranh, việc có một cái nhìn sâu sắc về nhu cầu tuyển dụng là vô cùng quan trọng. Để giải quyết bài toán này, em đã phát triển một hệ thống tự động nhằm cung cấp insight về thị trường việc làm DA tại Việt Nam.

Project của em bao gồm các phần chính sau:

- **Extract**: dùng Python crawl dữ liệu từ web tuyển dụng TopCV.

- **Transform**: làm sạch dữ liệu thô và chuẩn hóa lại các thông tin cần thiết quan trọng.

- **Load**: dữ liệu tải lên Google Sheets thông qua API, từ đó em tạo ra một dashboard tối giản, tập trung vào chỉ số cốt lõi nhất về thị trường.

## Insights

<aside>
    
###💡 **1/ Cấp độ tuyển dụng**

</aside>

Nhu cầu tuyển dụng tập trung mạnh nhất vào nhóm có **1-3 năm kinh nghiệm (YOE)**.

- **1-3 YOE:** 260 jobs (75.58%)

⇒ Điều này cho thấy thị trường có nhu cầu cao đối với các Data Analyst đã có nền tảng và có thể nhanh chóng bắt đầu công việc.

- **Không yêu cầu kinh nghiệm + Dưới 1 năm kinh nghiệm** (0-0.5YOE): 51 jobs (14.82%)

⇒ Vẫn cởi mở cho người mới

![image.png](attachment:b9f1b8ec-7b5b-4ffe-b5d3-091958098e54:image.png)

<aside>
    
###💡 **2/ Địa điểm làm việc**

</aside>

- **TP.HCM & Hà Nội:** 300 jobs (**87.2%**)

![image.png](attachment:c3b0d16e-16ec-4dff-8bb0-92b1857eeaa6:image.png)

<aside>
    
###💡 **3/ Ngành nghề** 

</aside>

- Ngành nghề IT áp đảo, ngoài ra còn có một số ngành nghề khác chiếm tỷ trọng lớn như Tài chính và Marketing

**⇒ Insights:** tập trung học domain/kiến thức liên quan đến những ngành nghề nổi bật để lấy lợi thế

- Data phân nhóm
    - **IT - phần mềm**: 124 jobs (36%)
    - **Tài chính + Ngân hàng + Chứng khoán**: 47 jobs (13.7%)
    - **Viễn thông + truyền thông / marketing**: 32 jobs (9.3%)
    - **Sản xuất**: 23 jobs (6.7%)
    - **Bán lẻ, tiêu dùng**: 19 jobs (5.5%)
    - **Dược phẩm, Y tế:** 14 jobs (4%)

![image.png](attachment:5fe05346-9381-4f45-a136-eae340609947:image.png)

<aside>
    
###💡 **4/ Công ty**

</aside>

- Một số công ty tuyển dụng nhiều nhất

![image.png](attachment:ef8de2cf-d655-4ece-872a-41cc51b32abd:image.png)

- **Tập đoàn (công ty >1000 nhân viên):** 186 jobs (54%)

⇒ Các tập đoàn lớn, có nguồn dữ liệu dồi dào và cấu trúc phòng ban rõ ràng, đang đầu tư mạnh mẽ nhất vào các đội ngũ phân tích dữ liệu.

- **Doanh nghiệp nhỏ (công ty <= 50 nhân viên):** 111 jobs (32%)

⇒ Các doanh nghiệp nhỏ đang tích cực ứng dụng data để tối ưu vận hành và tìm kiếm cơ hội tăng trưởng.

![image.png](attachment:4a0131bd-2947-4aa3-8873-b6423f78442c:image.png)

<aside>
    
###💡 **5/ Lương thưởng**

</aside>

- Mức lương từ vị trí >3 năm kinh nghiệm cao hơn đáng kể so với nhóm 1-3 năm

⇒ Tín hiệu tích cực: ngành DA có lộ trình phát triển rõ ràng và lương thưởng xứng đáng

![image.png](attachment:0fccf7e0-b74e-474d-96a4-add6e6f7bca6:image.png)

<aside>
    
###💡 **6/ Technical Skills yêu cầu**

</aside>

- Bộ ba **Nền tảng**: SQL - Excel - Power BI
    - **SQL**: 129 jobs (37.5%)
    - **Excel**: 116 jobs (33.7%)
    - **PowerBI**: 92 jobs (26.7%)
- Việt Nam: lượng công ty dùng PowerBI > Tableau
- **Python**: 68 jobs yêu cầu, trở thành kỹ năng quan trọng thứ tư

⇒ Vai trò của Data Analyst đang dần mở rộng, lấn sân sang các tác vụ phức tạp liên quan đến tự động hóa, Machine Learning

- **ETL, Airflow, và Cloud (AWS, Azure)** bắt đầu "lác đác xuất hiện"

⇒ Sự phát triển của vai trò **Analytics Engineer**

![image.png](attachment:9b2ee217-871b-4927-b0ef-2c0bb6b209e8:image.png)

<aside>
    
###💡 **7/ Chế độ phúc lợi**

</aside>

- Các phúc lợi cơ bản đa số được đảm bảo: **Bảo hiểm (BHXH, BHYT), Thưởng (tháng 13, Lễ/Tết)**
- Các công ty chú trọng vào việc cho nhân viên được đào tạo, học khóa học để nâng cao kỹ năng
