import random
import time

def type_text(text, delay=0.05):
    """Print text one character at a time with a delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # To move to the next line after the text is printed

def start_game():
    type_text("🌟 Welcome to Strategic Moves: Entrepreneur's Quest! 🌟")
    time.sleep(1)
    type_text("You are a budding entrepreneur on a journey to build your business empire.")
    time.sleep(3)
    print()
    type_text("Each decision you make will shape your destiny. Let's begin!")

    play_game()

def play_game():
    score = 0

    type_text("\n👤 PBD: 'Young entrepreneur, to succeed, you must first understand yourself. Do you have a clear vision of who you are and where you're going?'")
    print()
    time.sleep(3)
    move1 = input("A) Yes, I have a clear understanding.\nB) No, I'm still figuring it out.\n")

    if move1.upper() == 'A':
        score += 1
        time.sleep(2)
        type_text("🧠 PBD: 'Well done! Self-awareness is the first step to mastery.'")
    else:
        type_text("🔍 PBD: 'You must find clarity to move forward on your path.'")

    type_text("\n🔮 Scenario: 'A crucial decision lies ahead. Do you trust your gut or rely on data?'")
    move2 = input("A) I use data-driven decisions.\nB) I go with my gut instinct.\n")

    if move2.upper() == 'A':
        score += 1
        time.sleep(1.5)
        type_text("📊 PBD: 'Wise choice! Data is the backbone of sound decisions.'")
    else:
        type_text("💭 PBD: 'Instincts are valuable, but data should guide you.'")

    # Insert random event
    if random.choice([True, False]):
        type_text("\n⚡ Surprise Event: 'A sudden market shift occurs! How will you respond?'")
        surprise_move = input("A) Adapt quickly.\nB) Stick to the plan.\n")
        if surprise_move.upper() == 'A':
            score += 1
            time.sleep(1.5)
            type_text("🔥 PBD: 'Great agility! You’ve turned a crisis into an opportunity.'")
        else:
            type_text("🛑 PBD: 'Sometimes, sticking to the plan can lead to missed opportunities.'")

    print("\n🏢 Scenario: 'As your business grows, it’s time to build your team. What’s your strategy?'")
    move3 = input("A) Hire to complement my weaknesses.\nB) Focus on hiring more of my strengths.\n")

    if move3.upper() == 'A':
        score += 1
        time.sleep(1.5)
        type_text("🤝 PBD: 'A balanced team is the key to long-term success.'")
    else:
        type_text("⚠️ PBD: 'You risk creating a team that lacks diversity in skills.'")

    type_text("\n📈 Scenario: 'You’re planning to scale your business. Do you have a strategy?'")
    move4 = input("A) Yes, I have a clear roadmap.\nB) No, I'm still growing organically.\n")

    if move4.upper() == 'A':
        score += 1
        time.sleep(1.5)
        type_text("🚀 PBD: 'Scaling with strategy ensures sustainable growth.'")
    else:
        type_text("🌱 PBD: 'Organic growth is good, but a roadmap would accelerate your success.'")

    type_text("\n💼 Scenario: 'To stay ahead of the competition, will you make a bold power play?'")
    move5 = input("A) Yes, I take calculated risks.\nB) No, I play it safe.\n")

    if move5.upper() == 'A':
        score += 1
        time.sleep(1.5)
        type_text("⚔️ PBD: 'Bold moves lead to big wins. Well done!'")
    else:
        type_text("🛡️ PBD: 'Playing it safe can be smart, but sometimes boldness is required.'")

    determine_title(score)

def determine_title(score):
    titles = {
        5: ("Grandmaster", "https://veed.io/view/c6cb0675-306a-43cd-8101-0733552dd223"),
        4: ("CEO", "https://veed.io/view/c6cb0675-306a-43cd-8101-0733552dd223"),
        3: ("Strategist", "https://veed.io/view/c6cb0675-306a-43cd-8101-0733552dd223"),
        2: ("Manager", "https://veed.io/view/a472766e-c74f-4141-a390-07fbf74cef69"),
        1: ("Apprentice", "https://veed.io/view/a472766e-c74f-4141-a390-07fbf74cef69"),
        0: ("Novice", "https://veed.io/view/a472766e-c74f-4141-a390-07fbf74cef69")  # Added missing comma here
    }

    title, video_link = titles.get(score, ("Novice", "https://veed.io/view/a472766e-c74f-4141-a390-07fbf74cef69"))  # Corrected the get method
    type_text(f"\n🎉 Your title is: {title}!")
    type_text(f"🎥 Watch your BONUS VIDEO here: {video_link}")
    if title == "Grandmaster":
        type_text("🏆 PBD: 'Congratulations! You’ve mastered the 5 Moves and are now a business Grandmaster!'")
    elif title == "CEO":
        type_text("👑 PBD: 'Excellent work! You’re leading like a top-tier CEO.'")
    else:
        type_text(f"🚀 PBD: 'You’ve earned the title of {title}. Keep refining your strategy and aim for the top!'")

    end_game()

def end_game():
    replay = input("\nWould you like to play again and improve your title? (Yes/No)\n")
    if replay.lower() == 'yes':
        play_game()
    else:
        type_text("Goodbye! Remember, every great entrepreneur was once a novice. Keep learning and growing!")

start_game()
