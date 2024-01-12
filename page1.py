# page1.py

import customtkinter
import tkinter as tk
from detect import DetectPage  # Import DetectPage from detect.py

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk, tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the background color to white
        self.configure(bg='white')

        # Window
        self.title("Crack Detection App")
        self.geometry("800x480")

        # Frame1
        self.frame1 = customtkinter.CTkFrame(self)
        self.frame1.pack(expand=True, fill='both')

        # Buttons in Frame1
        self.button1 = customtkinter.CTkButton(self.frame1, text="DETECT", font=customtkinter.CTkFont(weight="bold", size=20), command=self.detect_button_clicked)
        self.button1.pack(side="top", ipadx=10, ipady=12, padx=10, pady=8)
        self.button2 = customtkinter.CTkButton(self.frame1, font=customtkinter.CTkFont(weight="bold", size=20), text="LOGS", command=self.logs_button_clicked)
        self.button2.pack(side="top", ipadx=10, ipady=12, padx=10, pady=8)

        # Create DetectPage instance but don't pack it initially
        self.detect_page = DetectPage(self)
        # Attach the method for going back to page1
        self.detect_page.button_home.configure(command=self.back_to_page1)

    def detect_button_clicked(self):
        print("Detect pressed")
        # Forget the frame1 widgets
        self.frame1.pack_forget()
        # Pack widgets in DetectPage
        self.detect_page.pack(expand=True, fill='both')

    def logs_button_clicked(self):
        print("Logs pressed")

    def back_to_page1(self):
        # Forget the DetectPage widgets
        self.detect_page.pack_forget()
        # Pack widgets in frame1
        self.frame1.pack(expand=True, fill='both')

app = App()
app.mainloop()
