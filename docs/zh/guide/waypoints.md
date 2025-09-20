# 航路点和导航设施

航路点段包含各种类型的导航点，包括机场、导航设施和航路点。

## 航路点类型

每个航路点都有一个标识其类别的类型代码：

| 类型 | 描述 | 用途 |
|------|-------------|-------|
| 0 | 机场 | 终端设施 |
| 1 | VFR 航路点 | 目视导航点 |
| 2 | VOR/TACAN | VOR/TAC合装 |
| 3 | TACAN | TACAN导航设施 |
| 4 | VOR/DME | VOR/DME合装 |
| 5 | NDB | 无方向信标 |
| 6 | 航路点 | 交汇点/定位点 |
| 9 | DME | 测距仪 |

## 机场记录（类型 0）

机场代表具有跑道和服务的终端设施。

### 格式
```
WPT ICAO IATA0ICAOAREA1CAREAGIONNAMEEEEE        DDDDDD     ±LLLLLLLLL±LLLLLLLLL±EEEEERRRRRFIRCODE    TTTT
```

### 示例
```
WPT ZBAA PEK0ZBAAZBP 1CZBCAPITAL                       016256     +40073333+116598333+0011612467ZBPE    9850
```

### 字段分解

| 字段         | 含义                 | 备注 / 示例 |
|--------------|----------------------|-------------|
| `WPT`        | 航路点类型标识       | 固定值，表示该条记录为航路点/机场/导航设施 |
| `ZBAA`       | ICAO 代码            |  |
| `PEK`        | IATA 代码            |  |
| `0`          | 类型代码             | 0 = 机场 |
| `ZBAA`       | ICAO 代码            | 与上方 ICAO 相同 |
| `ZB`         | 区域代码             |  |
| `P`          | 部分代码             | 机场（参考 ARINC424-18 5.4） |
| `1`          | 标志                 | 固定值，表示此记录为机场 |
| `C`          | 机场类别             | C = 民用，M = 军用，P = 私人 |
| `ZB`         | 区域代码             |  |
| `CAPITAL`    | 名称                 |  |
| `016256`     | 数据库 ID            | 唯一标识 |
| `+40073333`  | 纬度                 | WGS-84，小数度 × 1e6，+ = 北纬，- = 南纬 → 40.073333°N |
| `+116598333` | 经度                 | WGS-84，小数度 × 1e6，+ = 东经，- = 西经 → 116.598333°E |
| `+00116`     | 海拔高度（英尺）     | + = 海平面以上，- = 海平面以下 |
| `12467`      | 最长跑道长度（英尺） | 例如 12,467 ft |
| `ZBPE`       | 机场所属情报区代码   |  |
| `9850`       | 过渡高度（ft）       |  |

## 航路点（类型 6）

用于导航路由的交汇点和定位点。

### 示例  
```
WPT AVBOX   6AVBOXZBE0 ZBAVBOX                         097808     +38647778+116378056+0000000000ZBPE   
```

### 字段分解

| 字段          | 含义               | 备注 / 示例 |
|---------------|--------------------|-------------|
| `WPT`         | 航路点类型标识     | 固定值，表示该条记录为航路点/机场/导航设施 |
| `AVBOX`       | 航路点识别码       |  |
| `6`           | 类型代码           | 6 = 航路点 |
| `AVBOX`       | 航点识别码         |  |
| `ZB`          | 区域代码           |  |
| `E`           | 部分代码           | E = Enroute，P = Airport（参考 ARINC424-18 5.4） |
| `0`           | 终端区标志         | 0 = 非终端区航点，1 = 终端区航点 |
| `ZB`          | 区域代码           |  |
| `AVBOX`       | 航路点名称         | 若以 VOR 方位和距离命名，将是 `ZUH345015` |
| `097808`      | 数据库 ID          |  |
| `+38647778`   | 纬度               |  |
| `+116378056`  | 经度               |  |
| `+0000000000` | 非必要字段         | 航路点无需此字段 |
| `ZBPE`        | 飞行情报区         |  |

## VOR 台（类型 4）

VOR 导航设施。

### 示例
```
WPT PEK     4PEKZBD  0 ZBGUANZHUANG                    27126111470+40048333+116735000+0020300000ZBPE
```

### 字段分解

| 字段          | 含义               | 备注 / 示例 |
|---------------|--------------------|-------------|
| `WPT`         | 航路点类型标识     | 固定值，表示该条记录为航路点/机场/导航设施 |
| `PEK`         | VOR 识别码         |  |
| `4`           | 类型代码           | 4 = VOR/DME |
| `PEK`         | VOR 识别码         |  |
| `ZB`          | 区域代码           |  |
| `D`           | 部分代码           | D = 导航设施（参考 ARINC424-18 5.4） |
| `0`           | 终端区标志         | 0 = 非终端区航点，1 = 终端区航点 |
| `ZB`          | 区域代码           |  |
| `GUANZHUANG`  | 名称               |  |
| `271261`      | 数据库 ID          |  |
| `11470`       | 频率               | 11470 = 114.70 MHz |
| `+40048333`   | 纬度               |  |
| `+116735000`  | 经度               |  |
| `+00203`      | 标高               | 海拔高度（英尺），+ = 海平面以上，- = 以下 |
| `00000`       | 无需字段           | VOR 无需此字段 |
| `ZBPE`        | 飞行情报区         |  |

