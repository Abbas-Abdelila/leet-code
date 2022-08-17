class Solution(object):
    def uniqueMorseRepresentations(self, words):
        
        res = []
        
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        
        for word in words:
            code = ""
            for ch in word:
                code += morse_code[ord(ch)-ord('a')] #gets the right moorse "ord" returns ASCII
            
            if code not in res:
                res.append(code)
        
        return len(res)
            