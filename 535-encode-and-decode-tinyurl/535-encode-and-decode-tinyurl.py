import string
import random

class Codec:
    
    
    dictionary = {}
    characters = list(string.ascii_letters + string.digits)
    
    def pass_generator(self):
        
        random.shuffle(self.characters)
        
        password = []
        for i in range(5):
            password.append(random.choice(self.characters))
        
        return "".join(password)
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortened = self.pass_generator()
        self.dictionary[longUrl] = "http://tinyurl.com/"+shortened
        print(self.dictionary)
        return self.dictionary[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        keys = [k for k,v in self.dictionary.items() if v==shortUrl]
        if keys:
            return keys[0]
        return ""
         
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))