from tkinter.tix import TEXT
from gtts import gTTS

import os

# Constants
# AUDIO_DIR = "audio"
# TEXTS_FILENAME = "assets.txt"
# TEXTS_DIR = "text"
# AUDIO_DIR = "audio_texts"
# LANG = "en"

AUDIO_DIR = "audio2"
LANG = "en"
TEXTS_FILENAME = "instructions.txt"

# Main function
def main(): 

  if not os.path.exists(AUDIO_DIR):
    os.mkdir(AUDIO_DIR)

  with open(TEXTS_FILENAME, "r") as fp:
    text = fp.readlines()
    for line in text:
      line = line.split(' ', 1)
      filename = line[0]
      print(f"Generating {AUDIO_DIR}/{filename}.mp3...")
      audio = gTTS(text=line[1], lang=LANG, slow=True)
      audio.save(f"{AUDIO_DIR}/{filename}.mp3")


  # text_files = os.listdir(TEXTS_DIR)

  # for file in text_files:
  #   # print(file)
  #   with open(f"{TEXTS_DIR}/{file}", "r") as fp:
  #     text = fp.read()
  #     print(f"Generating {file}.mp3...")
  #     audio = gTTS(text=text, lang=LANG, slow=True)
  #     audio.save(f"{AUDIO_DIR}/{file}.mp3")


  # try:
  #   os.mkdir(AUDIO_DIR)
  # except OSError:
  #   pass

  # with open(TEXTS_FILENAME, "r") as file:
  #   words = set(file.readlines())
  #   # print(words)

  #   for word in words:
  #     word = word.strip()
  #     print(f"Generating {word}.mp3...")
  #     audio = gTTS(text=word, lang=LANG, slow=False)
  #     audio.save(f"{AUDIO_DIR}/{word}.mp3")


if __name__ == "__main__":
  main()
