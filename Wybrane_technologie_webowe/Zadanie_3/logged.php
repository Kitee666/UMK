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
                echo '<p>Zalogowany jako:'.$_SESSION['user'].'</p>';
            }
            require './menu.php';
        ?>
        <p> Treść wyświetlana tylko dla zalogowanego użytkownika</p>
    </body>
</html>