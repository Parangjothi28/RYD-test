import fitz

doc = fitz.Document("Arihant-general_knowledge.pdf")
print(doc.pageCount)
pg = doc[261]
txt = pg.getText()
questions = []
option1 = []
option2 = []
option3 = []
option4 = []
paper = []
answer = []
print(ord(txt[642]),txt[643],ord(txt[643]),txt[644],txt[645],txt[646],txt[647],txt[648],ord(txt[649]),txt[640],ord(txt[641]))
print(txt)
flag = 0
word = ""
prev = " "
for i in range(250,256):
    pg = doc[i]
    txt = pg.getText()
    choice = int(input("Enter 1) if questions 2) if answer with only number 3) if answer with statement"))
    if choice is 1:
        for letter in txt:
            if flag is 0:
                try:
                    a = int(letter)
                except ValueError:
                    if letter is '.':
                        flag = 1
            elif flag is 1:
                word = word + letter
                if letter is '?':
                    flag = 2
                    questions.append(word)
                    word = ""
            elif flag is 2:
                if letter is ')':
                    if prev is '1':
                        flag = 3
                    if prev is '2':
                        flag = 4
                    if prev is '3':
                        flag = 5
                    if prev is '4':
                        flag = 6
                    word = ""
            elif flag is 3:
                if letter is '(':
                    flag = 2
                    option1.append(word)
                    word = ""
                else:
                    word=word+letter
            elif flag is 4:
                if letter is '(':
                    flag = 2
                    option2.append(word)
                    word = ""
                else:
                    word=word+letter
            elif flag is 5:
                if letter is '(':
                    flag = 2
                    option3.append(word)
                    word = ""
                else:
                    word=word+letter
            elif flag is 6:
                if letter is '(':
                    flag = 7
                    option4.append(word)
                    word = ""
                else:
                    word=word+letter
            elif flag is 7:
                try:
                    a = int(letter)
                    if a and ord(prev) is 10:
                        flag = 0
                        paper.append(word)
                        word = ""
                    else:
                        word=word+letter
                except ValueError:
                    word = word+letter
            prev = letter
    elif choice is 2:
        flag1 = 0
        for letter in txt:
            if letter is '.':
                flag1 = 1
            elif flag1 is 1:
                word = word+letter
                if letter is ')':
                    flag1 = 0
                    answer.append(word)
                    word = ""
    elif choice is 3:
        flag1 = 0
        for letter in txt:
            if letter is '.':
                flag1 = 1
            elif flag1 is 1:
                word = word+letter
                if ord(prev) is 10:
                    try:
                        if int(letter):
                            word = word[:-1]
                            flag1 = 0
                            answer.append(word)
                            word = ""
                    except ValueError:
                        continue
            prev =letter
    else:
        print("Wrong choice, page ignored.")

q = int(input("Enter question number: "))
print("Requested question : ",questions[q-1])
print("Choices of the question are : ")
print(option1[q-1])
print(option2[q-1])
print(option3[q-1])
print(option4[q-1])
a = int(input("Enter answer you want to see : "))
print("Requested answer : ",answer[a])