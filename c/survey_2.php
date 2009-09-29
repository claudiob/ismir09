<?php
require_once('facebook-platform/php/facebook.php');
$appid   = '170850830008'; # COPY AND PASTE
$api_key = '7b835778bae3c255b0586a55fa2043f8'; # COPY AND PASTE
$secret  = '6ec34840390de9b86d7dd88ae33066f1'; # COPY AND PASTE
$facebook = new Facebook($api_key, $secret);

$user = $facebook->require_login();

$first_name = $last_name = $sex = $birthday = $city = '';
$user_info = $facebook->api_client->users_getStandardInfo($user, 
    array('first_name', 'last_name', 'sex', 'birthday', 'current_location'));
$info = $user_info[0];
if(isset($info['first_name'])) $first_name = $info['first_name'];
if(isset($info['last_name']))  $last_name = $info['last_name'];
if(isset($info['sex']))        $sex = $info[''];
if(isset($info['birthday']))   $birthday = $info['birthday'];
if(isset($info['current_location']) && isset($info['current_location']['city']))
    $city = $info['current_location']['city'];

if(!($vote = @$_GET['vote'])) {
?>
<fb:mp3 src="http://ismir2009.benfields.net/saxex.mp3" 
title="Autumn Leaves" album="Autumn Leaves" artist="Human or Robot?" />

<form>
    This song was performed by:
    <input type=submit value='Human' name='vote' /> or
    <input type=submit value='Robot' name='vote' /> ?
</form>

<?php
} else {
    $data_file = "/tmp/survey_2.txt";
    $text  = "|" . date("Y.m.d H:i:s") . "| ";
    $text .= "|" . $vote . "| ";
    $text .= "|" . $first_name ." ". $last_name ."| ";
    $text .= "|" . $sex . "| ";
    $text .= "|" . $birthday . "| ";
    $text .= "|" . $city . "|";
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
