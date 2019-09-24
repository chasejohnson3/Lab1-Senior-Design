<?php

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;
require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';

$number = $_REQUEST["number"];
$message = $_REQUEST["message"];
$mail = new PHPMailer(true);


$mail->SMTPDebug = 2;  
$mail->isSMTP();                                        
$mail->Host       = 'smtp.gmail.com'; 
$mail->SMTPAuth   = true;                                  
$mail->Username   = 'BuckyStuck11@gmail.com';                 
$mail->Password   = 'BuckyStuck440';                          
$mail->SMTPSecure = 'tls';                                
$mail->Port       = 587;                        

$mail->setFrom('BuckyStuck11@gmail.com');

//Adjust this line according to the mobile phone carrier 
$mail->addAddress($number.'@txt.att.net'); 

$mail->isHTML(true);                          
$mail->Subject = 'Temperature data';
$mail->Body    = $message;
$mail->AltBody = $message;

if (!$mail->send()) {
    echo "Mailer Error: " . $mail->ErrorInfo;
} else {
    echo "Message sent!";
}

?>