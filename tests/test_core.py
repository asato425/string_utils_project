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