## NDB 台（类型 5）

无方向信标无线电导航设施。

### 示例
```
WPT CU      5CUZBD   0 ZBSHAHE                         27392005550+40121667+116371667+0000000000ZBPE 
```

### 字段分解

| 字段          | 含义               | 备注 / 示例 |
|---------------|--------------------|-------------|
| `WPT`         | 航路点类型标识     | 固定值，表示该条记录为航路点/机场/导航设施 |
| `CU`          | NDB 识别码         |  |
| `5`           | 类型代码           | 5 = NDB |
| `CU`          | NDB 识别码         |  |
| `ZB`          | 区域代码           |  |
| `D`           | 部分代码           | D = 导航设施（参考 ARINC424-18 5.4） |
| `0`           | 终端区标志         | 0 = 非终端区航点，1 = 终端区航点 |
| `ZB`          | 区域代码           |  |
| `SHAHE`       | 名称               |  |
| `273920`      | 数据库 ID          |  |
| `05550`       | 频率               | 05550 = 555.0 kHz |
| `+40121667`   | 纬度               |  |
| `+116371667`  | 经度               |  |
| `0000000000`  | 无需字段           | NDB 不使用此字段 |
| `ZBPE`        | 飞行情报区         |  |

## 坐标转换

所有航路点坐标使用相同格式：

### 纬度
```
±DDDDDDDD（度 × 1,000,000）
+40073333 → 40.073333°N
-40073333 → 40.073333°S
```

### 经度  
```
±DDDDDDDDD（度 × 1,000,000）  
+116598333 → 116.598333°E
-116598333 → 116.598333°W
```

## 编程示例

### Python 航路点解析器

```python
import re

def parse_waypoint(line):
    """解析航路点记录。"""
    parts = line.split()
    if len(parts) < 3:
        return None
    
    record = {
        'identifier': parts[1],
        'raw_type_field': parts[2],
        'type_code': int(parts[2][0]) if parts[2] else None,
        'line': line
    }
    
    # 如果可用，提取坐标
    coord_match = re.search(r'([+-]\d{8,9})([+-]\d{8,9})', line)
    if coord_match:
        record['latitude'] = int(coord_match.group(1)) / 1_000_000
        record['longitude'] = int(coord_match.group(2)) / 1_000_000
    
    return record

# 使用方法
waypoint = parse_waypoint("WPT ZBAA PEK0ZBAAZBP 1CZBCAPITAL...")
print(f"机场：{waypoint['identifier']} 位于 {waypoint['latitude']}, {waypoint['longitude']}")
```

### 按类型过滤

```python
def filter_waypoints_by_type(lines, waypoint_type):
    """按类型代码过滤航路点。"""
    filtered = []
    for line in lines:
        if line.startswith('WPT'):
            parts = line.split()
            if len(parts) >= 3 and parts[2].startswith(str(waypoint_type)):
                filtered.append(line)
    return filtered

# 获取所有机场（类型 0）
airports = filter_waypoints_by_type(decoded_lines, 0)

# 获取所有 VOR 台（类型 4）  
vor_stations = filter_waypoints_by_type(decoded_lines, 4)
```

## 数据验证

### 常见验证检查

```python
def validate_waypoint(waypoint_data):
    """验证航路点数据。"""
    errors = []
    
    # 检查坐标范围
    if 'latitude' in waypoint_data:
        lat = waypoint_data['latitude']
        if not (-90 <= lat <= 90):
            errors.append(f"无效纬度：{lat}")
    
    if 'longitude' in waypoint_data:
        lon = waypoint_data['longitude']
        if not (-180 <= lon <= 180):
            errors.append(f"无效经度：{lon}")
    
    # 检查标识符格式
    identifier = waypoint_data.get('identifier', '')
    if len(identifier) < 2 or len(identifier) > 5:
        errors.append(f"无效标识符长度：{identifier}")
    
    return errors
```

## 相关数据

航路点连接到其他导航数据段：

- **[航路](./airways.md)**：路线连接航路点
- **[SID 程序](./sid-procedures.md)**：引用特定航路点
- **[STAR 程序](./star-procedures.md)**：使用航路点进行路由

## 下一步

- **[了解航路](./airways.md)** - 航路点如何通过路线连接
- **[探索程序](./sid-procedures.md)** - SID/STAR 中的航路点使用
- **[使用分析工具](../tools/examples.md)** - 提取和分析航路点数据
