from openpyxl import Workbook

class CreateExcel():
    def __init__(self, title: str):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.title = title
        self.__append_column()
        
    def __append_column(self):
        column = ['회사코드', '차량번호', '차량ID', '날짜', '주소', '속도', '발생시각']
        self.ws.append(column)

    def create_excel(self, items: tuple) -> str:
        return ' '.join(items)