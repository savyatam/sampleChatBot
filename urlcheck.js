const express = require('express');
const path = require('path');
const router = express.Router();
var http = require('https');
const fs = require('fs');
const axios = require('axios')
var request = require('request');
var unirest = require('unirest');
router.get('/',async(req,res)=>{
  res.send('works');
});
function fnc()
{
    let text='ex';
unirest
    .post('https://recognition.voicybot.com/recognize/Wit')
    .headers({'Content-Type': 'multipart/form-data'})
    .field('key','BHH56KIGVSKELNOZNHTWRYRVQTIEIEC2')
    .attach({
    'file':'bell.oga',
  })
    .then((response) => {
      console.log(response.body)
      text=response.body.text;
    })
}
module.exports={router,fnc};
