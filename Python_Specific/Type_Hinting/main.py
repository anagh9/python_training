def ceaser(text: str,key: str):
    result = ""
    for char in text:
        c :int = ord(char)
        enc_char : str  = chr(c+key)
        result += enc_char
    return result

print(ceaser("subscribe",2))
print(ceaser("ANagh",-2))