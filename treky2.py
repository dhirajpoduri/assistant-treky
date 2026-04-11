import random
import webbrowser

def open_website(user_input):
    if "google" in user_input:
        webbrowser.open("https://www.google.com")
        return "opening google 🌐"

    elif "youtube" in user_input:
        webbrowser.open("https://www.youtube.com")
        return "opening youtube ▶️"

    elif "chatgpt" in user_input:
        webbrowser.open("https://chat.openai.com")
        return "opening chatgpt 🤖"

    elif "github" in user_input:
        webbrowser.open("https://github.com")
        return "opening github 💻"

    return None


def play_game():
    number = random.randint(1, 10)
    chances = 2

    print("Treky: 😏 guess a number between 1 and 10. You got 2 chances.")

    while chances > 0:
        try:
            guess = int(input("Your guess: "))
        except:
            print("Treky: bro that’s not even a number 💀")
            continue

        if guess == number:
            print("Treky: lessgo you have won my gratitude 🎉")
            return

        else:
            chances -= 1
            if chances > 0:
                print(f"Treky: nope 😏 try again. Chances left: {chances}")

    print("Treky: hahaha sucker you loose 💀")


def handle_input(user_input):
    user_input = user_input.lower()

    # GREETING
    if "hey treky" in user_input:
        return random.choice([
            "hey 👋 how’s it been going?",
            "yo 😄 what’s up, how’s it been going?"
        ])

    # MOOD
    elif any(word in user_input for word in ["good", "fine", "great"]):
        return random.choice([
            "ayyy nice 😎",
            "good to hear bro 🔥"
        ])

    elif any(word in user_input for word in ["bad", "sad"]):
        return random.choice([
            "damn 😕",
            "we fixing that mood today 😎"
        ])

    # WEBSITE
    elif "open" in user_input:
        result = open_website(user_input)
        if result:
            return result
        return "which website bro? 🤔"

    # GAME TRIGGER
    elif "game" in user_input or "play" in user_input:
        play_game()
        return "that was fun 😏"

    # JOKES
    elif "joke" in user_input:
        return random.choice([
            "your code works? must be a rare event 😏",
            "if bugs were money, you'd be rich 💀"
        ])

    # HOW ARE YOU
    elif "how are you" in user_input:
        return "living the code life 😎"

    # EXIT
    elif "bye" in user_input:
        return "bye bro 👋"

    # DEFAULT
    else:
        return random.choice([
            "hmm 🤔 didn’t get that",
            "bro what are you saying 😭"
        ])


# MAIN LOOP
print("Treky is online... say 'hey treky' 😎")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Treky: bye bro 👋")
        break

    response = handle_input(user_input)
    print("Treky:", response)