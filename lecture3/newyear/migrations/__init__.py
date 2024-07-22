import pyttsx3

Robo = pyttsx3.init()

print("Welcome to RObospeaker created by Adesh P Singh")

while True:

    user_input = input("Enter what you want to say")
    if user_input == 0:
        break
    else:
        print(user_input)
        Robo.say(user_input)
        Robo.runAndWait()
