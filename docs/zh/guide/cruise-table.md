# 巡航表

巡航表包含用于飞行计划计算的飞行性能和高度限制数据。这些表提供了不同机型和飞行条件下的标准化巡航参数。

## 格式结构

```
XX HHH HHH T/M [ALTITUDE_RESTRICTIONS...]
```

其中：
- `XX` = 区域代码（2个字符）
- `HHH` = 起始航向（3位数字）
- `HHH` = 结束航向（3位数字）
- `T/M` = 航向类型（T=真航向，M=磁航向）
- `[ALTITUDE_RESTRICTIONS...]` = 高度限制数据（可变长度）

## 示例记录

```
AA 360 179 M 010000200029000 2900004000UNLTD                                 
AA 180 359 M 020000200028000 280000300031000 3100004000UNLTD                 
AO 360 179 M 020000200028000 280000300031000 3100004000UNLTD                 
AO 180 359 M 010000200029000 2900004000UNLTD                                 
BA 030 209 M 010000200029000 2900004000UNLTD                                 
BA 210 029 M 020000200028000 280000300031000 3100004000UNLTD                 
BB 030 209 M 010000200041000 4100004000UNLTD                                 
BB 210 029 M 020000200040000 400000300043000 4300004000UNLTD                 
BO 030 209 M 020000200040000 400000300043000 4300004000UNLTD                 
BO 210 029 M 010000200041000 4100004000UNLTD                                 
BZ 030 209 M 010000200041000 4100004000UNLTD                                 
BZ 210 029 M 020000200040000 400000300043000 4300004000UNLTD                 
CA 360 179 T M0090M0060M0810 M0810M0090M0900 M0900M0120M1500                 
CA 180 359 T M0060M0060M0840 M0840M0120M1440                                 
CO 360 179 T M0060M0060M0840 M0840M0120M1440                                 
CO 180 359 T M0090M0060M0810 M0810M0090M0900 M0900M0120M1500                 
CZ 090 269 M 010000100041000 4100002000UNLTD                                 
DA 090 269 M 010000200041000 4100004000UNLTD                                 
DA 270 089 M 020000200040000 400000300043000 4300004000UNLTD                 
DO 090 269 M 010000200041000 4100004000UNLTD                                 
DO 270 089 M 020000200040000 400000300043000 4300004000UNLTD                 
EA 090 269 M 010000200029000 2900004000UNLTD                                 
EA 270 089 M 020000200028000 280000300031000 3100004000UNLTD                 
EO 270 089 M 010000200029000 2900004000UNLTD                                 
EO 090 269 M 020000200028000 280000300031000 3100004000UNLTD                 
FA 360 179 T M0090M0060M0810 M0810M0080M0890 M0890M0060M1250 M1250M0120M1490 
FA 180 359 T M0060M0060M0840 M0840M0080M0920 M0920M0060M1220 M1220M0090M1310 
FA 180 359 T M1310M0120M1550                                                 
FO 360 179 T M0060M0060M0840 M0840M0080M0920 M0920M0060M1220 M1220M0090M1310 
FO 360 179 T M1310M0120M1550                                                 
FO 180 359 T M0090M0060M0810 M0810M0080M0890 M0890M0060M1250 M1250M0120M1490 
GA 360 179 M 030000190004900 049000200008900 089000190010800 108000200014800 
GA 360 179 M 148000190016700 167000200020700 207000190022600 226000200026600 
GA 360 179 M 266000250029100 291000200041100 411000380044900 449000400048900 
GA 180 359 M 020000190003900 039000200007900 079000190009800 098000200013800 
GA 180 359 M 138000190015700 157000200021700 217000190023600 236000200027600 
GA 180 359 M 276000250030100 301000200040100 401000290043000 430000390046900 
GA 180 359 M 469000400050900                                                 
GO 180 359 M 030000190004900 049000200008900 089000190010800 108000200014800 
GO 180 359 M 148000190016700 167000200020700 207000190022600 226000200026600 
GO 180 359 M 266000250029100 291000200041100 411000380044900 449000400048900 
GO 360 179 M 020000190003900 039000200007900 079000190009800 098000200013800 
GO 360 179 M 138000190015700 157000200021700 217000190023600 236000200027600 
GO 360 179 M 276000250030100 301000200040100 401000290043000 430000390046900 
GO 360 179 M 469000400050900                                                 
IZ 090 269 M 020000200040000 400000300043000 4300004000UNLTD                 
IZ 270 089 M 010000200041000 4100004000UNLTD                                 
KA 360 179 T M0090M0060M0810 M0810M0100M1210 M1210M0200M1610                 
KA 180 359 T M0120M0060M0780 M0780M0080M0860 M0860M0100M1160 M1160M0150M1310 
KA 180 359 T M1310M0200M1510                                                 
KO 180 359 T M0120M0060M0780 M0780M0080M0860 M0860M0100M1160 M1160M0150M1310 
KO 180 359 T M1310M0200M1510                                                 
KO 360 179 T M0090M0060M0810 M0810M0100M1210 M1210M0200M1610                 
NA 360 089 M 030000200013000 150000200029000 2900004000UNLTD                 
NA 090 179 M 035000200013500 150000200029000 2900004000UNLTD                 
NA 180 269 M 040000200012000 160000200028000 280000300031000 3100004000UNLTD 
NA 270 359 M 045000200012500 160000200028000 280000300031000 3100004000UNLTD 
OY 360 179 M 010003200033000 330001200045000 4500004000UNLTD                 
OY 180 359 M 020002800030000 300001300043000 4300004000UNLTD                 
PB 180 359 M 200000200032000 320000100041000                                 
PC 180 359 M 200000200034000 340000100038000 380000200040000 400000100041000 
PD 360 179 M 190000200029000 290000100035000 350000200041000                 
PE 360 179 M 010000200029000 290000800037000 3700004000UNLTD                 
PE 180 359 M 020000200028000 280000700035000 3500004000UNLTD                 
PF 180 359 M 030000200023000 230000600029000 290000800037000                 
PF 360 179 M 020000200024000 240000400028000 280000600034000                 
PG 360 179 M 020000200024000 240000400028000 280000600034000                 
PG 180 359 M 030000200023000 230000600029000 290000800037000                 
PH 360 179 M 010000200027000 270000400031000 310000200041000 4100004000UNLTD 
PH 180 359 M 280000400032000 320000200040000                                 
PI 360 179 M 010000200041000 4100004000UNLTD                                 
PI 180 359 M 300000600036000                                                 
PJ 360 179 M 010000200027000 270000400031000 310000100032000 320000300035000 
PJ 360 179 M 350000100036000 360000300039000 390000100040000 400000500045000 
PJ 360 179 M 4500004000UNLTD                                                 
PJ 180 359 M 020000200028000 280000300031000 310000100032000 320000300035000 
PJ 180 360 M 350000100036000 360000300039000 390000100040000 400000300043000 
PJ 180 359 M 4300004000UNLTD                                                 
PK 360 179 M 010000200029000 290000400037000 370000200041000 4100004000UNLTD 
PK 180 359 M 020000200030000 300000400038000 380000200040000 400000300043000 
PK 180 359 M 4300004000UNLTD                                                 
PL 360 179 M 010000200027000 270000600033000 3300004000UNLTD                 
PL 180 359 M 020000200028000 280000600034000 340000900043000 4300004000UNLTD 
PM 360 179 M 010000200027000 270000600033000 330001200045000 4500004000UNLTD 
PM 180 359 M 020000200026000 260000400030000 300001300043000 4300004000UNLTD 
PN 360 179 M 010000200029000 290000800045000 4500004000UNLTD                 
PN 180 359 M 020000200028000 280000600034000 340000900043000 4300004000UNLTD 
PO 360 179 M 010000200027000 270000600033000 330000800041000 4100004000UNLTD 
PO 180 359 M 020000200030000 300000800038000 380000500043000 4300004000UNLTD 
PQ 360 179 M 010000200027000 270000600033000 330000800041000 4100004000UNLTD 
PQ 180 359 M 020000200028000 280000500033000 330000800041000 410000200043000 
PQ 180 359 M 4300004000UNLTD                                                 
PR 360 179 M 010000200031000 310000600037000 370000800045000 4500004000UNLTD 
PR 180 359 M 020000200028000 280000400040000 400000300043000 4300004000UNLTD 
PT 360 179 M 010000200041000 4100004000UNLTD                                 
PT 180 359 M 020000200026000 260000400038000 380000500043000 4300004000UNLTD 
PU 360 179 M 010000200027000 270000400039000 390000600045000 4500004000UNLTD 
PU 180 359 M 020000200028000 280000400040000 400000300043000 4300004000UNLTD 
PV 360 179 M 010000200029000 290000400033000 330001200045000 4500004000UNLTD 
PV 180 359 M 020000200026000 260000400038000 380000500043000 4300004000UNLTD 
PW 360 179 M 010000200027000 270000300030000 300000800038000 380000700045000 
PW 360 179 M 4500004000UNLTD                                                 
PW 180 359 M 020000200026000 260000400030000 300000800038000 380000500043000 
PW 180 359 M 4500004000UNLTD                                                 
PX 360 179 M 010000200027000 270000400039000 390000600045000 4500004000UNLTD 
PX 180 359 M 020000200028000 280000400040000 400000300043000 4300004000UNLTD 
PY 360 179 M 030000200027000 270000400039000 390000600045000 4500004000UNLTD 
PY 180 359 M 020000200028000 280000400036000 360000200040000 400000300043000 
PY 180 359 M 4300004000UNLTD                                                 
PZ 360 179 M 010000200029000 290000400037000 370000800045000 4500004000UNLTD 
PZ 180 359 M 020000200026000 260000400038000 380000500043000 4300004000UNLTD 
QB 360 179 M 020000200024000 240000900033000 330001000043000 4300004000UNLTD 
QB 180 359 M 010000200025000 250000100026000 260000400030000 300000800038000 
QB 180 359 M 380000700045000 4500004000UNLTD                                 
QC 360 179 M 010000200027000 270000800035000 350000400039000 390000600045000 
QC 360 179 M 4500004000UNLTD                                                 
QC 180 359 M 020000200028000 280000400040000 400000300043000 4300004000UNLTD 
QD 360 179 M 010000200025000 250000100026000 260000400030000 300000800038000 
QD 360 179 M 380000700045000 4500004000UNLTD                                 
QD 180 359 M 020000200024000 240000300027000 270000600033000 330001000043000 
QD 180 359 M 4300004000UNLTD                                                 
QE 360 179 M 010000200027000 270001100038000 380000500043000                 
QE 180 359 M 020000200028000 280001000038000                                 
QF 360 179 M 010000200025000 250000700032000 320000400036000 360000200038000 
QF 360 179 M 380000700045000 4500004000UNLTD                                 
QF 180 359 M 020000200024000 240000700031000 3100004000UNLTD                 
QO 360 179 M 220000200028000 280000300031000 3100004000UNLTD                 
QO 180 359 M 210000200029000 2900004000UNLTD                                 
RA 360 179 T M0090M0060M0810 M0810M0100M1210 M1210M0200UNLTD                 
RA 180 359 T M0120M0060M0780 M0780M0080M0860 M0860M0100M1160 M1160M0150M1310 
RA 180 359 T M1310M0200UNLTD                                                 
RO 360 179 T M0120M0060M0780 M0780M0080M0860 M0860M0100M1160 M1160M0150M1310 
RO 360 179 T M1310M0200UNLTD                                                 
RO 180 359 T M0090M0060M0810 M0810M0100M1210 M1210M0200UNLTD                 
SA 360 179 M 010000200041000 4100004000UNLTD                                 
SA 180 359 M 020000200040000 400000300043000 4300004000UNLTD                 
SO 360 179 M 020000200040000 400000300043000 4300004000UNLTD                 
SO 180 359 M 010000200041000 4100004000UNLTD                                 
TA 360 179 M M0090M0060M0570 210000200029000 2900004000UNLTD                 
TA 180 359 M M0120M0060M0600 220000200028000 280000300031000 3100004000UNLTD 
UA 360 179 M 010000200027000 270000300030000 300000400038000 380000500043000 
UA 360 179 M 4300004000UNLTD                                                 
UA 180 359 M 020000200026000 260000300029000 2900004000UNLTD                 
UB 360 179 M 010000200029000 2900004000UNLTD                                 
UB 180 359 M 020000200030000 300000400038000 380000500043000 4300004000UNLTD 
UC 360 179 M 010000200027000 270000300030000 300000400038000 380000700045000 
UC 360 179 M 4500004000UNLTD                                                 
UC 180 359 M 020000200026000 260000500031000 310000100032000 320000300035000 
UC 180 359 M 350000100036000 360000300039000 390000100040000 400000300043000 
UC 180 359 M 4300004000UNLTD                                                 
VA 090 269 M 020000200040000 400000300043000 4300004000UNLTD                 
VA 270 089 M 010000200041000 4100004000UNLTD                                 
VB 360 179 M 010000200027000 270001800045000 4500004000UNLTD                 
VB 180 359 M 020000200028000 280000400032000 320000200034000 340000900043000 
VC 360 179 M 290001200041000                                                 
VC 180 359 M 300001000040000                                                 
VO 270 089 M 020000200040000 400000300043000 4300004000UNLTD                 
VO 090 269 M 010000200041000 4100004000UNLTD                                 
VV 000 179 M 020000200028000 290000200041000 4100004000UNLTD                 
VV 180 359 M 010000200027000 300000200040000 400000300043000 4300004000UNLTD 
WA 360 179 T 010000200041000 4100004000UNLTD                                 
WA 180 359 T 020000200040000 400000300043000 4300004000UNLTD                 
WO 360 179 T 020000200040000 400000300043000 4300004000UNLTD                 
WO 180 359 T 010000200041000 4100004000UNLTD                                 
YO 090 269 M 020000200040000 400000300043000 4300004000UNLTD                 
YO 270 089 M 010000200041000 4100004000UNLTD                                 
YY 090 269 M 010000200041000 4100004000UNLTD                                 
YY 270 089 M 020000200040000 400000300043000 4300004000UNLTD                 
ZA 090 269 M 040000200012000 120000400016000 160000200040000 400000300043000 
ZA 090 269 M 430000400047000                                                 
ZA 270 089 M 030000200041000 410000400045000                                 
```

