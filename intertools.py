'''Write a Python program using itertools.count() to:
Print the first 10 numbers
Starting from 5
With a step (difference) of 3'''

def main():
    import itertools
    count=0
    for i in itertools.count(5,3):
        if count==10:
            break
        print(i,end=" ")
        count+=1
    print()

if __name__=="__main__":
    main()




'''Write a Python program using itertools.cycle():
Given a list: [1, 2, 3]
Print first 10 elements in cyclic order'''
def main():
    import itertools
    count=0
    for i in itertools.cycle([1,2,3]):
        if count==10:
            break
        print(i,end=" ")
        count+=1
    print()

if __name__=="__main__":
    main()


def main():
    import itertools
    
    for i in itertools.accumulate([1,2,3,4,5]):
        print(i,end=" ")
    print()

if __name__=="__main__":
    main()



def main():
    import itertools
    
    for i in itertools.repeat(7,5):
        print(i,end=" ")
        
    print()

if __name__=="__main__":
    main()


def main():
    import itertools
    for i in itertools.count(2,2):
        if i>=20:
            break
        print(i,end=" ")
    print()

if __name__=="__main__":
    main()



def main():
    import itertools
    count_30 = 0
    for i in itertools.cycle([10, 20, 30]):
        print(i, end=" ")
        if i == 30:
            count_30 += 1
        if count_30 == 2:
            break
        print()
if __name__ == "__main__":
    main()