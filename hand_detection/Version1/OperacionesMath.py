import cv2
import SeguimientoManos as sm

detector = sm.detectormanos(Confdeteccion=0.785)
cap = cv2.VideoCapture(0)

d1 = 0
d2 = 0
r = 0
cx = 65
cy = 420
comp = 0
res = 0
t = 0  # Inicializamos t

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = detector.encontrarmanos(frame)

    # Rectángulo para contar dedos
    cv2.rectangle(frame, (50, 50), (130, 150), (0, 0, 0), cv2.FILLED)

    # Rectángulo para 1er dígito
    cv2.rectangle(frame, (50, 350), (130, 450), (0, 0, 0), cv2.FILLED)

    # Rectángulo para 2do dígito
    cv2.rectangle(frame, (250, 350), (330, 450), (0, 0, 0), cv2.FILLED)

    # Resultado
    cv2.rectangle(frame, (450, 350), (600, 450), (0, 0, 0), cv2.FILLED)

    # Etiquetas
    cv2.putText(frame, "Dedos", (52, 145), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
    cv2.putText(frame, "Digito 1", (45, 445), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
    cv2.putText(frame, "Digito 2", (245, 445), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
    cv2.putText(frame, "Resultado", (465, 445), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

    manosInfo, cuadro = detector.encontrarposicion(frame, dibujar=False)

    if len(manosInfo) != 0:
        dedos = detector.dedosarriba()
        contar = dedos.count(1)
        cv2.putText(frame, str(contar), (65, 125), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 10)

        # Teclas
        if t == 83 or t == 115:  # 'S' o 's'
            comp = 1
            d1 = contar

        # Mostrar suma
        if comp == 1:
            cv2.putText(frame, str(d1), (65, 420), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 10)
            cv2.putText(frame, "+", (165, cy), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 10)

        if t == 32:  # Espacio
            d2 = contar
            res = 1

        # Mostrar resultado
        if comp == 1 and res == 1:
            cv2.putText(frame, str(d2), (265, 420), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 10)
            cv2.putText(frame, "=", (365, cy), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 10)
            r = d1 + d2
            cv2.putText(frame, str(r), (495, 420), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 10)

        # Resetear
        if t == 67 or t == 99:  # 'C' o 'c'
            d1 = 0
            d2 = 0
            r = 0
            comp = 0
            res = 0

    # Mostrar ventana
    cv2.imshow("Contando Dedos", frame)

    t = cv2.waitKey(1)
    if t == 27:  # ESC para salir
        break

cap.release()
cv2.destroyAllWindows()
