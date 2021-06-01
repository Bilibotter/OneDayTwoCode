class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if len(first) > len(second):
            first, second = second, first
        if len(second) - len(first) > 1:
            return False
        for j, c in enumerate(first):
            if c != second[j]:
                if len(first) == len(second):
                    return first[j+1:] == second[j+1:]
                else:
                    return second[j+1:] == first[j:]
        return True
