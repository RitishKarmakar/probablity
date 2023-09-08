#BayesTheorm
'''
1.find intersection
2.compute probablity
3.compute conditional Probablity
4.compute Bays Proba
'''

def intersection(Event_A,Event_B):#calculating the intersection
    A_intersection_B = []
    set(A_intersection_B)

    if len(Event_A)> len(Event_B):
        for i in Event_A:
            if(i in Event_B):
                A_intersection_B.append(i)
        #print(A_intersection_B)
    else:
        for j in Event_B:
            if(j in Event_A):
                A_intersection_B.append(j)
        #print(A_intersection_B)
    return A_intersection_B
def probablity(event , sample_space):
    prob_numeric = len(event)/sample_space
    return prob_numeric
def conditional_probablity(Event_A,Event_B,sample_space):
    n=probablity(intersection(Event_A,Event_B),sample_space)
    cond_prob=n/probablity(Event_B,sample_space)
    return cond_prob
def Bays_probablity(Event_A,Event_B,sample_space):
    result = (conditional_probablity(Event_B,Event_A,sample_space)*probablity(Event_A,sample_space))/probablity(Event_B,sample_space)
    return result
Event_A=[]
Event_B=[]
sample_space_lst=[]
choice =""
print("Enter the values for Sample Space:")
while True:
    choice = input("Enter the number to be in the Sample Space or Press enter to exit:")
    if choice == "":
        break
    else:
        maze = int(choice)
        sample_space_lst.append(maze)
print("Enter the values for Event A:")
while True:
    choice = input("Enter the number to be in the Sample Space or Press enter to exit:")
    if choice == "":
        break
    else:
        maze = int(choice)
        Event_A.append(maze)
print("Enter the values for Event B:")
while True:
    choice = input("Enter the number to be in the Sample Space or Press enter to exit:")
    if choice == "":
        break
    else:
        maze = int(choice)
        Event_B.append(maze)



sample_space = len(sample_space_lst) 
print("The Bays Probablity:",Bays_probablity(Event_A,Event_B,sample_space))



    




