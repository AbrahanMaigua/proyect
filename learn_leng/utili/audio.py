from unicodedata import name
from gtts import gTTS
import os 


def say(text, name, LANG: str ='es', tld:str = 'es'):
      voice = gTTS(text=text, lang=LANG, tld=tld)
      print(f'save {name}.mp3 ')
      voice.save(f'{name}.mp3')
      
      return 'ok', 200

print(os.getcwd())
os.makedirs('audio', exist_ok=True)
os.chdir(os.getcwd() + '/audio')
print(os.getcwd())


if __name__ == '__main__':
   alfabeto = ['A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 
               'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'Y',
               'Z' ]

   print(len(alfabeto))

   for i in alfabeto:
      say(i, i)
