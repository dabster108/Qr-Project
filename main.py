import qrcode as qr
import customization
from url_handling import url

fill_color = input("Enter fill color first you need for qr : ") 
background_color = input("Enter background color : ") 


img = qr.make(url)


customization.customization(url, fill_color, background_color)
