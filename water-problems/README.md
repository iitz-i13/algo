# Water devide problems を解くアルゴリズム

## 実行の仕方（Usage）
`n_jugs`: 水差しの数  
`n_splits`: 何個の平均を作るか  
`size of jug`: 水差しの最大容量  
`amount of jug`: 水差しのにある水量  

## 実行結果（Result）

入力例（Input）：
```
n_jugs:  3
n_splits:  2
size of jug 1: 6
size of jug 2: 8
size of jug 3: 7
amount of jug 1: 4
amount of jug 2: 6
amount of jug 3: 4
```

出力例（Output）：  
解がある場合：
```
step:  2
0: (4, 6, 4)
1: (1, 6, 7)
2: (0, 7, 7)
```

解がない場合：
```
can't find solutions
```