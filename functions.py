import fitz # Our PDF reader
import requests # To request our API connection
import json # Need this to read json responses
import base64 # We will be needing this as the response that comes back, is coded in base64. We just need to translate it to normal characters.
import os # Will be used for environmental Variables as well as getting a directory list for our function
from pydub import AudioSegment # This is used to put all of our audio files together into one file
from tqdm import tqdm # Will be used to display a progress bar, as books can be quite extensive in pages


def text_to_speech(text, book_name, page):
    """The function that transforms inputed text, into speech"""
    api_key = "YOUR API KEY HERE" # Your own personalised api key here: https://console.cloud.google.com/apis/credentials
    url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={api_key}"
    data = { # The required parameters to be sent in, to get a basic conversion
        "input": {"text": text}, # Passing the text as a variable
        # Important: There are many voices in Google. Check here: https://cloud.google.com/text-to-speech/docs/voices
        "voice": {"languageCode": "en-GB", "name": "en-GB-Standard-O", "ssmlGender": "MALE"}, 
        # The preferred encoding method. Also supports: https://cloud.google.com/text-to-speech/docs/reference/rest/v1/AudioEncoding?utm_source=chatgpt.com
        "audioConfig": {"audioEncoding": "MP3"}
    }

    # Make the API request
    response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))

    # Handle the response
    if response.status_code == 200: # We check if the response is 200 or OK
        response = response.json() # We capture the response in json format
        if "audioContent" in response: # If encoded corectly, as audio content
            audio_content = base64.b64decode(response["audioContent"])  # Decode the base64 audio_content
            output_filename = f"audio-pages/{book_name}-{page}.mp3"
            with open(output_filename, "wb") as audio_file: # Will open a write only file
                audio_file.write(audio_content) # Will write the data in the mp3 format, to our desired file
            print(f"Audio file saved as {book_name}-{page}.mp3")
        else:
            print("Error: No 'audioContent' found in response.") # To capture if something went wrong
    else:
        print("Error:", response.status_code, response.text) # To capture other response codes, to see what the error or issue is


def read_pdf(file_path, page_number):
    """The function that reads a PDF type file to be returned as an input"""
    text = ""
    file_name = os.path.basename(file_path) # We use the os.path.basename function to get the name of the file
    book_name = file_name.split('-')[0] # And then we clas split it by the -, which is created by the ilovepdf.io conveniently
    file = fitz.open(file_path) # We use fitz to open and read our file
    for page in file: # Incase you input more pages then one at a time
        text += page.get_text("text") # Will combine the entrire text into one variable
        text_to_speech(text, book_name, page_number) # We call our text to speech function passing the page number


def get_audio_files(directory):
    """The function to get and return a list of files in a directory"""
    audio_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".mp3")] # List comprehension for directory
    print(audio_files) # Just in case
    return audio_files # Returns the audio files directory list


def join_audio_files():
    """The function to combine multiple audio files into one"""
    clear_console()
    audio_files = get_audio_files("audio-pages")
    file_name = os.path.basename(audio_files[0]) # We use the os.path.basename function to get the name of the file
    book_name = file_name.split('-')[0] # And then we clas split it by the -, which is created by the ilovepdf.io conveniently
    output_file = f"audio-books/{book_name}.mp3"

    combined_segment = AudioSegment.empty() # We start with an empty segment

    for audio_file in tqdm(audio_files, desc="Combining Audio Files", unit="file"): # We loop through each audio directory in the list
        audio = AudioSegment.from_mp3(audio_file) # Format can be changed, but needs to be throughout the projects at this stage
        combined_segment += audio # We add the new audio segment to our combined one

    combined_segment.export(output_file, format="mp3") # Calling out the export function, which will combine the list of Audio Files
    delete_audio_pages("audio-pages")
    print(f"All audio files have been combined to {output_file}") # Just in case, to confirm the file name


def clear_console():
    """Clears the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def delete_audio_pages(directory):
    """Deletes all files in the specified directory"""
    if not os.path.exists(directory): # Checks if directory does not exist
        print(f"Error: Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory): 
        file_path = os.path.join(directory, filename) # creates a filepath
        try:
            if os.path.isfile(file_path):  
                os.remove(file_path) # Removes the file
        except Exception as e:
            print(f"Error deleting {file_path}: {e}") # To catch errors
    print(f"All files deleted from {directory}") # Confirmation
