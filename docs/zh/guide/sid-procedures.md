# SID 程序（标准仪表离场）

标准仪表离场程序（SID）

## 格式结构

```
SID ICAORRR  DDDDDDWWWWWWNNNNNPPPPPPTTTTTTT ±LLLLLLLLL±LLLLLLLLLS
```

## 示例记录

```
SID RJNAALL  101992213869TALMITALMI4KAMMY +35471000+1366238140
SID RJNAALL  101993213858HEIANTALMI4KAMMY +35346375+1357621190
SID RJNAALL  101994075088KAMMYTALMI4KAMMY +34991006+1346885330
SID RJNAALL  101995213869TALMITALMI4PIONE +35471000+1366238140
SID RJNAALL  101996213858HEIANTALMI4PIONE +35346375+1357621190
SID RJNAALL  101997075867WAKITTALMI4PIONE +35032736+1349255530
SID RJNAALL  101998075515PIONETALMI4PIONE +34671378+1340151310
SID RJNAALL  101999213869TALMITALMI4WAKIT +35471000+1366238140
SID RJNAALL  102000213858HEIANTALMI4WAKIT +35346375+1357621190
SID RJNAALL  102001075867WAKITTALMI4WAKIT +35032736+1349255530
```

## 字段分解

| 字段         | 含义                     | 备注 / 示例 |
|--------------|--------------------------|-------------|
| `SID`        | 离场程序标识             | 固定值，表示该条记录为 SID |
| `RJNA`       | ICAO 代码                |  |
| `ALL`        | 跑道号                   | ALL = 所有跑道；xxB = xxL / xxC / xxR |
| `101992`     | SID 数据库 ID            |  |
| `213869`     | 航路点 ID（当前行）      |  |
| `TALMI`      | 航路点名称（当前行）     |  |
| `TALMI4`     | 程序识别码               |  |
| `KAMMY`      | 程序过渡点               | 若有过渡点，则填入其名称 |
| `+40073450`  | 纬度（当前航路点）       |  |
| `+116574192` | 经度（当前航路点）       |  |
| `0`          | 是否 RNAV 程序           | 0 = 否，1 = 是 |

## 跑道编号

### 标准格式
- **特定跑道**：`01`、`36`、`27L` - 适用于单跑道
- **多跑道**：`ALL` - 适用于所有跑道
- **分组跑道**：`36B` - 适用于 36L/36C/36R

### 示例
```
SID ZBAA01   ... → 跑道 01 特定
SID ZBAAALL  ... → 所有跑道
SID ZBAA36B  ... → 跑道 36L、36C、36R
```

## 编程示例

### Python 解析器

```python
import re

def parse_sid(line):
    """解析 SID 程序记录。"""
    # SID RJNAALL  101992213869TALMITALMI4KAMMY +35471000+1366238140
    pattern = r'SID (\w{4})(\w+)\s+(\d{6})(\d{6})(\w+)(\w+)(\w+) ([+-]\d{8,9})([+-]\d{8,9})(\d)'
    
    match = re.match(pattern, line)
    if match:
        return {
            'airport': match.group(1),
            'runway': match.group(2),
            'procedure_id': match.group(3),
            'waypoint_id': match.group(4),
            'waypoint_name': match.group(5),
            'sid_name': match.group(6),
            'transition': match.group(7),
            'latitude': int(match.group(8)) / 1_000_000,
            'longitude': int(match.group(9)) / 1_000_000,
            'rnav': bool(int(match.group(10)))
        }
    return None

# 使用方法
sid = parse_sid("SID RJNAALL  101992213869TALMITALMI4KAMMY...")
print(f"SID {sid['sid_name']} 从 {sid['airport']} 跑道 {sid['runway']}")
```

### 构建程序路线

```python
from collections import defaultdict

def build_sid_routes(sid_lines):
    """从单个记录构建完整的 SID 路线。"""
    procedures = defaultdict(list)
    
    for line in sid_lines:
        if line.startswith('SID'):
            sid = parse_sid(line)
            if sid:
                # 按程序和过渡分组
                key = f"{sid['airport']}-{sid['runway']}-{sid['sid_name']}-{sid['transition']}"
                procedures[key].append(sid)
    
    # 按程序 ID 排序航路点（顺序）
    for key in procedures:
        procedures[key].sort(key=lambda x: x['procedure_id'])
    
    return dict(procedures)
```

### 提取航路点序列

```python
def get_waypoint_sequence(sid_route):
    """提取 SID 路线的有序航路点序列。"""
    waypoints = []
    
    for waypoint in sorted(sid_route, key=lambda x: x['procedure_id']):
        waypoints.append({
            'name': waypoint['waypoint_name'],
            'latitude': waypoint['latitude'],
            'longitude': waypoint['longitude'],
            'sequence': len(waypoints) + 1
        })
    
    return waypoints

# 使用方法
routes = build_sid_routes(sid_lines)
for route_key, route_data in routes.items():
    waypoints = get_waypoint_sequence(route_data)
    print(f"路线 {route_key}：")
    for wp in waypoints:
        print(f"  {wp['sequence']}. {wp['name']} ({wp['latitude']:.6f}, {wp['longitude']:.6f})")
```

