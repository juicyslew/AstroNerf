from flask import Blueprint
from flask import jsonify, request
from backend.processes.VTController import VTController
#from backend.auth.key import emailPswrd
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
#from smtplib import SMTP


api = Blueprint('api', __name__)
controller = VTController()

@api.route('/getReps', methods=['GET'])
def getReps():
    """
    This route handles grabbing information for the start screen.
    """
    if request.method == 'GET':
        data = request.values
        stateID = data['stateID']
        res = controller.LoadReps(stateID)
        return jsonify(
            res
        )

"""
@api.route('/', methods=['GET'])
def via():
    '''
    This route handles any requests to the main via app, primarily controls
    '''
    if request.method == 'GET':
        res = controller.onReceive(request.values.to_dict(flat=False))
        print(res)
        return jsonify(
            res
        )
"""
"""
@api.route('/email', methods=['POST'])
def sendMail():
    '''
    Send an email using outlooks smtp server to the target address
    '''
    if request.method == 'POST':
        data = request.get_json()
        if 'body' not in data:
            raise Exception('GET request to /email missing "body" param')
        if 'targetAddr' not in data:
            raise Exception('GET request to /email missing "targetAddr" param')

        # Fill information about the emailto be sent
        msg = MIMEMultipart()
        toAddr = data['targetAddr']
        body = data["body"]
        msg["From"] = FROM_ADDR
        msg["Subject"] = "VIA Recorded Path Information - Id:" + str(data["sessionId"])
        msg.attach(MIMEText(body, 'html'))

        # Setup connection to outlook mailing service.
        server = SMTP('smtp-mail.outlook.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        # Login to our account
        server.login(FROM_ADDR, emailPswrd)

        # Set Email information and Send
        text = msg.as_string()
        server.sendmail(FROM_ADDR, toAddr, text)
        server.close()
    retdata = {"success": True}
    return jsonify(retdata)
"""