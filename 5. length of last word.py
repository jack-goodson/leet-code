def lengthOfLastWord(s: str) -> int:
    word = s.strip().split(" ")[-1]
    return len(word)

print(lengthOfLastWord("hello worlddd"))