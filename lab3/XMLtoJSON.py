#xml = open(r"C:\Users\kater\Desktop\XML.txt", 'r')
with open(r"C:\Users\kater\Desktop\XML.txt", 'r', encoding="UTF-8") as xml:
    json=open(r"C:\Users\kater\Desktop\fileWrite.txt",'w')
    xml.readline()
    args = xml.read().split('\n')
    b=[]
    power=0
    k=0
    for i in range(len(args)):
        if args[i].count('<')>1:
            args[i]=args[i].replace('>','":"')
            args[i] = args[i].replace('<', '"')
        else:
            if '/' in args[i]:
                if  i!=len(args):
                    args[i] = args[i].replace('>', '},')
                else:
                    args[i] = args[i].replace('>', '}')
                args[i] = args[i].replace('</', '')
            else:
                args[i]=args[i].replace('>','": {')
                args[i]=args[i].replace('<','"')
    k=1
    for i in range(len(args)):
        for j in range(len(args[i])):
            if args[i][j]=='/':
                b.append(args[i][:j]+',')
                k=0
            
        if k:
            b.append(args[i])
        k=1

    for i in range(len(b)):
        if '},' in b[i]:
            b[i] = '        '*(b[i].count("\t")+1)+b[i][b[i].index('},'):]

    for i in range(len(b)):
        if '\t' in b[i]:
            json.write('    '*b[i].count("\t")  + b[i] + '\n' )
        else:
            json.write(b[i]+'\n')

    xml.close()
    json.close()