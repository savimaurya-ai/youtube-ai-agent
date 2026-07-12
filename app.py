from ai_reply import generate_reply
from youtube_api import get_channel, get_comments
from history import is_processed, mark_processed
from comment_filter import is_simple_comment

# -----------------------------
# Connect to YouTube
# -----------------------------
youtube, channel_name, channel_id = get_channel()

print("\n==============================")
print("✅ Connected Channel :", channel_name)
print("==============================")

# -----------------------------
# Read Latest Comments
# -----------------------------
comments = get_comments(youtube, channel_id)

print("\n========== Latest Comments ==========")

for item in comments:

    comment = item["snippet"]["topLevelComment"]["snippet"]
    comment_id = item["snippet"]["topLevelComment"]["id"]

    # Skip already processed comments
    if is_processed(comment_id):
        print("\n⏭️ Already Processed - Skipping...")
        continue

    author = comment["authorDisplayName"]
    text = comment["textDisplay"]

    print("\n----------------------------------------")
    print("👤 Author :", author)
    print("💬 Comment:", text)

    # Skip simple comments
    if is_simple_comment(text):
        print("\n⏭️ Simple Comment Detected")
        print("🤖 AI Reply Skipped")
        mark_processed(comment_id)
        continue

    # Generate AI Reply
    reply_text = generate_reply(text)

    print("\n🤖 AI Reply:")
    print(reply_text)

    # Ask for approval
    choice = input("\nIs reply ko approve karte ho? (Y/N): ").strip().lower()

    if choice == "y":
        print("\n✅ Approved")
        print("Reply Ready:")
        print(reply_text)

        # Save comment ID in history
        mark_processed(comment_id)

    else:
        print("\n⏭️ Reply Skip Kar Diya")

print("\n🎉 Sabhi comments process ho gaye.")