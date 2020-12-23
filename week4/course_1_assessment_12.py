'''Q-1 : Below are a set of scores that students have
received in the past semester. Write code to determine
how many are 90 or above and assign
that result to the value a_scores.'''



scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
a_scores = 0
scores = scores.split(" ")
print(scores)
for x in scores:
    x = float(x)
    if x>=90:
<<<<<<< HEAD
        a_scores+=1
=======
        a_scores+=1


''' Q- 2 : Write code that uses the string 
stored in org and creates an acronym 
which is assigned to the variable acro. 
Only the first letter of each word should be used, 
each letter in the acronym should be a capital letter, 
and there should be nothing to separate the letters of 
the acronym. Words that should not be included in the 
acronym are stored in the list stopwords. For example, 
if org was assigned the 
string “hello to world” then the resulting acronym should be “HW”.'''


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

org = org.split()
print(org)

org = [x for x in org if x not in stopwords]

print(org)

acro = [x[0].upper() for x in org]
print(acro)
acro = "".join(acro)
str(acro)
type(acro)
print(acro.upper())


'''Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” then the 
resulting acronym should be “HE. EW. WO”.'''




stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

sent = sent.split(" ")
print(sent)

sent = [x for x in sent if x not in stopwords]
print(sent)

acro = [x[:2].upper() for x in sent]

acro = ". ".join(acro)
str(acro)



>>>>>>> Initial commit
