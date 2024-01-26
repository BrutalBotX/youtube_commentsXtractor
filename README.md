# youtube_commentsXtractor

As suggested by the name, all it does it extract comments when a Youtube URL and a account name is provided.
## Requirements

We'll first need a youtube data api to access it's contents.
So let's go to Google Cloud Console and login/signup there.

Then follow these screenshots to get your API key:

1. First make a new project and make sure you are in it.
![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%202023-12-12%20115105.png?raw=true)

2. Go to Youtube data API.
![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%202023-12-12%20120033.png?raw=true)

3. Enable it.
![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%202023-12-12%20120213.png?raw=true)

4. Click the Create 'Credentials button'.
![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%202023-12-12%20120306.png?raw=true)

5. Click 'Public data' and then click 'next'.
![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%202023-12-12%20120337.png?raw=true)

6. Copy your API key and then come out of there.
![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%202023-12-12%20120422.png?raw=true)

7. Paste your API key in the python code you're trying to run (There'll be a comment beside it, to make it easy to find)

8. (For yt_cmall_ui.py) Make sure you put in the location of the frame0 folder you download from here, in the python file, it should also be commented for easy access

Now, that's that, we'll now continue to get credentials for the auto replier (Skip, if you're not thinking of using it):

1. Select your project from the drop down menu above, then select Consent section from the side menu.
![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%20(7).png?raw=true)

2. Click Create credentials.
![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%20(8).png?raw=true)

3. Click OAuth client ID.
![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%20(9).png?raw=true)

4. Choose Desktop App.
![](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%20(10).png?raw=true)

5. Choose a name for it and click create.
![](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%20(11).png?raw=true)

6. Click save and download the json file.
![](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%20(12).png?raw=true)

7. Rename the json file to client_secret.json and place it in the same directory as the python files.

8. Also, place the main and rep folder in the same directory if using the version 2 and auto replier.
## Deployment

I've provided both CLI and GUI versions, so you run try any of them.

For CLI, make sure that google-api-python-client and urllib is installed. If not run this:
```bash
  pip install google-api-python-client

```

For GUI version, tkinker is required, it's in the optional feature list when installing python, so make sure you checked that box.

All of these steps are best done in a virtual environment to keep things clean.


## Usage/Examples

Make sure you are in the virtual environment (if using)
```javascript
<dir_name>/bin/activate
```

#CLI
```javascript
python yt_comments.py
```

#GUI
```javascript
python yt_comments_ui.py
```
#GUI (All comments version)
```javascript
python yt_cmall_ui.py
```
#GUI (All comments version 2)
```javascript
python yt_cmall_ui2.py
```
#Auto Replier
```javascript
python yt_reply.py
```
Or through GUI V2

$ While using the Auto replier, it will ask for user login, open the link provided in the terminal and log in the same account with which you created the json file, give your consent and copy the code and paste it into the terminal.
## Screenshots

Youtube comments section:
![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%202023-12-12%20124923.png?raw=true)

CLI: 
![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%202023-12-12%20124606.png?raw=true)

GUI:
![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%202023-12-12%20124724.png?raw=true)

GUI(All comments version):
![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%202024-01-12%20201425.png?raw=true)

GUI(All comments version 2):
![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Capture2.PNG?raw=true)

GUI(Auto Replier):
![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Capture.PNG?raw=true)
Exported CSV file:

![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Screenshot%202024-01-12%20201445.png?raw=true)

## Flowchart

![App Screenshot](https://github.com/BrutalBotX/youtube_commentsXtractor/blob/main/Screenshot/Untitled%20Diagram.drawio.png?raw=true)
