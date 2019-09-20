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

tempArr = [];
timeArr = [];

con.connect(function(err){
    if (err) throw err;
    console.log("Connected");
});

app.get('/', function(req, resp){
    // while(1){
        con.query(sql, function(err, result, fields){
            if (err) throw err;
            var i = 0;
            for (i=0; i<result.length; i++)
            {
                tempArr[i] = result[i].Temp;
                timeArr[i] = result[i].Time;
            }
            // resp.redirect(url.format({
            //     pathname:"https://chasejohnson3.github.io/Lab1-Senior-Design/",
            //     query: {
            //        "tempArr":JSON.stringify(tempArr),
            //        "timeArr": JSON.stringify(timeArr)
            //     }
            // }));
            // resp.sendFile("C:\\Users\\User\\OneDrive - University of Iowa\\2019 Fall Semester\\Senior Design\\node-js-getting-started\\index.html");
            // resp.sendFile(__dirname + "/index.html");
            resp.render(__dirname + "/index.ejs", {
                tempArr: tempArr,
                timeArr: timeArr
            });
            
            
            // console.log(tempArr);
            // console.log(timeArr);
        });
        // setTimeout(30000);
    // }
  
})
app.listen(PORT);
