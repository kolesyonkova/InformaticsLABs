import re

with open(r"C:\Users\kater\Desktop\task.txt", 'r', encoding="utf-8") as task:
    output = open(r"C:\Users\kater\Desktop\fileWrite.txt", 'w')
    args = task.read().split(' ')
    for i in range(len(args) - 1):
        if '.' in args[i]:
            args[i] = args[i][:-1]
    print(args)
    index_repeat = []
    for i in range(len(args) - 1):
        if args[i + 1] in args[i]:
            index_repeat.append(i)
    tmp = 0
    for i in range(len(index_repeat)):
        args.pop(index_repeat[i] - tmp)
        tmp += 1
    print(args)
    tmp = 0
    for i in range(len(args)):
        if re.search(r'[А-Я]', args[i][0]):
            tmp += 1
            if i == 0:
                pass
            else:
                if re.search(r'\?$', args[i - 1][-1]):
                    pass
                else:
                    args[i - 1] = args[i - 1][:] + '.'
    for i in range(len(args)):
        output.write(args[i] + ' ')
    task.close()
    output.close()
