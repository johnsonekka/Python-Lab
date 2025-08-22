def count_word_frequency(text):
    words = text.lower().split()

    word_count = {}

    for word in words:
        word = word.strip('.,!?;:"()')
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

user_text = input("Enter your text: ")
frequency = count_word_frequency(user_text)

print("\nWord Frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")
    
