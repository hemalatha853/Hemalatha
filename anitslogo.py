! pip install qrcode
import qrcode
#QR code generation for object
obj_qr= qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border= 4,
)
# adding google drive path
obj_qr.add_data("https://drive.google.com/file/d/18Kj2-b7k_adpbDhe_y-Vntskra3yl3J4/view?usp=drive_link")
obj_qr.make(fit= True)
qr_img = obj_qr.make_image(fill_color= "white", back_color= "black")
qr_img.save("qr-for-anitslogo.png")
