<?php
$servername = "localhost";
$username = "'root'@'localhos";
$dbname = "icfes_game";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}
?>
