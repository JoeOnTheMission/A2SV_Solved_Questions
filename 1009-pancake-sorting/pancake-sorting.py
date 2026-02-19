class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        s = sorted(arr)
        j = len(arr)-1
        res = []
        for last_index in range(len(arr)-1,-1,-1):
            
            i = 0 
            sub_arr = []
            while arr[i] != s[last_index]:# the num i want to put at last_index
                i += 1
            if i == last_index:
                continue
            
            if i != 0 and i != last_index:# put that num at 0
                res.append(i+1)
                #fliping at i+1
                sub_arr = arr[:i+1]
                sub_arr.reverse()
                sub_arr.extend(arr[i+1:])
                arr = sub_arr
                i = 0
            if i == 0:# put that num at last_index
                res.append(last_index+1)
                #fliping at j
                sub_arr = arr[:last_index+1]
                sub_arr.reverse()
                sub_arr.extend(arr[last_index+1:])
                arr = sub_arr 
        return res