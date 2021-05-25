# -*- coding: utf-8 -*-
"""
Created on Fri May 14 14:36:42 2021

@author: Vatsal Shah
"""
'''
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

fileName = "sample.pdf"
image = 'MAD_LOGO_11-4-17.png'
title = "Making A Difference Foundation"
subTitle1 = "Registered Under Society Act XXI of 1860, No.: 1353/2014 GBBSD"
no = "11"

doc = canvas.Canvas("Reciept "+ no + ".pdf", pagesize=A4)

doc.setFont('Times-Roman', 29)
doc.drawCentredString(300,750, title)

doc.setFont('Times-Roman', 10)
doc.drawCentredString(300,730, subTitle1)

doc.drawImage(image, 40, 670, width = 80, height = 80)

doc.save()
'''
'''
pdf = SimpleDocTemplate("re.pdf", pagesize = A4)
styles = getSampleStyleSheet()
title_style = styles['Heading1']
title_style.aligment = 2
title_style.fontSize = 10

par_1 = Paragraph(heading, title_style)
flowables = [par_1]

pdf.build(flowables)
'''
scope = ['https://www.googleapis.com/auth/spreadsheets']
serviceAccountFile = 'generator-keys.json'
from googleapiclient.discovery import build
from google.oauth2 import service_account
from num2words import num2words
creds = None
creds = service_account.Credentials.from_service_account_file(serviceAccountFile, scopes=scope)

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1lpiY659Dc0at_Z6rfr1pAJXzMKrxaoU1nUCqSAnZMKU'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,range="reciept!A:P").execute().get('values',[])

row = result[-1] if result else None
print(row[15])
date = row[0].split(' ')

data = {
        "srNo" : "1524",
        "date" : date[0],
        "firstName" : row[1],
        "middleName": row[2],
        "lastName" : row[3],
        "amountPaid" : row[13],
        "panCardNo" : row[15],
        "bankName" : row[14],
        "amountWord" : num2words(row[13])
    }
print(data)
