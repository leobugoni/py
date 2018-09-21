import requests as r 
from PIL import Image
from urllib.request import urlopen
import os
from fpdf import FPDF

pdf = FPDF(format=(1152, 1692), unit='pt')

if not os.path.exists("img"):
	os.mkdir("img")

def getPage(pageId):
	req = r.get("https://sunflowerbv.digitalpages.com.br//html/getPageZoom?editionId=11400&pageId=" + str(pageId))
	
	json = req.json()
	imgUrl = json['url']
	
	im = Image.open(urlopen(imgUrl))
	im.save("img/"+str(pageId)+".png")
	
	pdf.add_page()
	pdf.image("img/"+str(pageId)+".png", type="PNG", x = 0, y = 0)
	
	
for num in range(3246638, 3246638 + 123):
	getPage(num)
	
pdf.output("livro.pdf")