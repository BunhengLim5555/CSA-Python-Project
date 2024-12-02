import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyautogui
import time
import re
import os
import pywhatkit
import requests 
import signal
import sys
import pyttsx3
import PyPDF2
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import Tk, filedialog
import threading
import random

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.setProperty("Volume", 0.9)

# Assistant bot speak 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
  


# Greet user base on the time of day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 7 and hour < 12:
        speak("Good Morning")
        print("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
        print("Good Afternoon")
    elif hour >= 18 and hour < 21:
        speak("Good Evening!")
        print("Good Evening!")
    else:
        speak("Good night")
        print("Good night")
    speak("I am Skylar, your desktop assistant. How can I assist you today?")
    print("I am Skylar, your desktop assistant. How can I assist you today?")

# take voice command from user
def takeCommand():
    # Initialize the recognizer
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust for ambient noise and record audio
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
        try:
            # Use Google Web Speech API to recognize the audio
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()  # Return the command in lowercase
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

# Create a function to perform tasks based on user's voice command
voice_command_mode = False

def open_voice_mode():
    global voice_command_mode
    voice_command_mode = not voice_command_mode
    if voice_command_mode:
        speak("Voice command mode is now enabled.")
        print("Voice command mode is now enabled.")
    else:
        speak("Voice command mode is now disabled.")
        print("Voice command mode is now disabled.")

# handle command for the user to turn on or of voice command mode
def handle_input(command):
    global voice_command_mode

    # Turn on voice command mode via text input
    if command.lower() == 'turn on voice command':
        if not voice_command_mode:
            open_voice_mode()  # Enable voice command mode
        else:
            speak("Voice command mode is already enabled.")
            print("Voice command mode is already enabled.")
        return

    # If voice command mode is enabled, listen for commands
    if voice_command_mode:
        # This part is handled in the main loop when voice command mode is on
        return

    # Handle other text commands if voice command mode is not enabled
    handle_command(command)

# Dictionary of websites (you can add more websites)
websites = {
    "youtube": "https://youtube.com",
    "wikipedia": "https://www.wikipedia.com",
    "google": "https://google.com",
    "facebook": "https://www.facebook.com/",
    "canvas": "https://aupp.instructure.com/",
    "instagram": "https://www.instagram.com/",
    "x": "https://www.x.com",
    "reddit": "https://www.reddit.com",
    "stackoverflow": "https://stackoverflow.com",
    "github": "https://github.com",
    "discord": "https://discord.com",
    "pinterest": "https://www.pinterest.com",
    "twitch": "https://www.twitch.tv",
    "spotify": "https://www.spotify.com",
    "netflix": "https://www.netflix.com",
    "amazon": "https://www.amazon.com", 
    "google drive": "https://drive.google.com",
    }

# function to open a website from the dictionary of websites
def open_website(command):
    command = command.lower()
    for site_name, url in websites.items():
        if site_name in command:
            webbrowser.open(url)
            speak(f"Opening {site_name}")
            print(f"Opening {site_name}...")
            return
    speak("Sorry, I couldn't find that website.")
    print("Sorry, I couldn't find that website.")

# close specific website in chrome(my default browser)
def close_website(website_name):
    """Function to close a website by its name in the browser."""
    # Normalize the input by converting it to lowercase and stripping spaces
    website_name = website_name.strip().lower()

    # Check if the website is in the list of known websites
    if website_name in websites:
        print(f"Attempting to close the website: {website_name.capitalize()}")
        
        # Switch to the browser window
        pyautogui.hotkey('alt', 'tab')  # Activate the browser window
        time.sleep(0.1)  # Give time for the browser to activate

        # Loop through open tabs to find the target website
        for _ in range(10):  # Assuming 10 tabs, adjust as necessary
            pyautogui.hotkey('ctrl', 'tab')  # Switch to the next tab
            time.sleep(0.1)  # Allow time for the tab to load
            
            # In a real-world case, you would need a way to check the URL of the tab.
            # For simplicity, we'll assume that the tab contains a matching string.
            if website_name in pyautogui.getActiveWindowTitle().lower():  # Placeholder for actual URL check
                pyautogui.hotkey('ctrl', 'w')  # Close the current tab
                print(f"Closed the tab containing {website_name.capitalize()}.")
                return
            time.sleep(0.1)  # Wait a little before checking the next tab
    
# applications dictionary (you can add more applications but you need to make sure the path is correct)
applications = { 
    "chrome": "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "telegram": "C:/Users/Bunheng Lim/AppData/Roaming/Telegram Desktop/Telegram.exe",
    "microsoft edge": "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
    "powerpoint": "C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE",
    "micorsoft word" : "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE",
    "microsoft excel" : "C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE",
    "firefox" : "C:/Program Files/Mozilla Firefox/firefox.exe",
    "cmd" : "C:/Users/Bunheng Lim/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/System Tools/Command Prompt.lnk",
    "task manager" : "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/System Tools/Task Manager.lnk", 
    "control panel" : "C:/Windows/System32/control.exe",
    "notepad" : "C:/Users/Bunheng Lim/AppData/Local/Microsoft/WindowsApps/notepad.exe",
    "calculator" : "C:/Windows/System32/calc.exe",
    "paint" : "C:/Users/Bunheng Lim/AppData/Local/Microsoft/WindowsApps/mspaint.exe",

}

# open applications function 
def open_application(app_name):
    app_name = app_name.lower()
    if app_name in applications:
        os.startfile(applications[app_name])
        speak(f"Opening {app_name}...")
        print(f"Opening {app_name}...")
    else:
        speak("Sorry, I couldn't find that application.")
        print("Sorry, I couldn't find that application.")

#close applications function
def close_application(app_name):
    app_name = app_name.lower()
    app_executables = {
        "chrome": "chrome.exe",
        "telegram": "Telegram.exe",
        "microsoft edge": "msedge.exe",
        "firefox": "firefox.exe",
        "powerpoint": "POWERPNT.EXE",
        "microsoft word": "WINWORD.EXE",
        "microsoft excel": "EXCEL.EXE",
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "cmd": "cmd.exe",
        "task manager": "Taskmgr.exe",
        "control panel": "control.exe",
    }

    if app_name in app_executables:
        exe_name = app_executables[app_name]
        try:
            os.system(f'taskkill /f /im {exe_name} > NUL 2>&1')
            speak(f"Closing {app_name}...")
            print(f"Closing {app_name}...")
        except Exception as e:
            speak(f"Could not close {app_name}.")
            print(f"Error closing {app_name}: {e}")
    else:
        speak("Sorry, I couldn't find that application to close.")
        print("Sorry, I couldn't find that application to close.")
    
# play youtube video function      
video_title = ""
def play_video(video):
    if video and video != "none":
        speak(f"Playing {video}")
        print(f"Playing {video}...")
        pywhatkit.playonyt(video, open_video=True)
    else:
        speak("Sorry, I couldn't find the video title.")
        print("Sorry, I couldn't find the video title.")

# Function to play a song on YouTube
def play_music(song_name):
    speak(f" playing {song_name} on YouTube")
    print(f"Playing {song_name} on YouTube...")
    pywhatkit.playonyt(song_name)

# Function to stop music
def stop_music():
    pyautogui.press('space')  # Simulate pressing the spacebar to pause/play
    speak("Music has been paused.")
    print("Music has been paused.")

# function to tell the user the current time
def get_time():
    currentTime = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak(f", now it's {currentTime}")
    print(f"The time is {currentTime}")

# function to exit the program
def exit_program():
    speak("Goodbye! Have a great day!")
    print("Goodbye! Have a great day!")
    exit()

# function to calculate basic math operations( + - * /)
def calculate(query):
    try:
        # Remove the word "calculate" from the query
        query = query.replace("calculate", "").strip()

        # Allow for more complex expressions by using regex
        # This regex allows digits, operators, and parentheses
        if re.match(r'^[\d\s\+\-\*\/\(\)]+$', query):
            # Evaluate the expression safely
            result = eval(query)  # Be cautious with eval in production code
            speak(f"The result is {result}")
            print(f"The result is {result}")
        else:
            speak("Please provide a valid mathematical expression.")
            print("Invalid expression format.")
    except SyntaxError:
        speak("There was a syntax error in your calculation. Please check your input.")
        print("Syntax error in calculation.")
    except NameError:
        speak("I detected an invalid name in your calculation. Please try again.")
        print("Invalid name in calculation.")
    except ZeroDivisionError:
        speak("You cannot divide by zero. Please try again.")
        print("ZeroDivisionError: Division by zero.")
    except Exception as e:
        speak("Sorry, I couldn't perform the calculation. Please try again.")
        print(f"Calculation error: {e}")

# set a timer function 
def set_timer(query):
    print(f"Query received for timer: {query}")  # Debugging output
    # Updated regex to match both "minute/minutes" and "second/seconds"
    match = re.search(r'(\d+)\s*(minute|minutes|second|seconds)?', query)  
    if match:
        time_value = int(match.group(1))  # Get the first matched group (the number)
        time_unit = match.group(2)  # Get the second matched group (the unit)
        
        if time_unit in ["minute", "minutes"]:
            total_seconds = time_value * 60  # Convert minutes to seconds
            speak(f"Setting a timer for {time_value} minutes.")
            print(f"Timer set for {time_value} minutes.")  # Print in terminal
        elif time_unit in ["second", "seconds"]:
            total_seconds = time_value  # Use seconds as is
            speak(f"Setting a timer for {time_value} seconds.")
            print(f"Timer set for {time_value} seconds.")  # Print in terminal
        else:
            speak("Please specify a valid time unit, either minutes or seconds.")
            return
        
        for remaining in range(total_seconds, 0, -1):  # Countdown in seconds
            mins, secs = divmod(remaining, 60)
            timer_format = f"{mins:02d}:{secs:02d}"  # Format as MM:SS
            print(timer_format, end='\r')  # Print remaining time on the same line
            time.sleep(1)  # Wait for 1 second
        
        speak("Time is up!")  # Notify when the timer is done
        print("Time is up!")  # Print in terminal
    else:
        print(f"Invalid timer query: {query}")  # Debugging output
        speak("Please specify a valid number of minutes or seconds.")
        print("Please specify a valid number of minutes or seconds.")

# function tell the user the weather 
def get_weather(query):
    api_key = "b18f77dfdb0cfa0921f6d3cc919670ba"  # Replace with your OpenWeatherMap API key
    city = "Phnom Penh"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather_desc = data['weather'][0]['description']
        temperature = main['temp']
        speak(f"The weather in {city} is currently {weather_desc} with a temperature of {temperature} degrees Celsius.")
        print(f"The weather in {city} is currently {weather_desc} with a temperature of {temperature} degrees Celsius.")
    else:
        speak("Sorry, I couldn't find the weather information for that location.")
        print("Sorry, I couldn't find the weather information for that location.")


# List of quotes
quotes = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts."
    "My enemies are many, my equals are none.",
    "I came, I saw, I conquered.",
    "The biggest risk is not taking any risk",
    "If you keep making the same mistake over and over, the mistake isn't the problem, you are.",
    "Life is a mystery to be lived, not a problem to be solved.",
    "If you don't know what to pursue right now in life, pursue urself.",
    "Why are you afraid of losing, when nothing in the world actually belongs to you.",
    "The best way to predict the future is to create it.",
    "When you realize that life is really simple. You were making it complicated.",
    "Don't compare your beginning to someone else's middle.",
    "Sometimes you have to unplug yourself from the world for a moment, so you can reset yourself.",
    "if people hate for no reason, why not become someone who loves for no reason.",
    "I had this conversation with this guy the other day and he's making a lot of good points it seems he was saying that you don't need to get up early in the morning and that working out early in the morning isn't that big of a deal and it's better to do it later in the day and you know I said well what if what if something comes up and I miss the workout that day and he's like told me that it's nothing major you don't need to worry about it and he cited some scientific sources and the guy was making a lot of good points and I was almost going to listen to him but then I realized the guy who I was talking with was myself and he was a liar don't let your weak voice run things Step Up do what you got to do.",
    "You know you're heal when things don't emotionally trigger you anymore. Other people's hurtful words, their confusing actions, how they see you, what they say about you or how they treat you. It doesn't get to you anymore because you know that it's rarely about you.",
    "Once you carry your own water you will learn the value of every drop.",
    "Do it from love, not for love, when it comes from within, it's real. You don't need anyone's approval to truly be great. You already are.",
    "if you give up on your dreams what do you have left ? Nothing!!",
    "Never stop being a good person because of bad people.",
    "In order to become who you want to be, you must sacrifice who your are.",
        
]
# list of jokes
custom_jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What do you call fake spaghetti? An impasta!",
    "Final Exam is next week, assignment is due tomorrow but I'm just a CHILL Guy.",
     ]

    

