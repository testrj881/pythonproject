#reverse the order of word in sentence
#Simpler Alternative (Pythonic Way):
from operator import methodcaller

print("----another method WITH builtin methods:")
sent = "hello hello world good morning"
reverse_order= ' '.join(sent.split()[::-1])
print(reverse_order)

print("----another method without builtin methods:")
sent = "hello hello world good morning"
word_list = sent.split()
reverse_sent = []

# Fix the range: range(start, stop, step)
for i in range(len(word_list)-1, -1, -1):  # Add step=-1
    reverse_sent.append(word_list[i])  # Use append(), not +=

# Join the reversed words into a string
reversed_sentence = " ".join(reverse_sent)
print("another:",reversed_sentence)


