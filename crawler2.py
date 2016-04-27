#!/usr/bin/python3

###import the necessary packages
#import pymysql
import trace
import urllib
import time
from urllib import request
from bs4 import BeautifulSoup 
import re
import datetime
import json
import urllib
import os

log_file_name="Log_file.txt"
error_list=[]
m=1
n=100
for sound_id  in range(m,n):
   try:
      url="http://www.app-echo.com/sound/"+str(sound_id)
      url="http://www.xiayifa.com/go.php?url="+url
      html=urllib.request.urlopen(url).read()
      html=html.decode("utf-8")
      soup=BeautifulSoup(html)
      text=soup.find("p").text
      data=json.loads(text)
      data=data['data']
      mp3_url=data['mp3']
      title=data['title']
      image_url=data['img']	  
      local = os.path.join('/home/wanggaobin/code/Crawler/Download/result/',str(sound_id)+'.mp3')
      urllib.request.urlretrieve(mp3_url,local)
      local = os.path.join('/home/wanggaobin/code/Crawler/Download/result/',str(sound_id)+'.jpg')
      urllib.request.urlretrieve(image_url,local)
   except:
      error_list.append(sound_id)
      f=open(log_file_name,"a")
      datetime1=time.strftime('%Y-%m-%d',time.localtime(time.time()))
      datetime2=time.strftime('%H:%M:%S',time.localtime(time.time()))
      f.write("###"+"error sound_id:"+str(sound_id)+"###"+"error_time"+datetime1+" "+datetime2+'\n')
      f.write(str(error_list))
      #traceback.print_exc(file=f)
      f.flush()
      f.close()



