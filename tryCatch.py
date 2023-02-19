try:
    with open("Dummy.txt", 'r') as reader:
        reader.read()
except:
    print("Failure of the try block")

try:
    with open("Dummy.txt", 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print ("This is the finally block")
