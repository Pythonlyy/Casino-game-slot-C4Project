import random
from js import document

symbols = ["🍒", "🍋", "🍇", "💎", "7️⃣"]
coins = 10
game_active = True

def update_output(text):
    output = document.getElementById("output")
    output.innerText += text + "\n"

update_output("🎰 Welcome to Lucky Spin!")
update_output(f"You have {coins} coins.")

def spin():
    global coins, game_active
    if not game_active or coins <= 0:
        update_output("❗ Game over. Refresh to play again.")
        return

    coins -= 1
    update_output("\nSpinning...")

    result = [random.choice(symbols) for _ in range(3)]
    update_output(" ".join(result))

    if result[0] == result[1] == result[2]:
        update_output("🎉 JACKPOT! You win 5 coins!")
        coins += 5
    elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
        update_output("✨ Nice! You win 2 coins!")
        coins += 2
    else:
        update_output("💨 No match. Try again!")

    update_output(f"Coins left: {coins}")
    if coins == 0:
        update_output("🪙 Out of coins! Game over.")
        game_active = False

def quit_game():
    global game_active
    game_active = False
    update_output("\nThanks for playing Lucky Spin! 🎰")
