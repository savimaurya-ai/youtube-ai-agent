from comment_manager import clean_comment
from youtube_api import get_channel, get_comments
from ai_reply import generate_reply


def connect_youtube():

    try:

        youtube, channel_name, channel_id = get_channel()

        return {
            "success": True,
            "youtube": youtube,
            "channel_name": channel_name,
            "channel_id": channel_id
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


def read_latest_comments(youtube, channel_id):

    try:

        comments = get_comments(youtube, channel_id)

        data = []

        for item in comments:

            comment = item["snippet"]["topLevelComment"]["snippet"]

            data.append({
                "author": comment["authorDisplayName"],
                "text": clean_comment(comment["textDisplay"])
            })

        return {
            "success": True,
            "comments": data
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


def generate_ai_reply(comment):

    try:

        reply = generate_reply(comment)

        return {
            "success": True,
            "reply": reply
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }