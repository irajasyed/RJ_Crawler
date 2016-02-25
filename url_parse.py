
import zlib
from BeautifulSoup import BeautifulSoup
import os
# from bs4 import BeautifulSoup
from MyClass import myClass
__author__ = 'rajasyedabuthahir.j'
import sys
# sys.stdout = open('iamarks.txt', 'w')
import httplib, urllib,time

print "checking"


def autoCheck():
       params = urllib.urlencode({'regno': 711312104064})
       headers = {"Host": "coe1.annauniv.edu",
       "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0",
       "Accept": "text/plain, */*; q=0.01",
       "Accept-Language": "en-US,en;q=0.5",
       "Accept-Encoding": "gzip, deflate",
       "Content-Type": "application/x-www-form-urlencoded",
       "Authorization": "Basic ZW1zYXU6IUJlc3RHdW5AIzIwMTMh",
       "Referer": "http://sdpdr.nic.in/annauniv/result",
       "Content-Length": "18",
       "Origin": "http://sdpdr.nic.in",
       "Connection": "keep-alive"
       }
       conn = httplib.HTTPConnection("coe1.annauniv.edu")
       conn.request("POST", "/app/app_action/annauniv_results.php", params, headers)

       response = conn.getresponse()
       print response.length
       if(response.length==180):

              time.sleep(240)
              print "Refreshing"
              autoCheck()
autoCheck()
myClass()
os.system("""
cd ~/AnnaUniversity
git pull
cp ~/PycharmProjects/URL_Test/7thSem_Results.txt 7thSem_Results.txt &&

git add . &&
git commit . -m "log_test" &&
git push --repo https://rajasyed:'payoda8080'@github.com/rajasyed/AnnaUniversity.git""")
#os.system("ls")
print "ended"