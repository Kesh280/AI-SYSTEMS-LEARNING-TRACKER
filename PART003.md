# --STRINGS--

- Jo bhi hum single ya fir double quotes me likhte hai.
- String array ki tarah behave krti hai na ki vo array hoti hai kyoki hum isme index use krke unki values niakl skte hai 
- Strings are immutable.
- String Methods :-

- len()- To find the length of the string.
- upper()- To convert the string in the uppercase.
- lower()- To convert the string in the lowercase.
- rstrip()- To stop something to print.
- replace()- To replace somethong.
- split()- To convert from string to list.
- capitalize()- To convert first letter of first word into uppercase and adjust to lower case other of it.
- center()- We gave some value to shift the string.
- count()- To count how many times a string is repeated.
- endswith()- To check is string end with the provided data.
- find()- To find the index of the string. But if string is not there in the main string then it will return -1.
- index()- To find the index of the string. But if string is not there in the main string then it shows the error.
- isalnum()- To check is the string alphanumeric.
- isalpha()- To check is the string alpha.
- islower()- To check is it lowercase.
- isupper()- To check is it upper case.
- isprintable()- To check is it printable.
- isspace()- To check is there space in the string.
- istitle()- To check is the string Title.
- swapcase()- To swap lower to upper and upper to lower case.
- title()- To convert string to title.

## --SLICING--

- It is like a birthday boy cuts the cake.
- In this we cut the string according to our needs.
- string[start : stop : step]
- Start is the starting point from where we want to slice.
- Stop is the last index of the string but it is not included.
- Step is how many steps we have to skip.
- Negative slicing means the index starts from end with -1.
- String[::-1]--> it is the reversing the string without using loops and all.

## --STRING FORMATTING--

- In this we assign the values into the the print statement.
- There are two types of string formatting.

- format()
- print("Hello {}, aapka score {} hai!".format(naam, score))

- f-string
- print(f"Hello {naam}, aapka score {score} hai!")

# --LIST--

- It is the mutable sequence in the big brackets[].
- Slicing as same as string.

## --METHODS--

- l.append(val) #what you want to add just write in the brackets it will be added in the end of the list.

- l.insert(index,val) #In this we can add the vaue where we want.

- l.sort() #arrange in increasing order.

- l.reverse() #reverse the order.

# --TUPLES--

- It is the immutable sequence in the small brackets().
- Slicing is same as list.

## --METHODS--

- t.index(val) #in this we write a value it gives us the index of the value. where if the value is occurs more than once then it gives us first occurence index.

- t.count(val) #Count the total no. of occurences of the value.

# --DICTIONARY--

- In this type of sequence we have keys instead of index.

- key:value 

- In the slicing of the dictionary we have to get the values by using the keys.

## --METHODS--

- d.keys() #Return all keys. it takes no arguments in it.
- d.values() #Return all values. it also do not takes any argument.
- d.items() #Return (key,value) pairs. it takes no arguments in it.
- d.get(key) #returns value acc. to key.
- d.update(new_item) #It adds new items to dict.

# --SETS--

- Collection of unique elements(immutable). but the set is mutable.
- It menas we cannot store list type elements in it.

## --METHODS--

- s.add(val) #adds a value