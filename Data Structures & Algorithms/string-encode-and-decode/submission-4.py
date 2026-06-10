class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        if (len(strs) != 0):
            output += strs[0]

            for i in range(1, len(strs)):
                output += '\n'
                output += strs[i]

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