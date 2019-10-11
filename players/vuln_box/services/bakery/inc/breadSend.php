<?php

# need to ping addresses
if(isset($_GET['ip'])) {
  system('ping -c 1 '.$_GET['ip']);
  die();
}

?>
