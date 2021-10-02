import sys

if(len(sys.argv) > 1):
    print(sys.argv[1])
else:
    print("No arguement was provided")
    exit()
    
# argv[0] is the same name of the script
print(sys.argv[1])
print(sys.argv)