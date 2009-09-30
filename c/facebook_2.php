<?php
require_once('facebook_key.php');

require_once('facebook-platform/php/facebook.php');
$facebook = new Facebook($api_key, $secret_key);
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
    $info = reset($facebook->api_client->users_getStandardInfo($user, 
     array('first_name', 'last_name', 'sex', 'birthday', 'current_location')));
    $info['birth_year'] = isset($info['birthday']) ? 
     date("Y", strptime($info['birthday'], "%m %d, %Y")) : '';
    $info['city'] =  isset($info['current_location']) ? 
     $info['current_location']['city'] : '';

    $data_file = "/tmp/fb_survey.txt";
    $text  = "|" . date("Y.m.d H:i:s") . "| ";
    $text .= "|" . $vote . "| ";
    $text .= "|" . $info['first_name'] ." ". $info['last_name'] ."| ";
    $text .= "|" . $info['sex'] . "| ";
    $text .= "|" . $info['birth_year'] . "| ";
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
