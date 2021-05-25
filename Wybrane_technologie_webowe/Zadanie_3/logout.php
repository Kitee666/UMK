<!DOCTYPE html>
<html>
    <head>
    </head>
    <?php
        require './auth.php';
        header("WWW-Authenticate: Invalidate, Basic realm=logout");
        unset($_SESSION['user']);
        session_destroy();
    ?>
    <body>
        <?php
            require './menu.php';
        ?>
        <p style="color:green">Wylogowano pomyślnie.</p>
    </body>
</html>