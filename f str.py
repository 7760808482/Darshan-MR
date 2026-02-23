'''You will need to write a format string which prints out the data using the following syntax: Hello Robin. You are currently left with 10 chocolates.'''

def main():
    data = ("Robin", 10, "chocolates")
    
    # This matches the expected string exactly:
    format_string = "Hello %s. You are currently left with %d %s."
    
    print(format_string % data)
    
    return 0

if __name__ == '__main__':
    main()