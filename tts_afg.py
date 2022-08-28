from gtts import gTTS

import os

# Constants
AUDIO_DIR = "audio"
TEXTS_FILENAME = "assets.txt"
LANG = "en"


# Main function
def main(): 
  try:
    os.mkdir(AUDIO_DIR)
  except OSError:
    pass

  with open(TEXTS_FILENAME, "r") as file:
    words = set(file.readlines())
    # print(words)

    for word in words:
      word = word.strip()
      print(f"Generating {word}.mp3...")
      audio = gTTS(text=word, lang=LANG, slow=False)
      audio.save(f"{AUDIO_DIR}/{word}.mp3")


if __name__ == "__main__":
  main()
