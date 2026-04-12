"""print()
variable
str(), int(), float(), bool()
type()
True, False, None
variable += 1
len()       "lenght of"
.find()     "finds a substring. -1 if there isnt" .find(substring, start, stop)
.capitalize() "yusif becomes Yusif
.upper()    "uppercase all"
.lower()
.islower()  "checks whether letters are lowercase or not"
.isupper()
.isdigit()          "Gives a Boolean value whether it's digit or not. Only works with str variables.
                    "Any string with only digits(no other symbol) gives True."
.isalpha()          "gives a Boolean value whether it's only abc letter. Even spaces are not allowed to yield True!!!"
.count()                   "variable.count("o") counts how many o letters are there. Only works with strings"
.replace("x","y")          "replaces all "x"s with "y"s. Only strings.
print(variable * x)        "print variable x times"
int(str or float variable) "turns string or float into integer type. Note: decimal point gets truncated."
input()
import math
    round() "rounds the number: 3.14 becomes 3. You can add 2nd argument to choose how many digits to round."
    .ceil() "round up to the nearest integer: 3.14 becomes 4"
    .floor() "round down to the nearest integer: 3.14 becomes 3"
    .abs() "absolute value of the number: -3.14 becomes 3.14"
    .pow(x, y) "x to the power of y: x^y can also be written instead"
    .sqrt() "square root of the number: 3.14 becomes 1.612451"
    min() "finds the minimum number among given"
    max() "opposite of min()"
slicing = create a substring by extracting elements from another string
    variable[start:stop:step] (any blank value is accepted as 0)(using negative value for step will reserve)
    slicing_defined_as_a_variable = slice(start:stop:step)
        print(variable[slicing_defined_as_a_variable])
if, elif, else statements (requires colon after conditions except for else)
>, <, <=, >=, !, ==     *note: dont use single equal sign as python will confuse it by variable assignment
and, or, not
in              "it literally means 'in'. Checks whether given list or tuple comprises the given data"
while loop      "while statement makes its code run forever as long as the condition is true"
for loop, range()
    for i in range(x, y, z)  "the code will loop until i becomes y with steps of z just like in slicing"
    "i starts with x itself (if there is nothing, it is 0) and stops at right before y with steps of z"
    "Just like mathematical indentation [x;y)"

import time:
    .sleep()    "suspend execution for given number of seconds"
    .time()     "return current time in seconds since epoch(1970,1 January 00:00:00"
end=""          "used mostly in print() and prevents loops from adding a paragraph space
loop control:
    break       "used to terminate the loop entirely
    continue    "skips to the next iteration of the loop
    pass        "does nothing, acts as a placeholder
list:  [a,b]        "used to store multiple item in a single variable" "ordered and changeable"
    list.append()     "add an item"
    list.remove()     "removes the given item"
    list.pop()        "remove the item of a given index"
    list.insert()     "inserts an item to a given index"
    list.sort()       "sorts the list alphabetically"
    list.clear()      "eradicates all items from the list"
tuple: (a,b)     "collection which is ordered and unchangeable"
    tuple.index()     "finds the index of given item"
    tuple.count()     "finds the number of given item"
set:   {a,b}     "collection which is unordered, unindexed. No duplicate values. The brackets are called curly brackets"
                 "when you print it, the elements are ordered randomly each time as there is no order"
    set.add()                    "adds the element"
    set.remove()                 "removes the item"
    set.clear()                  "eradicates all elements"
    set.update(set_2)            "adds all elements of set_2 to the set"
    set = set_2.union(set_3)     "combines set_2 with set_3 to create set. Only one is copied if there are Duplicate."
    set.difference(set_2)        "finds the difference between sets"
    set.intersection(set_2)      "finds the intersection between sets(elements that both include)"
dictionary:  {key: value}   "changeable, unordered collection of key-value pairs"
    dict[key]                               "gives the value of the given key. Error will occur if a key doesnt exist"
    dict.get()                              "Check whether key exists or not"
    dict.keys()                             "gives all the keys"
    dict.values()                           "gives all the values
    dict.items()                            "returns a view object that displays a list of the dictionary's key-value pairs as tuples"
    dict.update({new_key: new_value})       "add a new pair to dictionary"
    dict.pop()                              "removes the given key and its value"
    dict.clear()                            "empties the dictionary"
index operators:  []            "works with str,list, tuples only"
    variable[starting:stopping:steps]
function:  def hello(parameters):           "a block of code which is executed only when it is called"
return                          "sends value or objects back to the caller"
keyword arguments               "allows the order of the arguments to not matter, unlike positional arguments.
local global        "local variable is only available inside the region unlike global, which is recognized everywhere"
*args                "its a parameter that will pack all arguments into a tuple"
**kwargs             "its a parameter that will pack all argument into a dictionary"
str.format()         "optional method that gives users more control when displaying output"
    print("The {} jumped over the {}".format(variable1, variable2))
    "You can also add index into the {} to specifically choose which variable you would like"
    {:<10}           "this allocates 10 spaces worth of room for your variable(starting with your variable at the left"
    {:>10}           "this allocates 10 spaces worth of room for your variable(stopping with your variable at the right"
    {:^10}           "centers it inside that 10 spaces worth of room"
    {:.2f}           "rounds the number by 2 digits after comma"
    {:,}             "adds commas for easier depiction of thousands: 10000000 becomes 10,000,000"
    {:b}             "displays your number as binary!"
    {:o}             "displays your number as octadecimal (8)"
    {:X}             "displays your number as hexadecimal (16)"
    {:E}             "displays the scientific notation of your number"
import random
    random.randint(x,y)     "generates random integer between x and y"
    random.ranom()          "random between 0 and 1"
    random.choice(list)     "random choice from a given list"
    random.shuffle(list)    "shuffles a given list"
exception           "events detected during execution that interrups the flow of program"
    try             "tries the following code"
    except          "do this if the given problem occurs"
    except Error as e:      "allows you to assign the error itself as a variable"


"""
