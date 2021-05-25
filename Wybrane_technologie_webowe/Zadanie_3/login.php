<!DOCTYPE html>
<html>
    <head>
    </head>
    <?php
        function http_digest_parse($txt){
            $needed_parts = array('nonce'=>1, 'nc'=>1, 'cnonce'=>1, 'qop'=>1, 'username'=>1, 'uri'=>1, 'response'=>1);
            $data = array();
            $keys = implode('|', array_keys($needed_parts));

            preg_match_all('@(' . $keys . ')=(?:([\'"])([^\2]+?)\2|([^\s,]+))@', $txt, $matches, PREG_SET_ORDER);

            foreach ($matches as $m) {
                $data[$m[1]] = $m[3] ? $m[3] : $m[4];
                unset($needed_parts[$m[1]]);
            }

            return $needed_parts ? false : $data;
        }

        require './auth.php';
        $user = array('admin' => 'admin',
        'administrator' => 'admin',
        'guest' => 'guest');

        $realm = 'Zajecia zdalne';

        if (empty($_SERVER['PHP_AUTH_DIGEST'])) {
            header('HTTP/1.1 401 Unauthorized');
            header('WWW-Authenticate: Digest realm="'.$realm.'",qop="auth",nonce="'.uniqid().'",opaque="'.md5($realm).'"');
            echo '<p><a href="./">Home</a></p>';
            die('<p style="color:red">Błędny login lub hasło</p>');
        }
        if (!($data = http_digest_parse($_SERVER['PHP_AUTH_DIGEST'])) || !isset($user[$data['username']])){
            header('HTTP/1.1 401 Unauthorized');
            header('WWW-Authenticate: Digest realm="'.$realm.'",qop="auth",nonce="'.uniqid().'",opaque="'.md5($realm).'"');
            echo '<p><a href="./">Home</a></p>';
            die('<p style="color:red">Błędny login lub hasło</p>');
        }
        $A1 = md5($data['username'] . ':' . $realm . ':' . $user[$data['username']]);
        $A2 = md5($_SERVER['REQUEST_METHOD'].':'.$data['uri']);
        $valid_response = md5($A1.':'.$data['nonce'].':'.$data['nc'].':'.$data['cnonce'].':'.$data['qop'].':'.$A2);
        
        if ($data['response'] != $valid_response){
            header('HTTP/1.1 401 Unauthorized');
            header('WWW-Authenticate: Digest realm="'.$realm.'",qop="auth",nonce="'.uniqid().'",opaque="'.md5($realm).'"');
            echo '<p><a href="./">Home</a></p>';
            die('<p style="color:red">Błędny login lub hasło</p>');
        }
        $_SESSION['user'] = $data['username'];


    ?>
    <body>
        <?php
            if(isset($_SESSION['user'])) {
                echo '<p style="color:blue">Zalogowany pomyślnie.</p>';
            }
            require './menu.php';
        ?>
    </body>
</html>