//Node.JS MySQL queries resource used: https://www.codediesel.com/nodejs/querying-mysql-with-node-js/

const express = require('express')
const path = require('path')
var mysql = require('mysql');
var app = express();
const url = require('url');

var bodyParser = require('body-parser');
app.use(bodyParser.json()); // for parsing application/json
app.use(bodyParser.urlencoded({ extended: true }));
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
var localDisPwr;

con.connect(function(err){
    if (err) throw err;
    console.log("Connected");
});

var timeArr3 =[], tempArr3 = [];
app.post('/postarrays', function(req,res){
  timeArr3 = req.body.timeArras;
  tempArr3 = req.body.tempArras;
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
        console.log(timeArr3);
        resp.render(__dirname + "/index.ejs", {
            tempArr: tempArr,
            timeArr: timeArr,
            timeArr3: timeArr3,
            tempArr3: tempArr3
        });
        
      });
      
});


app.post('/postarrays', function(req,res){
  timeArr3 = req.body.timeArras;
  tempArr3 = req.body.tempArras;
});

 app.get('/display', function(req, resp){
    con.query(displayStatusTablePath, function(err1, rows, fields){
        if (err1) throw err1;
		localDisPwr = rows[0].currDisPwr;
		
        resp.send([localDisPwr]); //Send the result back to the function that requested from /display
        });
    });

app.get('/sendTemps', function(req, resp){
	
  con.query(sql, function(err, result, fields){
    if (err) throw err;
    var i = 0;
	var timeArr2 = [];
	var tempArr2 = [];
    for (i=0; i<result.length; i++)
    {
		
		// Missing values in SQL are interpreted as NULL so the below if will translate null values between javascript and SQL
		if(result[i].Temp){
			tempArr2[i] = result[i].Temp;
		}else{
			tempArr2[i] = null;
		}
        timeArr2[i] = result[i].Time;
    }
  //console.log(tempArr2[tempArr2.length-1]);
    resp.send([tempArr2, timeArr2]);
    });
    
});

app.get('/sendText', function(req, resp){
    console.log("test in index.js");
    var nodemailer = require('nodemailer');
    var phone_num = req.query.phoneNum;
    var carrier_ext = req.query.carrierExt;
    var minMsg = req.query.minMsg;
    var maxMsg = req.query.maxMsg;
    console.log("Full Path: " + req.url);
    

    var message = "";
    if (minMsg != null)
    {
      message = minMsg;
    }
    if (maxMsg != null)
    {
      message = maxMsg;
    }
    
    var transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        //SOMEONE'S USERNAME AND PASSWORD REQUIRED HERE
        user: 'BuckyStuck11@gmail.com',
        pass: 'BuckyStuck440' 
      }
    });


	
    var mailOptions = {
      from: 'BuckyStuck11@gmail.com',
    //   to: phone_num + @email.uscc.net
    //   to: phone_num + "@messaging.sprintpcs.com",
      //to: phone_num + carrier_ext,
      to: phone_num + carrier_ext,
      // to: "trashtrashy75@gmail.com",
      subject: 'Sending Email using Node.js',
      text: message
    };
    
    transporter.sendMail(mailOptions, function(error, info){
      if (error) {
        console.log(error);
      } else {
        console.log('Email sent to ' + mailOptions.to + ': '+ info.response);
      }
    });
})

/* Add logic here to 1)Clear the Lab1.DisplayStatus table 2) Set the bit to 1(On) or 0 (Off)

app.get('/toggleDisplayPwr', function(req, resp){
	con.query("truncate Lab1.DisplayStatus", function(err1, rows, fields){
        if (err1) throw err1;
		
        });
    });
}) */
app.post('/sendDisplayStatus', function(req, resp){
	//Accomplishes a logical NOT of the display status that is stored in the database
	con.query("update Lab1.DisplayStatus set prevDisPwr = currDisPwr, currDisPwr =@temp where (@temp:=prevDisPwr) IS NOT NULL");
	
});

app.listen(PORT);
