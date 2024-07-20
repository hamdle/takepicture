<?php

// Usage:
// php run.php /home/eric/repos/takepicture 3

$file = 'takepicture.py';
$path = $argc > 1
    ? $argv[1]  // /home/eric/repos/takepicture
    : getcwd();
$cmd = 'python '.$path.'/'.$file;
$mins = $argc > 2
    ? $argv[2] // 3
    : 10;

while (true)
{
    echo 'Executing command: '.$cmd.PHP_EOL;
    $tmp = shell_exec($cmd);
    echo $tmp;
    sleep(60 * $mins);
}

?>
