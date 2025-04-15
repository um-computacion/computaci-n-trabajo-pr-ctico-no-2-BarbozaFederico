def is_palindrome(text) -> bool:
    text_a = text
    text = text_a[::-1]

    if text == text_a:
        return True
    elif text != text_a:
        return False
