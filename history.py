import json
import os

FILE_NAME = "history.json"


def load_history():

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_history(history):

    with open(FILE_NAME, "w") as file:
        json.dump(history, file, indent=4)


def is_processed(comment_id):

    history = load_history()

    return comment_id in history


def mark_processed(comment_id):

    history = load_history()

    history.append(comment_id)

    save_history(history)