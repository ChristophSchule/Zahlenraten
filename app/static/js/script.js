document.addEventListener("DOMContentLoaded", () => {
    console.log("Frontend JS loaded!");
});

const _USER_INPUT_PROMPT = document.querySelector('.userInputPrompt');
const _USER_INPUT = document.querySelector('.userInput');
const _GUESS_BTN = document.querySelector('.guessBtn');
const _RESTART_BTN = document.querySelector('.restartBtn');
const _SCOREBOARD = document.querySelector('.scoreboard');

_USER_INPUT.addEventListener('change', function () {
    if (this.value == '' || this.value == null) {
        _GUESS_BTN.classList.add('disabled');
    } else {
        _GUESS_BTN.classList.remove('disabled');
    }
});

_USER_INPUT.addEventListener('animationend', function () {
    this.classList.remove('borderPulse');
});

_GUESS_BTN.addEventListener('click', function () {
    if (_GUESS_BTN.classList.contains('disabled')) {
        _USER_INPUT.classList.add('borderPulse');
    } else {
        console.log(_USER_INPUT.value + ' geraten!');
    }
});