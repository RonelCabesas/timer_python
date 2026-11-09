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
# picker frame 
picker = tk.Frame(root, bg="#f2f2f2")
picker.pack(pady=20)

# make wheel function
def make_wheel(max_val):#Function that creates one wheel. max_val = 23 for hours, 59 for minutes/seconds.
    f = tk.Frame(picker, bg="#f1f1f1")#Creates a small box for wheel
    f.pack(side="left", padx=12)#Places it side-by-side to the left. So it get H | M | S horizontally.
    sb = tk.Spinbox(f, from_=0, to=max_val, width=3, font=("Arial", 38),
                    bg="#f2f2f2", bd=0, highlightthickness=0,
                    buttonbackground="#f2f2f2", justify="center", wrap=True,
                    format="%02.0f")# The actual scrollable number box button for add and minus the time.
    sb.pack()#Show the spinbox inside its frame. #-- separator line. --#
    tk.Label(f, text="", font=("Arial", 20), bg="#f2f2f2").pack() if max_val==23 or max_val==59 else None
    return sb

