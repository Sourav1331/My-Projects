import qrcode as qr

code = qr.QRCode(version=1, error_correction=qr.ERROR_CORRECT_H, box_size=10, border=4)
code.add_data("https://www.google.com")
code.make(fit=True)
img = code.make_image(fill_color = "green", back_color = "white")
img.save("Some.png")
