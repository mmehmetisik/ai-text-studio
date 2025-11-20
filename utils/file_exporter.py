"""
File saving and export operations
This file saves generated texts in TXT format
"""

from datetime import datetime  # For date and time


def save_as_txt(text, content_type):
    """
    Saves text as a TXT file

    Args:
        text (str): Text to be saved
        content_type (str): Content type (will be used in filename)

    Returns:
        str: Name of the saved file
    """
    # Get current date and time to use in filename
    # strftime function converts date to string in desired format
    # %Y = year, %m = month, %d = day, %H = hour, %M = minute, %S = second
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create filename
    # Replace spaces in content type with underscores
    # replace() function replaces one character with another
    safe_content_type = content_type.replace(" ", "_")
    filename = f"{safe_content_type}_{timestamp}.txt"

    # Write file
    # 'w' mode means write mode
    # encoding='utf-8' is important for proper display of special characters
    # with block automatically closes the file, it's a safe method
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)  # Write text to file
        return filename  # Return filename if successful

    except Exception as e:
        # If error occurs while writing file (disk full, no permission, etc.)
        return f"Error: {str(e)}"


def create_download_link(text, filename):
    """
    Creates downloadable file data for Streamlit

    Args:
        text (str): Text to be downloaded
        filename (str): File name

    Returns:
        tuple: (text data, file name, mime type)
    """
    # This function prepares data for Streamlit's download_button
    # Returns text data, filename, and MIME type
    # MIME type tells the browser "this is a text file"
    return text, filename, "text/plain"