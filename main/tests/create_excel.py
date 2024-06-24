from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.title = '과속 상세내역'

# 시트에 추가할 칼럼의 목록을 리스트형으로 'column'이라는 변수에 지정
column = ['회사코드', '차량번호', '차량ID', '날짜', '주소', '속도', '발생시각']

# column리스트 목록을 시트 첫 행에 입력
ws.append(column)



# # 시트에 추가할 데이터를 리스트형으로 'row'라는 변수에 지정
# row = [1, '이철수', '수학']

# # append로 row의 목록을 column 아래 행에 입력
# ws.append(row)


wb.save("./result.xlsx")
wb.close()

