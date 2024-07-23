from openpyxl import Workbook, load_workbook
import os


class CreateExcel():
    def __init__(self, title: str, sheet_name: str) -> None:
        self.file_name = 'APK.xlsx'
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        os.chdir('../excel')
        
        self.wb = load_workbook(os.getcwd() + '/' + self.file_name)
        self.ws = self.wb[sheet_name]
        self.ws.title = sheet_name
        

    def create_excel(self, items: tuple) -> str:
        return ' '.join(items)