## 字段分解

| 字段 | 含义 | 备注 / 示例 |
|------|------|-------------|
| `FA` | 巡航标识符 | 固定值，表示该条记录包含巡航性能数据 |
| `360` | 航向 | ICAO 机型代码 |
| `179` | 航向 | 标准飞行高度层（FL350 = 35,000 英尺） |
| `T` | 磁指示 | T=True，M=Magnetic |
| `M0090M0060M0810` | 巡航高度层标识 | 从 900M 至 8100M 每一个 RVSM 间隔为600M |
| `M0810M0080M0890` | 巡航高度层标识 | 从 8100M 至 8900M 每一个 RVSM 间隔为800M |
| `M0890M0060M1250` | 巡航高度层标识 | 从 8900M 至 12500M 每一个 RVSM 间隔为600M |
| `M1250M0120M1490` | 巡航高度层标识 | 从 12500M 至 14900M 每一个 RVSM 间隔为1200M |

## 说明

在示例中有类似`010000200027000`这样的高度层，如果在开头没有加上M，那么单位为英尺。在此示例当中，意为：从 10000FT 至 27000FT 每一个 RVSM 间隔为2000FT

## 航向范围

### 标准格式
- **全向覆盖**：`000 359` - 适用于所有航向（360度全覆盖）
- **半圆范围**：`360 179` - 适用于北半圆（360°-179°）
- **半圆范围**：`180 359` - 适用于南半圆（180°-359°）
- **象限范围**：`090 269` - 适用于东半圆（090°-269°）

