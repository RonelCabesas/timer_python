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
#create a value inside the box wheel
h_box = make_wheel(23)
m_box = make_wheel(59)
s_box = make_wheel(59)

#assign defult time
h_box.delete(0, "end")
h_box.insert(0, "00")   # default hours
m_box.delete(0, "end")
m_box.insert(0, "00")   # default minutes (hal. 00:01:00)
s_box.delete(0, "end") #delete inside in second box
s_box.insert(0,"01") # default 00:00:01

display = tk.Label(root, text="00:00:01", font=("Arial", 55, "bold"), bg="#f2f2f2") # the output when i click start

is_running = False #if false the button is start, but when it s true the button is stop
timer_thread = None # the one who count the ramaining time
stop_timer = False #second button, if false the countdown will continue, if true the countdown stop

def update_display(t):
    hh = t // 3600
    mm = (t % 3600) // 60
    ss = t % 60
    display.config(text=f"{hh:02d}:{mm:02d}:{ss:02d}") #display the upgraded label on screen
def countdown(total): #total second like 70 second, it will be 1minutes and 10 second
    global is_running, stop_timer, stop_alarm 
    t = total # the total time will be minus 1 second for the countdown
    while t >= 0:#loop , while there's a time
        if stop_timer:#when you click stop and it will become true, the loop exit and the countdown will cancelled
            return 
        root.after(0, update_display, t) #update the display if there's a time left 
        if t == 0:#if false you will go the time.sleep, then you can still click the stop button
            break #if true, break no need to go in time.sleep
        time.sleep(1)#continue to countdown the time left
        t -= 1
    #if we don't click the stop button and the countdown ends 
    if not stop_timer:
        root.after(0, lambda: display.config(text="TIME'S UP!"))
        ring()
def start_stop():
    global is_running, stop_timer, stop_alarm, timer_thread #used the switches outside

    if not is_running:
        # --- START ---
        #check if the timer is not yet running
        #read the 3 wheels, If reading fails → exit, don't start.
        try:
            H = int(h_box.get())
            M = int(m_box.get())
            S = int(s_box.get())
        except:
            return
        #Converts HH:MM:SS to total seconds → If total is 0 → exit, don't start.
        total = H*3600 + M*60 + S
        if total <= 0:
            return
    is_running = True #the code knows that the button is now on stop mood
        stop_timer = False #continue to countdown
        stop_alarm = False #the alarm is ready but not functioning

        picker.pack_forget() # hide the 3wheel
        display.pack(pady=80) # show the countdown label

        btn.config(text="■ STOP") #switch the button from start to stop
        # countdown is the only work then submit the total second for the countdown
        timer_thread = threading.Thread(target=countdown, args=(total,), daemon=True)
        timer_thread.start() # the timer will start to countdown
