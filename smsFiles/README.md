#### Sending SMS data
The php file uses `PHPMailer` to send the data. Install `PHPMailer` from [here](https://github.com/PHPMailer/PHPMailer)
Also uses the Apache server to host `email.php` to `localhost`

The html file can be used as a template for the web interface. 

`app.js` uses `jQuery` to `POST` the data (`number` and `message`) to `email.php`