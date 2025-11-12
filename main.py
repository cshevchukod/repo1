from collections import defaultdict


def main():
    print("Started!")
    
    words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
    grouped_words = defaultdict(list)

    for word in words:
        char = word[0]
        grouped_words[char].append(word)

    print(dict(grouped_words))

if __name__ == "__main__":
    main()