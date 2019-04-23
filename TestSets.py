#!/usr/bin/env python
# coding: utf-8

# In[26]:


import random


# In[42]:


def GenerateTestSet(Size_Genome, Size_SnapShots):
    Genome = ["A","C","T","G"]
    Read = random.choices(Genome,k = Size_Genome)

    SnapShots = []
    First = 0
    Last = First + Size_SnapShots

    while(Last < Size_Genome):
        SnapShots.append(Read[First:Last])
        First = random.randint(First,Last-1)
        Last = First + Size_SnapShots

    SnapShots.append(Read[Size_Genome-1-Size_SnapShots:Size_Genome-1])

    return Read, SnapShots


# In[43]:


def CheckAccuracy(Read, Result):
    Total_Positions = len(Read)
    Max_Correct = 0
    for i in range(0,Total_Positions-len(Result)):
        temp_correct = 0
        for n in range(0,len(Result)):
            if(Result[n]==Read[i+n]):
                temp_correct = temp_correct + 1
        if(temp_correct > Max_Correct):
            Max_Correct = temp_correct
    
    return Max_Correct/Total_Positions


# In[44]:


def main():
    Read, SnapShots = GenerateTestSet(50, 25)
    print(Read,"\n \n", SnapShots)
    CheckAccuracy(Read, SnapShots[2])

