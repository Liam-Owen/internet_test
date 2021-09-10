#Speedtest package to monitor internet speed
import speedtest

#Packages to use date and time to identify when test was ran
import datetime
import time

#Pandas library to clean and explore data returned
import pandas as pd

#Matplotlib package for data visualisation
import matplotlib.pyplot as plt

#initialize speedtest
speed=speedtest.Speedtest()

#Get internet speed with current time and convert to Mb/s
while True:
    current_time= datetime.datetime.now().strftime("%H:%M")
    download= round((round(speed.download())/1048576),2)
    upload= round((round(speed.upload())/1048576),2)
    print(f"Time: {current_time}, Download Speed: {download} Mb/s, Upload Speed: {upload} Mb/s.")