# function to give user a random quote
def get_random_quote():
    """Fetch and speak a random quote."""
    try:
        random_quote = random.choice(quotes)  # Get a random quote
        speak(random_quote)  # Use the speak function to read the quote aloud
        print(random_quote)  # Print the quote for reference in the console
    except Exception as e:
        speak("Sorry, I couldn't fetch a quote at the moment.")
        print(f"Error getting random quote: {e}")
# function to give user a random joke
def tell_joke():
    # Select a random joke from the custom jokes list
    joke = random.choice(custom_jokes)
    speak(joke)  # Use the speak function to read the joke aloud
    print(joke)

# function to read text or pdf files
def read_pdf(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()
    # Optional: Set voice rate or volume
    engine.setProperty('rate', 150)  # Adjust speed (words per minute)
    engine.setProperty('volume', 0.9)  # Adjust volume (0.0 to 1.0)
    engine.setProperty('voice', voices[1].id)
    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Function to select and read a file (txt or pdf)
def select_and_read_file():
    # Create a Tkinter root window, but hide it since you don't need a GUI
    root = tk.Tk()
    root.withdraw()  # Hide the Tkinter window
      # Set the Tkinter window to always stay on top
    root.attributes("-topmost", True)
    
    # Open file dialog for selecting a file (txt or pdf)
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("PDF files", "*.pdf"), ("Text files", "*.txt"), ("All files", "*.*")]      
    )

    if not file_path:
        print("No file selected.")
        speak ("No file selected.")
        return "No file selected"  # Return if no file is selected

    print(f"Selected file: {file_path}")  # Debugging message
    text = extract_text(file_path)  # Extract text from the selected file
    
    if text is None:
        speak("Sorry, I couldn't read the file")
        print("No text extracted from the file.")
        return "Error extracting text"  # Return if text extraction fails

    read_pdf(text)  # Read the extracted text aloud
    return "File read and text spoken successfully"  # Success message

