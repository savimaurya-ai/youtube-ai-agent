def is_simple_comment(comment):

    comment = comment.lower().strip()

    simple_comments = [
        "nice",
        "good",
        "great",
        "awesome",
        "amazing",
        "wow",
        "super",
        "thanks",
        "thank you",
        "❤️",
        "❤",
        "🔥",
        "👍",
        "👏",
        "nice video",
        "good video",
        "great video",
        "excellent",
        "best",
        "love it",
        "very nice",
        "mast",
        "bahut badhiya",
        "bahut accha",
        "acha",
        "accha",
        "thanku",
        "thnx"
    ]

    if comment in simple_comments:
        return True

    if len(comment.split()) <= 2:
        return True

    return False