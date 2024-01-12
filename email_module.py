import customtkinter
import tkinter as tk
from tkinter import messagebox

class CreateEmailPage(customtkinter.CTkFrame):
    def __init__(self, master=None, button_font=None, back_callback=None, **kwargs):
        super().__init__(master, **kwargs)

        if button_font is None:
            button_font = customtkinter.CTkFont(weight="bold", size=20)

        self.label_email = tk.Label(self, text="Email Page", font=('Bold', 15))
        self.label_email.pack(padx=10, pady=10)

        self.button_send_email = customtkinter.CTkButton(self, text="Send Email", font=button_font, command=self.send_email_click)
        self.button_send_email.pack(padx=10, pady=20, ipady=12)

        self.back_callback = back_callback

        self.button_back = customtkinter.CTkButton(self, text="Back", font=button_font, command=self.back_to_logs_page)
        self.button_back.pack(padx=10, pady=20, ipady=12)

    def send_email_click(self):
        print("Send Email button clicked")
        # Implement your email sending logic here
        # You can use smtplib, as shown in the previous examples
        # For example, show a message box indicating the email has been sent
        messagebox.showinfo("Email Sent", "Email has been sent successfully!")

        # Open a new pop-up window
        self.open_popup_window()

    def back_to_logs_page(self):
        # Call the callback function to go back to the LogsPage
        if self.back_callback:
            self.back_callback()

    def open_popup_window(self):
        # Create a new Toplevel window
        popup_window = tk.Toplevel(self.master)
        popup_window.title("Crack Detected")

        # Set the main window dimensions
        popup_window.geometry("800x480")

        # Display the message
        message_label = tk.Label(popup_window, text="This is an automated message: A crack has been detected in $logs. Please consider looking into it.")
        message_label.pack(padx=10, pady=10)

# Sample usage
if __name__ == "__main__":
    root = customtkinter.CTk()
    root.title("Email Page")
    email_page = CreateEmailPage(root)
    root.mainloop()
