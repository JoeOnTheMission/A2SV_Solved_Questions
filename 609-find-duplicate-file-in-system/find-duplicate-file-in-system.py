class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = {}
        for path in paths:
            directory = ""
            file_name = ""
            content = ""
            inD = True
            inF = False
            inC = False 
            for char in path:
                if inD:
                    if char == " ":
                        inD = False
                        inF = True
                    else:
                        directory += char
                elif inF:
                    if char == "(":
                        inF = False
                        inC = True
                    elif char != " ":
                        file_name += char
                elif inC:
                    if char == ")":
                        inC = False
                        inF = True
                        if content in d:
                            d[content].append([directory,file_name])
                        else:
                            d[content] = [[directory,file_name]]
                        file_name = ""
                        content = ""
                    else:
                        content += char
        res = []
        for content in d:
            if len(d[content]) > 1:#duplicate
                temp = []
                for dir,file in d[content]:
                    #print(content,dir + "/" + file)
                    temp.append(dir + "/" + file)
                res.append(temp)
        return res