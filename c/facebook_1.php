<?php
if(!($vote = @$_GET['vote'])) {
?>
<object type="application/x-shockwave-flash" data="mp3player.swf?autoplay=true&amp;song_url=http://ismir2009.benfields.net/m/saxex.mp3" height="30">
 <param name="movie" value="mp3player.swf?autoplay=true&amp;song_url=http://ismir2009.benfields.net/m/saxex.mp3" />
</object>

<form>
    <b>Personal data:</b><br />
    Your name: <input type=text name="first_name" size="17">
          <input type=text name="last_name" size="17"><br /><br />
    Your birth year: <input type=text name="birth_year" size="4">
    Your sex:  <input type=radio name="sex" value="male"> <i>Male</i>
          <input type=radio name="sex" value="female"> <i>Female</i><br /><br />
    Your current home-town: <input type=text name="city" size="25"><br /><br />

    <b>Survey:</b><br />
    This song was performed by a
    <input type=submit value='Human' name='vote' /> or by a
    <input type=submit value='Robot' name='vote' /> ?
</form>

<?php
} else {
    $info = $_GET;
    
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
