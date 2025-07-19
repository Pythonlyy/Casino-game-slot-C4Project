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

function startGame() {
  coins = 10;
  gameActive = true;
  content.innerHTML = ''; // Clear old output
  println("🎰 Welcome to Lucky Spin!");
  println(`You have ${coins} coins.`);
  println("\nPress Enter to spin or type 'q' to quit:");
}

function handleGameInput(key) {
  if (!gameActive) return;

  if (key === 'q') {
    println("\nThanks for playing Lucky Spin! 🎰");
    gameActive = false;
    runButton.disabled = false;
    return;
  }

  if (key === 'Enter') {
    if (coins <= 0) {
      println("🪙 You're out of coins! Game over.");
      gameActive = false;
      runButton.disabled = false;
      return;
    }

    coins -= 1;
    println("\nSpinning...");
    const result = Array.from({ length: 3 }, () =>
      symbols[Math.floor(Math.random() * symbols.length)]
    );
    println(result.join(" "));

    if (result[0] === result[1] && result[1] === result[2]) {
