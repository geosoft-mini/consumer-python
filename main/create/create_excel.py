from openpyxl import Workbook, load_workbook

class CreateExcel():
    def __init__(self, title: str, sheet_name: str) -> None:
        self.wb = load_workbook('./excel/apk.xlsx')
        self.wb.create_sheet(sheet_name)
        
        self.ws = self.wb[sheet_name]
        self.ws.title = title
        self.__append_column()
        
    def __append_column(self) -> None:
        column = ['회사코드', '차량번호', '차량ID', '날짜', '주소', '속도', '발생시각']
        self.ws.append(column)

    def create_excel(self, items: tuple) -> str:
        return ' '.join(items)