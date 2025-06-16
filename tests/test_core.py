import pytest
from string_utils.core import to_snake_case

def test_to_snake_case():
    # 通常のケース
    assert to_snake_case("HelloWorld") == "hello_world"
    assert to_snake_case("SnakeCase") == "snake_case"
    
    # 空文字列のケース
    assert to_snake_case("") == ""
    
    # 単一文字のケース
    assert to_snake_case("A") == "a"
    assert to_snake_case("a") == "a"
    
    # 数字を含むケース
    assert to_snake_case("Test123") == "test123"
    
    # 特殊文字を含むケース
    assert to_snake_case("Hello_World") == "hello__world"
    
def test_to_camel_case():
    from string_utils.core import to_camel_case
    
    # 通常のケース
    assert to_camel_case("hello_world") == "helloWorld"
    assert to_camel_case("snake_case") == "snakeCase"
    
    # 空文字列のケース
    assert to_camel_case("") == ""
    
    # 単一文字のケース
    assert to_camel_case("a") == "a"
    assert to_camel_case("A") == "a"
    
    # 数字を含むケース
    assert to_camel_case("test_123") == "test123"
    
    # 特殊文字を含むケース
    assert to_camel_case("hello__world") == "helloWorld"
    
def test_is_palindrome():
    from string_utils.core import is_palindrome
    
    # 通常のケース
    assert is_palindrome("acbca") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("1a2b3c2a1") == True
    assert is_palindrome("123") == False
    
def test_reverse_words():
    from string_utils.core import reverse_words
    
    # 通常のケース
    assert reverse_words("Hello World") == "World Hello"
    assert reverse_words("Python is fun") == "fun is Python"
    
    # 空文字列のケース
    assert reverse_words("") == ""
    
    # 単一単語のケース
    assert reverse_words("Hello") == "Hello"
    
    # 数字を含むケース
    assert reverse_words("123 456") == "456 123"
    
    # 特殊文字を含むケース
    assert reverse_words("Hello, World!") == "World! Hello,"