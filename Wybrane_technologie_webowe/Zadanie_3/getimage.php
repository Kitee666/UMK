<?php
    session_start();
    if(isset($_SESSION['user'])) {
        $url = './images/zalogowany.jpg';
    } else {
        $url = './images/niezalogowany.jpg';
    }
    $filepointer = fopen($url, 'rb');
    header("Content-Type: image/jpg");
    header("Content-Length: " . filesize($url));
    fpassthru($filepointer);
?>