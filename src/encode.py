import json
import base64

# Read JSON
json_file_path = "data/data.json"
with open(json_file_path, "r") as json_file:
    json_data = json.load(json_file)

# Convert JSON into a BASE64 string
json_str = json.dumps(json_data)
encoded_json = base64.b64encode(json_str.encode()).decode()

# Read the video
video_path = "data/video.mp4"
with open(video_path, "rb") as video_file:
    video_data = video_file.read()

# Define the separator
separator = b"VIDEOJSONSEPARATOR"

# Unify the video
encoded_video_data = video_data + separator + encoded_json.encode()

# Write the data in the new file
output_path = "output/video_c.mp4"
with open(output_path, "wb") as output_file:
    output_file.write(encoded_video_data)

print("Codificación completada.")
