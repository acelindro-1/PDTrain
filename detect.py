# detect.py
import customtkinter
import tkinter as tk
import cv2
from PIL import Image, ImageTk

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

        # Placeholder for camera display
        self.camera_display_label = tk.Label(self.frame_camera)
        self.camera_display_label.grid(row=1, column=0, padx=10, pady=10)

        # Second Frame: Buttons
        self.frame_buttons = customtkinter.CTkFrame(self)
        self.frame_buttons.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Buttons in detect.py
        button_font = customtkinter.CTkFont(weight="bold", size=20)

        self.button_home = customtkinter.CTkButton(self.frame_buttons, text="Home", font=button_font, command=self.button_home_click)
        self.button_home.grid(row=2, column=0, padx=10, pady=30, sticky="nsew", ipady=12)

        self.button_start_stop_var = tk.StringVar()  # Variable to track the state of the button
        self.button_start_stop_var.set("Start")  # Initial state is "Start"
        self.button_start = customtkinter.CTkButton(self.frame_buttons, textvariable=self.button_start_stop_var, font=button_font, command=self.button_start_click)
        self.button_start.grid(row=3, column=0, padx=10, pady=30, sticky="nsew", ipady=12)

        # Adjust row and column weights to center the buttons
        self.frame_buttons.grid_rowconfigure(0, weight=1)
        self.frame_buttons.grid_rowconfigure(1, weight=1)
        self.frame_buttons.grid_rowconfigure(2, weight=1)
        self.frame_buttons.grid_rowconfigure(3, weight=1)
        self.frame_buttons.grid_columnconfigure(0, weight=1)

        # Initialize the camera (but don't start capturing frames yet)
        self.cap = cv2.VideoCapture(0)  # Use 0 for the default camera, adjust accordingly
        self.is_camera_running = False

    def button_home_click(self):
        print("Home button clicked")

        # Release the camera when going back to the main page
        self.release_camera()

        # Hide DetectPage and show other pages
        self.grid_forget()

    def button_start_click(self):
        if not self.is_camera_running:
            # Start capturing frames when the "Start" button is clicked
            self.is_camera_running = True
            self.start_camera()
            self.button_start_stop_var.set("Stop")  # Change button text to "Stop"
        else:
            # Stop capturing frames when the "Stop" button is clicked
            self.is_camera_running = False
            self.button_start_stop_var.set("Start")  # Change button text to "Start"

    def start_camera(self):
        # Call the update method to start capturing frames
        self.update()

    def release_camera(self):
        # Release the camera when leaving the DetectPage
        self.is_camera_running = False  # Stop the camera loop
        self.after_cancel(self.update)  # Cancel any scheduled updates
        self.cap.release()  # Release the camera

    def update(self):
        if self.is_camera_running:
            # Read a frame from the camera
            ret, frame = self.cap.read()

            if ret:
                # Convert the frame from BGR to RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Convert the frame to a PhotoImage
                img = ImageTk.PhotoImage(Image.fromarray(rgb_frame))

                # Update the label with the new image
                self.camera_display_label.config(image=img)
                self.camera_display_label.image = img

                # Call the update method again after a delay (e.g., 33 milliseconds for ~30 fps)
                self.after(33, self.update)
