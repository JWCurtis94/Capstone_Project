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
        // User clicked when the light is green, calculate reaction time
        const reactionTime = Date.now() - startTime;
        reactionTimeDisplay.textContent = `Your reaction time: ${reactionTime} ms`;
        resetGame();
    } else if (gameStarted && !lightGreen) {
        // User clicked too early
        reactionTimeDisplay.textContent = "Too early! Wait for the green light!";
        resetGame();
    }
}

function resetGame() {
    clearTimeout(reactionTimeout);
    gameStarted = false;
    lightGreen = false;

    const startButton = document.getElementById("start-btn");
    const light = document.getElementById("light");

    startButton.textContent = "Start Game";  // Reset button text
    light.style.backgroundColor = "red";  // Reset light to red
    light.textContent = "Red";  // Reset light text to "Red"
}
