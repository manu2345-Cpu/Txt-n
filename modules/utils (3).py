import time
import math
import os
from pyrogram.errors import FloodWait
from datetime import datetime, timedelta


class Timer:
    def __init__(self, time_between=5):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False


# Convert bytes to human-readable format
def hrb(value, digits=2, delim="", postfix=""):
    if value is None:
        return None
    chosen_unit = "B"
    for unit in ("KiB", "MiB", "GiB", "TiB"):
        if value > 1000:
            value /= 1024
            chosen_unit = unit
        else:
            break
    return f"{value:.{digits}f}{delim}{chosen_unit}{postfix}"


# Convert seconds to human-readable time
def hrt(seconds, precision=0):
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

    return "".join(pieces[:precision]) if precision else "".join(pieces)


# Timer instance for controlling updates
timer = Timer()


# Main progress bar function with animations
async def progress_bar(current, total, reply, start):
    # Live animated emojis
    animated_emojis = ["⚡", "🚀", "✨", "🔥", "💫", "🌟", "⚙️", "🔄", "⏳"]
    emoji_index = int((time.time() - start) % len(animated_emojis))
    live_emoji = animated_emojis[emoji_index]

    # Spinner animation
    spinner_frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    spinner_index = int((time.time() - start) % len(spinner_frames))
    spinner = spinner_frames[spinner_index]

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
            eta = hrt(remaining_bytes / speed, precision=1) if speed > 0 else "-"
            sp = f"{hrb(speed)}/s"
            tot = hrb(total)
            cur = hrb(current)
