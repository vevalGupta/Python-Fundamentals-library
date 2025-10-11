import qrcode
data = "https://www.fuelone.in/sv/fuel-one-whey-max/SP-122555?navKey=VRNT-233369&itracker=w:home|best-seller|;"
qr = qrcode.QRCode(
    version=1,  # controls size (1–40); higher = bigger
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # L, M, Q, H
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border (minimum is 4)
)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qr_code.png")
print("QR Code saved as my_qr_code.png")
img.show()
