


// load tileset
var tilesetImage = new Image();
tilesetImage.src = '/static/tiles/tiles.png';
tilesetImage.onload = main;

// draw text
function drawText(targetCtx, text, x, y) {
  targetCtx.fillText(text, x, y);
}

// draw tile
function drawTile(targetCtx, tileX, tileY, canvasX, canvasY) {
  targetCtx.drawImage(tilesetImage, (16 * (tileX-1)), (16 * (tileY-1)), 16, 16, canvasX, canvasY, 16, 16);
}

// draw number
function drawNumber(targetCtx, number, x, y) {
  var numberCoords = [
    [1 , 21],
    [1 , 22],
    [2 , 22],
    [3 , 22],
    [1 , 23],
    [2 , 23],
    [3 , 23],
    [1 , 24],
    [2 , 24],
    [3 , 24]
  ];

  var numberCoord = numberCoords[number];
  drawTile(targetCtx, numberCoord[0], numberCoord[1], x, y);
}

// draw grass
function drawGrass(targetCtx, x, y) {
  drawTile(targetCtx, 1, 1, x, y);
}

// draw forest
function drawForest(targetCtx, x, y) {
  drawTile(targetCtx, 7, 1, x, y);
}

// draw flag
function drawFlag(targetCtx, x, y) {
  drawTile(targetCtx, 5, 22, x, y);
}

// draw service tower
function drawServiceTower(targetCtx, serviceId, serviceStatus, playerCityX, playerCityY) {

  var serviceIdLocOffsets = [
    [-16, 16],
    [-16, 0],
    [32, 0],
    [32, 16],
    [0, -16],
    [16, -16]
  ];

  var serviceLocOffsets = serviceIdLocOffsets[serviceId-1];
  var towerX = playerCityX + serviceLocOffsets[0];
  var towerY = playerCityY + serviceLocOffsets[1];



  if(serviceStatus != 'OFF') {
    // draw service buildings
    if(serviceId == 1) {
      drawTile(targetCtx, 2, 2, towerX, towerY)
    }
    if(serviceId == 2) {
      drawTile(targetCtx, 7, 7, towerX, towerY)
    }
    if(serviceId == 3) {
      drawTile(targetCtx, 5, 24, towerX, towerY)
    }
    if(serviceId == 4) {
      drawTile(targetCtx, 6, 3, towerX, towerY)
      drawTile(targetCtx, 7, 28, towerX, towerY)
    }
    if(serviceId == 5) {
      drawTile(targetCtx, 3, 6, towerX, towerY)
    }
    if(serviceId == 6) {
      drawTile(targetCtx, 7, 5, towerX, towerY)
    }
  }

  if(serviceStatus == 'CORRUPT') {
    drawTile(targetCtx, 1, 34, towerX, towerY)
  }

  drawNumber(targetCtx, serviceId, towerX, towerY);
}


// draw player city
function drawPlayerCity(targetCtx, playerName, x, y, isBlank) {

  //streets

  // service 5
  drawTile(targetCtx, 5, 10, x, y-32)
  drawTile(targetCtx, 4, 12, x, y-16)

  drawTile(targetCtx, 5, 11, x-16, y-32)
  drawTile(targetCtx, 5, 11, x-32, y-32)
  drawTile(targetCtx, 4, 11, x-48, y-32)
  drawTile(targetCtx, 4, 12, x-48, y-16)

  // service 6
  drawTile(targetCtx, 5, 10, x+16, y-32)
  drawTile(targetCtx, 4, 12, x+16, y-16)

  drawTile(targetCtx, 5, 11, x+32, y-32)
  drawTile(targetCtx, 5, 11, x+48, y-32)
  drawTile(targetCtx, 6, 11, x+64, y-32)
  drawTile(targetCtx, 4, 12, x+64, y-16)


  // service 2
  drawTile(targetCtx, 7, 12, x-48, y)
  drawTile(targetCtx, 5, 11, x-32, y)
  drawTile(targetCtx, 5, 11, x-16, y)

  // service 1
  drawTile(targetCtx, 7, 12, x-48, y+16)
  drawTile(targetCtx, 5, 11, x-32, y+16)
  drawTile(targetCtx, 5, 11, x-16, y+16)

  drawTile(targetCtx, 4, 12, x-48, y+32)
  drawTile(targetCtx, 4, 13, x-48, y+48)
  drawTile(targetCtx, 5, 11, x-32, y+48)
  drawTile(targetCtx, 5, 11, x-16, y+48)
  drawTile(targetCtx, 5, 11, x, y+48)

  // service 3
  drawTile(targetCtx, 7, 11, x+64, y)
  drawTile(targetCtx, 5, 11, x+48, y)
  drawTile(targetCtx, 5, 11, x+32, y)

  // service 4
  drawTile(targetCtx, 7, 11, x+64, y+16)
  drawTile(targetCtx, 5, 11, x+48, y+16)
  drawTile(targetCtx, 5, 11, x+32, y+16)

  drawTile(targetCtx, 4, 12, x+64, y+32)
  drawTile(targetCtx, 6, 13, x+64, y+48)
  drawTile(targetCtx, 5, 11, x+48, y+48)
  drawTile(targetCtx, 5, 11, x+32, y+48)
  drawTile(targetCtx, 6, 10, x+16, y+48)

  drawTile(targetCtx, 4, 12, x+16, y+32)
  drawTile(targetCtx, 4, 12, x+16, y+16)

  // decoration
  if(isBlank == false) {
    drawTile(targetCtx, 7, 4, x+32, y+32)
    drawTile(targetCtx, 5, 1, x+48, y+32)
    drawTile(targetCtx, 6, 3, x+32, y-16)
    drawTile(targetCtx, 7, 2, x+48, y-16)
    drawTile(targetCtx, 6, 1, x-16, y-16)
    drawTile(targetCtx, 4, 2, x-32, y-16)
    drawTile(targetCtx, 1, 6, x-16, y+32)
    drawTile(targetCtx, 6, 1, x-32, y+32)
    drawTile(targetCtx, 2, 1, x, y+32)
  }

  // city core
  drawTile(targetCtx, 1, 8, x, y);
  drawTile(targetCtx, 2, 8, x+16, y);
  drawTile(targetCtx, 1, 9, x, y+16);
  drawTile(targetCtx, 2, 9, x+16, y+16);

  if(isBlank == false) {


    // stats
    drawText(targetCtx, playerName + "'s City", x, y+36);
  }

}



// draw a knight

function drawKnight(targetCtx, knightName, x, y, hasFlag=false, number=0) {

  // draw knight tile
  drawTile(targetCtx, 4, 18, x, y);

  // draw knight flag
  if(hasFlag) {
    drawTile(targetCtx, 6, 22, x, y);
  }

  // draw knight service number
  if(number > 0) {
    drawNumber(targetCtx, number, x, y)
  }

  // draw knights name
  drawText(targetCtx, knightName, x, y);
}
