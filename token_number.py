from gtts import gTTS
from playsound import playsound

token = input("Enter token number")
txt = 'ടോക്കൺ നമ്പർ' + token
tts = gTTS(txt,lang='ml')
tts.save('token.mp3')
playsound('token.mp3')