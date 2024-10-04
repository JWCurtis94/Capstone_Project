let gameStarted = false;
let lightGreen = false;
let reactionTimeout;
let startTime;

// Function to start game
function startGame() {
    const light = document.getElementById("light");
    const reactionTimeDisplay = document.getElementById("reaction-time");
    const startButton = document.getElementById("start-btn");

    if (!gameStarted) {
        gameStarted = true;
        lightGreen = false;
        startButton.textContent = "Get Ready...";
        light.style.backgroundColor = "red";
        light.textContent = "Red";
        reactionTimeDisplay.textContent = "";

        const delay = Math.random() * 3000 + 2000;
        reactionTimeout = setTimeout(() => {
            lightGreen = true;
            light.style.backgroundColor = "green";
            light.textContent = "Go!";
            startTime = Date.now();
            startButton.textContent = "Click Now!";
        }, delay);

    } else if (gameStarted && lightGreen) {
        const reactionTime = Date.now() - startTime;
        reactionTimeDisplay.textContent = `Your reaction time: ${reactionTime} ms`;
        resetGame();

    } else if (gameStarted && !lightGreen) {
        reactionTimeDisplay.textContent = "Too early! Wait for the green light!";
        resetGame();
    }
}

// Function to restart game
function resetGame() {
    clearTimeout(reactionTimeout);
    gameStarted = false;
    lightGreen = false;

    const startButton = document.getElementById("start-btn");
    const light = document.getElementById("light");

    startButton.textContent = "Start Game";
    light.style.backgroundColor = "red";
    light.textContent = "Red";
}
