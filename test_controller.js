
var mysql = require('mysql');
var express = require('express');
var app = express();
const url = require('url');
var fs = require("fs");

var db_password = JSON.parse(fs.readFileSync("passwords.json")).password;





var con = mysql.createConnection({
    host: "34.68.18.19",
    user: "root",
    password: db_password
});

sql = "select * from Lab1.TempData";

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
        // resp.json(tempArr)
        // resp.redirect("https://chasejohnson3.github.io/Lab1-Senior-Design/")
        resp.redirect(url.format({
            pathname:"https://chasejohnson3.github.io/Lab1-Senior-Design/",
            query: {
               "tempArray":JSON.stringify(tempArr),
               "timeArr": JSON.stringify(timeArr)
            }
        }));
    
        // resp.sendFile("C:\\Users\\User\\OneDrive - University of Iowa\\2019 Fall Semester\\Senior Design\\Lab1-Senior-Design\\htmlExample.html")
        console.log(tempArr);
        console.log(timeArr);
    });
});

app.listen(1337);