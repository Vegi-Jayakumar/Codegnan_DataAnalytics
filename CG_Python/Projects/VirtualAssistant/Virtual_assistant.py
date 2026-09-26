'''
Virtual Assistant --> make conversations, locate maps, greetings...

#TTS --> gTTS (google text to speech)

'''

import gtts
from gtts import gTTS

#convert text to audio
text = "Hey Nee Ayya Jagiraa, Chal Maavaadochindra, Iga Jadthiyyaley, Jumbalikay Aaya Sher!"
obj = gTTS(text)
obj.save("output.mp3")
