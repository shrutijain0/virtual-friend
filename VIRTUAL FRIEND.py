import pyttsx3
friend=pyttsx3.init()
speech=input("SAY SOMETHING:")
friend.say(speech)
friend.runAndWait()