# class TimeMap:

#     def __init__(self):
#         self.timemap_dict=dict()
        

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.timemap_dict:
#             self.timemap_dict[key]=[(timestamp,value)]
#         else:
#             self.timemap_dict[key].append((timestamp,value))
#         # print(self.timemap_dict)
        

#     def get(self, key: str, timestamp: int) -> str:

#         # for k,v in self.timemap_dict:
#         #     print(k,v[0])
#         arr=[]
#         if key in self.timemap_dict:
#             for i in range(0,len(self.timemap_dict[key])):
#                 arr.append(self.timemap_dict[key][i][0])
#         else:
#             return ""
#         # print(arr)
        
#         if(len(arr)==1):
#             return self.timemap_dict[key][0][1]
#         elif timestamp<arr[0]:
#             return ""
#         else:
#             l=0
#             r=len(arr)-1
#             res=""
#             while l<=r:
#                 mid = (l+r)//2
#                 if timestamp>=arr[mid]:
#                     l=mid+1
#                     res=self.timemap_dict[key][mid][1]
#                 else:
#                     r=mid-1
#         # print("ind",ind)

#         return res
        


# # Your TimeMap object will be instantiated and called as such:
# # obj = TimeMap()
# # obj.set(key,value,timestamp)
# # param_2 = obj.get(key,timestamp)

class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([value , timestamp])
        # print(self.dic)

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.dic.get(key , [])
        # print(values)
        l , r = 0 , len(values) - 1
        while l <= r :
            mid = (l + r) //2
            if values[mid][1] <= timestamp:
                l = mid + 1
                res = values[mid][0]
            else:
                r = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# class TimeMap:

#     def __init__(self):
#         self.structure = {}
        

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.structure:
#             self.structure[key] = []
#         self.structure[key].append([value, timestamp])
        

#     def get(self, key: str, timestamp: int) -> str:
#         ans = ""
#         temp = self.structure.get(key, [])

#         low, high = 0, len(temp) - 1
#         while low <= high:
#             mid = (low + high) // 2

#             if temp[mid][1] <= timestamp:
#                 ans = temp[mid][0]
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return ans