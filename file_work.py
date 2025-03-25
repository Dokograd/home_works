#zapisat fail
# with open('file.txt', 'w') as file:
#     file.write("hello, world")
#
# #dopisat fail
# with open('file.txt', 'a') as file:
#     file.write('\nThis is a new file.')
#
#
#
#
#
# #prochitat file
# with open('file.txt','r') as file:
#     content = file.read()
#     print(content)
#
# #cozdat file
# # with open('file1.txt', 'x') as file:
# #     file.write('This open')
#
# #zapic and chteniy
# with open('file.txt', 'w+') as file:
#     file.write('hello, Dokon!\nThis is a new line.')
#     file.seek(0) #Peremestit cursos v nachalo file
#     content = file.read()
#     print(content)

with open('file.txt','w') as file:
    for i in range(5):
        d = int(input("enter san "))
        file.write(f'{i}\n')
des = []
with open('file.txt','r') as file:
    for line in file:
        des.append(int(line.strip()))
    print(sum(des))






