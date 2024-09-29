let startTime;
let reactionTimeout;

function startGame() {
    document.getElementById('reaction-time').textContent = '';
    document.getElementById('start-btn').disabled = true;
    document.getElementById('light').style.backgroundColor = 'red';
    document.getElementById('light').textContent = 'Red';

    // Random delay before the light turns green
    const delay = Math.floor(Math.random() * 5000) + 2000; // Between 2 to 7 seconds

    reactionTimeout = setTimeout(() => {
        document.getElementById('light').style.backgroundColor = 'green';
        document.getElementById('light').textContent = 'Green';
        startTime = Date.now();
        document.body.onclick = recordReaction;
    }, delay);
}

function recordReaction() {
    if (document.getElementById('light').style.backgroundColor === 'green') {
        const reactionTime = Date.now() - startTime;
        document.getElementById('reaction-time').textContent = `Your reaction time: ${reactionTime} ms`;
    } else {
        document.getElementById('reaction-time').textContent = `Too early! Wait for green!`;
    }
    resetGame();
}

function resetGame() {
    document.body.onclick = null; // Remove the click handler
    document.getElementById('start-btn').disabled = false;
    clearTimeout(reactionTimeout);
}