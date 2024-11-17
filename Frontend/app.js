
// DOM Elements
const startButton = document.getElementById('start-button');
const startScreen = document.getElementById('start-screen');
const gameScreen = document.getElementById('game-screen');
const endScreen = document.getElementById('end-screen');
const phraseDisplay = document.getElementById('phrase-to-repeat');
const statusDisplay = document.getElementById('status');
const scoreDisplay = document.getElementById('score');
const livesDisplay = document.getElementById('lives');
const startRecognitionButton = document.getElementById('start-recognition');
const playAgainButton = document.getElementById('play-again-button');
const totalScoreDisplay = document.getElementById('total-score');

// Game Variables
let allSentences = [
  "The dog jumped over the fence",
  "I like to read books",
  "She is playing the piano",
  "The sun is shining brightly",
  "He went to the store",
];
let userPoints = 0;
let questionCount = 0;
let currentLives = 3;
let currentQuestion = 0;
let currentPhrase = "";

// Initialize Game
startButton.addEventListener('click', () => {
  questionCount = parseInt(document.getElementById('questionCount').value);
  currentQuestion = 0;
  userPoints = 0;
  currentLives = 3;
  startScreen.classList.add('hidden');
  gameScreen.classList.remove('hidden');
  nextQuestion();
});

// Handle Speech Recognition
startRecognitionButton.addEventListener('click', startRecognition);

// Play Again
playAgainButton.addEventListener('click', () => {
  startScreen.classList.remove('hidden');
  endScreen.classList.add('hidden');
});

// Show the Next Question
function nextQuestion() {
  if (currentQuestion < questionCount) {
    currentPhrase = getRandomPhrase();
    phraseDisplay.textContent = `Repeat this phrase: "${currentPhrase}"`;
    currentLives = 3;
    livesDisplay.textContent = currentLives;
    currentQuestion++;
    statusDisplay.textContent = '';
  } else {
    endGame();
  }
}

// End the Game
function endGame() {
  gameScreen.classList.add('hidden');
  endScreen.classList.remove('hidden');
  totalScoreDisplay.textContent = userPoints;
}

// Randomly Select a Phrase
function getRandomPhrase() {
  return allSentences[Math.floor(Math.random() * allSentences.length)];
}

// Start Speech Recognition
function startRecognition() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = 'en-US';

  console.log("aaaa")
  recognition.start();

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript.toLowerCase();
    checkAnswer(transcript);
  };

  recognition.onerror = (event) => {
    statusDisplay.textContent = 'Error during speech recognition. Please try again!';
    console.error("Speech recognition error:", event);
  };
}

// Check User Answer
function checkAnswer(userAnswer) {
  if (userAnswer === currentPhrase.toLowerCase()) {
    userPoints++;
    statusDisplay.textContent = 'Correct!';
    nextQuestion();
  } else {
    statusDisplay.textContent = 'Incorrect. Try again!';
    currentLives--;
    livesDisplay.textContent = currentLives;
    if (currentLives <= 0) {
      endGame();
    }
  }
  scoreDisplay.textContent = userPoints;
}
