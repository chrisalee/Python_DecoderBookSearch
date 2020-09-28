# use the numbers to find the code hidden in the passage

passage = "Well, the second night a fog begun to come on, and we made for a \
towhead to tie to, for it wouldn't do to try to run in a fog; but when I \
paddled ahead in the canoe, with the line to make fast, there warn't \
anything but little saplings to tie to. I passed the line around one of them \
right on the edge of the cut bank, but there was a stiff current, and the \
raft come booming down so lively she tore it out by the roots and away \
she went. I see the fog closing down, and it made me so sick and scared \
I couldn't budge for most a half a minute it seemed to me."

numbers = [32, 71, 107, 65, 36, 49]

words = passage.split(" ")
sentence = ""
for i in range(len(numbers)):
    number = numbers[i]
    word = words[number]
    sentence = sentence + word + " " 
print(sentence)