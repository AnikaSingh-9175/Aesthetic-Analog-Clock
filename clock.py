import tkinter as tk
import time
import math

class BuiltInAestheticClock(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Aesthetic Clock")
        self.geometry("450x550")
        self.resizable(False, False)
        self.configure(bg="#121212")
        
        self.accent_color = "#FF3B30"
        self.text_main = "#FFFFFF"
        self.text_muted = "#555555"
        self.card_bg = "#1A1A1A"
        
        self.create_widgets()
        self.update_clock()

    def create_widgets(self):
        self.card = tk.Frame(self, bg=self.card_bg, bd=0, highlightthickness=0)
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=390, height=490)
        
        self.canvas = tk.Canvas(
            self.card, 
            bg=self.card_bg, 
            highlightthickness=0, 
            bd=0
        )
        self.canvas.pack(fill="both", expand=True, padx=20, pady=(30, 0))
        
        self.digital_time = tk.Label(
            self.card, 
            text="00:00", 
            font=("Helvetica Neue", 44, "bold"), 
            bg=self.card_bg,
            fg=self.text_main
        )
        self.digital_time.pack(pady=(10, 0))
        
        self.digital_date = tk.Label(
            self.card, 
            text="MON, JAN 01", 
            font=("Helvetica Neue", 11, "bold"), 
            bg=self.card_bg,
            fg=self.accent_color
        )
        self.digital_date.pack(pady=(0, 35))

    def update_clock(self):
        self.canvas.delete("all")
        
        current_time = time.localtime()
        hrs = current_time.tm_hour
        mins = current_time.tm_min
        secs = current_time.tm_sec
        
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        cx = width / 2 if width > 1 else 175 
        cy = height / 2 if height > 1 else 150
        radius = min(cx, cy) - 25
        
        self.canvas.create_oval(
            cx - radius, cy - radius,
            cx + radius, cy + radius,
            outline=self.text_muted, width=2
        )
        
        for i in range(12):
            angle = i * (360 / 12) * (math.pi / 180)
            
            num_x = cx + (radius - 20) * math.sin(angle)
            num_y = cy - (radius - 20) * math.cos(angle)
            
            display_num = 12 if i == 0 else i
            num_color = self.accent_color if display_num in [12, 3, 6, 9] else self.text_main
            
            self.canvas.create_text(
                num_x, num_y,
                text=str(display_num),
                font=("Helvetica Neue", 12, "bold"),
                fill=num_color
            )
            
        sec_angle = secs * (360 / 60) * (math.pi / 180)
        min_angle = (mins + secs / 60) * (360 / 60) * (math.pi / 180)
        hr_angle = (hrs % 12 + mins / 60) * (360 / 12) * (math.pi / 180)
        
        hr_len = radius * 0.45
        min_len = radius * 0.65
        sec_len = radius * 0.75
        
        hx, hy = cx + hr_len * math.sin(hr_angle), cy - hr_len * math.cos(hr_angle)
        self.canvas.create_line(cx, cy, hx, hy, fill=self.text_main, width=5, capstyle="round")
        
        mx, my = cx + min_len * math.sin(min_angle), cy - min_len * math.cos(min_angle)
        self.canvas.create_line(cx, cy, mx, my, fill=self.text_main, width=3, capstyle="round")
        
        sx, sy = cx + sec_len * math.sin(sec_angle), cy - sec_len * math.cos(sec_angle)
        sx_back, sy_back = cx - 15 * math.sin(sec_angle), cy + 15 * math.cos(sec_angle)
        self.canvas.create_line(sx_back, sy_back, sx, sy, fill=self.accent_color, width=1.5)
        
        self.canvas.create_oval(cx - 4, cy - 4, cx + 4, cy + 4, fill=self.card_bg, outline=self.accent_color, width=2)

        str_time = time.strftime("%H:%M")
        raw_date = time.strftime("%a, %b %d").upper()
        spaced_date = " ".join(list(raw_date))
        
        self.digital_time.configure(text=str_time)
        self.digital_date.configure(text=spaced_date)
        
        self.after(100, self.update_clock)

if __name__ == "__main__":
    app = BuiltInAestheticClock()
    app.mainloop()
