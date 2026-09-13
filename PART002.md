# --IF ELSE STATEMENTS--

- Ye 3 hote hai ek toh "if", "elif" and "else".
- bss ye 3 conditions me hum apni conditions rkhte hai.

# --CONDITIONAL OPERATORS--

- ">" Greater than.
- "<" Less than.
- ">=" Greater than equal to.
- "<=" Less than equal to.
- "==" Equal to.

# --NESTED CONDITION--

- Isme hum condition ke andar condition lagate hai.
- .py file me example hai.

# -- LOOPS--

- Kbhi kbhi kya hota hai ki programmer ko kisi cheez ko baar baar likhna hota hai toh uske liye hum loop ka use krte hai.

## --FOR LOOP--

- Iss loop me hum iterable object ko iterate krte hai in a sequence. 
- Jaise:- Strings, Lists, Tupples, Sets and Dictionaries.

- for example: 
                  name = "Keshav"
                  for i in name:
                       print(i)

- Hum loop ke andar loop bhi laga skte hai.

- Iteration:- steps ko baar baar repeat krna.

- Range:- Isme hum ek range dete hai jiske andar andar print hota hai.

- for i in range(1,15,2): 
     print(i)            ---> iss code me jo     teesri value hai vo gap hoga hrr value ke beech ka.


## --WHILE LOOP--

- Ye ek aisa loop hai jisme hum condition dete hai agar condition true hai toh loop chalta rahega aur jaise hee condition false hui toh loop ruk jaaega.

- isme hum sabse pehle initial point dete hai then codition.

## --ELSE WITH WHILE LOOP--

- Jaise hee condition false hogi toh interpreter bahar aake else me jaaega aur else ki statement ko execute krr dega.

## --DO WHILE LOOP(Not in Python)--

- It is not in python but just for knowledge.

- ye ek aisa loop hota hai jo kam se kam ek baar execute hota hee hota hai whether the condition is true or false.

- do{
    loop body
}while(condition);

- ye iska syntax hota hai

# --BREAK AND CONTINUE STATEMENTS--

## --BREAK STATEMENT--

- Break condition loop ko break krne ke liye hoti hai.

- Mtlb agar hum jaha bhi break laga dete hai toh loop vahi rook jata hai 

## --CONTINUE STATEMENT--

- Continue statement se hum given condition ko skip krke loop continue krte hai.

## --PASS STATEMENT--

- Pass statement mtlb kuchh nhi krna bss aage badhna.

- ye na toh loop rokta hai aur naa hee element skip krta hai.

# --PYTHON FUNCTION--

- Isme hum codes ka ek block bna dete hai jisse hume code ko baar baar repeat nhi krna padta.

- There are two types of functions:-

1. Built-in functions.
2. User-defined functions.

1. Built-in functions: jo pehle se hee defined hote hai. Hume def ka use nhi krna padta.
- min(),max(),len(),sum(),type(),etc.

2. User-defined functions: jisme hum functions ko khud define krte hai. Isme hum def function ka use krte hai.

- Functions me hum pass statement ka use krte hai uss function pe koi bhi operation perform na krne ke liye.

# --FUNCTION ARGUMENTS--

- Arguments jo hum function ko dete hai brackets me.

- There are four types of function arguments we can provide in a function:

* Default Argument
* Keyword Argument
* Variable length Arguments
* Required Arguments

- Default Argument: Isme araguments pehle se hee set hote hai. Inko hum change bhi krr skte hai.

- Keyword Argumnet: Isme hum argumnet ko "key = value" form me provide krte hai jisme ki hume order koi matter nhi krta.

- Required arguments: Isme hum jo required arguments hote hai unhe provide krte hai baaki default use ho jaate hai. Isme hum "key = value"
form me argument nhi dete toh isme order matter krta hai.

- Variable length Arguments: Isme hum kitni bhi values provide krde koi dikkat nhi.

## --RETURN STATEMENT--

- Isko use krke hum value ko return krr dete hai calling function ko. 
