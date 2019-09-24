var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'BuckyStuck11@gmail.com',
    pass: 'BuckyStuck440'
  }
});

var mailOptions = {
  from: 'BuckyStuck11@gmail.com',
  to: 'sachinshriram55@gmail.com',
  subject: 'Sending Email using Node.js',
  html: '<h1>Welcome</h1><p>That was easy!</p>'
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});