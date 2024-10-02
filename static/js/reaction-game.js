// Variables to track game state and timing
let gameStarted = false;
let lightGreen = false;
let reactionTimeout;
let startTime;

// Function to start or process the reaction game
function startGame() {
    // Get references to the light, reaction time display, and start button elements
    const light = document.getElementById("light");
    const reactionTimeDisplay = document.getElementById("reaction-time");
    const startButton = document.getElementById("start-btn");

    // If the game has not started yet
    if (!gameStarted) {
        // Reset game state and update button and light for pre-game state
        gameStarted = true;
        lightGreen = false;
        startButton.textContent = "Get Ready...";
        light.style.backgroundColor = "red";
        light.textContent = "Red";
        reactionTimeDisplay.textContent = "";

        // Set a random delay between 2 and 5 seconds before the light turns green
        const delay = Math.random() * 3000 + 2000;
        reactionTimeout = setTimeout(() => {
            // Light turns green after the random delay
            lightGreen = true;
            light.style.backgroundColor = "green";
            light.textContent = "Go!";
            startTime = Date.now();  // Record the time when the light turns green
            startButton.textContent = "Click Now!";
        }, delay);

    // If the game is in progress and the light is green
    } else if (gameStarted && lightGreen) {
        // Calculate reaction time and display it
        const reactionTime = Date.now() - startTime;
        reactionTimeDisplay.textContent = `Your reaction time: ${reactionTime} ms`;
        resetGame();  // Reset the game after displaying the result

    // If the game is in progress and the user clicks too early
    } else if (gameStarted && !lightGreen) {
        // Display "too early" message and reset the game
        reactionTimeDisplay.textContent = "Too early! Wait for the green light!";
        resetGame();
    }
}

// Function to reset the game state
function resetGame() {
    // Clear the timeout for light change in case the game is reset early
    clearTimeout(reactionTimeout);

    // Reset game state variables
    gameStarted = false;
    lightGreen = false;

    // Reset the button and light elements to their initial states
    const startButton = document.getElementById("start-btn");
    const light = document.getElementById("light");

    startButton.textContent = "Start Game";
    light.style.backgroundColor = "red";
    light.textContent = "Red";
}