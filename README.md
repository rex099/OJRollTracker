# 🍊 100% Orange Juice Roll Logger

**Author:** Daniel Longo  
**License:** MIT License

A lightweight, background utility built in Python for **100% Orange Juice** players. It logs your dice rolls instantly via hotkeys, tracks live session luck statistics, and automatically copies raw roll data to your clipboard for seamless import into Google Sheets or Excel.

---

## ✨ Features

* **Instant Hotkey Logging:** Tap `1`–`6` on your top row or Numpad (`Numpad 1`–`Numpad 6`) to log rolls without leaving full-screen mode.
* **Live Luck Stats:** Automatically calculates your live session average, natural 6s %, natural 1s %, and assigns a dynamic luck badge (*Blessed*, *Balanced*, or *Cursed*).
* **Audio Feedback:** Distinct sound cues via `winsound`—high chimes for natural 6s, low buzzes for natural 1s, and standard subtle clicks for other rolls.
* **Undo Support (`Backspace` / `U`):** Fat-fingered a number? Instantly remove the last roll from both memory and the active CSV log.
* **Pause / Resume Toggle (`F9`):** Temporarily pause hotkey recording so you can type in game chat or Discord without logging random numbers.
* **Clipboard Auto-Copy:** Hitting `Esc` finishes the session and automatically copies all raw rolls to your system clipboard (one number per line). Just press `Ctrl + V` into your spreadsheet!
* **Unique Session CSVs:** Generates a timestamped file (`oj_rolls_YYYYMMDD_HHMMSS.csv`) on every launch so past matches are never overwritten.