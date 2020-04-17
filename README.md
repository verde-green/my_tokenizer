# my_tokenizer

自分用の形態素解析器(MeCabとJumanのみ)のラッパーです

## 使い方
```python
from tokenizer import MeCabTokenizer, JumanTokenizer

# MeCab
# ------------------------------------------------
# 分かち書き
m = MeCabTokenizer()
m.parse("今日も天気がいい。")
# => ['今日', 'も', '天気', 'が', 'いい', '。']

# 除外する品詞を指定
m.parse("今日も天気がいい。", out=["助詞", "記号"])
# => ['今日', '天気', 'いい']

# 辞書を指定する場合
m = MeCabTokenizer(dict_path="<dict_path>")

# Juman(Jumanpp)
# ------------------------------------------------
# 分かち書き
j = JumanTokenizer()
j.parse("今日も天気がいい。")
# => ['今日', 'も', '天気', 'が', 'いい', '。']

# 除外する品詞を指定
j.parse("今日も天気がいい。", out=["助詞", "記号"])
# => ['今日', '天気', 'いい']
```
