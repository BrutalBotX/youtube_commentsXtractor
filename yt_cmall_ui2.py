import tkinter as tk
from tkinter import Canvas, Entry, Button, PhotoImage, messagebox
from googleapiclient.discovery import build
import os
import csv
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Others\Experiments\yt\main\build\assets\frame0") #Enter the path to the frame0 folder here 

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

API_KEY = 'AIzaSyCKdZA_JhVm_lElLxbUtRp9g3UM5DujadM'  # Replace with your YouTube API key
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_comments():
    video_url = entry_1.get()

    if not video_url:
        return

    video_id = video_url.split("v=")[1]

    youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)

    try:
        comments = get_all_comments(youtube, video_id)

        # Display comments in the textbox
        comments_textbox.delete("1.0", "end")
        for comment in comments:
            comments_textbox.insert("end", comment + "\n\n")

        save_to_csv(comments)

    except Exception as e:
        messagebox.showerror("Error", f"Error retrieving or saving comments:\n{e}")

def get_all_comments(youtube, video_id, comments=None, next_page_token=None):
    if comments is None:
        comments = []

    while True:
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            pageToken=next_page_token
        )

        response = request.execute()

        for item in response['items']:
            commenter_name = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(f"{commenter_name}: {comment_text}")

        next_page_token = response.get('nextPageToken')

        if not next_page_token:
            break

    return comments

def save_to_csv(comments):
    if not comments:
        return

    file_path = os.path.join(os.getcwd(), 'comments.csv')

    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Comments'])
        for comment in comments:
            csv_writer.writerow([comment])

    messagebox.showinfo("Success", f"Comments saved to:\n{file_path}")


def open_replier_py():
    os.system("python yt_reply_ui.py")

# UI
window = tk.Tk()
window.geometry("700x500")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=450,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    21.0,
    204.0,
    218.0,
    301.0,
    fill="#FFFFFF",
    outline=""
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    431.0,
    271.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    350.0,
    46.0,
    image=image_image_2
)

canvas.create_text(
    79.0,
    20.0,
    anchor="nw",
    text="Youtube_commentsXtractor\n\n",
    fill="#FFFFFF",
    font=("Inter", 40 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    344.0,
    169.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#c2b9b9",
    fg="#000716",
    highlightthickness=0
)

entry_1.place(
    x=60.0,
    y=139.0,
    width=568.0,
    height=58.0
)

canvas.create_text(
    54.0,
    110.0,
    anchor="nw",
    text="URL",
    fill="#000000",
    font=("KoHo Regular", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=get_comments,
    relief="flat"
)
button_1.place(
    x=44.0,
    y=223.0,
    width=150.0,
    height=60.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_replier_py(),
    relief="flat"
)
button_2.place(
    x=44.0,
    y=307.0,
    width=150.0,
    height=60.0
)

# Textbox
comments_textbox = tk.Text(window, height=2, width=75)
comments_textbox.place(x=44.0, y=450)
comments_textbox.configure(bg="#FFFFFF", fg="#000716", font=("KoHo Regular", 14 * -1))

window.resizable(False, False)
window.mainloop()
