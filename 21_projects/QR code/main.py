# '''
# We are going to ues a Python library like qrcode and convert url to qr
# '''
# import qrcode

# url = input("Enter your url: ")
# filename = input("Filename you want to save it as: ")
# if not(filename.endswith(".png")):
#     filename = filename + ".png"

# img = qrcode.make(url)
# img.save(filename)


# advanced version with customization

import qrcode

url = input("Enter your url: ")
filename = input("Filename you want to save it as: ")
if not(filename.endswith(".png")):
    filename = filename + ".png"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(filename)