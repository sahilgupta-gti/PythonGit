print('This is second 1.2v of PythonGit')
print('This is second 1.2v of PythonGit')
print('Change on github')
print('This is local after doing on github without pulling')
print("change on 09-jan-2019")
print("change on 10-jan-2019-2")
print("change on github")
print("change on ide")
print('Python\'s')
isHot = False
if isHot:
    print('hot day')
elif isHot:
    print('cold day')


f = open('Myfile.txt', 'r')
while True:
    a = f.readline()
    if a != '':
        print(a, end='')
    else:
        print()
        break
# noinspection PyBroadException
try:
    print(4/0)
except Exception:
    print("you cannot divide by zero")
