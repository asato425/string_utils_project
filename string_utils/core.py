def to_snake_case(text: str) -> str:
    """
    Convert a string to snake_case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The converted string in snake_case.
    """
    return ''.join(['_' + c.lower() if c.isupper() else c for c in text]).lstrip('_')

def to_camel_case(text: str) -> str:
    """
    Convert a string to camelCase.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The converted string in camelCase.
    """
    parts = text.split('_')
    return parts[0].lower() + ''.join(part.capitalize() for part in parts[1:])

def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome.
    
    Args:
        text (str): The input string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned_text == cleaned_text[::-1]

def reverse_words(text: str) -> str:
    """
    Reverse the order of words in a string.
    
    Args:
        text (str): The input string to reverse.
    
    Returns:
        str: The string with words in reverse order.
    """
    return ' '.join(text.split()[::-1])

