import json
import base64

# Leer el JSON
json_file_path = "data/data.json"
with open(json_file_path, "r") as json_file:
    json_data = json.load(json_file)

# Convertir el JSON a una cadena codificada en base64
json_str = json.dumps(json_data)
encoded_json = base64.b64encode(json_str.encode()).decode()

# Leer el video
video_path = "data/video.mp4"
with open(video_path, "rb") as video_file:
    video_data = video_file.read()

# Definir el separador
separator = b"VIDEOJSONSEPARATOR"

# Unir el video y los datos codificados con el separador
encoded_video_data = video_data + separator + encoded_json.encode()

# Escribir los datos codificados en un nuevo video
output_path = "output/video_c.mp4"
with open(output_path, "wb") as output_file:
    output_file.write(encoded_video_data)

print("Codificación completada.")
