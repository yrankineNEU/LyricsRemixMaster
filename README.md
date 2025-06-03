# 🎶 LyricsRemix Master

## 📌 Overview

ReMix Master is a simple Python-based song editing tool that allows users to interactively load a song, substitute lyrics, reverse word order, and reset or playback their custom remix. This project was built in 2023 as a personal practice in key programming concepts such as string manipulation, lists, conditionals, loops, and function design.

## 🧠 Features

- 🔁 **Load Songs**: Choose from a predefined playlist to start mixing.
- ✏️ **Substitute Words**: Replace any word in the lyrics with another.
- 🔃 **Reverse It**: Flip the word order in each line of the song.
- 🔊 **Playback**: Print out the current version of your custom remix.
- ♻️ **Reset**: Restore the original version of the loaded song.
- ❌ **Quit**: Exit the program with a farewell message.

## 🗂️ File Structure

- `remix_master.py` – Main program logic (includes menu, remix functions)
- `music.py` – External file containing:
  - `SONGS` – List of song lyrics (as lists of strings)
 - `remix_functions.py` - Helper functions for program feature logic

## 📚 Concepts Practiced

- String and list operations
- Input handling
- Control flow (`if`, `while`)
- Boolean logic
- Modular programming

## ▶️ How to Run

1. Ensure you have all files in the same directory.
2. Run the program:
   ```bash
   python remix_master.py
