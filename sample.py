# -*- coding: utf-8 -*-
"""
Created on Fri May 14 14:36:42 2021

@author: Vatsal Shah
"""
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

fileName = "sample.pdf"
image = 'MAD_LOGO_11-4-17.png'
title = "Making A Difference Foundation"
subTitle1 = "Registered Under Society Act XXI of 1860, No.: 1353/2014 GBBSD"

doc = canvas.Canvas(fileName, pagesize=A4)

doc.setFont('Times-Roman', 29)
doc.drawCentredString(300,750, title)

doc.setFont('Times-Roman', 10)
doc.drawCentredString(300,730, subTitle1)

doc.drawImage(image, 40, 670, width = 80, height = 80)

doc.save()

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