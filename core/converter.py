"""
文字轉換模組
使用 OpenCC 進行繁簡轉換與用語優化
"""

import logging
from opencc import OpenCC

logger = logging.getLogger("VoiceType.Converter")

# 支援的轉換模式對照表
# 鍵值為 settings 中的 chineseVariant，值為 OpenCC 的設定檔名
CONFIG_MAP = {
    "s2t": "s2t",      # 簡轉繁（標準）
    "t2s": "t2s",      # 繁轉簡（標準）
    "s2twp": "s2twp",  # 簡轉繁（台灣標準，含慣用語轉換）
    "s2hk": "s2hk",    # 簡轉繁（香港標準）
    "t2jp": "t2jp",    # 繁體漢字轉日文新字體
}

class TextConverter:
    """文字轉換引擎"""

    def __init__(self, settings):
        self.settings = settings
        self._current_variant = None
        self._opencc = None

    def _get_opencc(self, variant: str) -> OpenCC | None:
        """根據變體獲取或初始化 OpenCC 實例"""
        if variant == "original" or variant not in CONFIG_MAP:
            return None
        
        # 如果變體沒變，且實例已存在，直接回傳
        if variant == self._current_variant and self._opencc:
            return self._opencc

        try:
            config_file = CONFIG_MAP[variant]
            self._opencc = OpenCC(config_file)
            self._current_variant = variant
            logger.info("Initialized OpenCC with config: %s", config_file)
            return self._opencc
        except Exception as e:
            logger.error("Failed to initialize OpenCC with %s: %s", variant, e)
            return None

    def convert(self, text: str) -> str:
        """執行轉換"""
        if not text:
            return text

        variant = self.settings.get_config().get("chineseVariant", "original")
        
        converter = self._get_opencc(variant)
        if not converter:
            return text

        try:
            converted = converter.convert(text)
            logger.info("Converted text using variant: %s", variant)
            return converted
        except Exception as e:
            logger.error("Conversion failed: %s", e)
            return text
