

playerMapCoords = {};

function searchPlayer(player) {

  if(player in playerMapCoords){

    var searchX = playerMapCoords[player].x * -1;
    var searchY = playerMapCoords[player].y * -1;

    searchX -= 200;
    searchY -= 600;

    $('#mapCanvas').css('margin-left', searchX);
    $('#mapCanvas').css('margin-top', searchY);
    $('#knightsCanvas').css('margin-left', searchX);
    $('#knightsCanvas').css('margin-top', searchY);
  }

}


// draw map
function drawMap() {

  // clear map
  mapCtx.clearRect(0, 0, mapCanvas.width, mapCanvas.height);

  // draw grass on the map
  for (y = 0; y < mapCanvas.height; y += 16) {
    for (x = 0; x < mapCanvas.width; x += 16) {
      drawGrass(mapCtx, x, y);
    }
  }

  var squareCounter = 1;
  var currentX = 1;
  var currentY = 1;


  $.getJSON('/get_visualization', function(data) {


    var players = data.players;

    players.forEach(function(player) {

      var playerX =  (128 * currentX) - 70;
      var playerY = (96 * currentY) - 50;

      // drawPlayerCity(mapCtx, playerName, playerX,  playerY, players[playerName]['serviceStats'], false);
      playerMapCoords[player.name] = {'x' : playerX, 'y' : playerY};
      drawPlayerCity(mapCtx, player.name, playerX,  playerY, false);

      player.services.forEach(function(playerService) {
        drawServiceTower(mapCtx, playerService.id, playerService.status, playerX, playerY)
      });

      // update squareCounter
      if ((currentX == 1) && (currentY == 1)) {
        squareCounter = 2;
        currentX = 2;
      }
      else if((currentX == squareCounter) && (currentY != squareCounter)) {
        currentY += 1;
      }
      else if ((currentX == 1) && (currentY == squareCounter)) {
        squareCounter += 1;
        currentX = squareCounter;
        currentY = 1;
      }
      else if ((currentX > 1) && (currentY == squareCounter)) {
        currentX -= 1;
      }

    });


    // draw blank cities 1
    if(currentX == squareCounter) {
      for(var blankY = currentY; blankY < squareCounter+1; blankY++) {
        var playerX =  (128 * currentX) - 70;
        var playerY = (96 * blankY) - 50;
        drawPlayerCity(mapCtx, '', playerX,  playerY, true);
      }

      currentY = squareCounter;
    }

    // draw blank cities 2
    if(currentY == squareCounter) {
      for(var blankX = currentX; blankX > 0; blankX--) {
        var playerX =  (128 * blankX) - 70;
        var playerY = (96 * currentY) - 50;
        drawPlayerCity(mapCtx, '', playerX,  playerY, true);
      }
    }


    for(var y=1;y<squareCounter+1;y++){
      for(var x=1;x<squareCounter+1;x++) {

          var playerX =  (128 * x) - 70;
          var playerY = (96 * y) - 50;

          // street connections up
          if(y > 1) {
            drawTile(mapCtx, 5, 10, playerX, playerY-48)
            drawTile(mapCtx, 5, 12, playerX, playerY-32)
            drawTile(mapCtx, 5, 12, playerX+16, playerY-48)
            drawTile(mapCtx, 5, 12, playerX+16, playerY-32)
          }


          // street connections left
          if(x > 1) {
            drawTile(mapCtx, 5, 12, playerX-48, playerY)
            drawTile(mapCtx, 5, 12, playerX-64, playerY)
            drawTile(mapCtx, 5, 12, playerX-48, playerY+16)
            drawTile(mapCtx, 5, 12, playerX-64, playerY+16)
          }
        }
      }

  });
}


var knights = [];


