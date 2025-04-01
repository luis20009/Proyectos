<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Juego de Preguntas ICFES</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Juego de Preguntas ICFES</h1>
    <form action="procesar.php" method="post">
        <?php
        include 'conexion.php';

        $sql = "SELECT * FROM preguntas ORDER BY RAND() LIMIT 1";
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
            while($row = $result->fetch_assoc()) {
                echo "<div id='pregunta'>" . $row["pregunta"] . "</div>";
                for ($i = 1; $i <= 4; $i++) {
                    echo "<input type='radio' name='respuesta' value='" . $i . "'> " . $row["opcion" . $i] . "<br>";
                }
                echo "<input type='hidden' name='correcta' value='" . $row["correcta"] . "'>";
            }
        } else {
            echo "0 resultados";
        }
        $conn->close();
        ?>
        <button type="submit">Enviar Respuesta</button>
    </form>
    <div id="resultado">
        <?php
        if (isset($_GET['resultado'])) {
            echo $_GET['resultado'];
        }
        ?>
    </div>
</body>
</html>
