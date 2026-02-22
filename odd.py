'''You are given an integer N, print all the odd values, for all i, where 0 <= i < N. Print each values on a seperate line.'''
def main():
    N = int(input())
    # YOUR CODE GOES HERE
    for i in range(0,N):
        if i%2!=0:
            print(i)
    return 0

if __name__ == '__main__':
    main()