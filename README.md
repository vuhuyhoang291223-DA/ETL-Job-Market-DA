# ETL-Job-Market-DA
[Full ETL process to find out what is needed in the Data Analyst Job Market in Vietnam]

Khi thị trường Data Analyst ngày càng cạnh tranh, việc có một cái nhìn sâu sắc về nhu cầu tuyển dụng là vô cùng quan trọng. Để giải quyết bài toán này, em đã phát triển một hệ thống tự động nhằm cung cấp insight về thị trường việc làm DA tại Việt Nam.

Project của em bao gồm các phần chính sau:

- **Extract**: dùng Python crawl dữ liệu từ web tuyển dụng TopCV.

- **Transform**: làm sạch dữ liệu thô và chuẩn hóa lại các thông tin cần thiết quan trọng.

- **Load**: dữ liệu tải lên Google Sheets thông qua API, từ đó em tạo ra một dashboard tối giản, tập trung vào chỉ số cốt lõi nhất về thị trường.

## 1. Dashboard - Google Sheets

Phía dưới là hình ảnh Dashboard trên Google Sheets

Tuy nhiên để có thể có một cái nhìn cụ thể và có thể tương tác filters, mọi người có thể truy cập trực tiếp thông qua đường link sau: [Dashboard](https://docs.google.com/spreadsheets/d/1GJ1xw5WYdBKCCFBDVSMDevr7yNnQr0dcCcl8-FDWEYA/edit?gid=1237555201#gid=1237555201)

<img width="1853" height="682" alt="Image" src="https://github.com/user-attachments/assets/71f5cb6e-9101-435f-8f4c-6901614d927f" />

## 2. Insights

    
### **💡 1/ Cấp độ tuyển dụng**

Nhu cầu tuyển dụng tập trung mạnh nhất vào nhóm có **1-3 năm kinh nghiệm (YOE)**.

- **1-3 YOE:** 260 jobs (75.58%)

⇒ Điều này cho thấy thị trường có nhu cầu cao đối với các Data Analyst đã có nền tảng và có thể nhanh chóng bắt đầu công việc.

- **Không yêu cầu kinh nghiệm + Dưới 1 năm kinh nghiệm** (0-0.5YOE): 51 jobs (14.82%)

⇒ Vẫn cởi mở cho người mới

<img width="1489" height="490" alt="Image" src="https://github.com/user-attachments/assets/f5a5842b-2153-42d8-bf93-7f73f40b6853" />


    
### **💡 2/ Địa điểm làm việc**

- **TP.HCM & Hà Nội:** 300 jobs (**87.2%**)

<img width="1483" height="490" alt="Image" src="https://github.com/user-attachments/assets/7c834402-c29a-49d1-96cf-9a36d154f337" />


    
### **💡 3/ Ngành nghề** 

- Ngành nghề IT áp đảo, ngoài ra còn có một số ngành nghề khác chiếm tỷ trọng lớn như Tài chính và Marketing

**⇒ Insights:** tập trung học domain/kiến thức liên quan đến những ngành nghề nổi bật để lấy lợi thế

- Data phân nhóm
    - **IT - phần mềm**: 124 jobs (36%)
    - **Tài chính + Ngân hàng + Chứng khoán**: 47 jobs (13.7%)
    - **Viễn thông + truyền thông / marketing**: 32 jobs (9.3%)
    - **Sản xuất**: 23 jobs (6.7%)
    - **Bán lẻ, tiêu dùng**: 19 jobs (5.5%)
    - **Dược phẩm, Y tế:** 14 jobs (4%)

<img width="1489" height="489" alt="Image" src="https://github.com/user-attachments/assets/5e35231d-9693-43c6-9515-47a367fc618e" />


    
### **💡 4/ Công ty**

- Một số công ty tuyển dụng nhiều nhất

<img width="1489" height="489" alt="Image" src="https://github.com/user-attachments/assets/c860f618-4ad5-474d-82c8-935913d4daef" />

- **Tập đoàn (công ty >1000 nhân viên):** 186 jobs (54%)

⇒ Các tập đoàn lớn, có nguồn dữ liệu dồi dào và cấu trúc phòng ban rõ ràng, đang đầu tư mạnh mẽ nhất vào các đội ngũ phân tích dữ liệu.

- **Doanh nghiệp nhỏ (công ty <= 50 nhân viên):** 111 jobs (32%)

⇒ Các doanh nghiệp nhỏ đang tích cực ứng dụng data để tối ưu vận hành và tìm kiếm cơ hội tăng trưởng.

<img width="1489" height="490" alt="Image" src="https://github.com/user-attachments/assets/712d0008-5dfe-42b0-86e8-50fb9dbca5fb" />


    
### **💡 5/ Lương thưởng**

- Mức lương từ vị trí >3 năm kinh nghiệm cao hơn đáng kể so với nhóm 1-3 năm

⇒ Tín hiệu tích cực: ngành DA có lộ trình phát triển rõ ràng và lương thưởng xứng đáng

<img width="1489" height="490" alt="Image" src="https://github.com/user-attachments/assets/4f4c997c-6c92-4ee3-959e-5122c8fb07ca" />


    
### **💡 6/ Technical Skills yêu cầu**

- Bộ ba **Nền tảng**: SQL - Excel - Power BI
    - **SQL**: 129 jobs (37.5%)
    - **Excel**: 116 jobs (33.7%)
    - **PowerBI**: 92 jobs (26.7%)
- Việt Nam: lượng công ty dùng PowerBI > Tableau
- **Python**: 68 jobs yêu cầu, trở thành kỹ năng quan trọng thứ tư

⇒ Vai trò của Data Analyst đang dần mở rộng, lấn sân sang các tác vụ phức tạp liên quan đến tự động hóa, Machine Learning

- **ETL, Airflow, và Cloud (AWS, Azure)** bắt đầu "lác đác xuất hiện"

⇒ Sự phát triển của vai trò **Analytics Engineer**

<img width="1256" height="605" alt="Image" src="https://github.com/user-attachments/assets/a5b54425-db37-4f2f-b4b4-ad820873849d" />


    
### **💡 7/ Chế độ phúc lợi**

- Các phúc lợi cơ bản đa số được đảm bảo: **Bảo hiểm (BHXH, BHYT), Thưởng (tháng 13, Lễ/Tết)**
- Các công ty chú trọng vào việc cho nhân viên được đào tạo, học khóa học để nâng cao kỹ năng

<img width="1385" height="449" alt="Image" src="https://github.com/user-attachments/assets/05962804-1e79-4c77-94e8-20b064cdc2b8" />
