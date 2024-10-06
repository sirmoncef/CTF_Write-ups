<?php
getMessage();


$file = $_GET['file'];
includeFile($file);
$FLAG = getenv('FLAG');
class Admin
{
    public $is_admin = "";
    public $your_secret = "";
    public $my_secret = "";
    
    public function __construct($in, $ysecret, $msecret)
    {
        $this->is_admin = md5($in);
        $this->your_secret = $ysecret;
        $this->my_secret = $msecret;
    }
    
    public function __toString()
    {
        return $this->is_admin;
    }
}

if (isset($_COOKIE['can_you_get_me'])) {
    try {
        $f = base64_decode($_COOKIE['can_you_get_me']);
        if (!$f) {
            throw new Exception("");
        }
        $unout = unserialize($f);
        if (!$unout) {
            throw new Exception("\n wrong cookie");
        }
        $unout->my_secret = $FLAG;
        if ($unout->is_admin == 0 && $unout->your_secret === $unout->my_secret) {
            echo "Okay here is your flag:", $FLAG;
        } else {
            echo "no ";
        }
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    }
}
?>
