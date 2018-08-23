# Function prototype. When multiple values are printed they are appended with new line. But if you wanna print them in the same line, you need to overwrite end=' '
print(value1, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

#example printing in file
fh = open("data.txt","w")
print("42 is the answer, but what is the question?", file=fh)
fh.close()

#example printing in the error terminal
import sys
# output into sys.stderr:
print("Error: 42", file=sys.stderr)


