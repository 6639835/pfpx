# STAR 程序（标准仪表进场）

标准仪表进场程序（STAR）

## 格式结构

```
STR ICAORRR  DDDDDDWWWWWWNNNNNPPPPPPTTTTTTT ±LLLLLLLLL±LLLLLLLLLR
```

## 示例记录

```
STR YWLMALL  319972094283EKIPUIVTA1REKIPU -33207250+1517406671
STR YWLMALL  319973258035IVTAGIVTA1REKIPU -33038028+1517578331
STR YWLMALL  319974094930OVLUXIVTA1ROVLUX -33173056+1516178061
STR YWLMALL  319975258035IVTAGIVTA1ROVLUX -33038028+1517578331
STR YWLMALL  319976095000PUDUTIVTA1RPUDUT -32961389+1514733061
STR YWLMALL  319977258035IVTAGIVTA1RPUDUT -33038028+1517578331
STR YWLM30   319978258035IVTAGIVTA1R      -33038028+1517578331
STR YWLM30   319979258061UBGIMIVTA1R      -32942194+1518618331
```

## 字段分解

| 字段         | 含义                     | 备注 / 示例 |
|--------------|--------------------------|-------------|
| `STR`        | 进场程序标识             | 固定值，表示该条记录为 STAR |
| `YWLM`       | ICAO 代码                |  |
| `ALL`        | 跑道号                   | ALL = 所有跑道；xxB = xxL / xxC / xxR |
| `319972`     | STAR 数据库 ID            |  |
| `094283`     | 航路点 ID（当前行）      |  |
| `EKIPU`      | 航路点名称（当前行）     |  |
| `IVTA1R`     | 程序识别码               |  |
| `EKIPU`      | 程序过渡点               | 若有过渡点，则填入其名称 |
| `+40073450`  | 纬度（当前航路点）       |  |
| `+116574192` | 经度（当前航路点）       |  |
| `1`          | 是否 RNAV 程序           | 0 = 否，1 = 是 |

## 跑道编号

### 格式示例
- **特定跑道**：`30`、`12`、`06R` - 适用于单跑道
- **多跑道**：`ALL` - 适用于所有跑道  
- **分组跑道**：`36B` - 适用于 36L/36C/36R

## 特殊情况

### 航段起点定义
每个 STR 程序必须在第一行定义航段起点

示例：

```
STR ZGSZALL  322166098018BEKOLBEK1XA      +22543333+1141333330
STR ZGSZ15   322167098018BEKOLBEK1XA      +22543333+1141333330
STR ZGSZ15   322168259574CEN45BEK1XA      +22691161+1140501530
STR ZGSZ16   322169098018BEKOLBEK1XA      +22543333+1141333330
STR ZGSZ16   322170259574CEN45BEK1XA      +22691161+1140501530
```

> `BEKOL`表示该进场程序起点
> 

### 不同跑道航段
如果同一进场程序对应多个跑道，需要根据跑道编号分别列出所有航段

示例：

```
STR ZBAAALL  320182097915OSUBAOSUB7X      +40736389+1170372221
STR ZBAAALL  320183258281AA169OSUB7X      +40680611+1169732221
STR ZBAAALL  320184258278AA166OSUB7X      +40419722+1166791671
STR ZBAAALL  320185258277AA165OSUB7X      +40119222+1167258061
STR ZBAAALL  320186258264AA142OSUB7X      +40038056+1167383331
STR ZBAA01   320187258264AA142OSUB7X      +40038056+1167383331
STR ZBAA01   320188258263AA141OSUB7X      +39685972+1167923891
STR ZBAA36B  320189258264AA142OSUB7X      +40038056+1167383331
STR ZBAA36B  320190258263AA141OSUB7X      +39685972+1167923891
```

## 数据集成

STAR 程序连接到其他导航数据段：

- **[航路](./airways.md)**：来自航路结构的进入点
- **[航路点](./waypoints.md)**：STAR 路线中的导航点
- **[跑道](./runways.md)**：进场的目标跑道

## 下一步

- **[复习 SID 程序](./sid-procedures.md)** - 离场程序补充
- **[理解航路点](./waypoints.md)** - STAR 导航点
- **[使用分析工具](../tools/examples.md)** - 提取和分析 STAR 数据