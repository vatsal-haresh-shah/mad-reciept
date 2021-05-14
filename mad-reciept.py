# -*- coding: utf-8 -*-
"""
Created on Thu May 13 14:32:49 2021

@author: Vatsal Shah
"""

#from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

#Defining Variables
pdfName = "Hello.pdf"
heading = "Making A Difference Foundation"
width, height = A4
'''
#Defining Canvas object and Initializing PDF with pdfName
c = canvas.Canvas(pdfName, pagesize=A4, bottomup = 0)

#Setting the starting cooridnates from (20,20)
c.translate(20,20)

#Drawing a rectangle.
c.setFillColorRGB(0.48, 0.52, 0)
c.rect(0,0, 550, 400, fill = 1)

#
c.drawString(40,40,heading)
#c.setFillColor(colors.white)
#c.setStrokeColor(colors.white)
#c.rect(20,20,510,360, fill = 1)
c.rotate(90)
c.save()

'''
pdf = SimpleDocTemplate("re.pdf", pagesize = A4)
styles = getSampleStyleSheet()
title_style = styles['Heading1']
title_style.aligment = 2
title_style.fontSize = 10

par_1 = Paragraph(heading, title_style)
flowables = [par_1]

pdf.build(flowables)



