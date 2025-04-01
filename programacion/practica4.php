<!DOCTYPE html>
<html>
<head>
  <?php
  $Manzanas = 5;
  $COOKIE = 6;
  $GUallaba = 3;
  $Producto = array($Manzanas, $COOKIE, $GUallaba);  
  $Producto_1 = $Producto[rand(0, 2)];
  $Producto_2 = $Producto[rand(0, 2)];
  echo $Factura = $Producto_1 + $Producto_2, "<br>";
  
  do {
    if ($Factura >= 50) {
      echo "Pe causa, toma un descuento por ser muy pro jiji \n", "<br>";
      $Factura2 = $Factura - 2;
      echo $Factura2, "<br>";
      break;
    } else {
      $Factura += 1;
    }
  } while (true);
  ?>
</head>
<body>
    
</body>
</html>
