import base64

# Read the encoded video
encoded_video_path = "output/video_c.mp4"
with open(encoded_video_path, "rb") as encoded_video_file:
    encoded_video_data = encoded_video_file.read()

# Find the separator in the video
separator = b"VIDEOJSONSEPARATOR"
separator_index = encoded_video_data.rfind(separator)
if separator_index == -1:
    raise ValueError("Separador no encontrado en el video")

# Extract the encoded JSON data from the video
video_data = encoded_video_data[:separator_index]
encoded_json = encoded_video_data[separator_index + len(separator):]

# Decode the base64-encoded string
decoded_json = base64.b64decode(encoded_json).decode()

# Display the decoded JSON in the console
print("JSON decodificado:")
print(decoded_json)
