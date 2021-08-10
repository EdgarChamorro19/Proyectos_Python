from captcha.image import ImageCaptcha 

imagen=ImageCaptcha(width=280,height=100)

texto="hellouuu"

dato=imagen.generate(texto)

imagen.write(texto, "CAPTCHA.png")

