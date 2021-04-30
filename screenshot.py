from pyautogui import screenshot
from tkinter import messagebox
from tkinter import *
import time

def take_screenshot(root_window):
    try:
        now = time.time()
        root_window.destroy()
        my_screenshot = screenshot()
        my_screenshot.save(
            r"./screenshot_save/screenshot" + str(now) + ".png"
        )
    except:
        print("You have some error!")
    else:
        messagebox.showinfo(
            "Simpel Screenshot App",
            "Take Screenshot Successfuly\nPATH:./screenshot_save"
        )

    with open("screenshot_history.log", 'a') as log_file:
        log_file.write("\nTake Screenshot In >>> " + str(now))
