import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

# 1. Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'sheet_credential.json',
    scope
)
client = gspread.authorize(creds)

# 2. Đọc file CSV
with open('job_08092025.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

# 3. Mở Google Sheet
spreadsheet = client.open_by_key('')

# 4. Sheet mới
worksheet = spreadsheet.add_worksheet(title="Job_0809", rows="1000", cols="20")

# 5. Nhập data
for row in data:
    worksheet.append_row(row)
