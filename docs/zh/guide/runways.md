# 跑道数据

跑道段包含全球机场跑道的详细信息，包括尺寸、方向和地理坐标。

## 格式结构

每个跑道记录遵循此模式：

```
RWY ICAO## LLLLWWWHHHASP±LLLLLLLLL±LLLLLLLLL
```

## 示例记录

```
RWY ZBAA01   12467197359ASP+40058914+116617658
```

## 字段分解

### 记录类型
```
RWY
```
- **目的**：标识这是跑道数据
- **格式**：固定字符串 "RWY"
- **必需**：是

### 机场代码
```
ZBAA
```
- **目的**：ICAO 机场标识符
- **格式**：四位机场 ICAO 代码
- **示例**：`ZBAA` = 北京首都国际机场

### 跑道号
```
01
```
- **目的**：跑道编号
- **格式**：2 位跑道号（01-36）或 3 位跑道号（01L、01C、01R）
- **示例**：
  - `01` = 跑道 01
  - `36` = 跑道 36
  - `09` = 跑道 09

### 跑道长度
```
12467
```
- **目的**：物理跑道长度
- **格式**：长度（英尺）
- **示例**：`12467` = 12,467 英尺

### 跑道宽度  
```
197
```
- **目的**：物理跑道宽度
- **格式**：宽度（英尺）
- **示例**：`197` = 197 英尺

### 磁航向
```
359
```
- **目的**：跑道磁方位
- **格式**：3 位航向（000-359）
- **示例**：`359` = 359° 磁航向

### 道面类型
```
ASP
```
- **目的**：跑道表面材料
- **格式**：固定值 "ASP"（沥青）
- **注意**：在 PFPX 数据中始终显示为 "ASP"

### 入口纬度
```
+40058914
```
- **目的**：跑道入口纬度坐标
- **格式**：±DDDDDDDD（度 × 1,000,000）
- **符号**：`+` = 北，`-` = 南
- **转换**：除以 1,000,000 得到十进制度

### 入口经度
```
+116617658
```
- **目的**：跑道入口经度坐标  
- **格式**：±DDDDDDDDD（度 × 1,000,000）
- **符号**：`+` = 东，`-` = 西
- **转换**：除以 1,000,000 得到十进制度

## 坐标转换

### 纬度示例
```
+40058914 → 40058914 ÷ 1,000,000 = 40.058914°N
```

### 经度示例
```
+116617658 → 116617658 ÷ 1,000,000 = 116.617658°E
```

## 编程示例

### Python 解析

```python
import re

def parse_runway(line):
    pattern = r'RWY (\w{4})(\d{2})\s+(\d+)(\d{3})(\d{3})ASP([+-]\d{8})([+-]\d{9})'
    match = re.match(pattern, line)
    
    if match:
        return {
            'icao': match.group(1),
            'runway': match.group(2),
            'length_ft': int(match.group(3)),
            'width_ft': int(match.group(4)),
            'heading': int(match.group(5)),
            'latitude': int(match.group(6)) / 1_000_000,
            'longitude': int(match.group(7)) / 1_000_000
        }
    return None
```

### 坐标转换

```python
def convert_coordinates(lat_raw, lon_raw):
    """将原始坐标值转换为十进制度"""
    latitude = int(lat_raw) / 1_000_000
    longitude = int(lon_raw) / 1_000_000
    
    lat_hemisphere = 'N' if latitude >= 0 else 'S'
    lon_hemisphere = 'E' if longitude >= 0 else 'W'
    
    return {
        'latitude': abs(latitude),
        'longitude': abs(longitude),
        'lat_hemisphere': lat_hemisphere,
        'lon_hemisphere': lon_hemisphere
    }
```

## 数据验证

### 常见检查

1. **长度范围**：跑道长度应该合理（500-20,000 英尺）
2. **宽度范围**：跑道宽度通常为 75-400 英尺
3. **航向范围**：必须是 000-359°
4. **坐标范围**： 
   - 纬度：-90° 到 +90°
   - 经度：-180° 到 +180°

### 验证示例

```python
def validate_runway(runway_data):
    errors = []
    
    if not (500 <= runway_data['length_ft'] <= 20000):
        errors.append("无效的跑道长度")
    
    if not (75 <= runway_data['width_ft'] <= 400):
        errors.append("无效的跑道宽度")
    
    if not (0 <= runway_data['heading'] <= 359):
        errors.append("无效的航向")
    
    return errors
```

## 相关数据

跑道数据连接到其他导航数据段：

- **[航路点](./waypoints.md)**：机场航路点引用跑道
- **[SID 程序](./sid-procedures.md)**：离场指定跑道
- **[STAR 程序](./star-procedures.md)**：进场指定跑道

## 下一步

- **[了解航路点数据](./waypoints.md)** - 导航点和设施
- **[探索机场航路点](./waypoints.md#airports)** - 相关机场信息
- **[使用解码工具](../tools/)** - 提取和分析跑道数据
