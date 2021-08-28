class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        start = 97
        dic = collections.defaultdict(set)
        four = set([5,7])
        for i in range(8):
            span = 3  if i not in four else 4
            for j in range(span):
                dic[i].add(chr(start+j))
            start += span
        res = []
        num = list(map(int, num))
        for word in words:
            for d,c in zip(num, word):
                if c not in dic[d-2]:
                    break
            else:
                res.append(word)
        return res
