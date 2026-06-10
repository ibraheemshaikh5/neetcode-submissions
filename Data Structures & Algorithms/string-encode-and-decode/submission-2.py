class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in range(len(strs) - 1):
            output += strs[i]
            output += '\n'
        
        # edgecase for last string
        if (len(strs) != 1):
            output += strs[len(strs) - 1]

        return output 

    def decode(self, s: str) -> List[str]:
        word_num = 0
        result = [""]
        
        for char in s:
            if char == '\n':
                word_num += 1
                result.append("")
            else:
                result[word_num] += char

        return result