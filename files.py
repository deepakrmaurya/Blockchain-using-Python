f = open('demo.txt', mode='r')
# f.write('Add this content\n')
file_content = f.readlines()
f.close()
print(file_content)