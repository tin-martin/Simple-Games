class Ball{
    constructor(X, Y){
        this.X = X;
        this.Y = Y;
        this.radius = 8;
        this.angle = Math.floor(Math.random()*40)-20;
        this.velX = 1*3;
        this.velY = Math.tan(this.angle)*3;
        this.acceleration = 1.02;
        this.recipient = Paddle2;
    }
    draw(){
        ctx.beginPath();
        ctx.fillStyle = "white";
        ctx.arc(this.X, this.Y, this.radius, 0, 2 * Math.PI);
        ctx.fill();
    }

    move(){
        this.X += this.velX;
        this.Y += this.velY;
    }
}

class Paddle{
    constructor(X, Y){
        this.X = X;
        this.Y = Y;
        this.height = 50;
        this.width = 8;
        this.vel = 8;
        this.score = 0;
    }
    moveDown(){
        if(! (this.Y+this.height > HEIGHT) ){
            this.Y += this.vel;
        }
    }
    moveUp(){

        if (! (this.Y < 0) ){
            this.Y -= this.vel;
        }
    }
    draw(){
        ctx.fillStyle = "white";
        ctx.fillRect(this.X,this.Y,this.width,this.height);
    }
}

function clearCanvas(){
    ctx.fillStyle = "black";
    ctx.fillRect(0,0,WIDTH,HEIGHT);
    ctx.fillStyle = "white";
    
    ctx.lineWidth = 10;
    ctx.setLineDash([7,5]);
    ctx.beginPath();
    ctx.moveTo(WIDTH/2,0);
    ctx.lineTo(WIDTH/2,HEIGHT);
    ctx.stroke();

    ctx.strokeStyle = "white";
    ctx.font = "50px Fira Code";
    ctx.textAlign = "right";
    ctx.fillText(Paddle1.score,WIDTH/2-50,70);

    ctx.textAlign = "left";
    ctx.fillText(Paddle2.score,WIDTH/2+50,70);
}

function gameOver(winner){
    clearCanvas();
    ctx.strokeStyle = "white";
    ctx.font = "70px Fira Code";
    ctx.textAlign = "center";
    ctx.fillText("GAMEOVER!",250,250);


}
function checkOutOfBounds(){
    var outOfBounds = 0;
    if(Ball1.X < -Ball1.radius){
        Paddle2.score += 1;
        Ball1.X = WIDTH/2;
        Ball1.Y = HEIGHT/2;
        Ball1.angle = Math.floor(Math.random()*40)-20;
        Ball1.velX = 1*3;
        Ball1.velY = Math.tan(Ball1.angle)*3;
        Ball1.recipient = Paddle1;
        return true;
    }else if(Ball1.X > WIDTH+Ball1.radius){
        Paddle1.score += 1;
        Ball1.X = WIDTH/2;
        Ball1.Y = HEIGHT/2;
        Ball1.angle = Math.floor(Math.random()*40)-20;
        Ball1.velX = 1*3;
        Ball1.velY = -Math.tan(Ball1.angle)*3;
        Ball1.recipient = Paddle2;
        return true;  
    }
    return false;
    
}

function checkCollisions(){
    if(Ball1.X-Ball1.radius <= (Paddle1.X + Paddle1.width) && Ball1.X+Ball1.radius >= Paddle1.X && Ball1.Y+Ball1.radius >= Paddle1.Y && Ball1.Y-Ball1.radius <= (Paddle1.Y + Paddle1.height)  && Ball1.recipient == Paddle1    ){
        

        Ball1.velX *=-1;
        
    

        Ball1.recipient = Paddle2;
        Ball1.X *= Ball1.acceleration;
        Ball1.Y *= Ball1.acceleration;
    }else if( Ball1.X-Ball1.radius <= (Paddle2.X + Paddle2.width) && Ball1.X+Ball1.radius >= Paddle2.X  &&  Ball1.Y+Ball1.radius >= Paddle2.Y && Ball1.Y-Ball1.radius <= (Paddle2.Y + Paddle2.height) && Ball1.recipient == Paddle2){
        Ball1.velX *= -1;
        Ball1.recipient = Paddle1;
        Ball1.X *= Ball1.acceleration;
        Ball1.Y *= Ball1.acceleration;
        //Ball1.velX = -speed;
       // Ball1.velY = Math.tan(angle)*speed;
    }else if(Ball1.Y-Ball1.radius <= 0 || (Ball1.Y+Ball1.radius) >= HEIGHT){
        Ball1.velY = -Ball1.velY;
    }
}

var c;
var ctx;
var Paddle1;
var Paddle2;
var Ball1;
var HEIGHT;
var WIDTH;
var controller;

function init(){
    c = document.getElementById('myCanvas');
    ctx = c.getContext('2d');

    HEIGHT = c.height; 
    WIDTH = c.width;

    Paddle1 = new Paddle(50,HEIGHT/2-25);
    Paddle2 = new Paddle(450,HEIGHT/2-25);
    Ball1 = new Ball(250,250);

    controller = {
        38: {pressed: false, paddle: 2, direction: "up"},
        40: {pressed: false, paddle: 2, direction: "down"},
        87: {pressed: false, paddle: 1, direction: "up"},
        83: {pressed: false, paddle: 1, direction: "down"},
    }
    

    window.requestAnimationFrame(gameLoop);
}

function executeMoves(){
    Object.keys(controller).forEach(key => {
        if(controller[key].pressed){
            if(controller[key].paddle == 1){
                if(controller[key].direction == "up"){
                    Paddle1.moveUp();
                }else{
                    Paddle1.moveDown();
                }
            }else{
                if(controller[key].direction == "up"){
                    Paddle2.moveUp();
                }else{
                    Paddle2.moveDown();
                }

            }
        } 
    })
}

document.addEventListener('keydown', (e) => {
    if(controller[e.keyCode]){
        controller[e.keyCode].pressed = true;
    }
});
document.addEventListener('keyup', (e) => {
    if(controller[e.keyCode]){
        controller[e.keyCode].pressed = false;
    }
});

function gameLoop(){
    //Paddle1
    executeMoves();
    clearCanvas();

     

    if(!checkOutOfBounds()){
        checkCollisions();
    }else{
        if(Paddle1.score == 11){
            gameOver(1);
            
            return;
        }else if(Paddle2.score == 11){
            gameOver(2);
            return;
        }
    }

    Paddle1.draw();
    Paddle2.draw(); 
    
    Ball1.move();
    Ball1.draw();
    
    window.requestAnimationFrame(gameLoop);
}

window.onload = init;
