# -*- coding: utf-8 -*-
"""
Created on Thu May 13 14:32:49 2021

@author: Vatsal Shah
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
#from reportlab.platypus import Paragraph, SimpleDocTemplate
#from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

#Defining Variables
tR = 'Times-Roman'
fileName = "Hello.pdf"
docTitle = "Mad-Reciept"
title = "Making A Difference Foundation"
subTitle1 = "Registered Under Society Act XXI of 1860, No.: 1353/2014 GBBSD"
subTitle2 = "Registered Under Mumbai Public Act Trust of 1950, No. F 58681 (M)"
address = "10/2 Dhanlakshmi Society, Mogal Lane, Matunga (W), Mumbai - 400016"
email = "madmadfoundation@gmail.com"
image = 'MAD_LOGO_11-4-17.png'
recieptNo = "Reciept No.:"
date = "Date:"
name = "Recieved with Thanks From.:"
amount = "Amount.:"
panCard = "Pan Card No.:"
amountWord = "Amount In Words.:"
bank = "Bank.:"
payMode = "Payment Mode.:"
payDate = "Date.:"
currentDate = "17/03/2021"
subTitle3 = "12A Registration No: 47494 dated 17.06.2015   Pan No.: AADAM6362K"
subTitle4 = "Exemption Under 80-G of IT Act, No.: CIT9E/ 80G/ 961/ 2015-16"
rec = "Receiver's Sign"
thankYou = "Thank You!"
width, height = A4

#data
data = {"srNo" : "1524",
        "date" : "24/03/2021",
        "firstName" : "Vatsal",
        "middleName": "Haresh",
        "lastName" : "Shah",
        "amountPaid" : "0000",
        "panCardNo" : "1234567890",
        "bankName" : "IDFC First Bank",
        "paymentMode" : "Cheque"}

#Defining Canvas object and Initializing PDF with pdfName
doc = canvas.Canvas(fileName, pagesize=A4)

#Give the document a title
doc.setTitle(docTitle)

#Setting the starting cooridnates from (20,20)
#doc.translate(20,20)

#Main Title
doc.setFont(tR,29)
doc.drawCentredString(300,750, title)

#Mad Details
doc.setFont(tR, 10)
doc.drawCentredString(300,730, subTitle1)

doc.setFont(tR, 10)
doc.drawCentredString(300,720, subTitle2)

#Registered Address and email
doc.setFont(tR, 10)
doc.drawCentredString(300,695, address)

doc.setFont(tR, 10)
doc.drawCentredString(300,685, email)

#Mad Logo
doc.drawImage(image, 40, 670, width = 80, height = 80)

#Separation Line
doc.line(30, 665, 550, 665)

#Reciept No and Date
doc.setFont(tR, 12)
doc.drawString(40,640, recieptNo)
doc.drawString(110,640, data["srNo"])

doc.drawString(450,640,date)
doc.drawString(480,640,currentDate)

#Name of the Donor
doc.setFont(tR, 12)
doc.drawString(40,610, name)
doc.drawString(200,610, data["firstName"])
if data["middleName"] != None:
    doc.drawString(250,610,data["middleName"])
doc.drawString(300,610, data["lastName"])

#Amount paid and Pan card No
doc.setFont(tR, 12)
doc.drawString(40,580, amount)
doc.drawString(100, 580, data["amountPaid"])

doc.drawString(200,580, panCard)
doc.drawString(300,580, data["panCardNo"])

#Amount Paid in words
doc.setFont(tR, 12)
doc.drawString(40,550, amountWord)

#Payment Mode, Date of Payment and Bank
doc.setFont(tR, 12)
doc.drawString(40,520, payMode)
doc.drawString(120,520, data["paymentMode"])

doc.drawString(200,520, date)
doc.drawString(250,520, data["date"])

doc.drawString(350,520, bank)
doc.drawString(410,520, data["bankName"])

#Amount Box
doc.rect(60,460,60,30)
doc.setFont(tR, 16)
doc.drawString(70, 470, data["amountPaid"])

#Apprecition text
doc.setFont("Courier", 18)
doc.setFillColor(colors.red)
doc.drawCentredString(250, 475, thankYou)

#Mad detailes 
doc.setFont(tR, 10)
doc.setFillColor(colors.black)
doc.drawString(40,420, subTitle3)
doc.drawString(40,410,subTitle4)

#Signature and box
doc.rect(465,420,30,50)
doc.setFont(tR, 10)
doc.drawString(450,410, rec)

#Bottle line
doc.line(30, 395, 550, 395)

#Boundary Rectangle
doc.rect(20,375,540,410)
doc.save()




