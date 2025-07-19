import random  # Importing random to generate random choices

# List of symbols that can appear in the slot
symbols = ["🍒", "🍋", "🍇", "💎", "7️⃣"]
coins = 10  # Starting number of coins

print("🎰 Welcome to Lucky Spin!")
print("You have", coins, "coins.")

# Main game loop: continues as long as you have coins
while coins > 0:
    play = input("\nPress Enter to spin or type 'q' to quit: ")
    if play.lower() == 'q':  # Exit condition
        break

    coins -= 1  # Deduct 1 coin per spin

    result = []  # Create an empty list to store the 3 results
    print("\nSpinning...")

    # Generate 3 random symbols using a for loop
    for i in range(3):
        symbol = random.choice(symbols)
        result.append(symbol)  # Add symbol to result list

    print(" ".join(result))  # Display all three symbols on one line

    # Evaluate the result using conditionals
    if result[0] == result[1] == result[2]:
        print("🎉 JACKPOT! You win 5 coins!")
        coins += 5
    elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
        print("✨ Nice! You win 2 coins!")
        coins += 2
    else:
        print("💨 No match. Try again!")

    print("Coins left:", coins)  # Show coin count after each round

print("\nThanks for playing Lucky Spin! 🎰")
