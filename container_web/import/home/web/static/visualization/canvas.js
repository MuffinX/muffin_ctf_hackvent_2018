

// disables antialiasing for canvas context
function disableAntiAliasing(ctx) {
  ctx['imageSmoothingEnabled'] = false;       /* standard */
  ctx['mozImageSmoothingEnabled'] = false;    /* Firefox */
  ctx['oImageSmoothingEnabled'] = false;      /* Opera */
  ctx['webkitImageSmoothingEnabled'] = false; /* Safari */
  ctx['msImageSmoothingEnabled'] = false;     /* IE */
}

//initializies CTX for canvas
function initCtx(canvas) {
  canvas.width = 4000;
  canvas.height = 4000;

  var ctx = canvas.getContext('2d');
  disableAntiAliasing(ctx);
  ctx.scale(3, 3);
  ctx.font = "3px PressStart";

  return ctx;
}

// canvas for map
var mapCanvas = document.getElementById('mapCanvas');
var mapCtx = initCtx(mapCanvas);

// canvas for knights
var knightsCanvas = document.getElementById('knightsCanvas');
var knightsCtx = initCtx(knightsCanvas);
