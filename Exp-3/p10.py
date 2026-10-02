sentence = input("Enter a sentence: ")
words = sentence.split()

print("Longest word:", max(words, key=len))