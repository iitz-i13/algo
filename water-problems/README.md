# Water devide problems を解くアルゴリズム
水差しが与えられ，その水差しを何回か移し替えて最終的に入っている水量を均等に分割することができるか判定し，その最小回数と操作状態を表示するアルゴリズム


## 実行の仕方（Usage）
```main.py```ファイルを実行

### 入力  
`n_jugs`: 水差しの数  
`n_splits`: 何個の平均を作るか  
`size of jug`: 水差しの最大容量  
`amount of jug`: 水差しのにある水量  

### 出力  
解がある場合  
```step```: 操作回数
```
操作回数: 水差しの状態
```
解がない場合  
```
can't find solutions
```

## 実行結果例（Result）

入力例①（Input）：
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

出力例①（Output）：  
```
step:  2
0: (4, 6, 4)
1: (1, 6, 7)
2: (0, 7, 7)
```

入力例②（Input）：
```
n_jugs:  3
n_splits:  2
size of jug 1: 10
size of jug 2: 10
size of jug 3: 10
amount of jug 1: 5
amount of jug 2: 5
amount of jug 3: 5
```

出力例②（Output）：   
解がない場合：  
```
can't find solutions
```
