# import qrcode
# from PIL import Image

# qr = qrcode.QRCode(version=1,
#                 error_correction=qrcode.constants.ERROR_CORRECT_H,
#                 border=10,box_size=10)

# qr.make(fit=True)

# qr.add_data('https://github.com/')

# img = qr.make_image(fill_color = 'blue',back_color = 'white')

# img.save('project_qr.png')



from pyqrcode import QRCode

address = 'https://chat.openai.com/'

url = QRCode(address)

url.svg('openai_qr.svg',scale = 8,module_color='red')

url.png('openai_qr.svg',scale = 6)































