import html


def clean_comment(text):
    """
    Convert HTML entities to normal text.
    Example:
    I&#39;m  -> I'm
    <br>   -> New Line
    """

    text = html.unescape(text)

    text = text.replace("<br>", "\n")
    text = text.replace("<br/>", "\n")
    text = text.replace("<br />", "\n")

    return text.strip()