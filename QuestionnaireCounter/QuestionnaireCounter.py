import re
f=open("1.re.txt")
result=list()
i=1
mode_on=False
for line in f.readlines():
    if(line.startswith("##")):
        mode_on=False
        continue
    if(line.startswith("#")):
        mode_on=True
        line=line[1:].strip()
        mode=re.compile(line)
        continue
    if(mode_on and len(line.strip())):
        if(re.match(r"^[0-9]+.",line.strip())):
            line=re.sub(r"^[0-9]+.", "", line.strip())
        if(mode.match(line.strip())):
            line=line.strip()
            line=str(i)+"."+line+"\n"
            result.append(line)
            i=i+1
        else:
            result.append(line)
    else:
        result.append(line)
fobj=open("2.txt",'w+')
fobj.writelines([x for x in result])
fobj.close()
print("OK")
