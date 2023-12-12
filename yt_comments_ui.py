import tkinter as tk
from googleapiclient.discovery import build
import urllib.parse as urlparse
import html

def get_comments():
    # Get the video URL and username from the user
    video_url = video_url_entry.get()
    username = username_entry.get()

    # Extract the video ID from the URL
    url_data = urlparse.urlparse(video_url)
    query = urlparse.parse_qs(url_data.query)
    video_id = query["v"][0]

    # Call the get_comments function and print the comments
    comments = get_comments_from_api(youtube, video_id, username)
    for comment in comments:
        comments_text.insert(tk.END, html.unescape(comment) + '\n')

def get_comments_from_api(youtube, video_id, username, comments=[], token=''):
    # Make a request to the YouTube API to get the comment threads of the video
    video_response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        pageToken=token
    ).execute()

    # Iterate over each comment thread
    for item in video_response['items']:
        # Get the comment and the author's display name
        comment = item['snippet']['topLevelComment']['snippet']
        # If the author's display name matches the specified username, add the comment to the list
        if comment['authorDisplayName'] == username:
            comments.append(comment['textDisplay'])

    # If there are more comments, make a recursive call to get the next page of comments
    if 'nextPageToken' in video_response:
        return get_comments_from_api(youtube, video_id, username, comments, video_response['nextPageToken'])
    else:
        return comments

# Hard-code the API key
api_key = 'AIzaSyCKdZA_JhVm_lElLxbUtRp9g3UM5DujadM'

# Build the YouTube service
youtube = build('youtube', 'v3', developerKey=api_key)

# Create the main window
root = tk.Tk()

# Create the labels and entry fields for the video URL and username
video_url_label = tk.Label(root, text='Enter the video URL:')
video_url_label.pack()
video_url_entry = tk.Entry(root, width=50)
video_url_entry.pack()
username_label = tk.Label(root, text='Enter the username:')
username_label.pack()
username_entry = tk.Entry(root, width=50)
username_entry.pack()

# Create the text box for the comments
comments_text = tk.Text(root)
comments_text.pack()

# Create the button to get the comments
get_comments_button = tk.Button(root, text='Get Comments', command=get_comments)
get_comments_button.pack()

# Start the main loop
root.mainloop()
