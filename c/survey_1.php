<?php
if(!($vote = @$_GET['vote'])) {
?>
<object type="application/x-shockwave-flash" data="mp3player.swf?autoplay=true&amp;song_url=http://ismir2009.benfields.net/saxex.mp3">
 <param name="movie" value="mp3player.swf?autoplay=true&amp;song_url=http://ismir2009.benfields.net/saxex.mp3" />
</object>

<form>
    This song was performed by:
    <input type=submit value='Human' name='vote' /> or
    <input type=submit value='Robot' name='vote' /> ?
</form>

<?php
} else {
    $data_file = "/tmp/survey_1.txt";
    $text  = "|" . date("Y.m.d H:i:s") . "| ";
    $text .= "|" . $vote . "| ";
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
