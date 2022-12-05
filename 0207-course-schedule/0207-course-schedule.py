class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap ={i: [] for i in range(numCourses)}
        visit =set()
         
        for c, p in prerequisites:
            premap[c].append(p)
        
        def dfs(c):
            if c in visit:
                return False
            if not premap[c]:
                return True
            
            visit.add(c)
            for p in premap[c]:
                if not dfs(p): return False
                
            visit.remove(c)
            premap[c]=[]
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):return False
            
        return True
            
            
            
        