import random

def toss_coin():
    """Simulate a single coin toss."""
    return random.choice(["Heads", "Tails"])

def main():
    """Main function to handle user interaction and multiple tosses."""
    print("\n🎲 Virtual Coin Toss 🎲")
    
    while True:
        try:
            num_flips = int(input("\nEnter the number of times you want to flip the coin: "))
            if num_flips <= 0:
                print("❌ Please enter a positive number.")
                continue
        except ValueError:
            print("❌ Invalid input. Enter a valid number.")
            continue

       
        heads_count = 0
        tails_count = 0

        
        for _ in range(num_flips):
            result = toss_coin()
            print(f"🪙 {result}")
            if result == "Heads":
                heads_count += 1
            else:
                tails_count += 1

        
        total_flips = heads_count + tails_count
        print("\n📊 Coin Toss Results:")
        print(f"Heads: {heads_count} ({(heads_count/total_flips)*100:.2f}%)")
        print(f"Tails: {tails_count} ({(tails_count/total_flips)*100:.2f}%)")

        
        again = input("\nDo you want to flip again? (yes/no): ").strip().lower()
        if again != "yes":
            print("\n🎉 Thank you for using  Srishti's Virtual Coin Toss! 🎉")
            break

if __name__ == "__main__":
    main()
