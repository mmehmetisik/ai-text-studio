"""
Text processing and analysis functions
This file processes and analyzes generated texts
"""


def count_words(text):
    """
    Calculates the number of words in the text

    Args:
        text (str): Text to count words in

    Returns:
        int: Total word count
    """
    # Split text by spaces and count words
    # split() function splits text by spaces
    words = text.split()
    return len(words)


def clean_text(text):
    """
    Cleans text and removes unnecessary spaces

    Args:
        text (str): Text to be cleaned

    Returns:
        str: Cleaned text
    """
    # strip() function removes spaces from beginning and end
    # replace() function converts double spaces to single spaces
    text = text.strip()  # Remove spaces from beginning and end
    text = ' '.join(text.split())  # Reduce multiple spaces to single space
    return text


def truncate_text(text, max_words):
    """
    Truncates text according to specified word count

    Args:
        text (str): Text to be truncated
        max_words (int): Maximum word count

    Returns:
        str: Truncated text
    """
    # Split text into words
    words = text.split()

    # If text is already short, return as is
    if len(words) <= max_words:
        return text

    # Take first max_words words and join them
    # [:max_words] notation is list slicing, takes first max_words elements
    truncated = ' '.join(words[:max_words])

    # Add three dots at the end so user knows it's truncated
    return truncated + "..."