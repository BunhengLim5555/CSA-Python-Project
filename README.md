# CSA-Python-Project
My Python final project for CSA
1. Project Title: Skylar Assistant Bot 
2. Project Issue/Problem to be Solved

In today’s busy world, users often face challenges when trying to quickly access specific apps or websites. This process consumes valuable time and reduces productivity. The assistant bot was created to address this problem which includes:

Combines essential features
Provides a seamless, all-in-one solution.
Designed to streamline daily activities and reduce effort.
Enhances overall productivity for smarter, more convenient task management.
3. Current Progress (PDLC)
a. Problem Analysis: provide user interaction:
Input: User gives a voice or text command via a microphone or keyboard.
Output: The bot provides responses as text or speech

b.  Design: 

Input Handling: Processes voice commands (converted to text using speech_recognition) or direct text input.
Command Processing: Identifies user intent and routes it to the appropriate task module.
c. Error handling:
Provides feedback or re-prompts if a command is unclear or fails (e.g., unavailable apps or API errors).
4. Project Functions/Features

a. Take command: Take User input and command via text or voice

b. Give feedback: Implements basic voice feedback to user

c. Bot capability: can perform some actions such as:

List all commands the Bot can perform for better understanding 
User can turn on or turn off voice command
greet the user base on time of the day ( Good morning, Good Afternoon,.....)
Open specific websites (Such as Facebook, Youtube,...)
Open some important applications (Such as Telegram, Cmd, Notepad,....)
Close websites and applications 
Search topic on wikipedia and give back a summary ( Give a summary of 2 sentences)
Tell the user the current time
Provide current weather and temperature (Temperature)
Set a timer base on user command (seconds, mins, hours)
perform basic calculations (only for + - * /)
play music on Youtube with access control to pause the music 
Give user a random quotes or jokes 
close the assistant bot via command
Read text and pdf files( read text or select a .pdf or .txt files to read)
5. Expected Number of Pages : GUI is not require for this bot so you can only run it on terminal or others  python interpreter. But there is a window page for user to select files if read pdf files command is being perform.
6. Database: No Database is being applied for this project.

7. Project reference/source


Python mini Project (Desktop Assistant):

https://github.com/ndleah/python-mini-project/tree/main/desktopassistant#features

geeksforgeeks (Convert PDF File Text to Audio Speech using Python):  

https://www.geeksforgeeks.org/convert-pdf-file-text-to-audio-speech-using-python/

8. Instructions for Running the Application

Required Software and Libraries:

Python 3.9 or later.
Libraries:
pyttsx3 
datetime
speech_recognition 
webbrowser
pyautogui
time
os
tkinter 
pywhatkit
requests
signal
sys
re
random
pyPDF2
threading

Installation Instructions:

Install Python from python.orgLinks to an external site..
Install required libraries using pip:
pip install + module name. EX: pip install pyttsx3

Running the Application:

Save the provided python file into your computer
Run the script in the terminal or IDE:
SkylarAssistant.py

Configuration Settings:

For the path in the applications dictionary you have to modify it as the path of your actual computer application path. You can do this by going to the file location -> select properties -> copy Target.
Note: You need to change all the \ of the path you copy to / to prevent errors. 
You can add more websites, applications, jokes or quotes base on your preference. 

Dependencies:

Weather API: you can get the API from Openweather by creating an account and get your APi keys.