function updateKnights() {
  $.getJSON('/get_visualization', function(data) {

    var victims = data.players;

    victims.forEach(function(victim) {

      var victimServices = victim.services;

      victimServices.forEach(function(victimService) {

        var attackers = victimService.attacked_by;

        attackers.forEach(function(attacker) {

          if(victim.name in playerMapCoords){

            var attackerX = playerMapCoords[attacker].x;
            var attackerY = playerMapCoords[attacker].y;

            var victimX = playerMapCoords[victim.name].x;
            var victimY = playerMapCoords[victim.name].y;

            victimX += 16;
            victimY += 48;

            var attack_path = [
              [attackerX+16, attackerY+16],
              [attackerX+16, attackerY+32],
              [attackerX+16, attackerY+48]
            ];
            attackerX += 16;
            attackerY += 48;

            while((attackerX != victimX) || (attackerY != victimY)) {

              if((Math.floor(Math.random()*2) ) == 0) {
                if(attackerX < victimX) {
                  // right
                  attack_path.push([attackerX+16, attackerY]);
                  attack_path.push([attackerX+32, attackerY]);
                  attack_path.push([attackerX+48, attackerY]);
                  attack_path.push([attackerX+48, attackerY-16]);
                  attack_path.push([attackerX+48, attackerY-32]);
                  attack_path.push([attackerX+64, attackerY-32]);
                  attack_path.push([attackerX+64, attackerY-16]);
                  attack_path.push([attackerX+64, attackerY]);
                  attack_path.push([attackerX+80, attackerY]);
                  attack_path.push([attackerX+96, attackerY]);
                  attack_path.push([attackerX+112, attackerY]);
                  attack_path.push([attackerX+128, attackerY]);
                  attackerX = attackerX+128;
                }
                else if(attackerX > victimX) {
                  // left
                  attack_path.push([attackerX-16, attackerY]);
                  attack_path.push([attackerX-32, attackerY]);
                  attack_path.push([attackerX-48, attackerY]);
                  attack_path.push([attackerX-64, attackerY]);
                  attack_path.push([attackerX-64, attackerY-16]);
                  attack_path.push([attackerX-64, attackerY-32]);
                  attack_path.push([attackerX-80, attackerY-32]);
                  attack_path.push([attackerX-80, attackerY-16]);
                  attack_path.push([attackerX-80, attackerY]);
                  attack_path.push([attackerX-96, attackerY]);
                  attack_path.push([attackerX-112, attackerY]);
                  attack_path.push([attackerX-128, attackerY]);
                  attackerX = attackerX-128;
                }
              }
              else {



                if(attackerY < victimY) {
                  // down
                  attack_path.push([attackerX, attackerY+16]);
                  attack_path.push([attackerX+16, attackerY+16]);
                  attack_path.push([attackerX+32, attackerY+16]);
                  attack_path.push([attackerX+48, attackerY+16]);
                  attack_path.push([attackerX+48, attackerY+32]);
                  attack_path.push([attackerX+48, attackerY+48]);
                  attack_path.push([attackerX+48, attackerY+64]);
                  attack_path.push([attackerX+48, attackerY+80]);
                  attack_path.push([attackerX+48, attackerY+96]);
                  attack_path.push([attackerX+32, attackerY+96]);
                  attack_path.push([attackerX+16, attackerY+96]);
                  attack_path.push([attackerX, attackerY+96]);
                  attackerY = attackerY+96;
                }
                else if(attackerY > victimY) {

                  // up
                  attack_path.push([attackerX-16, attackerY]);
                  attack_path.push([attackerX-32, attackerY]);
                  attack_path.push([attackerX-48, attackerY]);
                  attack_path.push([attackerX-64, attackerY]);
                  attack_path.push([attackerX-64, attackerY-16]);
                  attack_path.push([attackerX-64, attackerY-32]);
                  attack_path.push([attackerX-64, attackerY-48]);
                  attack_path.push([attackerX-64, attackerY-64]);
                  attack_path.push([attackerX-64, attackerY-80]);
                  attack_path.push([attackerX-48, attackerY-80]);
                  attack_path.push([attackerX-32, attackerY-80]);
                  attack_path.push([attackerX-16, attackerY-80]);
                  attack_path.push([attackerX, attackerY-80]);
                  attack_path.push([attackerX, attackerY-96]);
                  attackerY = attackerY-96;
                }
              }

            }



            if(victimService.id == 1){
              attack_path.push([attackerX-16, attackerY]);
              attack_path.push([attackerX-32, attackerY]);
              attack_path.push([attackerX-48, attackerY]);
              attack_path.push([attackerX-64, attackerY]);
              attack_path.push([attackerX-64, attackerY-16]);
              attack_path.push([attackerX-64, attackerY-32]);
              attack_path.push([attackerX-48, attackerY-32]);
              attack_path.push([attackerX-32, attackerY-32]);
            }
            else if(victimService.id == 2){
              attack_path.push([attackerX-16, attackerY]);
              attack_path.push([attackerX-32, attackerY]);
              attack_path.push([attackerX-48, attackerY]);
              attack_path.push([attackerX-64, attackerY]);
              attack_path.push([attackerX-64, attackerY-16]);
              attack_path.push([attackerX-64, attackerY-32]);
              attack_path.push([attackerX-64, attackerY-48]);
              attack_path.push([attackerX-48, attackerY-48]);
              attack_path.push([attackerX-32, attackerY-48]);
            }
            else if(victimService.id == 3){
              attack_path.push([attackerX+16, attackerY]);
              attack_path.push([attackerX+32, attackerY]);
              attack_path.push([attackerX+48, attackerY]);
              attack_path.push([attackerX+48, attackerY-16]);
              attack_path.push([attackerX+48, attackerY-32]);
              attack_path.push([attackerX+48, attackerY-48]);
              attack_path.push([attackerX+32, attackerY-48]);
              attack_path.push([attackerX+16, attackerY-48]);
            }
            else if(victimService.id == 4){
              attack_path.push([attackerX+16, attackerY]);
              attack_path.push([attackerX+32, attackerY]);
              attack_path.push([attackerX+48, attackerY]);
              attack_path.push([attackerX+48, attackerY-16]);
              attack_path.push([attackerX+48, attackerY-32]);
              attack_path.push([attackerX+32, attackerY-32]);
              attack_path.push([attackerX+16, attackerY-32]);
            }
            else if(victimService.id == 5){
              attack_path.push([attackerX-16, attackerY]);
              attack_path.push([attackerX-32, attackerY]);
              attack_path.push([attackerX-48, attackerY]);
              attack_path.push([attackerX-64, attackerY]);
              attack_path.push([attackerX-64, attackerY-16]);
              attack_path.push([attackerX-64, attackerY-32]);
              attack_path.push([attackerX-64, attackerY-48]);
              attack_path.push([attackerX-64, attackerY-64]);
              attack_path.push([attackerX-64, attackerY-80]);
              attack_path.push([attackerX-48, attackerY-80]);
              attack_path.push([attackerX-32, attackerY-80]);
              attack_path.push([attackerX-16, attackerY-80]);
            }
            else if(victimService.id == 6){
              attack_path.push([attackerX+16, attackerY]);
              attack_path.push([attackerX+32, attackerY]);
              attack_path.push([attackerX+48, attackerY]);
              attack_path.push([attackerX+48, attackerY-16]);
              attack_path.push([attackerX+48, attackerY-32]);
              attack_path.push([attackerX+48, attackerY-48]);
              attack_path.push([attackerX+48, attackerY-64]);
              attack_path.push([attackerX+48, attackerY-80]);
              attack_path.push([attackerX+32, attackerY-80]);
              attack_path.push([attackerX+16, attackerY-80]);
              attack_path.push([attackerX, attackerY-80]);
            }


            knights.push({
                  'from' : attacker,
                  'to' : victim.name,
                  'serviceId' : victimService.id,
                  'path' : attack_path,
                  'pathCounter' : 0,
                  'dir' : 0
            });
          }
        });
      });
    });
  });

}


function drawKnights() {


  // clear knights
  knightsCtx.clearRect(0, 0, knightsCanvas.width, knightsCanvas.height);


  knights.forEach(function(knight) {

    var currentPath = knight['path'];
    var hasFlag = false;

    if(knight['dir'] == 1) {
      hasFlag = true;
      knight['pathCounter'] -= 1;
    }
    else {
      knight['pathCounter'] += 1;
    }

    if(knight['pathCounter'] > (currentPath.length-2)) {
      knight['dir'] = 1;
    }

    if(knight['pathCounter'] < 2) {
      knight['dir'] = 0;
    }

    var currLoc = currentPath[knight['pathCounter']];

    drawKnight(knightsCtx, (knight['from'] + ' > ' + knight['to']), currLoc[0], currLoc[1], hasFlag, knight['serviceId']);
  });

}


// main method
function main() {

  drawMap();
  //setInterval(function() { drawMap(); }, 60000);

  updateKnights();
  //setInterval(function() { updateKnights(); }, 60000);
  setInterval(function() { drawKnights(); }, 200);
}
