phrase = input("Enter the phrase you want to turn into a hashtag: ")

def hashtagGen(text):
	phrase1 = phrase.replace(" ", "")
	return "#" + phrase1

print(hashtagGen(phrase))
