from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        n = len(s)
        seen = set()
        repeated = set()
        i = 0
        while i + 9 < n:
            letter10 = s[i:i + 10]
            if  letter10 in seen:
                repeated.add(letter10)
            else:
                seen.add(letter10)
            i += 1
        
        return list(repeated)

solution = Solution()
print(solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))  # 出力: ["AAAAACCCCC","CCCCCAAAAA"]
print(solution.findRepeatedDnaSequences("AAAAAAAAAAAAA"))  # 出力: ["AAAAAAAAAA"]
print(solution.findRepeatedDnaSequences("ACGTACGTAC"))  # 出力: []
print(solution.findRepeatedDnaSequences("AAAAAAAAAA"))  # 出力: []
print(solution.findRepeatedDnaSequences("AAGTAAGTAAGT"))  # 出力: ["AAGTAAGTAA","AGTAAGTAAG"]
print(solution.findRepeatedDnaSequences("AGCTAGCTAGCTAGCT"))  # 出力: ["AGCTAGCTAG","GCTAGCTAGC","CTAGCTAGCT"]
print(solution.findRepeatedDnaSequences("TGCATGCATGCA"))  # 出力: ["TGCATGCATG","GCATGCATGC","CATGCATGCA"]
print(solution.findRepeatedDnaSequences("CCCCCCCCCCCC"))  # 出力: ["CCCCCCCCCC"]
print(solution.findRepeatedDnaSequences("GATTACAGATTACA"))  # 出力: ["GATTACAGAT","ATTACAGATT","TTACAGATTA","TTACAGATTAC","ACAGATTACA"]
print(solution.findRepeatedDnaSequences("ACGTACGTACGT"))  # 出力: ["ACGTACGTAC","CGT