x='''hi we are doing good in life, use is the worst country in the world. 
Hola!good news, Ebola is eradicated from the world for the first time. 1234...##
%%% ### this sequence is your password to play blue whale game. Die Sheldon 
die$$$$$ 678'''
word_frequency = {}
for line in x.splitlines():
 words = line.split()
 for word in words:
  word = word.lower()
  word = ''.join(char for char in word if char.isalnum())
  if word:
   if word in word_frequency:
    word_frequency[word] += 1
   else:
    word_frequency[word] = 1
sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
print("The 10 most frequently appearing words are:")
for word, frequency in sorted_words[:10]:
 print(f"Word: '{word}', Frequency: {frequency}")