from config import MAX_COMMENTS
import os
import pickle

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

CLIENT_SECRET_FILE = "client_secret_1092459055663-5e3ft2pug9q15q6untlnj9b3ei1thkuq.apps.googleusercontent.com.json"


def get_youtube_service():

    credentials = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)

    if not credentials:
        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRET_FILE,
            SCOPES
        )

        credentials = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(credentials, token)

    youtube = build("youtube", "v3", credentials=credentials)

    return youtube


def get_channel():

    youtube = get_youtube_service()

    channel = youtube.channels().list(
        part="snippet",
        mine=True
    ).execute()

    return (
        youtube,
        channel["items"][0]["snippet"]["title"],
        channel["items"][0]["id"]
    )


def get_comments(youtube, channel_id, max_results=MAX_COMMENTS):

    response = youtube.commentThreads().list(
        part="snippet",
        allThreadsRelatedToChannelId=channel_id,
        maxResults=max_results,
        order="time"
    ).execute()

    return response["items"]