import re

with open(r"C:\Users\kater\Desktop\task2.txt", 'r', encoding="UTF-8") as task:
    output = open(r"C:\Users\kater\Desktop\fileWrite.txt", 'w')
    args = task.read().split('\n')
    out = []
    for i in range(len(args)):
        match = re.search(r'P000', args[i])
        if match:
            if args[i][args[i].index(' ') + 1] == args[i][args[i].index(' ') + 3]:
                print('Попався', args[i])
                continue
        out.append(args[i])
    for i in range(len(out)):
        output.write(out[i] + '\n')
    task.close()
    output.close()
