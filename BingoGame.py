import random


def load_dictionary(filename="wordlist.txt"):
    """Load Scrabble words (first token of each line) into a set."""
    words = set()
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split()
            if parts:  # skip empty lines
                word = parts[0].lower()
                words.add(word)
    return words


def get_words_of_length(words, length):
    """Return all words of a given length."""
    return [w for w in words if len(w) == length]


def scramble_word(word):
    """Scramble the letters of a word."""
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)


def play_anagram_game(dictionary, word_length=7):
    # Choose a random base word
    candidates = get_words_of_length(dictionary, word_length)
    if not candidates:
        print(f"No words of length {word_length} found in dictionary.")
        return
    chosen_word = random.choice(candidates)

    # Scramble
    scrambled = scramble_word(chosen_word)
    while scrambled == chosen_word:  # Ensure it's actually scrambled
        scrambled = scramble_word(chosen_word)

    print(f"Unscramble this {word_length}-letter word: {scrambled}")
    print("Press ENTER to reshuffle, or type 'quit' to give up.\n")

    # Find all valid anagrams of the chosen word
    anagrams = {w for w in candidates if sorted(w) == sorted(chosen_word)}

    guessed = set()
    while True:
        guess = input("Your guess: ").strip().lower()

        if guess == "":  # Reshuffle on empty input
            scrambled = scramble_word(chosen_word)
            while scrambled == chosen_word:
                scrambled = scramble_word(chosen_word)
            print(f"\n🔀 Reshuffled: {scrambled}")
            continue

        if guess == "quit":
            print("\nGame over!")
            print(f"Possible anagrams were: {', '.join(sorted(anagrams))}")
            break
        elif guess not in dictionary:
            print("❌ Not a valid Scrabble word.")
        elif guess in guessed:
            print("⚠️ You already guessed that.")
        elif guess in anagrams:
            guessed.add(guess)
            print(f"✅ Correct! ({len(guessed)}/{len(anagrams)} anagrams found)")
            if guessed == anagrams:
                print("🎉 You found all anagrams!")
                break
        else:
            print("❌ That's a valid word, but not an anagram of the scrambled letters.")


def main():
    dictionary = load_dictionary()
    print("Welcome to the Scrabble Anagram Game!")
    while True:
        try:
            length = int(input("\nEnter word length to practice (e.g., 7 or 8, 0 to quit): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if length == 0:
            print("Goodbye!")
            break
        play_anagram_game(dictionary, word_length=length)


if __name__ == "__main__":
    main()
