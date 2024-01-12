import tkinter as tk
from tkinter import ttk
from random import choice
import cv2
from PIL import Image, ImageTk


#window
root = tk.Tk()
root.maxsize(900, 600)
root.title('Tkinter Hub')

options_frame = tk.Frame(root, bg='#c3c3c3')

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=200, height=900)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=900, width=600)

#Buttons
    #Home
home_btn = tk.Button(options_frame, text='Detect', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(home_indicate, home_page))
home_btn.place(x=10,y=50)
home_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
home_indicate.place(x=3, y=50, width=5, height=40)
    #History
history_btn = tk.Button(options_frame, text='History', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3' , command=lambda: indicate(history_indicate, history_page))
history_btn.place(x=10,y=100)
history_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
history_indicate.place(x=3, y=100, width=5, height=40)
    #MSG
msg_btn = tk.Button(options_frame, text='Send a Message', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(msg_indicate, msg_page))
msg_btn.place(x=10,y=150)
msg_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
msg_indicate.place(x=3, y=150, width=5, height=40)

#Home Button
def home_page():
    home_frame = tk.Frame(main_frame)
    home_frame.pack()

    label = tk.Label(home_frame, width=500, height=500)
    label.pack()

    cap = cv2.VideoCapture(0)
    def update_frame():
        ret, home_frame = cap.read()
        if ret:
            home_frame = cv2.resize(home_frame, (500, 500)) # resize the frame to 200x200
            img = cv2.cvtColor(home_frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            label.imgtk = imgtk
            label.configure(image=imgtk)
        root.after(10, update_frame)
    update_frame()
#History Button
#History Button
def history_page():
    # Create a new pop-up window
    history_popup = tk.Toplevel(root)
    history_popup.title("History")

    first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
    last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

    # treeview 
    table = ttk.Treeview(history_popup, columns=('first', 'last', 'email'), show='headings')
    table.heading('first', text='Crack Image')
    table.heading('last', text='Date Captured')
    table.heading('email', text='File Location')
    table.pack(fill='both', expand=True)

    # insert values into a table
    for i in range(100):
        first = choice(first_names)
        last = choice(last_names)
        email = f'{first[0]}{last}@email.com'
        data = (first, last, email)
        table.insert(parent='', index=0, values=data)

    table.insert(parent='', index=tk.END, values=('XXXXX', 'YYYYY', 'ZZZZZ'))

    # events
    def item_select(_):
        print(table.selection())
        for i in table.selection():
            print(table.item(i)['values'])
        # table.item(table.selection())

    def delete_items(_):
        print('delete')
        for i in table.selection():
            table.delete(i)

    table.bind('<<TreeviewSelect>>', item_select)
    table.bind('<Delete>', delete_items)


#MSG Button
# Define hide_indicators function first
def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    history_indicate.config(bg='#c3c3c3')
    msg_indicate.config(bg='#c3c3c3')


# Define delete_page function next
def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()

# Define indicate function after delete_page
def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_page()
    page()


def msg_page():
    def send_message():
        # Get the message from the entry field
        message_content = message_entry.get()

        # Your SMTP configurations
        smtp_server = 'smtp.gmail.com'
        smtp_port = 465
        sender_email = 'your_email@gmail.com'  # Replace with your sender email
        receiver_email = 'recipient_email@gmail.com'  # Replace with the recipient email

        # Get the password securely (you might want to improve the password handling)
        password = input("Type your password and press enter: ")

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Create the email message
        email_message = f"""\
        Subject: Test Email
        {message_content}"""

        try:
            # Send the email
            with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as smtp:
                smtp.login(sender_email, password)
                smtp.sendmail(sender_email, receiver_email, email_message)

            # Update the label to show the "message is sent" confirmation
            sent_label.config(text="Message is sent!")
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")

    msg_frame = tk.Frame(main_frame)

    lb = tk.Label(msg_frame, text='Send a Message.', font=('Bold', 30))
    lb.pack()

    # Adding a text field (Entry widget) for message input
    message_entry = tk.Entry(msg_frame, width=40)
    message_entry.pack(pady=10)

    # Adding a button to send the message
    send_button = tk.Button(msg_frame, text='Send', command=send_message)
    send_button.pack(pady=10)

    # Adding a label to display the "message is sent" confirmation
    sent_label = tk.Label(msg_frame, text='', fg='green')
    sent_label.pack(pady=10)

    msg_frame.pack(pady=20)


root.mainloop()