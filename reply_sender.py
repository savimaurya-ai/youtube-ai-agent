def send_reply(youtube, comment_id, reply_text):

    try:

        request = youtube.comments().insert(
            part="snippet",
            body={
                "snippet": {
                    "parentId": comment_id,
                    "textOriginal": reply_text
                }
            }
        )

        request.execute()

        print("\n✅ Reply Successfully Posted!")

    except Exception as e:

        print("\n❌ Reply Post Failed!")
        print(e)