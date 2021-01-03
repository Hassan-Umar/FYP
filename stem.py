#!/usr/bin/env python
# coding: utf-8

# In[1]:


def lemmatize(word):
    return applyrule(word)


# In[2]:


def applyrule(word):
    word=word.replace(" ", "")
    if word[-1:]=='ی':
        word=rule1(word)
        word=lemmatize(word)
    elif word[-2:]=='اں':
        word=rule2(word)
        word=lemmatize(word)
    elif word[-2:]=='وں':
        word=rule2(word)
        word=lemmatize(word)
    elif word[-2:]=='يں':
        word=rule2(word)
        word=lemmatize(word)
    elif word[-2:]=='ات':
        word=rule2(word)
        word=lemmatize(word)
    elif word[-1:]=='ے':
        word=rule6(word)
        word=lemmatize(word)
    elif word[-5:]=='انگیز':
        word=rule5(word)
        word=lemmatize(word)
    elif word[-4:]=='آمیز':
        word=rule4(word)
        word=lemmatize(word)
    elif word[-3:]=='آرا':
        word=rule3(word)
        word=lemmatize(word)
    elif word[-5:]=='اندیش':
        word=rule5(word)
        word=lemmatize(word)
    elif word[-3:]=='آور':
        word=rule3(word)
        word=lemmatize(word)
    elif word[-3:]=='باز':
        word=rule3(word)
        word=lemmatize(word)
    elif word[-5:]=='بردار':
        word=rule5(word)
        word=lemmatize(word)
    elif word[-2:]=='پن':
        word=rule2(word)
        word=lemmatize(word)
    elif word[-4:]=='پرست':
        word=rule4(word)
        word=lemmatize(word)
    elif word[-4:]=='خواہ':
        word=rule4(word)
        word=lemmatize(word)
    elif word[-3:]=='خور':
        word=rule3(word)
        word=lemmatize(word)
    elif word[-4:]=='خانہ':
        word=rule4(word)
        word=lemmatize(word)
    elif word[-3:]=='دار':
        word=rule3(word)
        word=lemmatize(word)
    elif word[-3:]=='دان':
        word=rule3(word)
        word=lemmatize(word)
    elif word[-3:]=='زدہ':
        word=rule3(word)
        word=lemmatize(word)
    elif word[-3:]=='ساز':
        word=rule3(word)
        word=lemmatize(word)
    elif word[-4:]=='فروش':
        word=rule4(word)
        word=lemmatize(word)
    elif word[-3:]=='کار':
        word=rule4(word)
        word=lemmatize(word)
    elif word[-3:]=='گار':
        word=rule3(word)
        word=lemmatize(word)
    elif word[-2:]=='گر':
        word=rule2(word)
        word=lemmatize(word)
    elif word[-3:]=='گین':
        word=rule3(word)
        word=lemmatize(word)
    elif word[-3:]=='گاہ':
        word=rule3(word)
        word=lemmatize(word)
    elif word[-3:]=='مند':
        word=rule3(word)
        word=lemmatize(word)
    elif word[-3:]=='ناک':
        word=rule3(word)
        word=lemmatize(word)
    elif word[-3:]=='یلا':
        word=rule3(word)
        word=lemmatize(word)
    elif word[-3:]=='یاب':
        word=rule3(word)
        word=lemmatize(word)
    elif word[:2]=='بے':
        word=rule7(word)
        word=lemmatize(word)
    elif word[:3]=='اہل':
        word=rule8(word)
        word=lemmatize(word)
    elif word[:2]=='بد':
        word=rule7(word)
        word=lemmatize(word)
    elif word[:2]=='پر':
        word=rule7(word)
        word=lemmatize(word)
    elif word[:3]=='خوش':
        word=rule8(word)
        word=lemmatize(word)
    elif word[:3]=='خود':
        word=rule8(word)
        word=lemmatize(word)
    elif word[:3]=='غیر':
        word=rule8(word)
        word=lemmatize(word)
    elif word[:2]=='کم':
        word=rule7(word)
        word=lemmatize(word)
    elif word[:2]=='لا':
        word=rule7(word)
        word=lemmatize(word)
    elif word[:2]=='نا':
        word=rule7(word)
        word=lemmatize(word)
    elif word[:2]=='نو':
        word=rule7(word)
        word=lemmatize(word)
    elif word[:2]=='ہم':
        word=rule7(word)
        word=lemmatize(word)
    elif word[:2]=='یک':
        word=rule7(word)
        word=lemmatize(word)
    return word


# In[3]:


def rule1(word):
    lemma=word[:-1]
    return lemma


# In[4]:


def rule2(word):
    lemma=word[:-2]
    return lemma


# In[5]:


def rule3(word):
    lemma=word[:-3]
    return lemma


# In[6]:


def rule4(word):
    lemma=word[:-4]
    return lemma


# In[7]:


def rule5(word):
    lemma=word[:-5]
    return lemma


# In[8]:


def rule6(word):
    lemma=word[:-1]+'ا'
    return lemma


# In[9]:


def rule7(word):
    lemma=word[2:]
    return lemma


# In[10]:


def rule8(word):
    lemma=word[3:]
    return lemma






