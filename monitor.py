#Speedtest package to monitor internet speed
import speedtest

#Packages to use date and time to identify when test was ran
import datetime
import time

#Import CSV Package to save results
import csv

#initialize speedtest
speed=speedtest.Speedtest()

#Save results into a csv called internet_speed_test
with open('internet_speed_test.csv', mode='w') as speedcsv:
    csv_writer = csv.DictWriter(speedcsv, fieldnames=['time','download speed', 'upload speed'])
    csv_writer.writeheader()
    
    #Set time for loop to end
    endTime = datetime.datetime.now() + datetime.timedelta(minutes=120)
    #Get internet speed with current time and convert to Mb/s
    while True:
        #If statement to check whether or not set time for the test to run has elapsed
        if datetime.datetime.now() >= endTime:
            break
        else:
            current_time= datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')
            download= round((round(speed.download())/1048576),2)
            upload= round((round(speed.upload())/1048576),2)
            print(f"Time: {current_time}, Download Speed: {download} Mb/s, Upload Speed: {upload} Mb/s.")
    
    #Write output to csv
            csv_writer.writerow({
                'time':current_time,
                'download speed':download,
                'upload speed':upload
    })
    
    #5 Minute gap between checks
            time.sleep(300)








