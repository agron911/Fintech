from turtle import st
from pandas_datareader import data as web
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os
import requests
from fake_useragent import UserAgent
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import numpy as np
from pathlib import Path
import random
import time
import wx
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


yf.pdr_override()
from stats_func import *


start = dt.datetime(2000, 1, 1)
end = dt.datetime(2024, 12, 24)

long_tail_stk = {}

save_file_path = Path(os.getcwd()) / "stk2"
print(save_file_path)

def delete_files():
    path = save_file_path
    # Use glob to find all .txt files in the directory
    for file in path.glob("*.txt"):
        file.chmod(0o777)  # Change the permissions if necessary
        file.unlink()  # Delete the file
    return "Files deleted"





def save_stock_data(df, stock_code, folder= save_file_path, long_tail=False):
    if long_tail:
        df.to_csv(folder / f"{stock_code}_long_tail.txt", sep="\t")
    else:
        df.to_csv(folder / f"{stock_code}.txt", sep="\t")


def fetch_stock_data(stock_code, suffix, start, end):
    try:
        df = web.get_data_yahoo([f"{stock_code}{suffix}"], start, end)
        df = df.drop(columns=["Adj Close"])
        df.index = df.index.strftime("%Y/%m/%d , %r")
        df.index = df.index.str.split(",").str[0]
        df["Date"] = df.index
        return df
    except Exception as e:
        print(f"Error fetching data for {stock_code}: {e}")
        return None


def crawl_all_ch():
    international_stock = pd.read_csv("international.txt")
    international_suffix = ""
    for code in international_stock["code"]:
        df = fetch_stock_data(code, international_suffix, start, end)
        if df is not None:
            save_stock_data(df, code)
            print(f"Crawled: {code}")


    stock_list = pd.read_excel(os.getcwd() + "/adjustments/list.xlsx")
    stock_list["code"] = stock_list.iloc[:, 0]

    listed_code = '.TW'

    for code in stock_list.code:
        df = fetch_stock_data(code, listed_code, start, end)
        if df is not None:
            save_stock_data(df, code)
            print(f"Crawled: {code}")

            if long_tail(df):
                save_stock_data(df, code, long_tail=True)
                long_tail_stk[code] = df
                print(f"LONG_TAIL: {long_tail_stk[code]}")
        else:
            print(f"Error fetching data for {code}")
            
    df = web.get_data_yahoo(["^TWII"], listed_code, start, end)
    if df is not None:
        save_stock_data(df, "TWII")

def crawl_otc_yf():
    stock_list = pd.read_excel(os.getcwd() + "/adjustments/otclist.xlsx")
    all_otc_stock = stock_list.iloc[:, 0]
    otc_code = ".TWO"
    
    for code in all_otc_stock:
        df = fetch_stock_data(code, otc_code, start, end)
        if df is not None:
            save_stock_data(df, code)
            print(f"Crawled: {code}")

            if long_tail(df):
                save_stock_data(df, code, long_tail=True)
                long_tail_stk[code] = df
                print(f"LONG_TAIL: {long_tail_stk[code]}")
        else:
            print(f"Error fetching data for {code}")
            
@np.deprecate()
def delete_files_deprecated(self):
    path = Path(os.getcwd()) / "stk2"  # Get the stk2 folder path
    # Use glob to find all .txt files in the directory
    for file in path.glob("*.txt"):
        file.chmod(0o777)  # Change the permissions if necessary
        file.unlink()  # Delete the file
    return "Files deleted"

@np.deprecate()
def crawl_all_ch_deprecated(self):

    International_stock = pd.read_csv("international.txt")
    for i in International_stock["code"]:
        df = web.get_data_yahoo([i], start, end)
        df = df.drop(columns=["Adj Close"])
        # df.index.strftime("%Y/%M/%D")
        df.index = df.index.strftime("%Y/%m/%d , %r")
        df.index = df.index.str.split(",").str[0]
        df["Date"] = df.index
        df.to_csv("./stk2/" + i + ".txt", sep="\t")

        print("Crawl:", i)

    stock_list = pd.read_excel(os.getcwd() + "/adjustments/list.xls")
    stock_list = stock_list.iloc[:, :1]
    stock_list["code"] = stock_list.iloc[:, 0].str.split("　").str[0]
    all = stock_list.code

    df = web.get_data_yahoo(["^TWII"], start, end)
    df = df.drop(columns=["Adj Close"])
    # df.index.strftime("%Y/%M/%D")
    df.index = df.index.strftime("%Y/%m/%d , %r")
    df.index = df.index.str.split(",").str[0]
    df["Date"] = df.index

    df.to_csv("./stk2/TWII.txt", sep="\t")

    num = 1
    print("ALL", all)
    for i in all:

        if num == 950:
            break
        num += 1
        try:
            df = web.get_data_yahoo([i + ".TW"], start, end)
        except Exception as e:
            print("web get yahoo error:", str(e))
        df = df.drop(columns=["Adj Close"])
        try:
            df.index = df.index.strftime("%Y/%m/%d , %r")
            df.index = df.index.str.split(",").str[0]
            df["Date"] = df.index
            self.frame.input6.SetValue("" + i)

            # print(df.Open)
            print("Stock code : ", i)
            if long_tail(df):
                df.to_csv("./stk2/" + i + "_long_tail.txt", sep="\t")
                long_tail_stk[i] = df
                print("LONG_TAIL", long_tail_stk[i])

            df.to_csv("./stk2/" + i + ".txt", sep="\t")
        except Exception as e:
            print(str(e))
            continue

