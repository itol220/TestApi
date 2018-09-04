# try:
#     import qrcode
#     from PIL import Image
#
#     url = "www.zhuanzhuan.com"
#     qr = qrcode.QRCode(
#         version=3,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=8,
#         border=2
#     )
#     qr.add_data(url)
#     qr.make(fit=True)
#     img = qr.make_image()
#     img = img.convert("RGBA")
#     icon = Image.open("C:/Users/kk/Desktop/logo.jpg")
#     img_w, img_h = img.size
#     factor = 4
#     size_w = int(img_w / factor)
#     size_h = int(img_h / factor)
#
#     icon_w, icon_h = icon.size
#     if icon_w > size_w:
#         icon_w = size_w
#     if icon_h > size_h:
#         icon_h = size_h
#     icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
#     w = int((img_w - icon_w) / 2)
#     h = int((img_h - icon_h) / 2)
#     img.paste(icon, (w, h), icon)
#
#     img.save("C:/Users/kk/Desktop/test.jpg")
# except Exception as e:
#     print(e)



import qrcode,winreg,string,os
class QrcodeMake():

    def __init__(self):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,\
                              r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
        self.get_desktop = winreg.QueryValueEx(key, "Desktop")[0]
        # return winreg.QueryValueEx(key, "Desktop")[0]

        # 根据输入内容生成二维码
    def osPath(self,fname):

        return fname.split('.')[0]+'1'+'.png' if os.path.exists(fname) else fname

    def qrcodeWithText(self, text):
        img = qrcode.make(text)
        # 保存图片

        Path = f'{self.get_desktop}/{text[0:9]}_text.png'
        savePath = self.osPath(Path)

        img.save(savePath)
        # print(img)

    # 根据url生成二维码
    def qrcodeWithUrl(self,url):
        img=qrcode.make(url)
        #保存图片
        urlH = url.split('/')[2].split('.')
        # if urlH[0] in string.ascii_letters:
        # urlN = re.findall('\.(.*)\.com',url)[0]
        urlI = ''.join(urlH)
        print([*urlI])
        Path = f'{self.get_desktop}/{urlH[1]}_url.png'\
            if urlH[0][0] in string.ascii_letters else f'{self.get_desktop}/w{urlI[0:9]}_url.png'
        # savePath = path if ':' not in [*urlI] else path.replace(':','')
        savePath = self.osPath(Path)
        img.save(savePath)
        # print(img)


    def parse(self):
        content = input('请输入内容：')
        if 'http' in content:
            self.qrcodeWithUrl(content)
        else:
            self.qrcodeWithText(content)
        print('二维码已生成！')

if __name__ == '__main__':
    QrcodeMake().parse()