# Implement a program that prompts the user for a str
# in English and then outputs the “emojized” version of that str,
# converting any codes (or aliases) therein to their corresponding emoji.
import emoji

answer = input("Input: ")
print(emoji.emojize(answer))

# 05/07
