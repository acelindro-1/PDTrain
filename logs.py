# logs.py

import customtkinter
import tkinter as tk
from tkinter import ttk, messagebox

from email_module import CreateEmailPage

class LogsPage(customtkinter.CTkFrame):
    def __init__(self, master=None, button_font=None, page1_class=None, **kwargs):
        super().__init__(master, **kwargs)

        if button_font is None:
            button_font = customtkinter.CTkFont(weight="bold", size=20)

        self.frame_logs = customtkinter.CTkFrame(self, width=600, height=400)
        self.frame_logs.pack(padx=10, pady=10, fill='both', expand=True)

        self.label_logs = tk.Label(self.frame_logs, text="Logs Display", font=('Bold', 15))
        self.label_logs.pack(padx=10, pady=10)

        self.tree = ttk.Treeview(self.frame_logs, columns=("FileName", "DateTaken", "Location", "Etc"), show="headings", height=10)
        self.tree.heading("FileName", text="File Name")
        self.tree.heading("DateTaken", text="Date Taken")
        self.tree.heading("Location", text="Location")
        self.tree.heading("Etc", text="Etc")
        self.tree.pack(padx=10, pady=10, fill='both', expand=True)

        self.button_home = customtkinter.CTkButton(self, text="Home", font=button_font, command=self.button_home_click)
        self.button_home.pack(side="bottom", anchor="e", ipady=12, padx=10, pady=20)
        
        self.button_create_email = customtkinter.CTkButton(self, text="Create Email", font=button_font, command=self.create_email_click)
        self.button_create_email.pack(side="bottom", anchor="e", ipady=12, padx=10, pady=20)

        # Create an instance of CreateEmailPage but don't pack it initially
        self.create_email_page = CreateEmailPage(self.master, back_callback=self.back_to_logs_page)
        self.create_email_page.pack_forget()  # Initially hide the CreateEmailPage

    def button_home_click(self):
        print("Home button clicked")
        self.frame_logs.pack_forget()

        from page1 import Page1
        page1 = Page1(self.master)
        page1.pack(expand=True, fill='both')

    def create_email_click(self):
        print("Create Email button clicked")

        # Hide all widgets from the logs page using pack_forget
        for widget in self.frame_logs.winfo_children():
            widget.pack_forget()

        # Show the CreateEmailPage using pack
        self.create_email_page.pack(expand=True, fill='both')

    def back_to_logs_page(self):
        # Set create_email_active to False
        self.create_email_page.pack_forget()

        # Show the widgets in frame_logs only if CreateEmailPage is not active
        for widget in self.frame_logs.winfo_children():
            widget.pack(expand=True, fill='both')

# Sample usage
if __name__ == "__main__":
    root = customtkinter.CTk()
    root.title("Logs Page")
    logs_page = LogsPage(root)
    root.mainloop()
