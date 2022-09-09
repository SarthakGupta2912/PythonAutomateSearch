import os
import time
import pyautogui

# Browser to open and cpu sleep to avoid concurrency issues
os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
time.sleep(1)

# Function to open the file with the correct extension or file name
def OpenFile(fileName=''):

    if  str(fileName) == "" or str(fileName).__contains__('.txt') == False:
        print("Please enter a valid text file name!")

    else:

        GetLinesAndAutomate(open(fileName),len(open(fileName).readlines()))

# Function to automate the task with some time intervals in between to avoid concurrency issues
def GetLinesAndAutomate(_path,numberOfLines):

    #open a new tab to remove any text written by default in the address/ search bar
    objToClick = pyautogui.locateOnScreen('newTab.jpg', confidence=0.8)
    pyautogui.click(objToClick)
    
    #for loop to iterate through all the lines/sentences in the text file
    for line in range(numberOfLines):
         # search bar of chrome or any browser
         time.sleep(1)
         objToClick = pyautogui.locateOnScreen('searchBar.jpg', confidence=0.6)
         pyautogui.click(objToClick)

         # press enter to search for the text in the search bar
         time.sleep(2)
         pyautogui.write(str(_path.readline()))
         pyautogui.hotkey('Enter')

         # new tab of chrome or any other browser
         if line < numberOfLines-1:
            time.sleep(1)
            objToClick = pyautogui.locateOnScreen('newTab.jpg', confidence=0.8)
            pyautogui.click(objToClick)
    time.sleep(1)
    pyautogui.alert('Executed successfully!')
    
# Specify which text file to open to iterate through and perform the required task
OpenFile("Test.txt")
