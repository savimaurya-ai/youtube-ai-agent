from datetime import datetime

LOG_FILE = "logs.txt"


def write_log(author, comment, status, reply=""):

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:

        file.write(f"\n[{time}]\n")
        file.write(f"Author : {author}\n")
        file.write(f"Comment : {comment}\n")

        if reply:
            file.write(f"AI Reply : {reply}\n")

        file.write(f"Status : {status}\n")
        file.write("-" * 40 + "\n")