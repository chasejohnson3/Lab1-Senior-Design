
var mysql = require('mysql');

var con = mysql.createConnection({
    host: "34.68.18.19",
    user: "root",
    password: ""
})

sql = "select * from Lab1.TempData"

tempArr = []
timeArr = []

con.connect(function(err){
    if (err) throw err;
    console.log("Connected");
    con.query(sql, function(err, result, fields){
        if (err) throw err;
        var i = 0;
        for (i=0; i<result.length; i++)
        {
            tempArr[i] = result[i].Temp;
            timeArr[i] = result[i].Time;
        }
        console.log(tempArr);
        console.log(timeArr);
    });
});