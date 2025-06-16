def to_snake_case(text: str) -> str:
    """
    Convert a string to snake_case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The converted string in snake_case.
    """
    return ''.join(['_' + c.lower() if c.isupper() else c for c in text]).lstrip('_')

