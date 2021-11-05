import speech_recognition
import pyttsx3
robot_brain = ""
robot_ear = speech_recognition.Recognizer()
engine = pyttsx3.init()
with speech_recognition.Microphone() as mic:
    print("Robot: I'm Listening")
    audio = robot_ear.listen(mic)
print("Robot....")
try:
    you = robot_ear.recognize_google(audio)
except:
    you = ""

print("you:"+you)  
if you == "":
    robot_brain="I can't hear you,please say"
elif you == "hello":
    robot_brain="hello xuan truong"
elif you == "can you help me":
        robot_brain="I am siri"
else:
    robot_brain= "i'm fine thank you"

print("Robot"+robot_brain)

engine.say(robot_brain)
engine.runAndWait()