import tkinter as tk
from tkinter import messagebox, scrolledtext

from controller import connect_youtube, read_latest_comments

youtube = None
channel_id = None


# -----------------------------
# Connect YouTube
# -----------------------------
def connect():

    global youtube
    global channel_id

    result = connect_youtube()

    if result["success"]:

        youtube = result["youtube"]
        channel_id = result["channel_id"]

        status.config(text="✅ Connected")
        channel.config(text=f"Channel : {result['channel_name']}")

        messagebox.showinfo(
            "Success",
            "YouTube Connected Successfully!"
        )

    else:

        messagebox.showerror(
            "Error",
            result["error"]
        )


# -----------------------------
# Read Real Comments
# -----------------------------
def read_comments():

    if youtube is None:

        messagebox.showwarning(
            "Warning",
            "Please connect YouTube first."
        )

        return

    result = read_latest_comments(
        youtube,
        channel_id
    )

    if not result["success"]:

        messagebox.showerror(
            "Error",
            result["error"]
        )

        return

    comments_box.delete("1.0", tk.END)

    for comment in result["comments"]:

        comments_box.insert(
            tk.END,
            f"👤 {comment['author']}\n"
        )

        comments_box.insert(
            tk.END,
            f"💬 {comment['text']}\n"
        )

        comments_box.insert(
            tk.END,
            "-" * 60 + "\n\n"
        )


# -----------------------------
# Generate Reply
# -----------------------------
def generate_reply():

    messagebox.showinfo(
        "AI",
        "Next Step 😊"
    )


# -----------------------------
# Main Window
# -----------------------------
window = tk.Tk()

window.title("YouTube AI Agent")
window.geometry("750x650")
window.resizable(False, False)

title = tk.Label(
    window,
    text="YouTube AI Agent",
    font=("Arial", 24, "bold")
)

title.pack(pady=20)

status = tk.Label(
    window,
    text="Status : Not Connected",
    font=("Arial", 12)
)

status.pack()

channel = tk.Label(
    window,
    text="Channel : ---",
    font=("Arial", 12)
)

channel.pack(pady=10)

btn1 = tk.Button(
    window,
    text="Connect YouTube",
    width=25,
    height=2,
    command=connect
)

btn1.pack(pady=5)

btn2 = tk.Button(
    window,
    text="Read Comments",
    width=25,
    height=2,
    command=read_comments
)

btn2.pack(pady=5)

btn3 = tk.Button(
    window,
    text="Generate AI Reply",
    width=25,
    height=2,
    command=generate_reply
)

btn3.pack(pady=5)

btn4 = tk.Button(
    window,
    text="Exit",
    width=25,
    height=2,
    command=window.destroy
)

btn4.pack(pady=10)

comments_box = scrolledtext.ScrolledText(
    window,
    width=80,
    height=15,
    font=("Arial", 10)
)

comments_box.pack(pady=15)

window.mainloop()