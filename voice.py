import speech_recognition as sr
import pyttsx3
import re
import subprocess
import random

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Memory
history = []
last_result = None

# 🔊 Speak
def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

# 🔤 Convert words → numbers
def word_to_number(text):
    text = text.lower()

    replacements = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "ten": "10",
        "eleven": "11",
        "twelve": "12",
        "twenty": "20",
        "thirty": "30",
        "forty": "40",
        "fifty": "50",
        "hundred": "100"
    }

    for word, num in replacements.items():
        text = text.replace(word, num)

    text = text.replace("oneplus", "1 plus")

    return text

# 🎤 Listen
def listen():
    try:
        with sr.Microphone() as source:
            print("Adjusting noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            print("Listening...")
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)

        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()

    except sr.WaitTimeoutError:
        print("No speech detected")
        return ""

    except Exception as e:
        print("Error:", e)
        speak("Sorry, I didn't understand")
        return ""

# 🧠 Process command
def process_command(text):
    text = word_to_number(text)

    numbers = list(map(int, re.findall(r'\d+', text)))

    if "add" in text or "plus" in text:
        return 1, numbers
    elif "subtract" in text or "minus" in text:
        return 2, numbers
    elif "multiply" in text or "times" in text:
        return 3, numbers
    elif "divide" in text:
        return 4, numbers
    elif "factorial" in text:
        return 5, numbers
    elif "power" in text:
        return 6, numbers
    elif "square" in text and "root" not in text:
        return 7, numbers
    elif "cube" in text:
        return 8, numbers
    elif "square root" in text:
        return 9, numbers
    else:
        return None, []

# ⚡ Run C++
def run_cpp(choice, numbers):
    input_data = f"{choice}\n"

    for num in numbers:
        input_data += f"{num}\n"

    result = subprocess.run(
        ["v.exe"],  # Windows executable
        input=input_data,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()

# 🔁 MAIN LOOP
print("🎤 Voice Calculator Started (say 'exit' to stop)")

while True:
    text = listen()

    if text == "":
        continue

    # Exit
    if "exit" in text:
        speak("Goodbye")
        break

    # History command
    if "history" in text:
        if len(history) == 0:
            speak("No history yet")
        else:
            speak("Here are your recent calculations")
            for item in history[-5:]:
                speak(item)
        continue

    # Last answer
    if "last answer" in text:
        if last_result:
            speak(f"Last answer was {last_result}")
        else:
            speak("No previous result")
        continue

    # Process
    choice, numbers = process_command(text)

    if choice is None or len(numbers) == 0:
        speak("Command not recognized")
        continue

    result = run_cpp(choice, numbers)

    print("DEBUG RESULT:", result)

    # Save history
    entry = f"{text} = {result}"
    history.append(entry)
    last_result = result

    # Smart responses
    responses = [
        f"The answer is {result}",
        f"That gives you {result}",
        f"Your result is {result}",
        f"I calculated it, it's {result}",
    ]

    speak(random.choice(responses))