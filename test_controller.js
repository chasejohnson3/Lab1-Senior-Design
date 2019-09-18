
var mysql = require('mysql');
var express = require('express')
var app = express();

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
    con.query(sql, function(err, result, fields){
        if (err) throw err;
        var i = 0;
        for (i=0; i<result.length; i++)
        {
            tempArr[i] = result[i].Temp;
            timeArr[i] = result[i].Time;
        }
        resp.json(tempArr)
        console.log(tempArr);
        console.log(timeArr);
    });
});

app.listen(1337);