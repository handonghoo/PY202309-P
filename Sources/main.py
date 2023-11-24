#필요할법한 모듈들을 긁어 모아봤습니다. 
import cv2 as cv
from difflib import get_close_matches  
import subprocess 
import os
import time
import pyautogui  
import pyperclip 

#아이디와 비밀번호를 입력받습니다.
ID = input("아이디를 입력하세요 : ")
PASSWORD = input("비밀번호를 입력하세요 : ")

#카카오톡을 키는 것을 자동화 하는 함수
def open_kakao():
    try:
        path = r"C:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe"
        subprocess.Popen(path)
        print('카카오톡을 열어볼까용~!')
    except:
        print("ㅠㅠ 카카오톡이 안열려요. 뭔가 잘못됬네요.")


#카카오톡을 끄는 것을 자동화 하는 함수
def kill_kakao():
     os.system("TASKKILL /F /IM KakaoTalk.exe")

#카카오톡 로그인을 자동화하는 함수
def login_kakao():
    button_location = pyautogui.locateOnScreen('images/prac.png', confidence=0.9)
    button_location_2 = pyautogui.locateOnScreen('images/login_login.png', confidence=0.9)
    if button_location is None and button_location_2 is None:
        print("패스워드 버튼 찾기 실패 ㅠㅠ")
    elif button_location is not None:
        button_point = pyautogui.center(button_location)
        pyautogui.click(button_point.x, button_point.y)
        pyautogui.write(PASSWORD) 
        pyautogui.press('enter')
    elif button_location_2 is not None:
        button_point = pyautogui.center(button_location_2)
#     pyautogui.moveTo(button_point.x, button_point.y, duration=0)
#     pyautogui.move(0, -45, 0.5, pyautogui.easeInQuad)  # Move 45 pixels Up
        pyautogui.doubleClick(button_point.x, button_point.y-45)
        pyautogui.write(PASSWORD)
        pyautogui.press('enter')

# 원활한 디버깅을 위해 추가 구현해본 함수
def login_kakao2():
    # 사용자의 입력을 받는다.
    username = input("기기에 따라 카카오톡 실행속도가 다릅니다. 프로그램이 실행되면 아무키나 누르고 엔터를 누르세요 ")
    




#main 부분 구성

#  카카오톡이 실행되고 있을수 있으므로 일단 끄고 초기화시킵니다.
kill_kakao()

#  카카오톡 프로그램을 실행시킵니다.
open_kakao()

# 이미지 인식을 바탕으로 로그인 합니다.

login_kakao()