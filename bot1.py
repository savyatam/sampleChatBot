from flask import Flask, request
#from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = np.array(pd.read_csv('new.csv'))
m,n= data.shape
for i  in range (3,m-1):
    data[i,n-1]=int(data[i,n-1])
Data1= pd.DataFrame(data[m-11:m,: ])
#print(data[m-1,n-1])
def doo():
    data = np.array(pd.read_csv('new.csv'))
    m,n= data.shape
    for i  in range (3,m-1):
        data[i,n-1]=int(data[i,n-1])
    
    Data1= pd.DataFrame(data[m-11:m,: ])
    X= (data[3:40,0])
    Y= (data[3:40,n-1])
    plt.plot(X,Y)
    plt.savefig('as')
    plt.savefig('as1')
    plt.show()
    print('Current Balance is',data[m-1,n-1])

    print("Standard Chartered Bank Personal Loan Details", 
      "Loan available for both salaried and self-employed professionals. Borrowers within the age group of 23 and 58 years.", 
      "Loan amount of minimum ₹ 1 Lakh to ₹ 30 Lakh. Standard Chartered personal loan rate of interest is in the range of 10.99% to 19.00%.")
app = Flask(__name__)
doo()
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
    response = MessagingResponse()
    message = Message()
    #resp.message("You said: {}".format(msg))
    if msg=="1":
        resp.message("Your  A/c XXXXXXX2138 on 02/02/2020 .Avl Bal Rs "+str(data[m-1,n-1]))
    if msg=="2":
        message.body('Expenditure Categorisation')
        message.media('https://cc70f734.ngrok.io/as1.png')
        response.append(message)
        return str(response)
    if msg=="3":
        message.body('Atms near me')
        message.media('https://cc70f734.ngrok.io/atms.png')
        response.append(message)
        return str(response)
    if msg=="4":
        resp.message("Standard Chartered Bank Personal Loan Details"+ 
      "Loan available for both salaried and self-employed professionals. Borrowers within the age group of 23 and 58 years."+ 
      "Loan amount of minimum ₹ 1 Lakh to ₹ 30 Lakh. Standard Chartered personal loan rate of interest is in the range of 10.99% to 19.00%.")
    if msg=="5":
        resp.message("you opted option 5")
    if msg=="6":
        message.body('transaction history')
        message.media('https://cc70f734.ngrok.io/transition.png')
        response.append(message)
        return str(response)
    if msg=="Options":
        resp.message("Transaction History:\n1-Balance Enquiry\n2-Expenditure Categorisation\n3-ATM Near Me\n4-Loan Details\n5-Balance Analysis\n6-Transaction History")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