### 磁偏角指示
- **T (True)**：真航向，基于地理北极
- **M (Magnetic)**：磁航向，基于磁北极

## 高度限制编码

### RVSM 间隔系统
RVSM (Reduced Vertical Separation Minimum) 系统定义了不同高度层的间隔：

```python
def parse_altitude_restrictions(altitude_string):
    """解析高度限制字符串。"""
    import re
    
    # 检测是否使用米制单位
    if altitude_string.startswith('M'):
        unit = 'meters'
        altitude_string = altitude_string[1:]  # 移除 M 前缀
    else:
        unit = 'feet'
    
    # 解析高度范围模式：起始高度+间隔+结束高度
    pattern = r'(\d{4,5})(\d{2,4})(\d{4,5})'
    matches = re.findall(pattern, altitude_string)
    
    altitude_ranges = []
    for match in matches:
        start_alt = int(match[0])
        interval = int(match[1])
        end_alt = int(match[2])
        
        altitude_ranges.append({
            'start_altitude': start_alt,
            'end_altitude': end_alt,
            'rvsm_interval': interval,
            'unit': unit
        })
    
    return altitude_ranges

# 示例使用
altitude_data = parse_altitude_restrictions("M0090M0060M0810")
print(f"高度范围：{altitude_data[0]['start_altitude']}-{altitude_data[0]['end_altitude']} 米")
print(f"RVSM 间隔：{altitude_data[0]['rvsm_interval']} 米")
```

