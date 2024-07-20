<?php

$file = 'takepicture.py';
$path = getcwd();
$cmd = 'python '.$path.'/'.$file;

while (true)
{
    echo 'Executing command: '.$cmd.PHP_EOL;
    $tmp = shell_exec($cmd);
    echo $tmp;
    sleep(60 * 10);
}

?>
