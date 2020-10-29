import re

with open(r"C:\Users\kater\Desktop\Macbeth.txt", 'r', encoding="UTF-8") as task:
    output = open(r"C:\Users\kater\Desktop\fileWrite.txt", 'w')
    args = task.read()
    b = []
    out = []
    args = re.sub(r'\n', "", args, count=0)
    args = re.sub(r'^\s+', '', args, count=0)
    b = re.split('[.]', args)
    for i in range(len(b)):
        match = re.search(r'\?', b[i])
        if match:
            if b[i].count(' ') <= 6:
                out.append(b[i])
    for i in range(len(out)):
        output.write(out[i])
    task.close()
    output.close()
