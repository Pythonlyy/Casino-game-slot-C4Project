const content = document.getElementById('content');
const runButton = document.getElementById('run-button');

let coins = 10;
let gameActive = false;
const symbols = ["🍒", "🍋", "🍇", "💎", "7️⃣"];

function println(text = '') {
  const line = document.createElement('div');
  line.textContent = text;
  content.appendChild(line);
  content.scrollTop = content.scrollHeight;
}

function showInputPrompt() {
  const inputLine = document.createElement('div');
  const input = document.createElement('input');
  input.className = 'terminal-input';
  input.placeholder = "Press Enter to spin or type 'q' to quit";
  input.autofocus = true;

  input.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
      const value = input.value.trim().toLowerCase();
      input.disabled = true;
      inputLine.textContent = `> ${value}`;
      handleInput(value);
    }
  });

  inputLine.appendChild(input);
  content.appendChild(inputLine);
  input.focus();
}

function startGame() {
  gameActive = true;
  println("🎰 Welcome to Lucky Spin!");
  println(`You have ${coins} coins.`);
  showInputPrompt();
}

function handleInput(input) {
  if (!gameActive) return;

  if (input === 'q') {
    println("\nThanks for playing Lucky Spin! 🎰");
    gameActive = false;
    return;
  }

  if (coins <= 0) {
    println("🪙 You're out of coins! Game over.");
    return;
  }

  coins -= 1;
  println("\nSpinning...");
  const result = [];
  for (let i = 0; i < 3; i++) {
    result.push(symbols[Math.floor(Math.random() * symbols.length)]);
  }

  println(result.join(" "));

  if (result[0] === result[1] && result[1] === result[2]) {
    println("🎉 JACKPOT! You win 5 coins!");
    coins += 5;
  } else if (result[0] === result[1] || result[1] === result[2] || result[0] === result[2]) {
    println("✨ Nice! You win 2 coins!");
    coins += 2;
  } else {
    println("💨 No match. Try again!");
  }

  println(`Coins left: ${coins}`);

  if (coins > 0) {
    showInputPrompt();
  } else {
    println("🪙 You're out of coins! Game over.");
  }
}

runButton.addEventListener('click', () => {
  runButton.disabled = true;
  startGame();
// Keep input focused even if user clicks elsewhere
document.addEventListener('click', () => {
  const inputs = document.querySelectorAll('.terminal-input');
  const lastInput = inputs[inputs.length - 1];
  if (lastInput && !lastInput.disabled) {
    lastInput.focus();
  }
});