# Function to extract text from txt or pdf files
def extract_text(file_path):
    try:
        if file_path.endswith('.txt'):
            with open(file_path, 'r') as file:
                return file.read()
        elif file_path.endswith('.pdf'):
            with open(file_path, 'rb') as file:
                reader = PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                return text
        else:
            speak("Unsupported file foramt.")
            print("Unsupported file format.")
            return None
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

# function to give user all commands this bot can  perform
def list_all_commands():
    commands = """
    Here are all the commands this bot can perform:
    1. turn on voice command 
    2. turn off voice command
    3. open webistes
    4. open applications
    5. close websites and applications
    6. play video on youtube
    7. play music on youtube
    8. pause the music on youtube
    9. Tell user the time
    10. Tell user the weather
    11. set a timer
    12. calculate basic maths
    13.tell random jokes or quotes 
    14. read user text
    15. read pdf files """
    print(commands)
# function to handle all command from the users 
def handle_command(query):
    query = query.lower()
    global video_title  
    # Turn off voice command mode via voice command
    if voice_command_mode and 'turn off voice command' in query:
        open_voice_mode()  # Disable voice command mode
        return
        
    # search wikipedia
    if 'open wikipedia' in query or 'wikipedia' in query or 'search wikipedia' in query:
        speak("Searching Wikipedia...")
        print("Searching Wikipedia...")
        speak("Please give the title you'd like to search for")
    
        # Check if voice command mode is enabled
        if voice_command_mode:
        # If voice command mode is enabled, use voice to get the search term
         search_term = takeCommand()  # Function to capture voice input
        else:
        # If voice command mode is disabled, prompt for text input
         speak("Please enter the title you'd like to search on Wikipedia")
         search_term = input("Please enter the title you want to search on Wikipedia: ")

        # Remove the word 'wikipedia' from the search term if it was included
        search_term = search_term.replace("wikipedia", "").strip()

        try:
            # Fetch and speak the results from Wikipedia
            results = wikipedia.summary(search_term, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
        except wikipedia.exceptions.PageError:
            # Handle the case where the page does not exist
            speak(f"Sorry, the page for '{search_term}' does not exist. Please try another term.")
        except Exception as e:
         # Handle any other exceptions that may occur
            speak("An error occurred while searching Wikipedia. Please try again.")
            print(f"Error: {e}")  # Print the error for debugging purposes
        return 

    # close the assistant bot   
    if 'stop and exit' in query or 'shut down' in query:
        speak("Goodbye, have a nice day!")
        print("Goodbye, have a nice day!")
        exit()

    # set timer
    if 'set a timer for' in query or 'set the time for' in query or 'set a timer' in query:
        print(f"Timer command detected: {query}")  # Debugging output
        set_timer(query)
        return
   
    # tell the weather
    if 'weather' in query or 'what is the weather today' in query or 'tell me the weather' in query:
        get_weather(query)  # Call the modified weather function without any parameters
        return

    # play song a from youtube
    if "play"  in query:
        song_name = query.replace("play", "").strip()
        if song_name:
            play_music(song_name)
        else:
            speak("Sorry, Please specify the name of the song you want to play.")
            print("Sorry, Please specify the name of the  song you want to play.")
        return

    # pause the song from youtube
    if "pause the music" in query or "stop the song" in query:
        # Attempt to stop the music first
        stop_music()  # Call the stop_music function to pause YouTube playback
    
        return  # Exit the function to avoid further processing
    
    # Check if the user wants to open YouTube
    if "open youtube" in query:
        speak("YouTube is now open. Please give the title of the video you want to watch.")
        print("YouTube is now open. Please give the title of the video you want to watch.")
        
        if voice_command_mode:
            # If voice command mode is enabled, use voice to get the video title
            video_title = takeCommand()  # Function to capture voice input
        else:
            # If voice command mode is disabled, prompt for text input
            video_title = input("Please enter the video you want to watch: ")  # Get the video title from user input

        if video_title:
            webbrowser.open(f"https://www.youtube.com/results?search_query={video_title}")
            speak(f"Playing {video_title} on YouTube.")
        else:
            speak("Please specify the name of the video you want to play.")
            print("Please specify the name of the video you want to play.")
        return
    
   # Open websites
    if 'open google' in query:
        open_website("google")
        return
    elif 'open canvas' in query:
        open_website("canvas")
        return
    elif 'open facebook' in query:
        open_website("facebook")
        return
    elif 'open instagram' in query:
        open_website("instagram")
        return
    elif 'open twitter' in query:
        open_website("twitter")
        return
    elif 'open reddit' in query:
        open_website("reddit")
        return
    elif 'open discord' in query:
        open_website("discord")
        return
    elif 'open github' in query:
        open_website("github")
        return
    elif 'open stack overflow' in query:
        open_website("stackoverflow")
        return
    elif 'open pinterest' in query:
        open_website("pinterest")
        return
    elif 'open twitch' in query:
        open_website("twitch")
        return
    elif 'open netflix' in query:
        open_website("netflix")
        return
    elif 'open amazon' in query:
        open_website("amazon")
        return
    elif 'open spotify' in query:
        open_website("spotify")
        return
    elif 'open google drive' in query: 
        open_website("google drive")
        return

    # tell the time
    if "time" in query or "what is the time" in query or "tell me the time" in query:
        get_time()
        return

    # open applications
    if 'open chrome' in query:
        open_application("chrome")
        return
    elif 'open telegram' in query:
        open_application("telegram")
        return
    elif 'open microsoft edge' in query:
        open_application("microsoft edge")
        return
    elif 'open firefox' in query:
        open_application("firefox")
        return
    elif 'open powerpoint' in query or 'open  micorsoft powerpoint' in query:
        open_application("powerpoint")
        return
    elif 'open excel' in query or 'open microsoft excel' in query:
        open_application("microsoft excel")
        return
    elif 'open word' in query or 'open microsoft word' in query:
        open_application(" microsoft word")
        return
    elif 'open calculator' in query:
        open_application("calculator")
        return
    elif 'open cmd' in query or 'open command prompt' in query:
        open_application("cmd")
        return
    elif 'open notepad' in query:
        open_application("notepad")
        return
    elif 'open paint' in query:
        open_application("paint")
        return
    elif 'open task manager' in query:
        open_application("task manager")
        return
    elif 'open control panel' in query:
        open_application("control panel")
        return

    applications_list = list(applications.keys())

    # Use the keys from the global websites dictionary
    websites_list = list(websites.keys())

    # Check for closing applications or websites
    # If the query contains "close", handle closing applications or websites
    if "close" in query:
        # Check for closing applications
        for app in applications_list:
            if app in query:
                close_application(app)
                return

        # Check for closing websites
        for website in websites_list:
            if website in query:
                close_website(website)
                return

    # read the pdf files
    if "read file" in query or "read a file" in query or "read this file" in query: 
        print("Entering read file command...")  # Debugging message
        result = select_and_read_file()  # Get the result from the file reading function
        print(result)  # Debugging print of result
        return result  # Return the result to handle it outside of this function
    # read text from the user 
    if "read text:" in query or "read this:" in query or "read" in query:
        if "read text:" in query:
            text = query.split("read text:", 1)[1].strip()  # Extract text after "read text:"
        elif "read this:" in query:
            text = query.split("read this:", 1)[1].strip()  # Extract text after "read this:"
        else:
            speak("What text would you like me to read?")
            text = input("Please type the text you want me to read: ").strip()  # Use input as fallback for text

        read_pdf(text)  # Call the function to read the text aloud
        return
    
    # Searching google    
    if 'search on google' in query  or 'search google' in query:
        speak("Searching Google...")
        print("Searching Google...")
        query = query.replace("search on google", "").replace("search google", "")
        url = "https://www.google.com/search?q=" + query
        webbrowser.open(url)
        return
    
    # perfom basisc calculation 
    elif 'calculate' in query:
        # Replace words with symbols for better processing
        query = query.replace("calculate", "").strip()
        query = query.replace("plus", "+").replace("minus", "-").replace("times", "*").replace("divided by", "/")
        calculate(query)
        return
    
    # Tell a joke
    if 'tell me a joke' in query or 'joke' in query or ' give me a joke' in query:
        tell_joke()
        return
    
    # Tell a random quote
    if 'tell me a quote' in query or 'give me quote' in query or 'quote' in query:
        get_random_quote()
        return

    # List available commands
    if 'list all commands' in query or 'what can you do' in query or 'give me all commands' in query or "print all commands" in query:
        list_all_commands()
        return 

    # if no command in query 
    else:
        speak("I'm sorry, I didn't understand that. Please try asking again or say a command.")
        print("I'm sorry, I didn't understand that. Please try asking again or say a command.")
    
# main function to run the program
if __name__ == "__main__":
    wishMe()
    while True:
        if voice_command_mode:
            # Continuously listen for voice commands
            command = takeCommand()  # Get command from voice
            if command:
                handle_command(command)  # Handle the command
        else:
            # Prompt for text input when voice command mode is disabled
            command = input("Enter command (or 'shut down' to quit or 'turn on voice command' to enable voice command mode): ")
            handle_input(command)

    
                    

