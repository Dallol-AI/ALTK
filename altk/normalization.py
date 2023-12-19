"""
Credit of Originality: Seid Muhie Yimam

Improved its implementation and added more normalization rules.
"""
import re

class AmharicNormalizer:
    def __init__(self, custom_rule: dict=None, merge=True):
        """
         Amharic Normalizer
        
        :param custom_rule (dict): add custom rules for normalization
        :param merge (bool): merge custom rules with the default rules if True, else override the default rules
        """
        
        if type(custom_rule) != dict:
            raise(TypeError("custom_rule must be a dictionary"))

        self.__replacements = {
            "ሀ": "ሃ", "ሐ": "ሃ", "ሓ": "ሃ", "ኅ": "ሃ", "ኻ": "ሃ", "ኃ": "ሃ",
            "ዅ": "ሁ", "ሗ": "ኋ", "ኁ": "ሁ", "ኂ": "ሂ", "ኄ": "ሄ", "ዄ": "ሄ", "ኅ": "ህ",
            "ኆ": "ሆ", "ሑ": "ሁ", "ሒ": "ሂ", "ሔ": "ሄ", "ሕ": "ህ", "ሖ": "ሆ", "ኾ": "ሆ",
            "ሠ": "ሰ", "ሡ": "ሱ", "ሢ": "ሲ", "ሣ": "ሳ", "ሤ": "ሴ", "ሥ": "ስ", "ሦ": "ሶ",
            "ዐ": "አ", "ዑ": "ኡ", "ዒ": "ኢ", "ዓ": "አ", "ኣ": "አ", "ዔ": "ኤ", "ዕ": "እ",
            "ዖ": "ኦ", "ፀ": "ጸ", "ፁ": "ጹ", "ጺ": "ፂ", "ጻ": "ፃ", "ጼ": "ፄ", "ፅ": "ጽ",
            "ፆ": "ጾ", "ሼ": "ሸ", "ሺ": "ሽ", "ዲ": "ድ", "ጄ": "ጀ", "ጂ": "ጅ", "ዉ": "ው",
            "ዎ": "ወ", "ዴ": "ደ", "ቼ": "ቸ", "ቺ": "ች", "ዬ": "የ", "ዪ": "ይ", "ጬ": "ጨ",
            "ጪ": "ጭ", "ኜ": "ኘ", "ኚ": "ኝ", "ዤ": "ዠ", "ዢ": "ዥ",
            "ሉ[ዋአ]": "ሏ", "ሙ[ዋአ]": "ሟ", "ቱ[ዋአ]": "ቷ", "ሩ[ዋአ]": "ሯ",
            "ሱ[ዋአ]": "ሷ", "ሹ[ዋአ]": "ሿ", "ቁ[ዋአ]": "ቋ", "ቡ[ዋአ]": "ቧ",
            "ቹ[ዋአ]": "ቿ", "ሁ[ዋአ]": "ኋ", "ኑ[ዋአ]": "ኗ", "ኙ[ዋአ]": "ኟ",
            "ኩ[ዋአ]": "ኳ", "ዙ[ዋአ]": "ዟ", "ጉ[ዋአ]": "ጓ", "ደ[ዋአ]": "ዷ",
            "ጡ[ዋአ]": "ጧ", "ጩ[ዋአ]": "ጯ", "ጹ[ዋአ]": "ጿ", "ፉ[ዋአ]": "ፏ",
            "[ቊ]": "ቁ", "[ኵ]": "ኩ", "\s+": " ",
        }
        
        if custom_rule:
            self.__replacements = self.__replacements.merge(custom_rule) if merge else custom_rule

    def normalize(self, text: str) -> str:
        """
        Apply normalization to the given text
        
        :param text (str): text to normalize
        :return: normalized text
        """
        for pattern, replacement in self.__replacements.items():
            text = re.sub(pattern, replacement, text)

        return text

