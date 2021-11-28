import qrcode
import image
qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
data="https://drive.google.com/file/d/1EhVtxX5bQ-4WMnP_3yip2Lo_sEreL1_c/view?usp=sharing"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",black_color="white")
img.save("test.png")