### 高度层示例

```python
def decode_altitude_examples():
    """解码高度层示例。"""
    examples = {
        'M0090M0060M0810': {
            'description': '米制单位，900-8100米，RVSM间隔600米',
            'start': 900,
            'end': 8100,
            'interval': 600,
            'unit': 'meters'
        },
        '010000200027000': {
            'description': '英尺单位，10000-27000英尺，RVSM间隔2000英尺',
            'start': 10000,
            'end': 27000,
            'interval': 2000,
            'unit': 'feet'
        },
        'UNLTD': {
            'description': '无限制高度',
            'start': None,
            'end': None,
            'interval': None,
            'unit': None
        }
    }
    return examples
```

## 扇区分析

### 按区域分组

```python
from collections import defaultdict

def analyze_sectors_by_region(sector_lines):
    """按区域分析扇区数据。"""
    sectors = defaultdict(list)
    
    for line in sector_lines:
        if len(line.strip()) > 0:
            # 提取前两个字符作为区域代码
            region_code = line[:2].strip()
            sectors[region_code].append(line.strip())
    
    # 统计每个区域的扇区数量
    region_stats = {}
    for region, sector_list in sectors.items():
        region_stats[region] = {
            'sector_count': len(sector_list),
            'has_true_heading': any('T' in sector for sector in sector_list),
            'has_magnetic_heading': any('M' in sector for sector in sector_list),
            'altitude_restricted': any('UNLTD' not in sector for sector in sector_list)
        }
    
    return region_stats

# 使用示例
stats = analyze_sectors_by_region(sector_lines)
for region, data in stats.items():
    print(f"区域 {region}：{data['sector_count']} 个扇区")
```

