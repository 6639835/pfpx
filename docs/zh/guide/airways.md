# 航路和路线

航路定义连接航路点的路线结构。

> **📍 寻找扇区高度限制或巡航数据？** 请参阅 **[巡航表](./cruise-table.md)** 了解情报区扇区、航向范围和高度限制信息。

## 格式结构

```
AWY ROUTEAA#SSSSSSEEEEEEDDDDD±LLLLLLLLL±LLLLLLLLL±LLLLLLLLL±LLLLLLLLLMMMMMMMMMMMMR
```

## 示例记录

```
AWY A461  FA30980180980530+22543333+114133333+22896389+113951667NESTBUNLTD1
```

## 字段分解

### 基本信息
| 字段 | 含义 | 备注 / 示例 |
|------|------|-------------|
| `AWY` | 航路标识符 | 固定值，表示该条记录为航路 |
| `A461` | 航路编号 | 航路名称标识 |
| `FA` | 巡航标识符 | 见[巡航表](./cruise-table.md) |
| `3` | 航路类型 | 1=高空，2=低空，3=高低空 |
| `098018` | 起始航路点数据库 ID |  |
| `098053` | 结束航路点数据库 ID |  |
| `0` | 方向标志 | 1=双向，0=单向 |
| `+22543333` | 起始点纬度 |  |
| `+114133333` | 起始点经度 |  |
| `+22896389` | 结束点纬度 |  |
| `+113951667` | 结束点经度 |  |
| `NESTB` | 最低高度 | 下限或 "NESTB" 表示无下限 |
| `UNLTD` | 最高高度 | 上限或 "UNLTD" 表示无限制 |
| `1` | 导航类型 | 1=RNAV航路，0=非RNAV航路 |

## 高度编码

### 特殊值
- **NESTB** - 无下限规定
- **UNLTD** - 无上限规定
- **数字** - 特定高度（英尺或飞行高度层）

### 格式示例
```
04500  → 4,500 英尺海拔
FL290  → 飞行高度层 290（29,000 英尺）
NESTB  → 无下限
UNLTD  → 无上限
```

## 路线类型

| 代码 | 描述 | 用途 |
|------|-------------|-------|
| 1 | 高空 | FL180 及以上 |
| 2 | 低空 | FL180 以下 |
| 3 | 高/低空 | 两个高度范围 |

## 方向代码

| 代码 | 描述 | 限制 |
|------|-------------|--------------|
| 0 | 单向 | 单向航路 |
| 1 | 双向 | 双向航路 |

## 编程示例

### Python 解析器

```python
import re

def parse_airway(line):
    """解析航路记录。"""
    # AWY A461  FA30980180980530+22543333+114133333+22896389+113951667NESTBUNLTD1
    pattern = r'AWY (\w+)\s+(\w{2})(\d)(\d{6})(\d{6})(\d)([+-]\d{8})([+-]\d{9})([+-]\d{8})([+-]\d{9})(\w+)(\w+)(\d)'
    
    match = re.match(pattern, line)
    if match:
        return {
            'route_id': match.group(1),
            'region': match.group(2),
            'route_type': int(match.group(3)),
            'start_waypoint_id': match.group(4),
            'end_waypoint_id': match.group(5),
            'direction': int(match.group(6)),
            'start_lat': int(match.group(7)) / 1_000_000,
            'start_lon': int(match.group(8)) / 1_000_000,
            'end_lat': int(match.group(9)) / 1_000_000,
            'end_lon': int(match.group(10)) / 1_000_000,
            'min_altitude': match.group(11),
            'max_altitude': match.group(12),
            'rnav': bool(int(match.group(13)))
        }
    return None

# 使用方法
airway = parse_airway("AWY A461  FA30980180980530...")
print(f"路线 {airway['route_id']}：{airway['start_lat']},{airway['start_lon']} 到 {airway['end_lat']},{airway['end_lon']}")
```

### 路线网络分析

```python
from collections import defaultdict

def build_route_network(airway_lines):
    """从航路数据构建网络图。"""
    network = defaultdict(list)
    
    for line in airway_lines:
        if line.startswith('AWY'):
            airway = parse_airway(line)
            if airway:
                # 添加路线段
                start = (airway['start_lat'], airway['start_lon'])
                end = (airway['end_lat'], airway['end_lon'])
                
                network[start].append({
                    'destination': end,
                    'route': airway['route_id'],
                    'min_alt': airway['min_altitude'],
                    'max_alt': airway['max_altitude']
                })
                
                # 如果是双向，添加反向
                if airway['direction'] == 1:
                    network[end].append({
                        'destination': start,
                        'route': airway['route_id'],
                        'min_alt': airway['min_altitude'],
                        'max_alt': airway['max_altitude']
                    })
    
    return dict(network)
```

## 高度验证

```python
def parse_altitude_limit(alt_string):
    """解析高度限制字符串。"""
    if alt_string == "NESTB":
        return None, "no_lower_limit"
    elif alt_string == "UNLTD":
        return None, "unlimited"
    elif alt_string.startswith("FL"):
        # 飞行高度层
        fl = int(alt_string[2:])
        return fl * 100, "flight_level"
    else:
        # 海拔英尺
        return int(alt_string), "msl"

def validate_altitude_range(min_alt, max_alt, aircraft_altitude):
    """检查飞机高度是否在航路限制内。"""
    min_val, min_type = parse_altitude_limit(min_alt)
    max_val, max_type = parse_altitude_limit(max_alt)
    
    # 检查下限
    if min_val is not None and aircraft_altitude < min_val:
        return False, f"低于最低高度 {min_alt}"
    
    # 检查上限  
    if max_val is not None and aircraft_altitude > max_val:
        return False, f"高于最高高度 {max_alt}"
    
    return True, "在限制范围内"
```

## 路线规划应用

### 查找路线段

```python
def find_route_segments(network, route_id):
    """查找特定路线的所有段。"""
    segments = []
    
    for start_point, connections in network.items():
        for connection in connections:
            if connection['route'] == route_id:
                segments.append({
                    'start': start_point,
                    'end': connection['destination'],
                    'min_alt': connection['min_alt'],
                    'max_alt': connection['max_alt']
                })
    
    return segments

# 使用方法
a461_segments = find_route_segments(network, "A461")
print(f"路线 A461 有 {len(a461_segments)} 个段")
```

### 高度规划

```python
def plan_route_altitudes(route_segments, requested_altitude):
    """检查路线上的高度兼容性。"""
    issues = []
    
    for i, segment in enumerate(route_segments):
        valid, message = validate_altitude_range(
            segment['min_alt'], 
            segment['max_alt'], 
            requested_altitude
        )
        
        if not valid:
            issues.append({
                'segment': i,
                'start': segment['start'],
                'end': segment['end'],
                'issue': message
            })
    
    return issues
```

## 数据集成

航路连接到其他导航数据段：

- **[航路点](./waypoints.md)**：路线段的起止点
- **[SID 程序](./sid-procedures.md)**：连接到航路系统
- **[STAR 程序](./star-procedures.md)**：从航路系统连接

## 下一步

- **[了解 SID 程序](./sid-procedures.md)** - 离场如何连接到航路
- **[探索 STAR 程序](./star-procedures.md)** - 进场如何使用航路
- **[使用分析工具](../tools/examples.md)** - 提取和分析航路数据
