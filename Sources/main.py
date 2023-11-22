#필요할법한 모듈들을 긁어 모아봤습니다. 
import cv2 as cv
from difflib import get_close_matches  
import subprocess 
import os
import time
import pyautogui  
import pyperclip 
import datetime


#카카오톡을 키는 것을 자동화 하는 함수
def open_kakao():
    try:
        path = r"C:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe"
        subprocess.Popen(path)
        print('opening Kakao Talk')
    except:
        print("cannot open KakaoTalk")


#카카오톡을 끄는 것을 자동화 하는 함수
def kill_kakao():
    os.system("TASKKILL /F /IM KakaoTalk.exe")

#카카오톡 로그인을 자동화하는 함수
def login_kakao():
    pass

#일단 요번주 목표 = 켜고 끄고 로그인하는것까지 구현해보기!