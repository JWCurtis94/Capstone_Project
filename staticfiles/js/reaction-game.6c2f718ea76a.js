let gameStarted = false;
let lightGreen = false;
let reactionTimeout;
let startTime;

function startGame() {
    const light = document.getElementById("light");
    const reactionTimeDisplay = document.getElementById("reaction-time");
    const startButton = document.getElementById("start-btn");

    if (!gameStarted) {
        // Start game: reset all previous states
        gameStarted = true;
        lightGreen = false;
        startButton.textContent = "Get Ready...";
        light.style.backgroundColor = "red";
        light.textContent = "Red";
        reactionTimeDisplay.textContent = "";

        const delay = Math.random() * 3000 + 2000;  // Random delay between 2-5 seconds
        reactionTimeout = setTimeout(() => {
            lightGreen = true;
            light.style.backgroundColor = "green";
            light.textContent = "Go!";
            startTime = Date.now();
            startButton.textContent = "Click Now!";
        }, delay);

    } else if (gameStarted && lightGreen) {
        // Calculate reaction time if button is pressed when light is green
        const reactionTime = Date.now() - startTime;
        reactionTimeDisplay.textContent = `Your reaction time: ${reactionTime} ms`;
        resetGame();
    } else {
        // User pressed too early
        reactionTimeDisplay.textContent = "Too early!";
        resetGame();
    }
}

function resetGame() {
    clearTimeout(reactionTimeout);
    gameStarted = false;
    lightGreen = false;
    const startButton = document.getElementById("start-btn");
    startButton.textContent = "Start Game";
}
