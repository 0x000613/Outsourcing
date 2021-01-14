from cx_Freeze import setup, Executable
import sys
import os

buildOptions = {"packages":["os", "bs4", "openpyxl", "selenium"], "include_files":[os.path.realpath(os.path.join(os.path.dirname(__file__), "chromedriver.exe"))]}

exe = [Executable("CovidCrawler.py")]

setup(
    name='COVIDCrawler',
    version = '1.0.0',
    author = "XeroSoftware",
    description = "코로나 확산 현황 공공데이터 크롤링 프로그램",
    options = dict(build_exe = buildOptions),
    executables = exe
)
