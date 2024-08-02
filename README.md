# 最長片道きっぷの旅 解答

## 想定条件

1. 駅間において、距離の異なる道は考慮していない(始点 1,終点 2 に距離が 2 の路線と 3 の路線が存在するなど)

2. 1→2→1 や 1→2→3→2 など同じ道を二度通ることは片道きっぷの条件に反すると判断し、考慮していない

3. ６の字になるような経路を考慮

## 使用言語

- Python

## ディレクトリ構成

<pre>
.
├── answer.py 
├── input.py 
└── README.md 
</pre>

## 動作確認方法

以下の方法で動作確認を行った。

1. input.txt に入力を記載

2. 以下のコマンドを実行

```
python3 answer.py < input.txt
```

※ コマンドラインに直接打ち込む場合、入力は一度に全ての行を入力することを想定しており、入力終了時には ctrl + D などで入力を終了する必要がある。
（入力される行が不明であるためこのような実装としている）

### 入力例

```
1, 2, 8.54
2, 3, 3.11
3, 1, 2.19
3, 4, 4
4, 1, 1.4
```

### 出力例

```
$ python3 answer.py < input.txt
4
3
2
1
3
```
