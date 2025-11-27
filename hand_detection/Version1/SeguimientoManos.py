import math
import cv2
import mediapipe as mp
import time

class detectormanos:
    def __init__(self, mode=False, maxManos=20, Confdeteccion=0.5, Confsegui=0.5):
        """
        Inicializa el detector de manos.
        mode -> Si es True, procesa imágenes estáticas
        maxManos -> Número máximo de manos a detectar
        Confdeteccion -> Confianza mínima para detección
        Confsegui -> Confianza mínima para seguimiento
        """
        self.mode = mode
        self.maxManos = maxManos
        self.Confdeteccion = Confdeteccion
        self.Confsegui = Confsegui

        # Detector y dibujador de manos de MediaPipe
        self.mpmanos = mp.solutions.hands
        self.manos = self.mpmanos.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxManos,
            min_detection_confidence=self.Confdeteccion,
            min_tracking_confidence=self.Confsegui
        )
        self.dibujo = mp.solutions.drawing_utils
        self.tip = [4, 8, 12, 16, 20]  # Puntas de los dedos

    def encontrarmanos(self, frame, dibujar=True):
        """Detecta manos en el frame."""
        imgcolor = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.resultados = self.manos.process(imgcolor)

        if self.resultados.multi_hand_landmarks:
            for mano in self.resultados.multi_hand_landmarks:
                if dibujar:
                    self.dibujo.draw_landmarks(
                        frame, mano, self.mpmanos.HAND_CONNECTIONS
                    )
        return frame

    def encontrarposicion(self, frame, ManoNum=0, dibujar=True):
        """
        Devuelve la lista de posiciones (id, x, y) de la mano detectada.
        También puede dibujar los puntos y el rectángulo delimitador.
        """
        xlista = []
        ylista = []
        bbox = []
        self.lista = []

        if self.resultados.multi_hand_landmarks:
            miMano = self.resultados.multi_hand_landmarks[ManoNum]
            for id, lm in enumerate(miMano.landmark):
                alto, ancho, c = frame.shape
                cx, cy = int(lm.x * ancho), int(lm.y * alto)
                xlista.append(cx)
                ylista.append(cy)
                self.lista.append([id, cx, cy])
                if dibujar:
                    cv2.circle(frame, (cx, cy), 5, (0, 0, 0), cv2.FILLED)

            xmin, xmax = min(xlista), max(xlista)
            ymin, ymax = min(ylista), max(ylista)
            bbox = xmin, ymin, xmax, ymax

            if dibujar:
                cv2.rectangle(
                    frame,
                    (xmin - 20, ymin - 20),
                    (xmax + 20, ymax + 20),
                    (0, 255, 0),
                    2,
                )

        return self.lista, bbox

    def dedosarriba(self):
        """Devuelve una lista indicando qué dedos están levantados."""
        dedos = []

        # Pulgar
        if self.lista[self.tip[0]][1] > self.lista[self.tip[0] - 1][1]:
            dedos.append(1)
        else:
            dedos.append(0)

        # Resto de dedos
        for id in range(1, 5):
            if self.lista[self.tip[id]][2] < self.lista[self.tip[id] - 2][2]:
                dedos.append(1)
            else:
                dedos.append(0)

        return dedos

    def distancia(self, p1, p2, frame, dibujar=True, r=15, t=3):
        """
        Calcula la distancia entre dos puntos (p1, p2) de la mano.
        Devuelve (distancia, frame, [x1, y1, x2, y2, cx, cy])
        """
        x1, y1 = self.lista[p1][1:]
        x2, y2 = self.lista[p2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if dibujar:
            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), t)
            cv2.circle(frame, (x1, y1), r, (0, 0, 255), cv2.FILLED)
            cv2.circle(frame, (x2, y2), r, (0, 0, 255), cv2.FILLED)
            cv2.circle(frame, (cx, cy), r, (0, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        return length, frame, [x1, y1, x2, y2, cx, cy]


# Ejecutar el detector directamente para prueba rápida
def main():
    ptiempo = 0
    cap = cv2.VideoCapture(0)
    detector = detectormanos()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = detector.encontrarmanos(frame)
        lista, bbox = detector.encontrarposicion(frame)

        # FPS
        ctiempo = time.time()
        fps = 1 / (ctiempo - ptiempo) if ctiempo != ptiempo else 0
        ptiempo = ctiempo

        cv2.putText(
            frame, f"FPS: {int(fps)}", (10, 70),
            cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3
        )

        cv2.imshow("Seguimiento de Manos", frame)
        if cv2.waitKey(1) == 27:  # ESC para salir
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
