<?php
    session_start();
    $protectedUrl = ['/auth.php', '/logged.php', '/logout.php'];
    $url = strtok($_SERVER["REQUEST_URI"], '?');
    foreach($protectedUrl as $link) {
        if(strpos($url, $link) !== false && !isset($_SESSION['user'])) {
            echo '<p><a href="./">Home</a></p>';
            die('<p style="color:red">Zasoby dostępne po zalogowaniu.</p>');
        }
    }
?>