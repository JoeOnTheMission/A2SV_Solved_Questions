class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        inBlock = False
        newline = ""

        for line in source:
            i = 0
            while i < len(line):
                if inBlock:
                    if line[i] == "*" and i+1 < len(line) and line[i+1] == "/":
                        inBlock = False
                        i += 2
                    else:
                        i += 1
                else: # not in Block
                    if line[i] == "/" and i+1 < len(line):
                        if line[i+1] == "/":
                            break 
                        elif line[i+1] == "*":
                            inBlock = True
                            i += 2
                        else:
                            newline += line[i]
                            i += 1
                    else:
                        newline += line[i]
                        i += 1
            if not inBlock and newline:
                    res.append(newline)
                    newline = ""
        return res
                    
