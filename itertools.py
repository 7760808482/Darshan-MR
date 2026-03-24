def main():
    # print 1000 space separated integers starting from 1000 with common difference 500
    # 1000 1500 2000 2500 3000........
    # There should be exactly one space after every integer

    # print 1000 space separated integers starting from 1000 with step 500
    
    import itertools
    
    count = 0
    
    for i in itertools.count(1000, 500):
        if count == 1000:
            break
        print(i, end=" ")
        count += 1
        
    # print all uppercase alphabets 15 times, printing from A-Z then repeating again
    # A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B C D........
    # There should be exactly one space after every character
    
    count=0
    for i in itertools.cycle('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        if count==15*26:
            break
        print(i,end=" ")
        count+=1
    
    
    # print list of integers containing 1000 4's
    
    print(list(itertools.repeat(4,1000)))
    return 0

if __name__ == '__main__':
    main()