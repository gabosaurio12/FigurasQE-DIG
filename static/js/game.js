/**
 * Actualiza las figuras visibles según el número de dedos detectados.
 * Puedes llamar a esta función desde tu código de reconocimiento:
 *   updateFingerCount(3)
 */
function updateFingerCount(count) {
  const circles = document.querySelectorAll(".figure-circle");
  const n = Math.max(0, Math.min(circles.length, Number(count) || 0));

  circles.forEach((circle, idx) => {
    if (idx < n) {
      circle.classList.add("active");
    } else {
      circle.classList.remove("active");
    }
  });
}

// Ejemplo de prueba manual desde consola:
// updateFingerCount(1), updateFingerCount(5), etc.