## 分析示例

### 机场 SID 汇总

```python
def analyze_airport_sids(sid_lines, airport_icao):
    """分析特定机场的所有 SID。"""
    airport_sids = defaultdict(set)
    
    for line in sid_lines:
        if line.startswith('SID'):
            sid = parse_sid(line)
            if sid and sid['airport'] == airport_icao:
                airport_sids[sid['runway']].add(sid['sid_name'])
    
    print(f"{airport_icao} 的 SID 分析")
    print("=" * 40)
    
    for runway in sorted(airport_sids.keys()):
        sids = sorted(airport_sids[runway])
        print(f"跑道 {runway}：{', '.join(sids)}")
    
    total_sids = sum(len(sids) for sids in airport_sids.values())
    print(f"\n总 SID 数：{total_sids}")
    print(f"服务跑道数：{len(airport_sids)}")

# 使用方法
analyze_airport_sids(sid_lines, "ZBAA")
```

### 路线距离计算

```python
import math

def calculate_distance(lat1, lon1, lat2, lon2):
    """计算两点间的大圆距离。"""
    R = 3440.065  # 地球半径（海里）
    
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2) 
    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)
    
    a = (math.sin(delta_lat/2) * math.sin(delta_lat/2) + 
         math.cos(lat1_rad) * math.cos(lat2_rad) * 
         math.sin(delta_lon/2) * math.sin(delta_lon/2))
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def calculate_sid_distance(waypoint_sequence):
    """计算 SID 路线的总距离。"""
    total_distance = 0
    
    for i in range(len(waypoint_sequence) - 1):
        wp1 = waypoint_sequence[i]
        wp2 = waypoint_sequence[i + 1]
        
        distance = calculate_distance(
            wp1['latitude'], wp1['longitude'],
            wp2['latitude'], wp2['longitude']
        )
        total_distance += distance
    
    return total_distance
```

## 程序验证

### 检查路线连续性

```python
def validate_sid_continuity(waypoint_sequence, max_segment_distance=50):
    """验证 SID 路线是否有不合理的段。"""
    issues = []
    
    for i in range(len(waypoint_sequence) - 1):
        wp1 = waypoint_sequence[i]
        wp2 = waypoint_sequence[i + 1]
        
        distance = calculate_distance(
            wp1['latitude'], wp1['longitude'],
            wp2['latitude'], wp2['longitude']
        )
        
        if distance > max_segment_distance:
            issues.append({
                'segment': f"{wp1['name']} 到 {wp2['name']}",
                'distance': distance,
                'issue': '段距离过长'
            })
    
    return issues
```

## 数据集成

SID 程序连接到其他导航数据段：

- **[跑道](./runways.md)**：程序的离场跑道
- **[航路点](./waypoints.md)**：SID 路线中的导航点
- **[航路](./airways.md)**：到航路结构的连接点

## 特殊考虑

### 公共段
SID 的公共段

```
STR KF41ALL  199955043375STNLIJFRYE5STNLI +34404792-0994160061
STR KF41ALL  199956043051POTZYJFRYE5STNLI +34018117-0986128611
STR KF41ALL  199957041410BUROZJFRYE5STNLI +33918744-0984093781
STR KF41ALL  199958042672LNDUSJFRYE5STNLI +33604175-0977727781
STR KF41ALL  199959042015GREGSJFRYE5STNLI +33450608-0974660561
STR KF41ALL  199960043540TURKIJFRYE5TURKI +34300925-1010608391
STR KF41ALL  199961041873GANJAJFRYE5TURKI +34204189-1002545281
STR KF41ALL  199962041602DEDWTJFRYE5TURKI +34021694-0992525671
STR KF41ALL  199963044059ZORDAJFRYE5TURKI +33781175-0984901331
STR KF41ALL  199964042015GREGSJFRYE5TURKI +33450608-0974660561
STR KF41ALL  199965044059ZORDAJFRYE5ZORDA +33781175-0984901331
STR KF41ALL  199966042015GREGSJFRYE5ZORDA +33450608-0974660561
STR KF41ALL  199967042015GREGSJFRYE5      +33450608-0974660561
STR KF41ALL  199968042784MNKEEJFRYE5      +33429283-0969174581
STR KF41ALL  199969042291JFRYEJFRYE5      +33389456-0968322331
STR KF41ALL  199970042291JFRYEJFRYE5      +33389456-0968322331
```

无过渡点的为本程序的公共段


## 下一步

- **[了解 STAR 程序](./star-procedures.md)** - 进场程序补充
- **[探索航路点](./waypoints.md)** - 理解 SID 导航点
- **[使用分析工具](../tools/examples.md)** - 提取和分析 SID 数据
