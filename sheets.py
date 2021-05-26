#PDF Generation libraries
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
#Google Libraries
from googleapiclient.discovery import build
from google.oauth2 import service_account
from apiclient import errors
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from num2words import num2words
import pickle
import os
#Email Libraries
import base64
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import mimetypes

scope = ['https://www.googleapis.com/auth/spreadsheets']
serviceAccountFile = 'generator-keys.json'
SCOPES = ['https://mail.google.com/']

def get_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    return service


def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()

        print('Message Id: {}'.format(message['id']))

        return message
    except Exception as e:
        print('An error occurred: {}'.format(e))
        return None


def create_message_with_attachment(sender, to, subject, message_text, file,):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg = MIMEText(message_text)
    message.attach(msg)

    (content_type, encoding) = mimetypes.guess_type(file)

    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'

    (main_type, sub_type) = content_type.split('/', 1)

    if main_type == 'text':
        with open(file, 'rb') as f:
            msg = MIMEText(f.read().decode('utf-8'), _subtype=sub_type)

    elif main_type == 'image':
        with open(file, 'rb') as f:
            msg = MIMEImage(f.read(), _subtype=sub_type)
        
    else:
        with open(file, 'rb') as f:
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(f.read())

    filename = os.path.basename(file)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)

    raw_message = base64.urlsafe_b64encode(message.as_string().encode('utf-8'))
    return {'raw': raw_message.decode('utf-8')}




def sheetData(scope, serviceAccountFile):
    creds = None
    creds = service_account.Credentials.from_service_account_file(serviceAccountFile, scopes=scope)

    # The ID and range of a sample spreadsheet.
    SPREADSHEET_ID = '1lpiY659Dc0at_Z6rfr1pAJXzMKrxaoU1nUCqSAnZMKU'

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,range="reciept!A:P").execute().get('values',[])
    
    row = result[-1] if result else None
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
            "amtWord" : num2words(row[13]),
            "email" : row[10]
        }
    
    return row

def createReciept(data, fileName):
    #Defining Variables
    tR = 'Times-Roman'
    file = fileName
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
    currentDate = "17/03/2021"
    subTitle3 = "12A Registration No: 47494 dated 17.06.2015   Pan No.: AADAM6362K"
    subTitle4 = "Exemption Under 80-G of IT Act, No.: CIT9E/ 80G/ 961/ 2015-16"
    #rec = "Receiver's Sign"
    thankYou = "Thank You!"
    auto = "*This is an autogenerated reciept"
    


    #Defining Canvas object and Initializing PDF with pdfName
    doc = canvas.Canvas(file, pagesize=A4)
    
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
    doc.drawString(480,640, data["date"])
    
    #Name of the Donor
    doc.drawString(40,610, name)
    doc.setFont(tR, 18)
    doc.drawString(200,610, data["firstName"])
    if data["middleName"] != None:
        doc.drawString(280,610,data["middleName"])
    doc.drawString(380,610, data["lastName"])
    
    #Amount paid and Pan card No
    doc.setFont(tR, 12)
    doc.drawString(40,580, amount)
    doc.drawString(100, 580, data["amountPaid"] + "/-")
    
    doc.drawString(200,580, panCard)
    doc.drawString(300,580, data["panCardNo"])
    
    #Amount Paid in words
    doc.setFont(tR, 12)
    doc.drawString(40,550, amountWord)
    doc.drawString(150,550, data["amtWord"])
    
    '''
    #Payment Mode, Date of Payment and Bank
    doc.setFont(tR, 12)
    doc.drawString(40,520, payMode)
    doc.drawString(120,520, data["paymentMode"])
    '''

    doc.drawString(40,520, date)
    doc.drawString(70,520, data["date"])
    
    doc.drawString(250,520, bank)
    doc.drawString(300,520, data["bankName"])
    
    #Amount Box
    doc.rect(60,460,60,30)
    doc.setFont(tR, 16)
    doc.drawString(60, 470, data["amountPaid"] + "/-")
    
    #Apprecition text
    doc.setFont("Courier", 18)
    doc.setFillColor(colors.red)
    doc.drawCentredString(250, 475, thankYou)
    
    #Mad detailes 
    doc.setFont(tR, 10)
    doc.setFillColor(colors.black)
    doc.drawString(40,420, subTitle3)
    doc.drawString(40,410,subTitle4)
    #Bottle line
    doc.line(30, 395, 550, 395)
    
    #Adding the auto generated message
    doc.setFont(tR, 9)
    doc.drawString(40,385, auto)
    
    #Boundary Rectangle
    doc.rect(20,375,540,410)
    
    #Saving the pdf with the above changes 
    doc.save()

if __name__ == "__main__":
    data = sheetData(scope,serviceAccountFile)
    '''
    user_id = 'me'
    sender = 'reciept.mad@gmail.com'
    to = data["email"]
    sub = "MAD Reciept " + data["firstName"] + " " + data["lastName"]
    body = 'This is a test, Hopefull it works. Thank you for your donation'
    file = "MAD-Reciept " + data["firstName"] + " " + data["lastName"] + ".pdf"
    '''
    print(data)

    #createReciept(data, file)
    #service = get_service()
    #msg = create_message_with_attachment(sender, to, sub, body, file)
    #send_message(service, user_id, msg)