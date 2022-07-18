import pyttsx3

vtf = pyttsx3.init()

rate = vtf.getProperty('rate')
print(rate)
vtf.setProperty('rate', 170)

def vtf_speak(text):
    print("Speaking...")
    vtf.say(text)
    vtf.runAndWait()

txt = "Heyy Friend, I am your Virtual Talking Friend. My Name is Hayavadan"
vtf_speak(txt)

while txt != 'bye':
    txt = input('What should I say: ')
    txt = txt.lower()
    if txt != 'bye':
        vtf_speak(txt)
    else:
        vtf_speak('See You Again Friend !! That was nice talking to you !')
