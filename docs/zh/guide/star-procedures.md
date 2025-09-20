# STAR 程序（标准仪表进场）

标准仪表进场程序（STAR）

## 格式结构

```
STR ICAORRR  DDDDDDWWWWWWNNNNNPPPPPPTTTTTTT ±LLLLLLLLL±LLLLLLLLLS
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


## 编程示例

### Python 解析器

```python
import re

def parse_star(line):
    """解析 STAR 程序记录。"""
    # STR YWLMALL  319972094283EKIPUIVTA1REKIPU -33207250+1517406671
    pattern = r'STR (\w{4})(\w+)\s+(\d{6})(\d{6})(\w+)(\w+)(\w+) ([+-]\d{8,9})([+-]\d{8,9})(\d)'
    
    match = re.match(pattern, line)
    if match:
        return {
            'airport': match.group(1),
            'runway': match.group(2),
            'procedure_id': match.group(3),
            'waypoint_id': match.group(4),
            'waypoint_name': match.group(5),
            'star_name': match.group(6),
            'transition': match.group(7),
            'latitude': int(match.group(8)) / 1_000_000,
            'longitude': int(match.group(9)) / 1_000_000,
            'rnav': bool(int(match.group(10)))
        }
    return None

# 使用方法
star = parse_star("STR YWLMALL  319972094283EKIPUIVTA1REKIPU...")
print(f"STAR {star['star_name']} 到 {star['airport']} 跑道 {star['runway']}")
```

### 构建进场路线

```python
from collections import defaultdict

def build_star_routes(star_lines):
    """从单个记录构建完整的 STAR 路线。"""
    procedures = defaultdict(list)
    
    for line in star_lines:
        if line.startswith('STR'):
            star = parse_star(line)
            if star:
                # 按程序和过渡分组
                key = f"{star['airport']}-{star['runway']}-{star['star_name']}-{star['transition']}"
                procedures[key].append(star)
    
    # 按程序 ID 排序航路点（顺序）
    for key in procedures:
        procedures[key].sort(key=lambda x: x['procedure_id'])
    
    return dict(procedures)
```

### 分析进场流量

```python
def analyze_arrival_flows(star_lines, airport_icao):
    """分析机场的进场模式。"""
    arrival_data = {
        'transitions': defaultdict(set),
        'runway_stars': defaultdict(set),
        'total_procedures': 0
    }
    
    for line in star_lines:
        if line.startswith('STR'):
            star = parse_star(line)
            if star and star['airport'] == airport_icao:
                # 跟踪过渡
                arrival_data['transitions'][star['transition']].add(star['star_name'])
                
                # 跟踪跑道分配
                arrival_data['runway_stars'][star['runway']].add(star['star_name'])
                
                arrival_data['total_procedures'] += 1
    
    return arrival_data

# 使用方法
flows = analyze_arrival_flows(star_lines, "YWLM")
print(f"{airport_icao} 进场分析")
for transition, stars in flows['transitions'].items():
    print(f"过渡 {transition}：{', '.join(stars)}")
```

## 路线连续性

### 初始进近定位点定义
每个 STAR 的第一个航路点定义进入点：

```python
def find_initial_approach_fixes(star_routes):
    """查找 STAR 程序的初始进近定位点。"""
    iaf_points = {}
    
    for route_key, waypoints in star_routes.items():
        if waypoints:
            # 第一个航路点是 IAF
            first_waypoint = min(waypoints, key=lambda x: x['procedure_id'])
            iaf_points[route_key] = {
                'name': first_waypoint['waypoint_name'],
                'latitude': first_waypoint['latitude'],
                'longitude': first_waypoint['longitude']
            }
    
    return iaf_points
```

### 多跑道路由

STAR 程序通常为多个跑道提供服务，并有不同的最终段：

```python
def group_stars_by_runway(star_routes):
    """按目标跑道分组 STAR 路线。"""
    runway_groups = defaultdict(list)
    
    for route_key, waypoints in star_routes.items():
        # 从路线密钥提取跑道
        airport, runway, star_name, transition = route_key.split('-')
        runway_groups[runway].append({
            'star_name': star_name,
            'transition': transition,
            'waypoints': waypoints
        })
    
    return dict(runway_groups)
```

## 验证和分析

### 路线验证

```python
def validate_star_sequence(waypoints):
    """验证 STAR 航路点序列。"""
    issues = []
    
    if not waypoints:
        return ["未找到航路点"]
    
    # 检查正确的顺序
    ids = [wp['procedure_id'] for wp in waypoints]
    if ids != sorted(ids):
        issues.append("航路点不按顺序排列")
    
    # 检查合理的距离
    for i in range(len(waypoints) - 1):
        wp1 = waypoints[i]
        wp2 = waypoints[i + 1]
        
        distance = calculate_distance(
            wp1['latitude'], wp1['longitude'],
            wp2['latitude'], wp2['longitude']
        )
        
        if distance > 200:  # 航路点间超过 200 海里
            issues.append(f"{wp1['waypoint_name']} 和 {wp2['waypoint_name']} 之间间隙过大：{distance:.1f}海里")
    
    return issues
```

### 过渡分析

```python
def analyze_star_transitions(star_routes):
    """分析 STAR 过渡模式。"""
    transition_stats = defaultdict(lambda: {
        'count': 0,
        'airports': set(),
        'runways': set()
    })
    
    for route_key, waypoints in star_routes.items():
        airport, runway, star_name, transition = route_key.split('-')
        
        stats = transition_stats[transition]
        stats['count'] += 1
        stats['airports'].add(airport)
        stats['runways'].add(f"{airport}-{runway}")
    
    # 转换集合为列表以便显示
    result = {}
    for transition, stats in transition_stats.items():
        result[transition] = {
            'count': stats['count'],
            'airports': list(stats['airports']),
            'runways': list(stats['runways'])
        }
    
    return result
```

## 与其他数据的集成

### 连接到航路

```python
def find_star_airway_connections(star_routes, airway_data):
    """查找 STAR 和航路之间的连接。"""
    connections = []
    
    for route_key, star_waypoints in star_routes.items():
        if not star_waypoints:
            continue
            
        # 获取初始进近定位点
        iaf = min(star_waypoints, key=lambda x: x['procedure_id'])
        iaf_pos = (iaf['latitude'], iaf['longitude'])
        
        # 查找附近的航路端点
        for airway in airway_data:
            airway_end = (airway['end_lat'], airway['end_lon'])
            
            distance = calculate_distance(
                iaf_pos[0], iaf_pos[1],
                airway_end[0], airway_end[1]
            )
            
            if distance < 5:  # 5 海里内
                connections.append({
                    'star': route_key,
                    'airway': airway['route_id'],
                    'distance': distance,
                    'connection_point': iaf['waypoint_name']
                })
    
    return connections
```

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

## 总结

STAR 程序提供结构化的进场路由，可以：

- **标准化**进入机场的进场流量
- **减少**飞行员和管制员的工作负荷  
- **提高**效率和安全性
- **连接**航路结构到终端区
- **支持**常规和 RNAV 导航
