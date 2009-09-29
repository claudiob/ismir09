<?php
require_once('facebook-platform/php/facebook.php');
$appid   = '170850830008'; # COPY AND PASTE
$api_key = '7b835778bae3c255b0586a55fa2043f8'; # COPY AND PASTE
$secret  = '6ec34840390de9b86d7dd88ae33066f1'; # COPY AND PASTE
$facebook = new Facebook($api_key, $secret);
$user = $facebook->require_login();

if(!($vote = @$_GET['vote'])) {
?>
<fb:mp3 src="http://ismir2009.benfields.net/m/saxex.mp3" 
title="Autumn Leaves" album="Autumn Leaves" artist="Human or Robot?" />

<form>
    <b>Survey:</b><br />
    This song was performed by a
    <input type=submit value='Human' name='vote' /> or by a
    <input type=submit value='Robot' name='vote' /> ?
</form>

<?php
} else {
    $user_info = $facebook->api_client->users_getStandardInfo($user, 
      array('first_name', 'last_name', 'sex', 'birthday', 'current_location'));
    $info = $user_info[0];
    $birth_year = isset($info['birthday']) ? 
     date("Y", strptime($info['birthday'], "%m %d, %Y") : '';
    $city =  isset($info['current_location']) ? 
     $info['current_location']['city'] : '';

    $data_file = "/tmp/survey.txt";
    $text  = "|" . date("Y.m.d H:i:s") . "| ";
    $text .= "|" . $vote . "| ";
    $text .= "|" . $info['first_name'] ." ". $info['last_name'] ."| ";
    $text .= "|" . $info['sex'] . "| ";
    $text .= "|" . $info['birthday'] . "| ";
    $text .= "|" . $info['city'] . "|";
    $file = fopen($data_file, "a");
    fwrite($file, $text ."\n");
    fclose($file);
    $file = file_get_contents($data_file, 'r');
    $human = substr_count($file, '|Human|');
    $robot = substr_count($file, '|Robot|');
    echo "Votes so far: Human ". $human ." - Robot ". $robot;
    echo "<pre>". $file ."</pre>";   
}
?>
