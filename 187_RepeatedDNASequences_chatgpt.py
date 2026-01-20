class Solution:
    def findRepeatedDnaSequences(self, s: str):
        if len(s) < 10:
            return []

        encode = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        seen = set()
        repeated = set()

        hash_val = 0
        mask = (1 << 20) - 1  # 20ビット分だけ残す

        for i in range(len(s)):
            hash_val = ((hash_val << 2) | encode[s[i]]) & mask

            if i >= 9:
                if hash_val in seen:
                    repeated.add(s[i-9:i+1])
                else:
                    seen.add(hash_val)

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