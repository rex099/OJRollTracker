"""
🍊 100% Orange Juice Roll Logger
Author: Daniel Longo
Description: Automated roll logging tool with live stats, audio feedback, 
             undo functionality, and automatic spreadsheet copy.
"""

import csv
import os
import time
import winsound
from datetime import datetime
from pynput import keyboard
import pyperclip

# Program Metadata
AUTHOR = "Daniel Longo"

# Generate unique CSV file for this session
session_time = datetime.now().strftime("%Y%m%d_%H%M%S")
CSV_FILE = f"oj_rolls_{session_time}.csv"

# Global state
rolls = []
logging_active = True

# Create empty session CSV
with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
    pass

def play_sound(roll_val):
    """Play audio feedback depending on roll value."""
    try:
        if roll_val == 6:
            winsound.Beep(1200, 120)  # High chime for Nat 6
        elif roll_val == 1:
            winsound.Beep(300, 150)   # Low buzz for Nat 1
        else:
            winsound.Beep(750, 80)    # Standard click beep
    except Exception:
        pass

def play_undo_sound():
    """Play low double beep on undo."""
    try:
        winsound.Beep(400, 80)
        winsound.Beep(300, 80)
    except Exception:
        pass

def rewrite_csv():
    """Sync CSV file with the current in-memory rolls list."""
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for r in rolls:
            writer.writerow([r])

def display_stats():
    """Print current live session metrics to the console."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 60)
    status_str = "🟢 ACTIVE" if logging_active else "🔴 PAUSED (Press F9 to Resume)"
    print(f" 🍊 100% Orange Juice Roll Logger | Author: {AUTHOR}")
    print(f" Status: {status_str}")
    print(f" 📁 Session File: {CSV_FILE}")
    print(" [1-6] Log Roll | [Backspace/U] Undo Last | [F9] Pause/Resume | [Esc] Finish & Copy")
    print("=" * 60)

    if not rolls:
        print("\n No rolls recorded yet. Waiting for input...")
        return

    total = len(rolls)
    avg = sum(rolls) / total
    sixes = rolls.count(6)
    ones = rolls.count(1)

    # Calculate luck rating
    if avg >= 4.0:
        luck = "🔥 Blessed by RNG"
    elif avg <= 3.0:
        luck = "💀 Strictly Cursed"
    else:
        luck = "⚖️ Balanced"

    print(f"\n Last Logged Roll : {rolls[-1]}")
    print(f" Total Rolls      : {total}")
    print(f" Session Average  : {avg:.2f} ({luck})")
    print(f" Natural 6s       : {sixes} ({sixes/total*100:.1f}%)")
    print(f" Natural 1s       : {ones} ({ones/total*100:.1f}%)")
    print("-" * 60)

def log_roll(roll_val):
    rolls.append(roll_val)
    rewrite_csv()
    play_sound(roll_val)
    display_stats()

def undo_last_roll():
    if rolls:
        removed = rolls.pop()
        rewrite_csv()
        play_undo_sound()
        display_stats()
        print(f"\n ⚠️ UNDO: Removed roll ({removed})")

def copy_to_clipboard():
    """Copy raw rolls (one per line) to Windows clipboard on exit."""
    if rolls:
        clipboard_text = "\n".join(str(r) for r in rolls)
        pyperclip.copy(clipboard_text)
        print("\n 📋 SUCCESS: All session rolls copied to clipboard!")
        print("    You can now paste (Ctrl + V) directly into your Google Sheet.")
    else:
        print("\n ℹ️ No rolls logged this session.")

def on_press(key):
    global logging_active

    try:
        # Toggle logging state with F9
        if key == keyboard.Key.f9:
            logging_active = not logging_active
            winsound.Beep(1000 if logging_active else 500, 150)
            display_stats()
            return

        # If logging is paused, ignore other input
        if not logging_active:
            return

        # Handle Undo via Backspace key
        if key == keyboard.Key.backspace:
            undo_last_roll()
            return

        # Handle keyboard characters ('1'-'6' or 'u' for undo)
        if hasattr(key, 'char') and key.char:
            char = key.char.lower()
            if char in ['1', '2', '3', '4', '5', '6']:
                log_roll(int(char))
            elif char == 'u':
                undo_last_roll()

        # Handle Numpad Virtual Keys (VK 97 = Numpad 1, VK 102 = Numpad 6)
        elif hasattr(key, 'vk') and 97 <= key.vk <= 102:
            log_roll(key.vk - 96)

    except Exception as e:
        print(f"Error handling key input: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        copy_to_clipboard()
        print("\n Closing logger in 3 seconds...")
        time.sleep(3)  # Delay so you can read the confirmation message
        return False

# Initial display setup
display_stats()

# Start listening for key events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()