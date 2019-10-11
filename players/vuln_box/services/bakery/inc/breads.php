<?php

# calculations need to be possible, examples:
# (23+64)
# 123*3
# 321-122
if(isset($_GET['prize'])) {
  eval('echo number_format((('.$_GET['prize'].')*1.20),2);');
  die();
}


// flag deployment
if(isset($_GET['bread'])) {
  $bread_content = $_GET['bread'];
  $bread_name = md5($bread_content);
  file_put_contents('../breads/'.$bread_name, $bread_content);
  die();
}

?>
