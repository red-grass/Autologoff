import time
import os
import sys
from tkinter import *
from tkinter import ttk

if sys.platform == "win32":
    import win32api

    def getIdleTime():
        return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0


if __name__ == "__main__":
    start = Tk()
    start.geometry("500x50")
    start.title("Inactivity Notice")

    start_text = "Your session will be logged off after 1 hr if inactive."
    warning = Label(start, text=start_text, fg="black", font=("Calibri", 12))
    warning.place(x=70, y=30, anchor="sw")

    start.mainloop()

    while True:
        duration = getIdleTime()
        # prints inactivity seconds 
        print(f"User idle for {duration} seconds")
        time.sleep(1)

        if duration >= 3300 and duration <= 3301:
            top = Tk()
            top.geometry("900x50")
            top.title("User Inactivity")

            message_text = "You have been inactive for 55 minutes. Your session will be logged off in 5 minutes if no activity is detected."
            warning = Label(top, text=message_text, fg="black", font=("Calibri", 12))
            warning.place(x=70, y=30, anchor="sw")
            # warning.pack()

            top.after(3000, lambda: top.destroy()) #close after 3 seconds, adding on 3 seconds 
            top.mainloop()

        if (duration >= 3600):
            final = Tk()
            final.geometry("700x50")
            final.title("User Inactivity")

            action = Label(
                final,
                text="Inactivity Warning: User has been inactive for more than an hour. Logging off...",
                fg="black",
                font=("Calibri", 12),
            )
            action.place(x=90, y=30, anchor="sw")

            final.after(2000, lambda: final.destroy())
            final.mainloop()
            os.system("shutdown /l /f")  # force log off
