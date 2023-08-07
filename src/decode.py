import base64

# Leer el video codificado
encoded_video_path = "output/video_c.mp4"
with open(encoded_video_path, "rb") as encoded_video_file:
    encoded_video_data = encoded_video_file.read()

# Encontrar el separador en el video
separator = b"VIDEOJSONSEPARATOR"
separator_index = encoded_video_data.rfind(separator)
if separator_index == -1:
    raise ValueError("Separador no encontrado en el video")

# Extraer los datos codificados del JSON del video
video_data = encoded_video_data[:separator_index]
encoded_json = encoded_video_data[separator_index + len(separator):]

# Decodificar la cadena codificada en base64
decoded_json = base64.b64decode(encoded_json).decode()

# Mostrar el JSON decodificado en la consola
print("JSON decodificado:")
print(decoded_json)
