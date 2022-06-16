# CODE IS ORIGINALLY WRITTEN BY MR. NAMAN SHARMA
import random
import time
import webbrowser
import wikipedia
import playsound
import datetime
import pywhatkit as pw
import pyttsx3
import os

engine = pyttsx3.init()


def speak(contex):
    engine.say(contex)
engine.runAndWait()


song = """Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are
When the blazing sun is gone
When he nothing shines upon
Then you show your little light
Twinkle, twinkle, all the night
Twinkle, twinkle, little star
How I wonder what you are"""

hwno = 1

print('=========THIS BOT IS MADE BY NAMAN 9TH-A============\n=========BOT IS INITIALIZING PLEASE WAIT============')
# playsound.playsound("start_sound.wav")
time.sleep(5)


def write(CTX):
    print(f"Kiara-| {CTX}")


def ask():
    queryy = input('You:)-│ ')
    queryy = queryy.replace('?', '')
    queryy = queryy.replace('.', '')
    queryy = queryy.replace('!', '')
    queryy = queryy.replace('|', '')
    queryy = queryy.lower()

    return queryy


def ask_org():
    queryy = input('You-│ ')
    return queryy


def askname():
    hrs = int(datetime.datetime.now().hour)
    if 0 < hrs < 12:
        write("Good Morning!, What's your name?")
        name = ask()
        name = name.replace('myself', '')
        name = name.replace('my name is', '')
        write(f"Okay! {name}, How may I help you? :)")

    elif 12 <= hrs <= 16:
        write("Good Afternoon!, What's your name?")
        name = ask()
        name = name.replace('myself', '')
        name = name.replace('my name is', '')
        write(f"Okay! {name}, How may I help you? :)")

    else:
        write("Good Evening!, What's your name?")
        name = ask()
        name = name.replace('myself', '')
        name = name.replace('my name is', '')
        write(f"Okay! {name}, How may I help you? :)")
    return name


naam = askname()

