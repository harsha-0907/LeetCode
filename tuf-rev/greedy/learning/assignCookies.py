class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g); s = sorted(s); cnt = 0; g_pos = 0; g_length = len(g)
        for s_pos in range(len(s)):
            if g_pos < g_length:
                if s[s_pos] >= g[g_pos]:
                    cnt += 1
                    g_pos += 1
            else:
                break
        return cnt
            

        