class Reversecipher: 
        
    def revencrypt(self,msg):
        self.msg=msg
        res=self.msg[::-1]
        return res
    
    def revdecrypt(self,msg):
        self.msg=msg
        res=self.msg[::-1]
        return res