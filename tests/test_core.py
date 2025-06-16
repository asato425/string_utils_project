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