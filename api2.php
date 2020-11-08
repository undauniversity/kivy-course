<?php
include "config.php";


$auth = $_GET['auth']; //888
$perintah = $_GET['perintah'];
$kodemk = $_GET['kodemk'];
$namamk = $_GET['namamk'];
$id = $_GET['id'];

//echo $kodemk;echo $namamk;

if($auth == "888"){

if(!empty($_GET) && $perintah=="insert"){

    $sql = "INSERT INTO matakuliah (kodemk, nama_matakuliah) VALUES ('". $kodemk. "', '".$namamk."')";
    echo"<br>";
    echo $sql;

    if (mysqli_query($conn, $sql)) {
        echo "<br>";
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }


}

if(!empty($_GET) && $perintah=="update"){

    $sql = "update matakuliah set nama_matakuliah='".$namamk."' where kodemk='".$kodemk."'";
    echo"<br>";
    echo $sql;

    if (mysqli_query($conn, $sql)) {
        echo "<br>";
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }


}

if(!empty($_GET) && $perintah=="delete"){

    $sql = "delete from matakuliah where id=".$id;
    echo"<br>";
    echo $sql;

    if (mysqli_query($conn, $sql)) {
        echo "<br>";
        echo "Record has been deleted";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }


}

$return_arr = array();
//$sql = "SELECT id, npm, nama FROM mahasiswa";
$sql = "select id, kodemk, nama_matakuliah from matakuliah";
$result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // output data of each row
        while($row = $result->fetch_assoc()) {
            //echo "<br>";
            //echo "id= ". $row["id"]. ", kodemk= ". $row["kodemk"]. ", nama matakuliah = ".$row["nama_matakuliah"];
            //echo "id = $row['id'] , kodemk= $row['kodemk']";
            
            $row_array['id'] = $row['id'];
            $row_array['kodemk'] = $row['kodemk'];
            $row_array['nama_matakuliah'] = $row['nama_matakuliah'];

            array_push($return_arr,$row_array);
        }
        echo json_encode($return_arr);
    } else {
            echo "0 results";
    }



$conn->close();

}
?>