<?php
include "config.php";
$perintah=$_GET['perintah'];
$npm=$_GET['npm'];
$nama=$_GET['nama'];

//print "halo";

$sql = "SELECT id, npm, nama FROM mahasiswa";
$result = $conn->query($sql);

echo "<br>";
echo $perintah;

if (!empty($_GET) && $perintah=="select") {
    if ($result->num_rows > 0) {
  // output data of each row
        while($row = $result->fetch_assoc()) {
            echo "<br>";
            echo "id: " . $row["id"]. " - npm: " . $row["npm"]. " " . $row["nama"]. "<br>";
        }
    } else {
            echo "0 results";
    }

$conn->close();
}

if (!empty($_GET) && $perintah=="insert") {

    $sql = "INSERT INTO mahasiswa (npm, nama) VALUES ('". $npm. "', '".$nama."')";
    echo"<br>";
    echo $sql;

    if (mysqli_query($conn, $sql)) {
        echo "<br>";
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }

    mysqli_close($conn);
}


?>