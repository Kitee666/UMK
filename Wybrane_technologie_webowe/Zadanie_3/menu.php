<?php
    echo '<p><a href="./">Home</a></p>';
    if(isset($_SESSION['user'])) {
        echo '<p><a href="./logout.php">Logout</a></p>';
    } else {
        echo '<p><a href="./login.php">Login</a></p>';
    }
    echo '<p><a href="./logged.php">Only for logged</a></p>';
?>