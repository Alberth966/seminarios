import cv2
import numpy as np

# Cargar modelo
ruta_prototxt = "MobileNetSSD_deploy.prototxt"
ruta_modelo = "MobileNetSSD_deploy.caffemodel"
red = cv2.dnn.readNetFromCaffe(ruta_prototxt, ruta_modelo)

# Clases de objetos detectables en español
CLASES = ["fondo", "avión", "bicicleta", "pájaro", "bote",
          "botella", "autobús", "coche", "gato", "silla", "vaca", "mesa de comedor",
          "perro", "caballo", "motocicleta", "persona", "planta en maceta",
          "oveja", "sofá", "tren", "televisor"]

# Activar la cámara
captura = cv2.VideoCapture(0)

while True:
    ret, cuadro = captura.read()
    if not ret:
        break

    (alto, ancho) = cuadro.shape[:2]
    blob = cv2.dnn.blobFromImage(cuadro, 0.007843, (300, 300), 127.5)
    red.setInput(blob)
    detecciones = red.forward()

    for i in range(detecciones.shape[2]):
        confianza = detecciones[0, 0, i, 2]
        if confianza > 0.5:  # Umbral de confianza
            idx = int(detecciones[0, 0, i, 1])
            etiqueta = f"{CLASES[idx]}: {confianza * 100:.2f}%"
            caja = detecciones[0, 0, i, 3:7] * np.array([ancho, alto, ancho, alto])
            (inicioX, inicioY, finX, finY) = caja.astype("int")

            # Dibujar caja y etiqueta
            cv2.rectangle(cuadro, (inicioX, inicioY), (finX, finY), (0, 255, 0), 2)
            cv2.putText(cuadro, etiqueta, (inicioX, inicioY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Detección de Accesorios", cuadro)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura.release()
cv2.destroyAllWindows()

