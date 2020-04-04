var express = require('express'),
    dogs    = require('./dog'),
    both  =require('./urlcheck');
var unirest=require('unirest');
var app = express();
var http = require('https');
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended:true }));
var port = process.env.PORT || 3000;
app.use('/dogs',  dogs);
app.use('/',both.router);
both.fnc()
app.listen(port);
