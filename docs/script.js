let number = Math.floor(Math.random() * 100) + 1;
let attempts = 0;

const input = document.getElementById('guessInput');
const button = document.getElementById('guessButton');
const result = document.getElementById('result');

button.addEventListener('click', () => {
    const guess = parseInt(input.value, 10);
    if (isNaN(guess)) {
        result.textContent = 'Please enter a valid integer';
        return;
    }
    attempts += 1;
    if (guess < number) {
        result.textContent = 'Too low!';
    } else if (guess > number) {
        result.textContent = 'Too high!';
    } else {
        result.textContent = `Correct! You guessed in ${attempts} attempts.`;
        button.disabled = true;
        input.disabled = true;
    }
    input.value = '';
    input.focus();
});
