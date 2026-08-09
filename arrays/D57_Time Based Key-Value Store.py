class TimeMap:

    def __init__(self):
        self.store={}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        value=self.store[key]
        lo=0
        hi=len(value)-1
        answer=""
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if value[mid][0] <= timestamp:
                answer= value[mid][1]
                lo=mid+1
            else:
                hi=mid-1
        return answer             


        
