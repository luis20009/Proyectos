<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>
<body>
    <?php
    $Precio_inicial = 100.3457;
    $iva = 1.49;
    $Precio_total = $Precio_inicial * $iva;
    echo"<b>El precio inicial es:</b> ". $Precio_inicial. "<br>";
 echo "El valor 
 del iva es de: ". $iva,"%", "<br>";
 echo "El precio total seria de: ". $Precio_total."<br>";
 echo "El precio redondiado seria de ". round($Precio_total,2) ."<br>";
 $Resultado_dos = sprintf("%01.2f", $Precio_total);
 echo "Esta es otra forma de aproximar con la funcion sprinft: ". $Resultado_dos."<br>";
    ?>
</body>
</html>