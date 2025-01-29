import datetime
import webbrowser
import wikipedia
import webbrowser
import re

#Function to greet the user based on the time of the day
def regards():
    hr = int(datetime.datetime.now().hour)
    if hr >= 0 and hr < 12:
        print("Good Morning, JYOTSHNA!")
    elif hr >= 12 and hr < 17:
        print("Good Afternoon, JYOTSHNA!")
    else:
        print("Good Evening, JYOTSHNA!")
    print("I am ROSE, your Personal Chatbot. What is your request?")

    # Main chatbot functionality
if __name__ == "__main__":

    regards()
    while True:
        print("\nI can perform tasks like 'open YouTube,' 'give weather report,' or 'exit.'")
        query = input("ME: ").lower()

        # Rule-based responses
        if re.search(r'\bhello\b|\bhi\b|\bhey\b', query):
            print("ROSE: Hello! How can I help you?")
        elif 'how are you' in query:
            print("ROSE:  I'm doing well! Thanks for asking.")

        elif 'open youtube' in query:
            print("ROSE: Opening YouTube...")
            webbrowser.open('https://www.youtube.com/')
        elif 'open gmail' in query:
            print("ROSE: Opening Gmail...")
            webbrowser.open('https://www.gmail.com/')
        elif 'search google' in query:
            print("ROSE: What would you like to search for?")
            search_query = input("Enter your search query: ")
            print("ROSE: Searching Google...")
            webbrowser.open(f'https://www.google.com/search?q={search_query}')
        elif 'current time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"ROSE: The current time is {current_time}.")
        elif 'open facebook' in query:
            print("ROSE: Opening Facebook...")
            webbrowser.open('https://www.facebook.com/')
        elif 'open instagram' in query:
            print("ROSE: Opening Instagram...")
            webbrowser.open('https://www.instagram.com/')
        elif 'weather' in query:
            print("ROSE: Conveying you to weather report...")
            webbrowser.open('https://www.weather.com/')
        elif 'news' in query:
            print("ROSE: Opening the latest news for you...")
            webbrowser.open('https://news.google.com/')
        elif  'exit' in query:
            print("ROSE: SAYONARA, JYOTSHNA! It was nice chatting with you")
            break
        else:
            print("ROSE: I cannot undertand your request.Please say again")
