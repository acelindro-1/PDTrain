# detect.py

import customtkinter
import tkinter as tk

class DetectPage(customtkinter.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # Set the size of the detect page
        self.master.geometry("800x480")

        # First Frame: Camera Display
        self.frame_camera = customtkinter.CTkFrame(self, width=600, height=400)
        self.frame_camera.grid(row=0, column=0, padx=10, pady=10)

        self.label_camera = tk.Label(self.frame_camera, text="Camera Display", font=('Bold', 15))
        self.label_camera.grid(row=0, column=0, padx=10, pady=10)

        # Placeholder for camera display - you need to replace this with actual camera code
        # For simplicity, I'm just using a label as a placeholder
        self.camera_display = tk.Label(self.frame_camera, text="Camera Placeholder")
        self.camera_display.grid(row=1, column=0, padx=10, pady=10)

        # Second Frame: Buttons
        self.frame_buttons = customtkinter.CTkFrame(self)
        self.frame_buttons.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.button_home = customtkinter.CTkButton(self.frame_buttons, text="Home", command=self.button_home_click)
        self.button_home.grid(row=0, column=0, padx=10, pady=10)

        self.button_start = customtkinter.CTkButton(self.frame_buttons, text="Start", command=self.button_start_click)
        self.button_start.grid(row=1, column=0, padx=10, pady=10)

        # Adjust row and column weights to control the layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def button_home_click(self):
        print("Home button clicked")

        # Hide DetectPage and show other pages
        self.grid_forget()

    def button_start_click(self):
        print("Start button clicked")

# Example of using DetectPage
if __name__ == "__main__":
    root = customtkinter.CTk()
    root.title("Detection Page")  # Set the title for the entire application
    root.geometry("800x480")  # Set the main window size
