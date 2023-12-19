import re

# Source: https://www.researchgate.net/publication/344756957_PySBD_Pragmatic_Sentence_Boundary_Disambiguation

class Rule(object):
    def __init__(self, pattern, replacement):
        self.pattern = pattern
        self.replacement = replacement

    def __repr__(self):  # pragma: no cover
        return f'<{self.__class__.__name__} pattern="{self.pattern}" and replacement="{self.replacement}">'

# Define rules
NewLineInMiddleOfWordRule = Rule(r'\n(?=[\u1200-\u1248\u1250-\u1256\u1260-\u1288\u1290-\u12B0\u12C0-\u12C8\u12D0-\u12D6\u12E0-\u12F2\u1300-\u1342\u1350-\u137C]{1,2}\n)', '')
DoubleNewLineWithSpaceRule = Rule(r'\n \n', "\r")
DoubleNewLineRule = Rule(r'\n\n', "\r")

# https://rubular.com/r/EjupO3vKTiNkNs
NewLineFollowedBySentenceEndingRule = Rule(r'\n(?=።(\s|\n))', '') 

ReplaceNewlineWithCarriageReturnRule = Rule(r'\n', "\r")
EscapedNewLineRule = Rule(r'\\n', "\n")
EscapedCarriageReturnRule = Rule(r'\\r', "\r")
TypoEscapedNewLineRule = Rule(r'\\\ n', "\n")
TypoEscapedCarriageReturnRule = Rule(r'\\\ r', "\r")

InlineFormattingRule = Rule(r'{b\^&gt;\d*&lt;b\^}|{b\^>\d*<b\^}', '')

# https://rubular.com/r/BYeOZohszuZfhR
TableOfContentsRule = Rule(r'\.{4,}\s*([\d\u1369-\u137C]+-?[\d\u1369-\u137C]*)', "\r")
ConsecutivePeriodsRule = Rule(r'\.{5,}', ' ')
ConsecutiveForwardSlashRule = Rule(r'\/{3}', '')

# https://rubular.com/r/Hb0630k5sdGUpM
NO_SPACE_BETWEEN_SENTENCES_REGEX = r'(?<=[\u1200-\u137F])።(?=[\u1200-\u1248\u1250-\u1256\u1260-\u1288\u1290-\u12B0\u12C0-\u12C8\u12D0-\u12D6\u12E0-\u12F2\u1300-\u1342\u1350-\u137C])'
NoSpaceBetweenSentencesRule = Rule(NO_SPACE_BETWEEN_SENTENCES_REGEX, '። ')

# https://rubular.com/r/evfxyYN2mkoUJL
NO_SPACE_BETWEEN_SENTENCES_DIGIT_REGEX = r'(?<=[\d\u1369-\u137C])።(?=[\u1200-\u137F])'
NoSpaceBetweenSentencesDigitRule = Rule(NO_SPACE_BETWEEN_SENTENCES_DIGIT_REGEX, '። ')

URL_EMAIL_KEYWORDS = ['@', 'http', '.com', 'net', 'www', '//']
NEWLINE_IN_MIDDLE_OF_SENTENCE_REGEX = r'(?<=\s)\n(?=([\u1200-\u1248\u1250-\u1256\u1260-\u1288\u1290-\u12B0\u12C0-\u12C8\u12D0-\u12D6\u12E0-\u12F2\u1300-\u1342\u1350-\u137C]|\())'
NewLineFollowedByBulletRule = Rule(r"\n(?=•')", "\r")
QuotationsFirstRule = Rule(r"''", '"')
QuotationsSecondRule = Rule(r'``', '"')

RULES = [
    NewLineInMiddleOfWordRule,
    DoubleNewLineWithSpaceRule,
    DoubleNewLineRule,
    NewLineFollowedBySentenceEndingRule,
    ReplaceNewlineWithCarriageReturnRule,
    EscapedNewLineRule,
    EscapedCarriageReturnRule,
    TypoEscapedNewLineRule,
    TypoEscapedCarriageReturnRule,
    InlineFormattingRule,
    TableOfContentsRule,
    ConsecutivePeriodsRule,
    ConsecutiveForwardSlashRule,
    NoSpaceBetweenSentencesRule,
    NoSpaceBetweenSentencesDigitRule,
    NewLineFollowedByBulletRule,
    QuotationsFirstRule,
    QuotationsSecondRule,
]

def apply_rules(text, rules):
    for rule in rules:
        text = re.sub(rule.pattern, rule.replacement, text)
    return text