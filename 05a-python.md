# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples are lists which can't be edited. i.e., tuples are immutable and lists are mutable. Therefore we cannot add, remove or sort items in a tuple. Lists are homogenous as the items in a list express the same concept. 
   * Tuples will work as keys in a dictionary because they are immutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> A list is an ordered collection of items with duplicates whereas a set is an unordered collection with no duplicates. A set can be created by using the keyword set. We use lists when we want to store items which we will be iterating over. 
   * Sets are significantly faster when it comes to finding an element. This is because sets use a hash function to map to a bucket and no matter the size of the set, look up time is constant.'

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The lambda operator is used to create small anonymous functions, i.e., functions without a name. These functions are just needed when they hane been created. eg: >>> f = lambda x, y: x + y >>> f(1,1)
* Eg of using lambda in the key argument to sorted: >>> sorted(['Some', 'words', 'sort', 'differently'], key = lambda word: word.lower())

   

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a substitute for the lambda function as well as map(), filter() and reduce(). It is a natural and easy way to construct lists. Eg of list comprehension with map: >>> things = [2,5,9] >>> newlist = [value * 2 for value in things] >>> print newlist -- Here the for loop tells to execute some code once for each item in things
* Eg os list comprehension with filter: >>> things = [3,4,6,7,0,1] >>> print [x*2 for x in things if x%2 == 0]. The if clause of a list comprehension can be used to do the filter opration.
* we can combine map and filter operations togeather with a single list comprehension.
* Set comprehensions allow sets to be created using the principles as list comprehensions. Eg: >>> names = ['Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob'] >>> print { name[0].upper() + name[1:].lower() for name in names if len(name) > 1 }. This prints {'Bob', 'John', 'Alice'} which is a set. Dictionary comprehensions are similar to list and set comprehensions. eg: d = {key: value for (key, value) in ietrable} creates a dictionary with key, value pairs.

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





