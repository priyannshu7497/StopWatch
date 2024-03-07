import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        
        self.time_label = tk.Label(master, text="", font=("Helvetica", 48))
        self.time_label.pack(pady=20)
        
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer, state="disabled")
        self.stop_button.pack(pady=10)
        
        self.timer_running = False
        self.remaining_time = 0
        
    def start_timer(self):
        self.timer_running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        
        self.remaining_time = 60  # Set the initial duration here (in seconds)
        
        self.update_timer()
    
    def update_timer(self):
        if self.timer_running:
            mins, secs = divmod(self.remaining_time, 60)
            timer_text = '{:02d}:{:02d}'.format(mins, secs)
            self.time_label.config(text=timer_text)
            
            if self.remaining_time <= 0:
                messagebox.showinfo("Time's Up!", "The countdown timer has ended!")
                self.timer_running = False
                self.start_button.config(state="normal")
                self.stop_button.config(state="disabled")
            else:
                self.remaining_time -= 1
                self.master.after(1000, self.update_timer)
    
    def stop_timer(self):
        self.timer_running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

def main():
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
