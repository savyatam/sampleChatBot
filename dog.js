const express = require('express');
const { MessagingResponse } = require('twilio').twiml;
const http = require('https');
const fs = require('fs');
const axios = require('axios')
const router = express.Router();
const bodyParser = require('body-parser');
var request = require('request');
var voice  =require('./urlcheck');
var unirest = require('unirest');
var urlencodedParser = bodyParser.urlencoded({ extended: false })
router.post('/', async (req, res) => {
  let message;
   console.log(req.body);
  res.set('Content-Type', 'text/xml');
  if(req.body.Body)
  {message = new MessagingResponse().message(req.body.Body);
    res.send(message.toString()).status(200);
  }
  if(req.body.MediaUrl0)
  {
    request(req.body.MediaUrl0).pipe(fs.createWriteStream('xp.ogg'))
    .on('error', () => {
    console.log('ERROR');
    message = new MessagingResponse().message('fails');
    res.send(message.toString()).status(200);
  })
  .on('finish', () => {
    unirest
        .post('https://recognition.voicybot.com/recognize/Wit')
        .headers({'Content-Type': 'multipart/form-data'})
        .field('key','BHH56KIGVSKELNOZNHTWRYRVQTIEIEC2')
        .attach({'file':'xp.ogg',})
        .then((response) => {
          console.log(response.body);
          var text=response.body.text;
          message = new MessagingResponse().message(text);
          res.send(message.toString()).status(200);
        })
        .catch(e=>{
          message = new MessagingResponse().message('fails');
          res.send(message.toString()).status(200);
        });
  });
  }
});

module.exports = router;
