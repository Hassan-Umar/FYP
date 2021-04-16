#!/usr/bin/env python
# coding: utf-8

# In[10]:


def conv2alpha(word):
    letters=[]
    for letter in word:
        letters.append(letter)
    return letters


# In[27]:


def chklst(word):
    fh=open('C:\\Users\\Hassan\\Downloads\\fyp\\root.csv', "r",encoding = "utf-8")
    if word in fh.read():
        return True
    else:
        return False


# In[28]:


def lemmatize(word):
    if chklst == True:
        return word
    else:
        return applyrule(word)


# In[29]:


def rule1(word):
    lemma=''
    for x in range(0,len(word)-1):
        lemma=lemma+word[x]
    if chklst(lemma) == True:
        return lemma
    else:
        return word


# In[30]:


def rule2(word):
    lemma=''
    for x in range(0,len(word)-2):
        lemma=lemma+word[x]
    if chklst(lemma) == True:
        return lemma
    else:
        return word


# In[31]:


def rule3(word):
    lemma=''
    s=len(word)
    word[s-1]='ا'
    for x in range(0,s):
        lemma=lemma+word[x]
    if chklst(lemma) == True:
        return lemma
    else:
        return word


# In[22]:


def rule4(word):
    return word


# In[23]:


def applyrule(word):
    s=len(conv2alpha(word))-1
    if conv2alpha(word)[s]=='ی':
        word=rule1(conv2alpha(word))
        word=lemmatize(word)
    elif conv2alpha(word)[s]=='ں' and conv2alpha(word)[s-1]=='ا':
        word=rule2(conv2alpha(word))
        word=lemmatize(word)
    elif conv2alpha(word)[s]=='ں' and conv2alpha(word)[s-1]=='و':
        word=rule2(conv2alpha(word))
        word=lemmatize(word)
    elif conv2alpha(word)[s]=='ں' and (conv2alpha(word)[s-1]=='ي' or conv2alpha(word)[s-1]=='ی'):
        word=rule2(conv2alpha(word))
        word=lemmatize(word)
    elif conv2alpha(word)[s]=='ت' and conv2alpha(word)[s-1]=='ا':
        word=rule2(conv2alpha(word))
        word=lemmatize(word)
    elif conv2alpha(word)[s]=='ے':
        word=rule3(conv2alpha(word))
        word=lemmatize(word)
    return word






