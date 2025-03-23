// script.js
document.getElementById('userText').addEventListener('input', function() {
    const mood = getMood(this.value); // A function to process the mood dynamically
    document.getElementById('moodSuggestion').innerText = `Your mood seems to be: ${mood}`;
});

function getMood(inputText) {
    // Placeholder for mood prediction logic (could call an API or use a local function)
    if (inputText.includes("happy")) {
        return "Happy";
    } else if (inputText.includes("sad")) {
        return "Sad";
    } else {
        return "Neutral";
    }
}

