
# Pandora MP4

This repository contains two Python scripts that demonstrate a technique for concealing data by encoding a video file and JSON data using base64 encoding. This approach showcases a basic form of steganography, where information is hidden within seemingly innocuous files.

## Encoding Process

The first script, encode.py, performs the following steps:

* Reads a JSON file located at data/data.json.
* Converts the JSON into a string and encodes it using base64.
* Reads a video file from data/video.mp4.
* Uses b"VIDEOJSONSEPARATOR" as a unique separator.
* Combines the video data and the encoded JSON string with the separator.
* Creates a new video file at output/video_c.mp4 with the combined data.

## Decoding Process

The second script, decode_script.py, executes the following actions:

* Reads the encoded video file from output/video_c.mp4.
* Locates the position of b"VIDEOJSONSEPARATOR" within the video file.
* Separates the video data and the encoded JSON string based on the separator's position.
* Decodes the base64-encoded string, revealing the original JSON content.
* Displays the decoded JSON content in the terminal.
  
## Usage

Clone this repository:
```bash
git clone https://github.com/your-user/your-repo.git
```
Ensure Python is installed on your system.

Navigate to the cloned directory:
```bash
cd your-repo
```

Run the first script to encode data within the video:
```bash
python encode.py
```

This will create an encoded video file in the output folder.

Run the second script to decode and display the concealed data:
```bash
python decode.py
```

The hidden JSON content will be revealed in the terminal.

## Considerations

These scripts provide educational insight into basic steganography using base64 encoding. They might not be suitable for secure or production-level data concealment.
Ensure that data.json and video.mp4 are correctly placed before running the scripts.
Note that this repository is intended for educational purposes and might require modifications for specific use cases.
