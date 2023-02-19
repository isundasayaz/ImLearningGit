# with open ('Textfile.txt' , 'r') as reader:
#     content = reader.readlines()
#     print (content)
#     reversed(content)
#     with open ('Textfile.txt' , 'w') as writer:
#         for line in content:
#             writer.write(line)

with open ("Dummy.txt" , 'r') as reader:
    content = reader.readlines()
    print (content)
    data = reversed(content)
    with open ("Dummy.txt", 'w') as writer:
        for line in data:
            writer.write(line)

