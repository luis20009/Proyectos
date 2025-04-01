<?php
$respuesta = $_POST['respuesta'];
$correcta = $_POST['correcta'];

if ($respuesta == $correcta) {
    $resultado = "¡Correcto!";
} else {
    $resultado = "Incorrecto. La respuesta correcta es la opción " . $correcta;
}

header("Location: index.php?resultado=" . urlencode($resultado));
exit();
?>
