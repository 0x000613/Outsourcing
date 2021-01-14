from cx_Freeze import setup, Executable
import sys
import os

buildOptions = {"packages":["os", "bs4", "time", "pandas", "selenium", "openpyxl"], "include_files":[os.path.realpath(os.path.join(os.path.dirname(__file__), "chromedriver.exe"))]}

exe = [Executable("Yogiyo_Crawling.py")]

setup(
    name='YogiyoXCrawler',
    version = '1.0.0',
    author = "XeroSoftware",
    description = "요기요 등록 매장 정보 수집 크롤러 프로그램",
    options = dict(build_exe = buildOptions),
    executables = exe
)