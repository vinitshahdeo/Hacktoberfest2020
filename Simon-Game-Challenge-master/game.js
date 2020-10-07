var buttonColours = ["red", "blue", "green", "yellow"];

var userClickedPattern = [];
var gamePattern = [];

var level = 0;

var started = false;

$(document).keypress(function() {
    
    if(!started)
    {
        $("#level-title").text("Level " + level);
        nextSequence();
        started = true;
    }
});

function checkAnswer(currentLevel)
{
    if(gamePattern[currentLevel] === userClickedPattern[currentLevel])
    {
        if(userClickedPattern.length === gamePattern.length)
        {
            setTimeout(function() {
                nextSequence();
            },1000);
        }
    }
    else
    {
        playSound("wrong");
        $("body").addClass("game-over");
        $("#level-title").text("Game Over, Press Any Key to Restart");

        setTimeout(function () {
            $("body").removeClass("game-over");
        },200);

        startOver();
    }
}
function nextSequence()
{
    userClickedPattern = [];
    level++;
    $("#level-title").text("Level " + level);
    
    var randomNumber = Math.floor(Math.random() * 4);
    var randomChosenColour = buttonColours[randomNumber];
    
    gamePattern.push(randomChosenColour);
    
    $("#" + randomChosenColour).fadeIn(100).fadeOut(100).fadeIn(100);   
    playSound(randomChosenColour);
}

$(".btn").click(function() {
    var userChosenColor = $(this).attr("id");
    userClickedPattern.push(userChosenColor);
    
    playSound(userChosenColor);
    animatePress(userChosenColor);

    checkAnswer(userClickedPattern.length-1);
});

function playSound(name)
{
    var audio = new Audio("sounds/" + name + ".mp3");
    audio.play();
}

function animatePress(currentColor)
{
    $("#" + currentColor).addClass("pressed");
    setTimeout(function() {
    $("#" + currentColor).removeClass("pressed")
    },100);
}

function startOver()
{
    level = 0;
    gamePattern = [];
    started = false;
}