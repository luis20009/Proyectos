<?php 
/* Mostraremos el uso de la sentencia While y comenzamos a usar entrada 
del teclado mediante un formulario simple */ 
if ( isset( $_POST['number'] )) { 
$number = $_POST['number']; 
$counter = 1; 
while ($counter <= $number) { 
echo "Los bucles son faciles!<br>\n"; 
$counter++; 
} 
echo "Se acabo.\n"; 
} 

 
 
 
?>
