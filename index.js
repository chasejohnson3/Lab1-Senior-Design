const express = require('express')
const path = require('path')
var mysql = require('mysql');
var app = express();
const url = require('url');

const PORT = process.env.PORT || 5000

var con = mysql.createConnection({
    host: "34.68.18.19",
    user: "root",
    password: "dreamteam1"
});

sql = "select * from Lab1.TempData";
displayStatusTablePath = "select * from Lab1.DisplayStatus";

tempArr = [];
timeArr = [];

con.connect(function(err){
    if (err) throw err;
    console.log("Connected");
});

app.get('/', function(req, resp){
    con.query(sql, function(err, result, fields){
        if (err) throw err;
        var i = 0;
        for (i=0; i<result.length; i++)
        {
            tempArr[i] = result[i].Temp;
            timeArr[i] = result[i].Time;
        }
        resp.render(__dirname + "/index.ejs", {
            tempArr: tempArr,
			disPwr: 1,
            timeArr: timeArr
        });
    });
	
})

/* app.get('/onoff', function(req, resp){
    con.query(displayStatusTablePath, function(err, result, fields){
        if (err) throw err;
       var localDisPwr = results[0].dispPwrOnOff;
		
        resp.render(__dirname + "/index.ejs", {	
			disPwr: localDisPwr
        });
    });
}) */


app.get('/sendText', function(req, resp){
    console.log("test in index.js");
    var nodemailer = require('nodemailer');
    var phone_num = req.query.phoneNum;
    var carrier_ext = req.query.carrierExt;
    console.log("Full Path: " + req.url);
    console.log("Phone number is " + phone_num);
    
    
    var transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: 'BuckyStuck11@gmail.com',
        pass: 'BuckyStuck440'
      }
    });
    
    var mailOptions = {
      from: 'BuckyStuck11@gmail.com',
    //   to: phone_num + @email.uscc.net
    //   to: phone_num + "@messaging.sprintpcs.com",
      to: phone_num + carrier_ext,
      subject: 'Sending Email using Node.js',
      text: 'That was easy!'
    };
    
    transporter.sendMail(mailOptions, function(error, info){
      if (error) {
        console.log(error);
      } else {
        console.log('Email sent to ' + mailOptions.to + ': '+ info.response);
      }
    });
    resp.redirect("/");  
})

app.listen(PORT);
