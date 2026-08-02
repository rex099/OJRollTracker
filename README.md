# 🍊 100% Orange Juice Roll Logger

**Author:** Daniel Longo  
**License:** MIT License

A lightweight, background utility built in Python for **100% Orange Juice** players. It logs your dice rolls instantly via hotkeys, tracks live session luck statistics, and automatically copies raw roll data to your clipboard for seamless import into Google Sheets or Excel.

---

## ✨ Features

* **Instant Hotkey Logging:** Tap `1`–`6` on your top row or Numpad (`Numpad 1`–`Numpad 6`) to log rolls without leaving full-screen mode.
* **New Game / Instant Restart (`R`):** Start a new match instantly! Automatically copies the current game's rolls to your clipboard, clears live stats, and creates a fresh CSV file without restarting the program.
* **Live Luck Stats:** Calculates your session average, natural 6s %, natural 1s %, and assigns a dynamic luck badge (*Blessed*, *Balanced*, or *Cursed*).
* **Audio Feedback:** Distinct sound cues via `winsound`—high chimes for natural 6s, low buzzes for natural 1s, rising tones on game restart, and standard clicks for other rolls.
* **Undo Support (`Backspace` / `U`):** Fat-fingered a number? Instantly remove the last roll from both memory and the active CSV log.
* **Pause / Resume Toggle (`F9`):** Temporarily pause hotkey recording so you can type in game chat or Discord without logging random numbers.
* **Clipboard Auto-Copy:** Finishing a game (`Esc` or `R`) automatically copies all raw rolls to your system clipboard (one number per line). Just hit `Ctrl + V` into your spreadsheet!
* **Full CSV File Path Display:** Shows the exact absolute path to the active session CSV in the console frame for easy copying and navigation.
* **Unique Session CSVs:** Generates a timestamped file (`oj_rolls_YYYYMMDD_HHMMSS.csv`) on every launch or game reset so past matches are never overwritten.

---

## 🎮 Controls & Shortcuts

| Key | Action |
| :--- | :--- |
| **`1` – `6`** (or **`Numpad 1` – `6`**) | Log die roll value |
| **`Backspace`** or **`U`** | Undo / remove last recorded roll |
| **`R`** | **New Game** (Copies current match to Clipboard & initializes fresh session) |
| **`F9`** | Toggle Pause / Resume logging |
| **`Esc`** | Exit program & copy session rolls to Clipboard (3s delay to read confirmation) |