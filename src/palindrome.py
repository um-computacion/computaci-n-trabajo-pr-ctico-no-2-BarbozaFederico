def is_palindrome(text:str) -> bool:
    import string 
    text = text.lower()
    text = text.replace(" ","") 
    text = text.translate(str.maketrans("", "", string.punctuation))
    text_a = text
    text = text_a[::-1]
    
    if text == text_a:
        return True
    elif text != text_a:
        return False
    