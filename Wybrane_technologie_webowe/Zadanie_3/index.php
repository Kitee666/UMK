<!DOCTYPE html>
<html>
    <head>
    </head>
    <?php
        require './auth.php';
    ?>
    <body>
        <?php
            if(isset($_SESSION['user'])) {
                echo '<p>Zalogowany jako: <span style="font-weight:bold">'.$_SESSION['user'].'</span></p>';
            }
            require './menu.php';
        ?>
        <img src="login.jpg" alt="status">
    </body>
</html>