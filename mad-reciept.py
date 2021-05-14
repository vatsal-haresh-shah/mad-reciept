# -*- coding: utf-8 -*-
"""
Created on Thu May 13 14:32:49 2021

@author: Vatsal Shah
"""

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

pdfName = "Hello.pdf"
width, height = A4
c = canvas.Canvas(pdfName, pagesize=A4)
c.translate(20,420)
c.drawString(40,40,"Making")
c.setFillColorRGB(48, 52, 0)
c.rect(0,0, 550, 400, fill = 1)
c.setFillColor(colors.white)
c.setStrokeColor(colors.white)
c.rect(20,20,510,360, fill = 1)
c.rotate(0)
c.save()

#setFillColorRGB(r, g, b)
pdf = SimpleDocTemplate("re.pdf", pagesize = A4)
styles = getSampleStyleSheet()
