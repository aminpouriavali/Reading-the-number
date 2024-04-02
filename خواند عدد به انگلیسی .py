import pyttsx3
from num2words import num2words

engine = pyttsx3.init()

def convert_number_to_text(number):
    text = num2words(number)
    return text

number = int(input("Enter a number: "))
text = convert_number_to_text(number)

engine.say(text)
engine.runAndWait()