@np.deprecate()
def crawl_otc_yf_deprecated(self):

    stock_list = pd.read_excel(os.getcwd() + "/adjustments/otclist.xls")
    stock_list = stock_list.iloc[:, :1]
    stock_list["code"] = stock_list.iloc[:, 0]
    all = stock_list.code

    for i in all:

        try:
            df = web.get_data_yahoo([str(i) + ".TWO"], start, end)
            df = df.drop(columns=["Adj Close"])
        except Exception as e:
            print("web get yahoo error:", str(e))
        try:
            df.index = df.index.strftime("%Y/%m/%d , %r")
            df.index = df.index.str.split(",").str[0]
            df["Date"] = df.index
            self.frame.input6.SetValue("" + str(i))

            # print(df.Open)
            print("Stock code : ", i)
            if long_tail(df):
                df.to_csv("./stk2/" + str(i) + "_long_tail.txt", sep="\t")
                long_tail_stk[i] = df
                print("LONG_TAIL", long_tail_stk[i])

            df.to_csv("./stk2/" + str(i) + ".txt", sep="\t")
        except Exception as e:
            print(str(e))
            continue

@np.deprecate()
def crawl_all_otc_deprecated(self):
    codes = pd.read_csv("otc.txt")
    # codes = ['5009','1108','3293','6152','5490','6160','2025','2516','4903','8255','6188','6143','9945']

    for code in codes["code"]:

        try:
            s = os.getcwd()
            user_path = (
                s.split("\\")[0]
                + os.sep
                + s.split("\\")[1]
                + os.sep
                + s.split("\\")[2]
                + os.sep
            )
            user_path_download = user_path + "Downloads\\"
            # filePath ='C:\\Users\\XPS-9365\\Downloads\\'+ code +'_history.csv'
            filePath = Path(user_path_download + str(code) + "_history.csv")
            os.chmod(filePath, 0o777)
            file = Path(filePath)
            os.remove(file)
        except Exception as e:
            print(e)
    # code = input()
    for code in codes.code:

        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--test-type")
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-ssl-errors=yes")

        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        service = Service(executable_path="./chromedriver.exe")
        # options = webdriver.ChromeOptions()

        driver = webdriver.Chrome(options=options, service=service)
        print(
            "!!",
        )
        driver.get(
            "https://www.cnyes.com/twstock/" + str(code) + "/charts/technical-history"
        )
        time.sleep(random.random())
        # offset = 100
        # driver.execute_script(f"window.scrollBy(0, {offset})")
        print("scroll down below the offset")
        time.sleep(random.random())

        # click_date = driver.find_element(By.XPATH,"""//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/div/button""")
        # click_date.click()
        # time.sleep(2)

        driver.execute_script("window.scrollTo(0, 1910)")
        time.sleep(5)

        click_date = driver.find_element(
            By.XPATH,
            """//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/div/button""",
        )
        click_date.click()

        time_value = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    """//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/div/div[2]/div[2]/div[1]/input""",
                )
            )
        )
        print("MINMIN before setting:", time_value)
        mindate = "2000-01-01"
        driver.execute_script(
            "arguments[0].setAttribute('min', arguments[1])", time_value, mindate
        )
        time_value.clear()  # Ensure  input field is cleared before setting  date
        time_value.send_keys(mindate)

        WebDriverWait(driver, 50, 0.8).until(
            EC.text_to_be_present_in_element_value(
                (
                    By.XPATH,
                    """//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/div/div[2]/div[2]/div[1]/input""",
                ),
                mindate,
            )
        )

        time.sleep(1)

        apply = driver.find_element(
            By.XPATH,
            """//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/div/div[2]/div[3]/button[2]""",
        )
        apply.click()

        time.sleep(3)
        download = driver.find_element(
            By.XPATH,
            """//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/a/button""",
        )
        download.click()

        print(os.listdir)

        time.sleep(1)

        # df = pd.read_csv('C:/Users/XPS-9365/Downloads/'+ code +'_history.csv')
        df = pd.read_csv(user_path_download + str(code) + "_history.csv")

        df = df[["日期", "開盤", "最高", "最低", "收盤", "成交張數"]]
        df.rename(
            columns={
                "日期": "Date",
                "開盤": "Open",
                "最高": "High",
                "最低": "Low",
                "收盤": "Close",
                "成交張數": "Volume",
            },
            inplace=True,
        )
        # df = df[['Date','Open','High','Low','Close',"Volume('000 shares)"]]
        # df = df.rename(columns={"Volume('000 shares)":"Volume"})
        df["Date1"] = df.Date

        df.sort_values(by="Date", inplace=True)

        df.set_index("Date", inplace=True)
        df = df.rename(columns={"Date1": "Date"})

        # df.to_csv('C:/Users/XPS-9365/Desktop/Fintech/fintect proj/crawler/stk2/'+code+'.txt',sep='\t')
        df.to_csv(s + "\\stk2\\" + str(code) + ".txt", sep="\t")

        print(df)


# execute the delete and crawl crawl_all_ch which is not deprecated

delete_files()
crawl_all_ch()
