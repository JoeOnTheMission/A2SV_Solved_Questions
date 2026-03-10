class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for op in logs:
    
            if op == "../":
                if stack:# not at the main directiory 
                    stack.pop()
            elif op == "./":
                continue
            else:
                stack.append(op)
    
        return len(stack)
                

