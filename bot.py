from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import numpy
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    # Create reply
    resp = MessagingResponse()
    #resp.message("You said: {}".format(msg))
    if msg=="1":
        resp.message("you opted option 1")
    if msg=="2":
        resp.message("you opted option 2")
    if msg=="3":
        resp.message("you opted option 3")
    if msg=="4":
        resp.message("you opted option 4")
    if msg=="5":
        resp.message("you opted option 5")
    if msg=="6":
        resp.message("you opted option 6")
    if msg=="Options":
        resp.message("Transaction History:\n1-Balance Enquiry\n2-Expenditure Categorisation\n3-ATM Near Me\n4-Loan Details\n5-Balance Analysis\n6-Transaction History")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
