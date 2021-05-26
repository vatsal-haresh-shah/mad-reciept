import os.path
#Google API Libraries
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
#Email libraries 
import base64
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
import mimetypes
import os

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/']

def getService():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    return service

def sendMessage(service, id, message):
    try:
        message = service.users().messages().send(userId = id, body = message).execute()

        print('Message ID: {}'.format(message['id']))

        return message
    except Exception as e:
        print('An error occurred: {}'.format(e))
        return None

def createMessageAttactment(sender, to, subject, messageText, file,):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg = MIMEText(messageText)
    message.attach(msg)

    (contentType, encoding) = mimetypes.guess_type(file)

    if contentType is None or encoding is not None:
        contentType = 'application/octet-stream'

    (mainType, subType) = contentType.split('/',1)

    if mainType == 'text':
        with open(file, 'rb') as f:
            msg = MIMEText(f.read().decode("utf-8"), _subtype=subType)
    elif mainType == 'image':
        with open(file, 'rb') as f:
            msg = MIMEImage(f.read(), _subtype = subType)
    elif mainType == 'application' and subType == 'pdf':
        with open(file, 'rb') as f:
            msg = MIMEApplication(f.read(), _subtype = subType)
    else:
        with open(file, 'rb') as f:
            msg = MIMEBase(mainType, subType)
            msg.set_payload(f.read())

    fileName = os.path.basename(file)
    msg.add_header('Content-Dispostion','attachment', filename = fileName)
    message.attach(msg)

    rawMsg = base64.urlsafe_b64encode(message.as_string().encode("utf-8"))

    return{'raw':rawMsg.decode("utf-8")} 
    

if __name__ == '__main__':
    service = getService()
    id = 'me'
    sender = 'reciept.mad@gmail.com'
    to = 'clever.vatsal@yahoo.com'
    subject = 'TESTING'
    body = "Hopefully this will work"
    file = './Hello.pdf'

    msg = createMessageAttactment(sender, to, subject, body, file)
    sendMessage(service, id, msg)