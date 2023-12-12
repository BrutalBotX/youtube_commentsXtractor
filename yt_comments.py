# Import the required library
from googleapiclient.discovery import build

# Define a function to get comments from a specific video
def get_comments(youtube, video_id, username, comments=[], token=''):
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
        return get_comments(youtube, video_id, username, comments, video_response['nextPageToken'])
    else:
        return comments

# add your api key here
api_key = ''

# Get the video ID and username from the user
video_id = input('Enter the video ID: ')
username = input('Enter the username: ')

# Build the YouTube service
youtube = build('youtube', 'v3', developerKey=api_key)

# Call the get_comments function and print the comments
comments = get_comments(youtube, video_id, username)
print(comments)
