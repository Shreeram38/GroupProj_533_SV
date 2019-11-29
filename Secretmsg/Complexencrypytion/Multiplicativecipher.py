class Multiplicativecipher:         
    def mulencrypt(self,msg,key):
        self.msg=msg
        self.key=key
        alphabet="abcdefghijklmnopqrstuvwxyz"
        newmsg=""
        flag=0
        if key%2==0 or key==1:
            print("key must be odd and greater than 1, within 26")
            return -1
        else:
            for character in self.msg:
                if character >= 'A' and character <= 'Z':
                    flag=1
                elif character >= 'a' and character <='z':
                    flag=0
                else:
                    flag=2
                if flag!=2:
                    character=character.lower()
                    pos=alphabet.find(character)
                    newpos=(pos*self.key)%26
                    newchar=alphabet[newpos]
                    if flag==1:
                        newchar=newchar.upper()
                else:
                    newchar=chr(ord(character)+self.key)
                newmsg+=newchar
            return newmsg
    
    def modulo_multiplicative_inverse(A, M):
        for i in range(0, M):
            if (A*i) % M == 1:
                return i
        return -1
    
    def muldecrypt(self,msg,key):
        self.msg=msg
        self.key=key
        alphabet="abcdefghijklmnopqrstuvwxyz"
        newmsg=""
        flag=0
        if key%2==0 or key==1:
            print("key must be odd and greater than 1, within 26")
            return -1
        else:
            for character in self.msg:
                if character >= 'A' and character <= 'Z':
                    flag=1
                elif character >= 'a' and character <='z':
                    flag=0
                else:
                    flag=2
                if flag!=2:
                    character=character.lower()
                    pos=alphabet.find(character)
                    ans=modulo_multiplicative_inverse(key, 26)
                    newpos=(pos*ans)%26
                    newchar=alphabet[newpos]
                    if flag==1:
                        newchar=newchar.upper()
                else:
                    newchar=chr(ord(character)-self.key)
                newmsg+=newchar
            return newmsg

c=Multiplicativecipher()
res=(c.mulencrypt("v is!'' !cd",3))
print(res," ",c.muldecrypt(res,3))