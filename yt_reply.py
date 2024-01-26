import os
import json
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import tkinter as tk
from tkinter import ttk

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Others\Experiments\Tkinter designer\Out\Main\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Your YouTube API key
API_KEY = "AIzaSyCKdZA_JhVm_lElLxbUtRp9g3UM5DujadM"

# Function to authenticate with YouTube API
def authenticate():
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        "client_secret.json", scopes
    )

    credentials = None

    if os.path.exists("token.json"):
        with open("token.json", "r") as json_file:
            try:
                data_str = json_file.read()  # Read the string from the file
                data = json.loads(data_str)  # Convert the string to a dictionary
                if isinstance(data, dict):
                    credentials = google.oauth2.credentials.Credentials.from_authorized_user_info(data)
                else:
                    raise ValueError("The loaded data is not a dictionary.")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
            except ValueError as ve:
                print(f"Error: {ve}")

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow.redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
            auth_url, _ = flow.authorization_url(prompt="consent")
            print("Please go to this URL: {}".format(auth_url))
            code = input("Enter the authorization code: ")
            flow.fetch_token(code=code)
            credentials = flow.credentials

        with open("token.json", "w") as token_file:
            json.dump(credentials.to_json(), token_file)

    return build("youtube", "v3", credentials=credentials, developerKey=API_KEY)

# Rest of your code remains unchanged...



# Function to reply to comments containing specified string
def extract_video_id(video_url):
    parsed_url = urlparse(video_url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get("v", [None])[0]

# Function to reply to comments containing specified string
def reply_to_comments(api_service, video_url, search_string, reply_text):
    video_id = extract_video_id(video_url)

    if not video_id:
        print("Invalid YouTube video URL.")
        return

    try:
        request = api_service.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            maxResults=100,
        )

        response = request.execute()

        for item in response.get("items", []):
            comment_text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            if search_string.lower() in comment_text.lower():
                comment_id = item["id"]
                reply_comment(api_service, comment_id, reply_text)
    except Exception as e:
        print(f"Error while replying to comments: {e}")

# Function to reply to a specific comment
def reply_comment(api_service, parent_id, reply_text):
    request = api_service.comments().insert(
        part="snippet",
        body={
            "snippet": {
                "parentId": parent_id,
                "textOriginal": reply_text,
            }
        },
    )

    request.execute()

# GUI setup
import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("YouTube Comment Bot")

    label = tk.Label(window, text="Enter the video URL:")
    label.pack()

    video_id_entry = tk.Entry(window)
    video_id_entry.pack()

    search_string_label = tk.Label(window, text="Enter the search string:")
    search_string_label.pack()

    search_string_entry = tk.Entry(window)
    search_string_entry.pack()

    reply_text_label = tk.Label(window, text="Enter the reply text:")
    reply_text_label.pack()

    reply_text_entry = tk.Entry(window)
    reply_text_entry.pack()

    def handle_button_click():
        video_id = video_id_entry.get()
        search_string = search_string_entry.get()
        reply_text = reply_text_entry.get()

        # Call your function here
        # reply_to_comments(api_service, video_id, search_string, reply_text)

    button = tk.Button(window, text="Reply to comments", command=handle_button_click)
    button.pack()

    window.mainloop()

create_window()
