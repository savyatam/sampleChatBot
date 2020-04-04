const accountSid = 'AC4187cd169e98759f0c5e7ca47c0c3948';
const authToken = '233ac673b0a4c53e97ad433f55ee5d23';
const client = require('twilio')(accountSid, authToken);

client.messages
      .create({
         body: 'Your appointment is coming up on July 21 at 3PM',
         from: 'whatsapp:+14155238886',
         to: 'whatsapp:+917380713610'
       })
      .then(message => console.log(message.sid))
      .done();
