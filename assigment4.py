#!/usr/bin/env python
# coding: utf-8

# 1.What exactly is[]?
# 
# 
# 
# Ans:-
# The empty list represented by [] is a list thatcontains no items this is similar to ' 'which represents an empty string.
# 

# 2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
# 
# 
# 
# Ans:-
# spam[2]='hello'

# In[1]:


#Example
spam=[2,4,6,8,10]
print(spam)
spam[2]='hello'
print(spam)


# Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.
# 3. What is the value of spam[int(int('3' * 2) / 11)]?
# 
# 
# 
# Ans:-
#     'd'(Note that '3'*2 is the string '33'which is passed to int()before being divided by 11. This eventually evaluates to 3, spam[3]is equal to d)
#     

# In[2]:


spam=['a','b','c','d']
print("spam[int(int('3'*2)//11)]->",spam[int(int('3'*2)//11)])


# 4. What is the value of spam[-1]?
# 
# 
# Ans:-
#     'd'(Lists support negative indexing, Hence spam[-1] returns 'd')

# In[3]:


spam=['a','b','c','d']
print('spam[-1]->',spam[-1])


# 5. What is the value of spam[:2]?
# 
# 
# Ans:-
#     spam [:2] returns all elements in the list spam from 0 to 2 excluding 2.

# In[4]:


print(spam)
print(spam[:2])


# Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.
# 6. What is the value of bacon.index('cat')?
# 
# 
# Ans:-
#     The value of bacon.index('cat')is 1.(Note:-Index method returns the index of first occuerence of 'cat').

# In[5]:


bacon=[3.14,'cat',11,'cat',True]
print("bacon.index('cat')->",bacon.index('cat'))


# 7. How does bacon.append(99) change the look of the list value in bacon?
# 
# 
# Ans:-
#     The append method adds new elements to the end of the list 

# In[6]:


#Example
print(bacon)
bacon.append(99) #appends 99 to the end of the list 
print(bacon)


# 8. How does bacon.remove('cat') change the look of the list in bacon?
# 
# 
# Ans:-
#     The remove method removes the first occurence of the element in the list.

# In[7]:


print(bacon)
bacon.remove('cat')
print(bacon)


# 9. What are the list concatenation and list replication operators?
# 
# 
# Ans:-
#     The operator for list concatenation is +,While the operator for replication is *.(This is the same as for strings).

# In[8]:


#Example
List_1=['ML','DL','AI','CV','NLP']
List_2=['RNN','CNN','SVN',]
print(List_1+List_2)
print(List_2*2)


# 10. What is difference between the list methods append() and insert()?
# 
# 
# Ans:-
#     While append() will add values only to the end of a list insert()can add them anywhere in the list.

# In[9]:


#Example
list=[1,2,3,4,5]
list.append(6)
print(list)
list.insert(2,'Demo')
print(list)


# 11. What are the two methods for removing items from a list?
# 
# 
# Ans:-
#     The del statement and the remove()method are two ways to remove values from a list.

# 12. Describe how list values and string values are identical.
# 
# 
# Ans:-
#     Both lists and strings can be passed to len()function, have index and slice be used in for loops, be concateneted or replicated and be used with the in and not in operators.

# 13. What's the difference between tuples and lists?
# 
# 
# 
# Ans:-
#     Lists are mutable indexable and slicable they can have values added removed or changed tuples are Immutable but indexable and slicable the tuple values cannot be changed at all also tuples are represented using parentheses()while listes use the square brackets[].

# 14. How do you type a tuple value that only contains the integer 42?
# 
# 
# Ans:-
#     (42,)(The trailling comm is mandatry otherwise its considerd as a int by python interpreter).

# In[12]:


Tup1=(42)
Tup2=(42,)
print(type(Tup1))
print(type(Tup2))


# 15. How do you get a list value's tuple form? How do you get a tuple value's list form?
# 
# 
# Ans:-
#     The tuple()and list()functions respectively are used to convert a list to tuple and vice versa.

# 16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
# 
# 
# 
# Ans:-
#     They contain references to list values.

# 17. How do you distinguish between copy.copy() and copy.deepcopy()?
# 
# 
# Ans:-
#     The copy.copy()function will do a shallow copy of a list, while the copy deecopy()function will do a deep copy of a list that is only copy.deepcopy()will duplicate any listes inside the list.
