""" 
Leslie Vargas
CIS103
LAB 4
Working with Python Dictionaries
"""
# create a library named student and asign key-pair values
student = {"Name":"John Doe","Age":20,"Major":"Computer Science","GPA":3.8}
print(student)

# returns the value of the keys selected
print(student["Name"],student["Major"])

# adds 2 more key-pairs and updates the value for one.
student["e-mail"] = "johndoe@example.com"
student["Graduation_Year"] = 2026
student["GPA"] = 3.9
print(student)

# deletes key-pair with pop
student.pop("Age")
print(student)

# checks to see if a Key is in the list
# returns true if found, returns False if not found
if "e-mail" in student:
    print("True")
else:
    print("False")

# loops over student dictionary returning
# each key and its value
for key, value in student.items():
    print(f"{key}:{value}")


def counting_words(sentence):
    words = sentence.split()
# split() method seperates the words in the sentence by the spaces
    word_count = {}
# empty dictionary to store the word count
    for word in words:
        if word:  # Skip empty strings
            word_count[word] = word_count.get(word, 0) + 1
# .get(word,0)+1 = each word starts at zero times in the
# dictionary so if it keeps coming up it wil keep going up by a number
    return word_count

sentence = input("Enter Your sentence: ")
result = counting_words(sentence)
# calls the function with the user input and saves the outcome in a variable

print("\nWord count:")
for word, count in result.items(): # loops over each word printing the word and its count
    print(f"'{word}': {count}")

scores = {"Alice":85,"Bob":92,"Charlie":88,"David":75}
highscore = max(scores, key=scores.get)
print(f"{highscore} has the highest score.")

dict1 = {"a":100,"b":200}
dict2 = {"c":300,"d":400}
dict1.update(dict2) # combines both dictionaries
print(dict1)

ages = {"Alice":25,"Bob":30,"Charlie":35}
newdictionary = {value: key for key, value in ages.items()}
# switches the place for the keys and their values
print(newdictionary)

data = {"name1":"apple","name2":"banana","name3":"apple","name4":"orange"}
dupechecker = set() # keeps track of data being counted
new_data = {key: value for key, value in data.items()
            if value not in dupechecker and not dupechecker.add(value)}
# checks to see if data items are accounted for in the dupechecker if not it will be added.
print(new_data)

sales = {"John":1500,"Alice":2200,"Bob":1800}
# sales.items pulls the contents so then sorted() and key=lambda sort it by index
# reverse=True  descending order
sorted_sales = {key: value for key, value in sorted(sales.items(), key=lambda item:
                                                    item[1], reverse=True)}
print(sorted_sales)

# Nested dictionary one holding name, and position.
# The inner dictionary holding the salary base and bonus.
employee = {
    "Name":"Alice",
    "Position":"Software Engineer",
    "Salary": {
        "Base":70000,
        "Bonus":5000
    }
}

print(employee["Name"])
print(employee["Salary"]["Base"])
print(employee["Salary"])


from collections import Counter
# importing the counter function from the collections module
text = "Hello"
# accounted stores the character count
accounted = Counter(text)
# Iterates and prints the characters and their counts as key item pairs
for char, count in accounted.items():
    print (f"{char}:{count}")


# dictionary named locks holding key pairs
locks = {1:0,2:0,3:0,4:0,5:0}
# new dictionary iterates over the key and assigns its squared values {key: key**2}
squaredkeys = {key: key**2 for key in locks.keys()}
print(squaredkeys)

