def encrypt(encryption_string,shift):
    enc_string=""
    for ch in encryption_string :
        if ord(ch)==122 or ord(ch)==90: #z or Z
            x = chr(ord(ch)-26+(shift%26))
            # print(ord(ch)-26+shift) 
            enc_string=enc_string+x
        elif ord(ch)==32: #space
            enc_string=enc_string+ch
        else:
            
            if ord(ch)>96 and (ord(ch)+(shift%26)<=122 and ord(ch)+(shift%26)>96): #if shift is less than z
                # print(ord(ch)+shift%26)
                x=chr(ord(ch)+(shift%26))
                enc_string=enc_string+x
            elif ord(ch)<=90 and (ord(ch)+(shift%26)<=90 and ord(ch)+(shift%26)>=65):#if shift is less than Z
                # print(ord(ch)+shift%26)
                x=chr(ord(ch)+(shift%26))
                enc_string=enc_string+x
            else:                       #if shift is greater than z or Z
                x=chr(ord(ch)+(shift%26)-26)      
                enc_string=enc_string+x
    return (enc_string)

def decrypt(encrypted_string,key):
    enc_string=""
    for ch in encrypted_string :
        if ord(ch)==97 or ord(ch)==65: #z or Z
            x = chr(ord(ch)+26-(key%26))
            enc_string=enc_string+x
        elif ord(ch)==32: #space
            enc_string=enc_string+ch
        else:
            
            if ord(ch)>96 and (ord(ch)-(key%26)>=97 and ord(ch)-(key%26)<=122): #if shift is less than z
                # print(ord(ch)+shift%26)
                x=chr(ord(ch)-(key%26))
                enc_string=enc_string+x
            elif ord(ch)<=90 and (ord(ch)-(key%26)>=65 and ord(ch)-(key%26)<=90):#if shift is less than Z
                # print(ord(ch)+shift%26)
                x=chr(ord(ch)-(key%26))
                enc_string=enc_string+x
            else:                       #if shift is greater than z or Z
                x=chr(ord(ch)-(key%26)+26)      
                enc_string=enc_string+x
    return (enc_string)
encryption_string = raw_input("Enter text to be encrypted")
shift = int(raw_input("Enter shift value"))
print(encrypt(encryption_string,shift))
encrypted_string = raw_input("Enter text to be decrypted")
key = int(raw_input("Enter key value"))
print(decrypt(encrypted_string,key))

