from pytube import YouTube as YT
link=input("Ingrese el link del Video")
descarga=YT(link).streams.first().download()
print("Descargando..... ", descarga)
print("Video Descargado")