### 航向覆盖分析

```python
def analyze_heading_coverage(sector_data):
    """分析航向覆盖情况。"""
    heading_coverage = {}
    
    for sector in sector_data:
        parts = sector.split()
        if len(parts) >= 3:
            region = parts[0][:2]
            start_heading = int(parts[0][2:5])
            end_heading = int(parts[1])
            
            if region not in heading_coverage:
                heading_coverage[region] = []
            
            heading_coverage[region].append({
                'start': start_heading,
                'end': end_heading,
                'range': calculate_heading_range(start_heading, end_heading)
            })
    
    return heading_coverage

def calculate_heading_range(start, end):
    """计算航向范围角度。"""
    if start <= end:
        return end - start + 1
    else:
        return (360 - start) + end + 1
```

## 高度优化

### 最优高度选择

```python
def find_optimal_altitude(sector_data, aircraft_performance):
    """根据扇区限制找到最优高度。"""
    optimal_altitudes = {}
    
    for sector in sector_data:
        # 解析扇区高度限制
        altitude_restrictions = parse_sector_altitudes(sector)
        
        # 找到性能最优的高度层
        for restriction in altitude_restrictions:
            if restriction['unit'] == 'feet':
                # 转换为标准飞行高度层
                fl_start = restriction['start'] // 100
                fl_end = restriction['end'] // 100
                
                # 在允许范围内找到最优FL
                optimal_fl = find_best_flight_level(
                    fl_start, fl_end, aircraft_performance
                )
                
                optimal_altitudes[sector[:2]] = {
                    'optimal_fl': optimal_fl,
                    'altitude_feet': optimal_fl * 100,
                    'restriction_range': f"FL{fl_start}-FL{fl_end}"
                }
    
    return optimal_altitudes
```

