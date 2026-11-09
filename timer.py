import tkinter as tk #--DESIGNER--#
import time #--It makes the counting work.--#
import threading #--The GUARD so it doesn't FREEZE --#
# ---loop for alarm soud repeat 25 times
stop_alarm = False #if false, don't stop the the alarm 
#check if it is in windos 
try:
    import winsound
    def ring():
        global stop_alarm
        for _ in range(25):
            if stop_alarm: return # if the button stop the  sound also stop
            winsound.Beep(1000, 300)
            time.sleep(0.2)
except:
    def ring():
        for _ in range(25):
            if stop_alarm: return
            print("\aTIME'S UP!")
            time.sleep(0.5)
            # for mac/linux beep
            root.bell()
# --- create main layout ---
root = tk.Tk()
root.title("Timer")
root.geometry("360x520")
root.config(bg="#f2f2f2")

tk.Label(root, text="Timer", font=("Arial", 22, "bold"), bg="#f2f2f2").pack(anchor="w", padx=20, pady=20)
