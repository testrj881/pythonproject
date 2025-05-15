print("Hello, World!")
# Find the occurrence of words in sentence
para = "hello hello world good good morning"
para_arr = para.split()
word_dict = {}
for i in para_arr:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1  # Fixed this line
print(word_dict)

#find the occurance of word in a paragrapgh #Alternative (using get() method) of dictionary:
# find the count of occurance of word in sentence
para2= "hello hello world hello hello world"
para_arr2=para2.split()
word_dict2={}
for i in para_arr2:
    word_dict2[i] = word_dict2.get(i, 0) + 1
print("===",word_dict2)


'''
In Python, the get() method is a safe and flexible way to retrieve values from dictionaries. 
Unlike using square brackets (dict[key]), get() doesn’t raise a KeyError if the key is missing — it returns None or a default value.
Here are different ways to use the get() method in a dictionary:

1. Basic Usage
my_dict = {'name': 'Alice', 'age': 30}
print(my_dict.get('name'))  # Output: Alice

2. Key Not Found Returns None
print(my_dict.get('gender'))  # Output: None

3. Providing a Default Value
print(my_dict.get('gender', 'Not Specified'))  # Output: Not Specified

4. Using with a Loop
Useful when accessaing multiple keys and wanting to void exceptions:
keys = ['name', 'age', 'gender']
for key in keys:
    print(f"{key}: {my_dict.get(key, 'N/A')}")

5. Using get() in List Comprehension
keys = ['name', 'age', 'gender']
values = [my_dict.get(key, 'Unknown') for key in keys]
print(values)  # Output: ['Alice', 30, 'Unknown']
6. Nested Dictionary Access with get()
python
Copy
Edit
nested_dict = {'user': {'name': 'Bob', 'email': 'bob@example.com'}}
print(nested_dict.get('user', {}).get('email', 'No Email'))  # Output: bob@example.com
7. Conditional Check with get()
python
Copy
Edit
if my_dict.get('age') > 18:
    print("Adult")
8. Avoiding KeyError in Function
python
Copy
Edit
def get_user_age(user_dict):
    return user_dict.get('age', 'Age not available')

print(get_user_age(my_dict))  # Output: 30
9. Using get() with Mutable Default (Be Careful!)
python
Copy
Edit
my_dict = {}
value = my_dict.get('data', [])
value.append(100)
print(value)       # [100]
print(my_dict)     # {} – dict not updated unless assigned explicitly
To update safely:

python
Copy
Edit
my_dict['data'] = my_dict.get('data', [])
my_dict['data'].append(100)
Let me know if you'd like examples on more advanced use cases or comparison with other methods like dict.setdefault() or collections.defaultdict.












'''