## 数据验证

### 扇区完整性检查

```python
def validate_sector_data(sector_lines):
    """验证扇区数据的完整性。"""
    issues = []
    region_coverage = defaultdict(list)
    
    for line in sector_lines:
        if len(line.strip()) > 0:
            parts = line.split()
            if len(parts) >= 3:
                region = parts[0][:2]
                start_heading = int(parts[0][2:5])
                end_heading = int(parts[1])
                
                region_coverage[region].append((start_heading, end_heading))
    
    # 检查每个区域的航向覆盖是否完整
    for region, headings in region_coverage.items():
        total_coverage = 0
        for start, end in headings:
            total_coverage += calculate_heading_range(start, end)
        
        if total_coverage < 360:
            issues.append(f"区域 {region} 航向覆盖不完整：{total_coverage}°/360°")
        elif total_coverage > 360:
            issues.append(f"区域 {region} 航向覆盖重叠：{total_coverage}°/360°")
    
    return issues
```

## 数据集成

巡航扇区数据连接到其他导航数据段：

- **[航路](./airways.md)**：扇区内的航路限制
- **[航路点](./waypoints.md)**：扇区边界的导航点
- **[SID 程序](./sid-procedures.md)**：离场时的扇区管制
- **[STAR 程序](./star-procedures.md)**：进场时的扇区管制

## 实际应用

### 飞行计划整合

```python
def integrate_with_flight_plan(route_waypoints, sector_data):
    """将扇区数据整合到飞行计划中。"""
    sector_assignments = []
    
    for i, waypoint in enumerate(route_waypoints):
        # 计算航段航向
        if i < len(route_waypoints) - 1:
            next_waypoint = route_waypoints[i + 1]
            track = calculate_track(waypoint, next_waypoint)
            
            # 查找适用的扇区
            applicable_sector = find_sector_for_track(track, sector_data)
            
            sector_assignments.append({
                'waypoint': waypoint['name'],
                'track': track,
                'sector': applicable_sector,
                'altitude_restrictions': parse_sector_altitudes(applicable_sector)
            })
    
    return sector_assignments
```

## 下一步

- **[了解空域管理](./airways.md)** - 扇区与航路的关系
- **[探索导航方法](./waypoints.md)** - 扇区边界导航
- **[使用飞行计划工具](../tools/examples.md)** - 扇区数据在飞行计划中的应用