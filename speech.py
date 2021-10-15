import datetime
from datetime import datetime
import time
import requests
import pyttsx3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as spreg
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path=("D://chromedriver.exe"))


username = "amathdeveru_"
userpassword = "Vishal@1234"

# Integrating speech module

def speechmod():
    recog = spreg.Recognizer()
    driver.quit()
    global text
    with spreg.Microphone() as source:
        print('Tell Something: ')
        speech = recog.listen(source)
    try:
        text = recog.recognize_google(speech)

        return text
    except spreg.UnknownValueError:
        speak('Unable to recognize the audio')


# Integrating speak function

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


# Instagram login

def instalogin():
    try:
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        login_id = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        login_id.send_keys(username)
        time.sleep(1)
        password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(userpassword)
        clicklog = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        clicklog.click()
        time.sleep(3)
        saveinf = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        saveinf.click()
        time.sleep(2)
        notnow = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        notnow.click()


    except:
        speak("login failed")


# Integrating count of message on instagram

def instamsgcount():
    instalogin()
    global count
    try:
        instamsg = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div/div')
        count = int(instamsg.get_attribute('innerText'))
        msgtext = "You have " + str(count) + " total messages"
        speak(msgtext)
        print(msgtext)
        instamsg.click()
        if (count < 1):
            speak('you dont haave any new messages')
    except:
        speak('you dont have any new messages')


# Integrating whose msg is there

def messagedperson():
    try:
        instamsgcount()
        time.sleep(7)
        arr = []
        for i in range(1, count + 1):
            nameofrecent = driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[' + str(
                    i) + ']/a/div/div[2]/div[1]/div/div/div/div')
            ++i
            nameofrecent.click()
            time.sleep(5)
            personnn = driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div/div')
            personnn.click()
            time.sleep(3)
            personname = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/h1')
            PNAME = personname.get_attribute('innerHTML')
            arr.append(PNAME)
            speak("you have messages from , ")
            for i in arr:
                speak(i)
                print(i)
    except:
        speak('you dont have any new messages')



messagedperson()
