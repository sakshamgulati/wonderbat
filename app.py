from os.path import splitext, exists
import streamlit as st
import pandas as pd
from io import StringIO


# Function to read and parse WebVTT file
def read_webvtt(file):
    captions = []
    with open(file, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i % 4 == 2:
                captions.append(line.strip())
    return captions


# Function to read and parse text file
def read_text(file):
    with open(file, "r") as f:
        text = f.read()
    return text


# Main function to run the Streamlit app
def main():
    st.title("Meetings made easy")

    # Create file upload widget
    file = st.file_uploader("Upload a WebVTT or text file", type=["vtt", "txt"])

    # If file is uploaded
    if file is not None:
        # Check file type and read contents accordingly
        if file.type == "text/vtt":
            captions = read_webvtt(file)
            text = "\n".join(captions)
        else:
            text = read_text(file)

        # Display file contents in formatted way
        st.subheader("File Contents:")
        st.write(text)
    st.title("🎙️Minutes of the Meeting App -Wonderbat")
    st.subheader(
        """
        This app was made by Saksham Gulati.
        """
    )
    with st.expander("About this App"):
        st.markdown(
            """
        Wonderbat uses the OpenAI API to perform minutes of the meeting.
        
        Libraries used:
        - `streamlit` - web framework
        - `openai` - Python client for OpenAI API
        - `pandas` - Python data manipulation library
        - `io` - Python I/O library
        - `os` - Python operating system library
        - `sys` - Python system library
        - `re` - Python regular expressions library 
        """
        )


if __name__ == "__main__":
    main()
