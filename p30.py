input_file_path = input("Enter the input file path: ")
output_file_path = input("Enter the output file path to save the sorted content: ")
with open(input_file_path, 'r') as input_file:
lines = [line.strip() for line in input_file.readlines()]

lines.sort()
with open(output_file_path, 'w') as output_file:
for line in lines:
output_file.write(line + '\n')

print(f"Sorted contents have been written to {output_file_path}")