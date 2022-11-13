def IsInt(_n):
    try:
        temp = int(_n)
        return True
    except Exception:
        return False
def Erase(_n):
    try:
        int(_n)
    except Exception:
        return "invalid value"
    global inString
    for i in range(_n):
        inString.pop(0)
    return
resultString = ""
global inString
inString = "22D7AC18FGD"
inString = list(inString)
parsedString = []
while(len(inString)>0):
    if(IsInt(inString[0]) and len(inString) > 1):
        if(IsInt(inString[0+1]) and len(inString) > 2):
            parsedString.append(int(inString[0]+inString[0+1]))
            parsedString.append(inString[0+2])
            Erase(3)
        else:
            parsedString.append(int(inString[0]))
            parsedString.append(inString[0+1])
            Erase(2)
    else:
        parsedString.append(1)
        parsedString.append(inString[0])
        Erase(1)
print(int(len(parsedString)/2))
for i in range(0, int(len(parsedString)/2)+2, 2):
    resultString = resultString + (parsedString[i] * parsedString [i+1])
print(resultString)






