# -*- coding: utf-8 -*-
"""统计《正文/第一卷》各章字数：汉字数、含中文标点的字符数（Word口径）、不含空白总字符数"""
import os
import re
import unicodedata

DIR = r"D:\Users\yueguang\AIProject\AIBook3\正文\第一卷"

def is_cjk(ch):
    return '\u4e00' <= ch <= '\u9fff' or '\u3400' <= ch <= '\u4dbf' or '\uf900' <= ch <= '\ufaff'

def is_zh_punct(ch):
    # 常用中文标点（全角）
    return unicodedata.category(ch) == 'Po' and (ord(ch) > 0x2000) or ch in '，。！？；：“”‘’（）《》【】、——…·'

def stats(text):
    han = 0          # 汉字数
    zh_chars = 0     # 汉字 + 中文标点 + 数字 + 英文（近似 Word 字数，不含空白）
    non_blank = 0    # 去除空白字符后的总字符数
    for ch in text:
        if ch.isspace():
            continue
        non_blank += 1
        if is_cjk(ch):
            han += 1
            zh_chars += 1
        elif is_zh_punct(ch):
            zh_chars += 1
        elif ch.isalnum():
            zh_chars += 1
    return han, zh_chars, non_blank

files = []
for fn in os.listdir(DIR):
    if fn.lower().endswith('.md'):
        files.append(fn)

files.sort(key=lambda x: int(re.search(r'第(\d+)章', x).group(1)) if re.search(r'第(\d+)章', x) else 999)

rows = []
tot_han = tot_zh = tot_nb = 0
for fn in files:
    p = os.path.join(DIR, fn)
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
    han, zh, nb = stats(text)
    rows.append((fn, han, zh, nb))
    tot_han += han; tot_zh += zh; tot_nb += nb

print(f"{'章节文件':<40}{'汉字数':>8}{'含标点字符数':>12}{'非空白字符数':>12}")
print('-' * 76)
for fn, han, zh, nb in rows:
    print(f"{fn:<40}{han:>8,}{zh:>12,}{nb:>12,}")
print('-' * 76)
print(f"{'合计':<40}{tot_han:>8,}{tot_zh:>12,}{tot_nb:>12,}")
print(f"\n章节数: {len(rows)}")
