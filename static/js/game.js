const videoElement = document.getElementById("camera");

const hands = new Hands({
  locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`,
});

hands.setOptions({
  maxNumHands: 1,
  modelComplexity: 1,
  minDetectionConfidence: 0.5,
  minTrackingConfidence: 0.5,
});

hands.onResults(onResults);

const camera = new Camera(videoElement, {
  onFrame: async () => {
    await hands.send({ image: videoElement });
  },
  width: 640,
  height: 480,
});

camera.start();

function onResults(results) {
  updateFingerCount(0);
  if (!results.multiHandLandmarks || results.multiHandLandmarks.length === 0) {
    return;
  }

  const lm = results.multiHandLandmarks[0];

  let fingers = 0;

  if (lm[4].x < lm[3].x) fingers++;

  // Índice
  if (lm[8].y < lm[6].y) fingers++;

  // Medio
  if (lm[12].y < lm[10].y) fingers++;

  // Anular
  if (lm[16].y < lm[14].y) fingers++;

  // Meñique
  if (lm[20].y < lm[18].y) fingers++;

  updateFingerCount(fingers);
}


function updateFingerCount(count) {
  console.log("Dedos detectados: ", count);
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