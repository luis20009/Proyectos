<html>
<head>
<title>Ejemplo de operadores Logicos</title>
</head>
<body>
<h1>Ejemplo de operaciones logicas en PHP</h1>
<?php
$Fresa = 5;
$Pera = 6;
$Melon = 5;
$Resultado = ($Melon = $Pera) || ($Melon <= $Fresa)? 'True' : 'false';
echo "Tu resultado es \n";
 echo ($Resultado == 'True')? 'Tu maldita madre' : 'paila' . "<br>";
?>
</body>
</html>