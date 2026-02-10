class FrequencyTracker:

    def __init__(self):
        self.d = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        f_number = self.d[number]    
        if f_number in self.freq:#deduct old
            self.freq[f_number] -= 1
            if self.freq[f_number] == 0:# if zero remove
                self.freq.pop(f_number)
        # add to d and to freq 
        self.d[number] += 1  
        f_number = self.d[number]  
        self.freq[f_number] += 1
        

    def deleteOne(self, number: int) -> None:
        f_number = self.d[number]    
        if f_number in self.freq:#deduct old
            self.freq[f_number] -= 1
            if self.freq[f_number] == 0:# if zero remove
                self.freq.pop(f_number)

        if number in self.d:
            self.d[number] -= 1

            if self.d[number] <= 0:
                self.d.pop(number)
            else:
                f_number = self.d[number]  
                self.freq[f_number] += 1
        
    def hasFrequency(self, frequency: int) -> bool:
       
        if frequency in self.freq:
            return True
        else:
            return False
