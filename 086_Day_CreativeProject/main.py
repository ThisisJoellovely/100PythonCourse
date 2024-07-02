import tkinter as tk
from tkinter import messagebox
import time

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        
        self.sample_text = "The quick brown fox jumps over the lazy dog"
        self.start_time = None

        self.create_widgets()
        
    def create_widgets(self):
        # Sample text display
        self.text_label = tk.Label(self.root, text=self.sample_text, wraplength=300)
        self.text_label.pack(pady=10)

        # Typing entry box
        self.typing_entry = tk.Text(self.root, height=5, width=50)
        self.typing_entry.pack(pady=10)
        self.typing_entry.bind("<FocusIn>", self.start_timer)

        # Button to submit and calculate WPM
        self.submit_button = tk.Button(self.root, text="Submit", command=self.calculate_wpm)
        self.submit_button.pack(pady=10)

    def start_timer(self, event):
        self.start_time = time.time()

    def calculate_wpm(self):
        if self.start_time is None:
            messagebox.showerror("Error", "Please start typing to begin the test.")
            return
        
        end_time = time.time()
        typed_text = self.typing_entry.get("1.0", tk.END).strip()
        time_taken = end_time - self.start_time

        if not typed_text:
            messagebox.showerror("Error", "Please enter the text to calculate your typing speed.")
            return
        
        word_count = len(typed_text.split())
        wpm = word_count / (time_taken / 60)

        messagebox.showinfo("Typing Speed", f"Your typing speed is {wpm:.2f} words per minute.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
