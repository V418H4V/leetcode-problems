class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students = dict()
        sids = set()
        avg = dict()
        for sid, score in items:
            if sid not in students:
                students[sid] = [score]
                sids.add(sid)
            else:
                students[sid].append(score)
                
        for key, val in students.items():
            students[key] = sorted(val, reverse=True)
            ans  = 0
            for i in range(0, 5):
                ans += students[key][i]
            ans = ans // 5    
            avg[key] = ans
        
        # print(students)    
        # print(avg)
        
        ans = []
        for key in sids:
            ans.append([key, avg[key]])
        
        return ans