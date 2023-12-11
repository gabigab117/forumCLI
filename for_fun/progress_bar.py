from rich.progress import track
import time

def progress_bar(description):
    total = 0
    for _ in track(range(100), description=description):
        time.sleep(0.01)
        total += 1