import random
from js import document

# Initialize variables
symbols = ["🍒", "🍋", "🍇", "💎", "7️⃣"]
coins = 10
game_active = True
waiting_for_input = True

terminal = document.getElementById("terminal")
input_box = document.getElementById("user-input")

def println(text=""):
    terminal.innerText += text + "\n"
    terminal.scrollTop = terminal.scrollHeight  # auto-scroll

def start_game():
    println("🎰 Welcome to Lucky Spin!")
    println(f"You have {coins} coins.")
    println("\nPress Enter to spin or type 'q' to quit:")

start_game()

def handle_input(event):
    global coins, game_active

    if event.key == "Enter":
        user_input = input_box.value.strip().lower()
        input_box.value = ""  # clear input field

        if not game_active:
            println("Game over. Please refresh to play again.")
            return

        if user_input == "q":
            println("\nThanks for playing Lucky Spin! 🎰")
            game_active = False
            return

        if coins <= 0:
            println("🪙 No coins left. Game over!")
            game_active = False
            return

        coins -= 1
        println("\nSpinning...")
        result = [random.choice(symbols) for _ in range(3)]
        println(" ".join(result))

        if result[0] == result[1] == result[2]:
            println("🎉 JACKPOT! You win 5 coins!")
            coins += 5
        elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
            println("✨ Nice! You win 2 coins!")
            coins += 2
        else:
            println("💨 No match. Try again!")

        println(f"Coins left: {coins}")

        if coins > 0:
            println("\nPress Enter to spin or type 'q' to quit:")
        else:
            println("🪙 No coins left. Game over!")
            game_active = False

# Attach key event
input_box.addEventListener("keydown", handle_input)
