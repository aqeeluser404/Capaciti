document.addEventListener('DOMContentLoaded', function() {
  // Define constants for HTML elements and game parameters
  const selectionButtons = document.querySelectorAll('[data-selection]')
  const finalColumn = document.querySelector('[data-final-column]')
  const computerScoreSpan = document.querySelector('[data-computer-score]')
  const yourScoreSpan = document.querySelector('[data-your-score]')
  const startButton = document.getElementById('start-button');
  const gameContainer = document.getElementById('game-container');
  const winnerMessage = document.getElementById('winner-message');
  const restartButton = document.getElementById('restart-button');
  const MAX_SCORE = 5;

  // Initialize player and computer scores, and set the game state
  let playerScore = 0;
  let computerScore = 0;
  let gameOver = false;

  // Define the game's possible selections with their properties
  const SELECTIONS = [
    {
      name: 'rock',
      emoji: '✊',
      beats: 'scissors'
    },
    {
      name: 'paper',
      emoji: '✋',
      beats: 'rock'
    },
    {
      name: 'scissors',
      emoji: '✌',
      beats: 'paper'
    }
  ]

  // Event listener for the "Start Game" button
  startButton.addEventListener('click', () => {
    startGame();
  });

  // Event listener for the "Restart Game" button
  restartButton.addEventListener('click', () => {
    startGame();
  });

  // Function to start a new game
  function startGame() {
    playerScore = 0;
    computerScore = 0;
    yourScoreSpan.innerText = '0';
    computerScoreSpan.innerText = '0';
    removeAllSelectionResults();
    startButton.style.display = 'none';
    gameContainer.style.display = 'block';
    restartButton.style.display = 'none';
    winnerMessage.style.display = 'none';
    gameOver = false;
    selectionButtons.forEach(selectionButton => {
      selectionButton.disabled = false;
    });
  }

  // Event listeners for player's selection buttons
  selectionButtons.forEach(selectionButton => {
    selectionButton.addEventListener('click', e => {
      if (gameOver) return;
      // assign selection into variable
      const selectionName = selectionButton.dataset.selection
      const selection = SELECTIONS.find(selection => selection.name === selectionName)
      makeSelection(selection)
    })
  })

  // Function to handle player's selection and computer's random selection
  function makeSelection(selection) {
    const computerSelection = randomSelection()
    const yourWinner = isWinner(selection, computerSelection)
    const computerWinner = isWinner(computerSelection, selection)

    addSelectionResult(computerSelection, computerWinner)
    addSelectionResult(selection, yourWinner)

    if (yourWinner) incrementScore(yourScoreSpan)
    if (computerWinner) incrementScore(computerScoreSpan)

  //   if (playerScore === MAX_SCORE || computerScore === MAX_SCORE) {
  //     endGame();
  //   }
  }

  // Function to increment the player or computer score
  function incrementScore(scoreSpan) {
    const newScore = parseInt(scoreSpan.innerText) + 1;
    scoreSpan.innerText = newScore;

    if (newScore === MAX_SCORE) {
      declareWinner(scoreSpan === yourScoreSpan ? 'You' : 'Computer');
    }
  }

  // Function to add the selection result to the display
  function addSelectionResult(selection, winner) {
    const div = document.createElement('div')
    div.innerText = selection.emoji
    div.classList.add('result-selection')
    if (winner) div.classList.add('winner')
    finalColumn.after(div)
  }

  // Function to remove all selection result elements
  function removeAllSelectionResults() {
    const resultSelections = document.querySelectorAll('.result-selection');
    resultSelections.forEach(result => {
      result.remove();
    });
  }

  // Function to determine if a selection is a winner
  function isWinner(selection, opponentSelection) {
    return selection.beats === opponentSelection.name
  }

  // Function to generate a random selection for the computer
  function randomSelection() {
    const randomIndex = Math.floor(Math.random() * SELECTIONS.length)
    return SELECTIONS[randomIndex]
  }

  // Function to declare the winner and end the game
  function declareWinner(winner) {
    winnerMessage.innerText = `${winner} Wins the Game!`;
    winnerMessage.style.display = 'block';
    restartButton.style.display = 'block';
    gameOver = true;
    selectionButtons.forEach(selectionButton => {
      selectionButton.disabled = true;
    });
  }
});