while True:
    query = ask()

    try:
        if 'date' in query:
            dateis = datetime.datetime.now().date()
            write(f"The date is {dateis}")

        elif 'whats your age' in query or 'how old are you' in query:
            write("My age is about 40 days! lol")

        elif 'are you boy or girl' in query or 'whats your gender' in query or 'what is your gender' in query or 'are you male or female' in query:
            write("As my name says I am a girl!")

        elif 'open owners github' in query:
            write("Opening Owner's Github")
            webbrowser.open("https://www.github.com/naman3428")

        elif 'open github' in query:
            write("Opening Github")
            webbrowser.open("https://www.github.com/")

        elif 'open youtube' in query:
            write("Opening youtube")
            webbrowser.open("https://www.youtube.com/")

        elif 'open discord' in query:
            write("Opening Discord")
            webbrowser.open("https://www.discord.com/app")

        elif 'open whatsapp' in query:
            write("Opening Whatsapp")
            webbrowser.open("https://web.whatsapp.com")

        elif 'open gmail' in query or 'open mails' in query:
            write("Opening Gmail")
            webbrowser.open("https://www.gmail.com/")

        elif 'open browser' in query:
            brlocation = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            write("Opening your browser🙂")
            os.startfile(brlocation)

        elif 'open calculator' in query:
            write("Opening calculator")
            calloc = "C:\Windows\System32\calc.exe"
            os.startfile(calloc)



        elif "how is your day" in query or 'wassup' in query or 'whatsup' in query:
            write(random.choice("It's Good😊", "Ahh... Neither good neither bad", "Same as you😁"))

        elif "sing a song" in query:
            write("For Sure! I am now singing🤪")
            speak(song)

        elif "where you live" in query or "where do you live" in query:
            write(random.choice("That's a secret🤫", "Ofcourse, I live in your PC lol! 🤷‍"))

        elif 'time' in query:
            timeis = datetime.datetime.now().strftime("%H:%M")
            write(f"The time is {timeis}")

        elif 'hi' in query or 'hello' in query or 'hey' in query:
            write('Hello!!')

        elif 'thanks' in query:
            write("Your Welcome!")

        elif 'your face' in query:
            write('༼ つ ◕_◕ ༽つ')

        elif 'who made you' in query:
            write("My author is MR.NAMAN SHARMA 9th-A")


        elif 'how are you' in query or "how r u" in query:
            write('I am great! What about you?')
            time.sleep(0.5)
            ask()
            if 'fine' or 'great' or 'good' or 'happy' in query:
                write(random.choice(['Oh! Great!', "That's great", "Noice!"]))


            else:
                sed = ['You can listen to songs', 'You can play outside', 'You can watch your favorite movie!']
                write(random.choice(sed))
                ask()
                write('cool!')

        elif 'play' in query:
            vidname = query.replace('play', "")
            write(f"Playing {vidname} on Youtube")
            pw.playonyt(vidname)

        elif 'exit' in query or 'bye' in query or 'goodbye' in query or 'cya' in query or 'see you' in query:
            write(f"Okay! I am exiting... Goodbye! {naam}")
            time.sleep(3)
            break

        # not working##
        elif 'add' in query or '+' in query:
            try:
                ques = query.replace("add", "")
                ques = ques.replace("and", "")
                ques = ques.replace("what", "")
                ques = ques.replace("is", "")
                ques = ques.replace("find", "")
                ques = ques.replace("+", " ")
                n1 = int(ques.split()[0])
                n2 = int(ques.split()[1])
                addans = n1 + n2
                write(f"The sum of {n1} and {n2} is {addans}")


            except Exception as err:
                ques = query.replace("add", "")
                ques = query.replace("and", "")
                n1 = int(ques.split()[0])
                n2 = int(ques.split()[1])
                print(err)
                print(n1, n2)
                write("Please provide two numbers")

        elif 'subtract' in query or '-' in query:
            try:
                ques = query.replace("add", "")
                ques = ques.replace("and", "")
                ques = ques.replace("what", "")
                ques = ques.replace("is", "")
                ques = ques.replace("find", "")
                ques = ques.replace("-", " ")
                ques = ques.replace("minus", "")
                ques = ques.replace("subtract", "")
                n1 = int(ques.split()[0])
                n2 = int(ques.split()[1])
                addans = n1 - n2
                write(f"The sum of {n1} and {n2} is {addans}")


            except Exception as err:
                ques = query.replace("add", "")
                ques = query.replace("and", "")
                n1 = int(ques.split()[0])
                n2 = int(ques.split()[1])
                print(err)
                print(n1, n2)
                write("Please provide two numbers")

        elif 'multiply' in query or '*' in query:
            try:
                ques = query.replace("multiply", "")
                ques = ques.replace("and", "")
                ques = ques.replace("by", "")
                ques = ques.replace("*", " ")
                ques = ques.replace("what", "")
                ques = ques.replace("is", "")
                ques = ques.replace("find", "")

                n1 = int(ques.split()[0])
                n2 = int(ques.split()[1])
                addans = n1 * n2
                write(f"The multiplication of {n1} and {n2} is {addans}")


            except:
                write("Please provide two numbers")


        elif 'divide' in query or "/" in query:
            try:
                ques = query.replace("multiply", "")
                ques = ques.replace("and", "")
                ques = ques.replace("by", "")
                ques = ques.replace("is", "")
                ques = ques.replace("find", "")
                ques = ques.replace("/", " ")
                ques = ques.replace("what", "")
                n1 = int(ques.split()[0])
                n2 = int(ques.split()[1])
                addans = n1 / n2
                write(f"{n1} divided by {n2} is {addans}")


            except:
                write("Please provide two numbers")


        elif 'square root' in query:
            try:
                ques = query.replace("square root", "")
                ques = ques.replace("of", "")
                ques = ques.replace("by", "")
                ques = ques.replace("what is the", "")
                ques = ques.replace("what", "")
                n1 = int(ques.split()[0])
                addans = n1 ** 0.5
                write(f"The square root of {n1} is {addans}")

            except:
                write("Sorry i got a error")


        elif 'square' in query:
            try:
                ques = query.replace("square", "")
                ques = ques.replace("of", "")
                ques = ques.replace("by", "")
                ques = ques.replace("what is the", "")
                n1 = int(ques.split()[0])
                # n2 = int(ques.split()[1])
                addans = n1 * n1
                write(f"Square of {n1} is {addans}")

            except:
                write("Got an error")

        elif 'cube' in query:
            try:
                ques = query.replace("cube", "")
                ques = ques.replace("of", "")
                ques = ques.replace("by", "")
                ques = ques.replace("what is the", "")
                n1 = int(ques.split()[0])
                # n2 = int(ques.split()[1])
                addans = n1 * n1 * n1
                write(f"Cube of {n1} is: {addans}")

            except:
                write("Got an error")


        elif 'cube root' in query:
            try:
                ques = query.replace("cube root", "")
                ques = ques.replace("of", "")
                ques = ques.replace("by", "")
                ques = ques.replace("what is the", "")
                n1 = int(ques.split()[0])
                addans = n1 ** (1 / 3)
                write(f"The cube root of {n1} is {addans}")


            except:
                write("Sorry i got a error")




        elif 'wikipedia' in query:
            print("Searching Wikipedia... Please wait...")
            ques = query.replace("wikipedia", "")
            ques = query.replace("who is", "")
            ques = query.replace("what is", "")
            ques = query.replace("what are", "")
            ques = query.replace("search", "")
            ans = wikipedia.summary(ques, sentences=2)
            write(ans)

        elif 'who is' in query or 'what is' in query:
            try:
                write("Searching Wikipedia... Please wait...")
                query = query.replace("wikipedia", "")
                query = query.replace("who", "")
                query = query.replace("what", "")
                query = query.replace("what", "")
                query = query.replace("search", "")
                query = query.replace("is", "")
                query = query.replace("are", "")
                ans = wikipedia.summary(query, sentences=2)
                write(ans)

            except:
                write("I can't search it on wikipedia opening your query in browser...")
                webbrowser.open(query)



        elif 'i love you' in query:
            write(random.choice(['Oh... I love you too🥰', "Bruh... I don't love you"]))
            ask()

        elif 'what do you eat' in query:
            write('I am a bot... How can I eat something!? 🙄')

        elif 'naman' in query:
            write("He is a great guy! He developed me.. He lives in 9th-A you can meet him by going there! 😁")

        elif 'rishabh' in query:
            write("He is also a good guy.. But he get angry too fast lmao")

        elif 'pushkar' in query:
            write("Hecc! This name is kinda sus... Btw I know him he is a boy who lives in 9th-A")

        elif 'iqra' in query:
            write("She is Naman's and his classmates A.I. Teacher... She is great")

        elif 'game' in query:
            write("Sure! Let's Play game..... Which game do you want to play? Choose any: Magical Ball")
            gamename = ask()
            if "magical" in gamename:
                write("Hmm... Okay! Ask me anything and I will reply yes or no. You can also ask about your future")
                on = 0
                while on == 0:
                    q = ask()
                    if "quit" in q:
                        write("Okay! Sure")
                        on = 1
                    else:
                        write("Please wait.. Magical ball is thinking the answer")
                        time.sleep(3)
                        write(random.choice(["Yes", "No"]))

        elif 'play a song' in query:
            write('Sure! which song do you want to listen?')
            songname = ask()
            write(f'Playing {songname} on youtube')
            pw.playonyt(songname)

        elif 'text to handwriting' in query or 'do my homework' in query or 'do my assignment' in query:
            write("What will be the text or content in your homework.. You can copy from anywhere and paste it here!")
            content = ask()
            write("What will be the pen color? choose only: RED, BLUE, BLACK, GREEN")
            p_color = ask_org()
            if 'red' in p_color:
                write("Okay! Assignment is in progress! Please wait a little bit...")
                pw.text_to_handwriting(content, rgb=[255, 0, 0], save_to=(f"yourhomework{hwno}.png"))
                write("Done! Your homework is saved in the bot's folder! :)")
                hwno += 1

            elif 'blue' in p_color:
                write("Okay! Assignment is in progress! Please wait a little bit...")
                pw.text_to_handwriting(content, rgb=[0, 0, 155], save_to=(f"yourhomework{hwno}.png"))
                write("Done! Your homework is saved in the bot's folder! :)")
                hwno += 1

            elif 'black' in p_color:
                write("Okay! Assignment is in progress! Please wait a little bit...")
                pw.text_to_handwriting(content, rgb=[0, 0, 0], save_to=(f"yourhomework{hwno}.png"))
                write("Done! Your homework is saved in the bot's folder! :)")
                hwno += 1

            elif 'green' in p_color:
                write("Okay! Assignment is in progress! Please wait a little bit...")
                pw.text_to_handwriting(content, rgb=[0, 155, 0], save_to=(f"yourhomework{hwno}.png"))
                write("Done! Your homework is saved in the bot's folder! :)")
                hwno += 1

            else:
                write('got an error rip')




        else:
            write('If I was in the place of you, I had searched this to google or wikipedia')
            write(f'Query: {query}')


    except Exception as exp:
        print(exp)

        write('I got an error')
        playsound.playsound('erro.mp3')
