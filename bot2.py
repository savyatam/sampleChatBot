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
    data[i,0]=(data[i,0])[:5]
    
Data1= pd.DataFrame(data[m-11:m,2: ])
    
X= (data[6:16,0])
Y= (data[6:16,n-1])
plt.plot(X,Y,color='red')
plt.savefig('myfig')

A=[0,0,0,0,0]
print(data[3,5])

print (A[0])
A[0]=A[0]+5
print(data[1,4])

for i in range (3,m-1):
    if (data[i,5] == 'Shoping'):
        A[0] =int(A[0])+int(data[i,3])*(-1)
    elif (data[i,5] == 'Travel'):
        A[1] =int(A[1])+int(data[i,3])*(-1)
    elif (data[i,5] == 'Food'):
        A[2] =int(A[2])+int(data[i,3])*(-1)
    elif (data[i,5] == 'Health'):
        A[4] =int(A[4])+int(data[i,3])*(-1)
    elif (data[i,5] == 'Personal account'):
        A[3] =int(A[3])+int(data[i,3])*(-1)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['Shoping', 'Travel', 'Food', 'Health','Unknown']
ax.pie(A, labels = langs,autopct='%1.2f%%')
plt.savefig('myfig1')
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
    response = MessagingResponse()
    message = Message()
    #resp.message("You said: {}".format(msg))
    if msg=="1":
        resp.message("Your  A/c XXXXXXX2138 on 02/02/2020 .Avl Bal Rs "+str(data[m-1,n-1]))
    if msg=="2":
        message.body('Expenditure Categorisation')
        message.media('https://cc70f734.ngrok.io/myfig1.png')
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
        message.body('Balance Analysis')
        message.media('https://cc70f734.ngrok.io/myfig.png')
        response.append(message)
        return str(response)  
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
