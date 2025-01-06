with open("story.txt", "r") as f:
    story = f.read()

start_of_word = -1
start_char = '<'
end_char = '>'

words = set()

for i, char in enumerate(story):
    if char == start_char:
        start_of_word = i

    if char == end_char and start_of_word != -1:
        word = story[start_of_word : i + 1]
        words.add(word)

answers = {}
for word in words:
    answer = input(f"Enter a word for {word} : ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)
