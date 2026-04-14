"""
TextConverter 單元測試
驗證繁簡轉換與變體切換是否如預期運作
"""

import pytest
from unittest.mock import MagicMock
from core.converter import TextConverter

@pytest.fixture
def mock_settings():
    settings = MagicMock()
    # 預設為不轉換
    settings.get_config.return_value = {"chineseVariant": "original"}
    return settings

def test_no_conversion(mock_settings):
    converter = TextConverter(mock_settings)
    text = "这是一個測試"
    assert converter.convert(text) == text

def test_s2t_conversion(mock_settings):
    # 設定為簡轉繁
    mock_settings.get_config.return_value = {"chineseVariant": "s2t"}
    converter = TextConverter(mock_settings)
    
    simple = "这是一个测试，软件正在运行"
    traditional = converter.convert(simple)
    
    # 基本繁體檢查
    assert "這是一個測試" in traditional
    assert "軟體" not in traditional # s2t 不會轉換用語

def test_s2twp_conversion(mock_settings):
    # 設定為台灣用語優化
    mock_settings.get_config.return_value = {"chineseVariant": "s2twp"}
    converter = TextConverter(mock_settings)
    
    simple = "這是一個測試，軟體正在運行" # 這裡輸入已經是繁體，測的是詞彙
    simple_with_terms = "软件正在运行，内存不足"
    traditional = converter.convert(simple_with_terms)
    
    assert "軟體" in traditional
    assert "記憶體" in traditional
    assert "軟體正在執行" in traditional

def test_variant_switching(mock_settings):
    converter = TextConverter(mock_settings)
    text = "软件"
    
    # 1. 原始模式
    mock_settings.get_config.return_value = {"chineseVariant": "original"}
    assert converter.convert(text) == "软件"
    
    # 2. 切換到 s2t
    mock_settings.get_config.return_value = {"chineseVariant": "s2t"}
    assert converter.convert(text) == "軟件"
    
    # 3. 切換到 s2twp
    mock_settings.get_config.return_value = {"chineseVariant": "s2twp"}
    assert converter.convert(text) == "軟體"

def test_empty_text(mock_settings):
    converter = TextConverter(mock_settings)
    assert converter.convert("") == ""
    assert converter.convert(None) is None
