class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        dic = collections.defaultdict(collections.deque)
        for son,par in zip(pid, ppid):
            dic[par].append(son)
        if dic[0][0] == kill:
            return pid
        kills = set()
        kills.add(kill)
        stack = collections.deque(dic[kill])
        while stack:
            son = stack.pop()
            kills.add(son)
            if son in dic:
                stack.extend(dic[son])
        return list(kills)

        
