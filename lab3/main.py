# xml = open(r"C:\Users\kater\Desktop\XML.txt", 'r')
import time
with open(r"C:\Users\kater\Desktop\XML.txt", 'r', encoding="UTF-8") as xml:
    import time

    start_time = time.time()
    json = open(r"C:\Users\kater\Desktop\fileWrite.txt", 'w')

    json.write('{' + '\n')
    xml.readline()
    args = xml.read().split('\n')
    b = []
    k = 0
    for i in range(len(args)):
        if args[i].count('<') > 1:
            args[i] = args[i].replace('>', '":"')
            args[i] = args[i].replace('<', '"')
        else:
            if '/' in args[i]:
                if i != len(args):
                    args[i] = args[i].replace('>', '},')
                else:
                    args[i] = args[i].replace('>', '}')
                args[i] = args[i].replace('</', '')
            else:
                args[i] = args[i].replace('>', '": {')
                args[i] = args[i].replace('<', '"')
    k = 1
    for i in range(len(args)):
        for j in range(len(args[i])):
            if args[i][j] == '/':
                b.append(args[i][:j] + ',')
                k = 0

        if k:
            b.append(args[i])
        k = 1

    for i in range(len(b)):
        if '},' in b[i]:
            b[i] = '        ' * b[i].count("\t") + b[i][b[i].index('},'):]
    for i in range(len(b) - 1):
        if '"' in b[i + 1]:
            continue
        else:
            b[i] = b[i].replace(',', '')
    for i in range(len(b)):
        if '\t' in b[i]:
            json.write('    ' * (b[i].count("\t") + 1) + b[i] + '\n')
        else:
            json.write('\t' + b[i] + '\n')
    json.write('}' + '\n')
    print("--- %s seconds ---" % (time.time() - start_time))
    xml.close()
    json.close()
