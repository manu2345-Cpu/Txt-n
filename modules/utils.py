
import time
import math
import os
import tkinter as tk
import itertools
from datetime import timedelta
from pyrogram.errors import FloodWait

emojis = ["😀", "😂", "😍", "😎", "😴", "🤔", "🎉", "✨", "🔥"]

def animate_emoji(index=0):
    label.config(text=emojis[index])  # Update emoji
    next_index = (index + 1) % len(emojis)  # Get next index cyclically
    root.after(500, animate_emoji, next_index)  # Call the function again after 500ms

root = tk.Tk()
root.title("Live Emoji Animation")
root.geometry("200x200")

label = tk.Label(root, text="", font=("Arial", 50))
label.pack(expand=True)

root.after(0, animate_emoji)
root.mainloop()






import time
import math
import os
import tkinter as tk
import itertools
from pyrogram.errors import FloodWait

class Timer:
    def __init__(self, time_between=5):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False


from datetime import datetime,timedelta

#lets do calculations
def hrb(value, digits= 2, delim= "", postfix=""):
    """Return a human-readable file size.
    """
    if value is None:
        return None
    chosen_unit = "B"
    for unit in ("KiB", "MiB", "GiB", "TiB"):
        if value > 1000:
            value /= 1024
            chosen_unit = unit
        else:
            break
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix

def hrt(seconds, precision = 0):
    """Return a human-readable time delta as a string.
    """
    pieces = []
    value = timedelta(seconds=seconds)
    

    if value.days:
        pieces.append(f"{value.days}d")

    seconds = value.seconds

    if seconds >= 3600:
        hours = int(seconds / 3600)
        pieces.append(f"{hours}h")
        seconds -= hours * 3600

    if seconds >= 60:
        minutes = int(seconds / 60)
        pieces.append(f"{minutes}m")
        seconds -= minutes * 60

    if seconds > 0 or not pieces:
        pieces.append(f"{seconds}s")

    if not precision:
        return "".join(pieces)

    return "".join(pieces[:precision])



timer = Timer()

async def progress_bar(current, total, reply, start):
    if timer.can_send():
        now = time.time()
        diff = now - start
        if diff < 1:
            return
        else:
            perc = f"{current * 100 / total:.1f}%"
            elapsed_time = round(diff)
            speed = current / elapsed_time
            remaining_bytes = total - current
            if speed > 0:
                eta_seconds = remaining_bytes / speed
                eta = hrt(eta_seconds, precision=1)
            else:
                eta = "-"
            sp = str(hrb(speed)) + "/s"
            tot = hrb(total)
            cur = hrb(current)
            bar_length = 11
            completed_length = int(current * bar_length / total)
            remaining_length = bar_length - completed_length
            progress_bar = "🔴" * completed_length + "🟧" * remaining_length
            
            try:
                await reply.edit(f'`\n ╭──⌯════𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐢𝐜𝐬═════⌯──╮ \n├⚡ {progress_bar} |﹝{perc}﹞ \n├🚀 Speed ➤ {sp} \n├📟 Processed ➤ {cur}\n├🧲 Size - ETA ➤ {tot} - {eta} \n╰─═══ ✨🦋PELU HARSHU🦋✨ ═══─╯`\n') 
            except FloodWait as e:
                time.sleep(e.x)

emojis = ["😀", "😂", "😍", "😎", "😴", "🤔", "🎉", "✨", "🔥"]

def animate_emoji():
    for emoji in itertools.cycle(emojis):  # Loop through emojis infinitely
        label.config(text=emoji)  # Update emoji on label
        root.update()  # Refresh the GUI
        time.sleep(0.5)  # Add a delay for animation

# Set up the tkinter GUI
root = tk.Tk()
root.title("Live Emoji Animation")
root.geometry("200x200")

# Create a label to display the emoji
label = tk.Label(root, text="", font=("Arial", 50))
label.pack(expand=True)

# Start the animation in a new thread
root.after(0, animate_emoji)

# Run the tkinter main loop
root.mainloop()

        
