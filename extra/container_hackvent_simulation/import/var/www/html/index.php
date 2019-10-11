<html>
<head></head>
<body>
<pre>
This simulates the Hackvent Portal.
Test for muffinCTF.
</pre>
<?php

  //$LOGIN_URL = 'http://whale.hacking-lab.com:9280/';

  $LOGIN_URL = 'http://0.0.0.0:9280/';


  $PUBLIC_KEY = <<<EOF
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAtdRKcARZCK+tJNLGvZyC
C2oXZohwvkgUlYwZXkuFkNWu85nO9Fr91bvwSI+BGvHcSBAgQGdmFoNQb+8uC5IN
d84CTbuTwc4RDWvcmxWHwXNum/qYo6zMB7bguZ2MbzW8A8T1XWrde/O6xj2Lp7Hy
oi/HeM9Ma1h8usMDrgGWOVmFJzL1lxTiHfxUDWiqb8msQfO25FB3rKienA8JMvs7
6hHlSVRHrOT1FLoXXgjsANvewFSeu5kzV/izxMhmPY7grrzGDa16r/VZnGOpU2vx
FqOQQIHyPRfy5IFix9SK0YMYkuetB6hpHikQyjghp66wZT4+k08FL5HS/4TDOjM3
0phSWBZpiNSaScur8aWywjHCLYO6PkAj2u/7aSEb7KUR6TxJoDLWRbrhVaNATeKr
QT6r9zuOMVUxcYZA19ZWRarSHVSBq2HfVaCSNATYeORpkld0xVjdnJPL173PxZ6s
Nao+j8noKSeQUve7GMp08Cb3Q4cEuB2PGEwd2b1kmBUAeU3LOI0MzpB6cuHpDkfl
Roxf3QItQjxWa5hwQhftOyx2L0ePFf5SQzy9qGuhIrYEqrQDEeEv9ByEY+z3VRwT
40drGXfZdSXBkIS9B0/Dey3I2IkuiJvy/2QTkFAR/fnzhsZ69aAFwrCJSvoCfk5B
Ru6NsJaBEDafD5hjxPohITUCAwEAAQ==
-----END PUBLIC KEY-----
EOF;

  $PUBLIC_KEY = openssl_get_publickey($PUBLIC_KEY);

  $user = '';
  if(isset($_GET['user'])) {
    if($_GET['user'] === 'ed6f8761d0ce200d98cd95ebecd70f43b2006cb9f407cfb3408077088b9f21ba613a58f5d662de066b1c60d14e69622c95f7aa63d7278f96aecea1fd3743b909') {
      $user = 'muffinx';
    }
    if($_GET['user'] === '131d1d6ba89743ba3188423cfce773e6ca36a6a2891fad21357df3be340d703a1df695b3c842f03ac644b3ef32b4a8b83b0c83687fd0b2b4558ac43640aaed1e') {
      $user = 'pyth0n33';
    }
    if($_GET['user'] === '05ad8e707599d6130f27f385357059421ec52d6996f80ed0b323d4a371176dca2f579c8240892efa8459cc194db9c9572b379432136f3dbef40e5e1fc6caeac1') {
      $user = 'kiwi';
    }
  }

  if($user !== '') {
    echo '<pre>Welcome '.$user.' </pre>';

    $auth_json = json_encode(array(
      'timestamp' => time(),
      'user' => $user
    ));

    $enc_json = '';
    openssl_public_encrypt('[BEGIN_JSON]'.$auth_json, $enc_json, $PUBLIC_KEY);
    $enc_json = base64_encode($enc_json);

    echo '<form method="GET" action="'.$LOGIN_URL.'login">';
    echo '<input type="hidden" name="auth_token" value="'.$enc_json.'" />';
    echo 'Login: <input type="submit" />';
    echo '</form>';
  }

?>
</body>
</html>
