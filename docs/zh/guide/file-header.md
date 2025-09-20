# 文件头

PFPX 导航数据文件头部以明文格式包含有关导航数据库的基本元数据。

## 结构

头部出现在每个导航数据文件的开头，并且**未编码**。它提供有关数据源、版本和有效期的信息。

## 格式示例

```
PFPX NAVDATA
NG2509
2025/09/04
2025/10/01
NAVIGRAPH
```

## 字段说明

### 第 1 行：数据库标识符
```
PFPX NAVDATA
```
- **目的**：将文件标识为 PFPX 导航数据
- **格式**：固定字符串
- **必需**：是

### 第 2 行：数据库版本
```
NG2509
```
- **目的**：数据库版本/周期标识符
- **格式**：提供商前缀 + 周期号
- **示例**：
  - `NG2509` = Navigraph 周期 2509
  - `AS2509` = Aerosoft 周期 2509

### 第 3 行：生效日期
```
2025/09/04
```
- **目的**：导航数据何时生效
- **格式**：`YYYY/MM/DD`
- **标准**：遵循 AIRAC 周期日期

### 第 4 行：失效日期
```
2025/10/01
```
- **目的**：导航数据何时失效
- **格式**：`YYYY/MM/DD`
- **标准**：遵循 AIRAC 周期日期（28 天间隔）

### 第 5 行：数据提供商
```
NAVIGRAPH
```
- **目的**：标识导航数据源
- **常见值**：
  - `NAVIGRAPH` - Navigraph 导航数据
  - `AEROSOFT` - Aerosoft 导航数据
  - 可能出现自定义提供商名称

## AIRAC 周期

导航数据遵循 AIRAC 标准：

- **周期长度**：28 天

### 周期编号

AIRAC 周期按顺序编号：
- **格式**：YYWW（年份 + 周数）
- **示例**：`2509` = 2025 年，第 9 周期

## 验证

处理导航数据文件时，始终验证：

1. **日期有效性**：检查当前日期是否在有效期内
2. **版本匹配**：确保与您的 PFPX 版本兼容
3. **提供商一致性**：确认预期的数据源

## 编程注意事项

### 解析示例（Python）

```python
def parse_header(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [f.readline().strip() for _ in range(5)]
    
    return {
        'database': lines[0],
        'version': lines[1],
        'effective_date': lines[2],
        'expiration_date': lines[3],
        'provider': lines[4]
    }
```

### 日期处理

```python
from datetime import datetime

def is_current(effective_date, expiration_date):
    today = datetime.now().date()
    effective = datetime.strptime(effective_date, '%Y/%m/%d').date()
    expiration = datetime.strptime(expiration_date, '%Y/%m/%d').date()
    
    return effective <= today <= expiration
```

## 常见问题

### 编码问题
- **症状**：头部文本乱码
- **原因**：文本编码错误
- **解决方案**：使用 UTF-8 或 ANSI 编码

### 日期格式变化
- **标准**：`YYYY/MM/DD`
- **替代方案**：某些文件可能使用不同的分隔符
- **处理**：实现灵活的日期解析

### 缺失行
- **问题**：头部截断
- **原因**：文件损坏或下载不完整
- **检测**：检查确切的 5 个头部行

## 集成

头部信息对以下方面至关重要：

- **版本控制**：跟踪数据库更新
- **验证**：确保数据时效性
- **兼容性**：与 PFPX 版本匹配
- **日志记录**：记录数据源和版本

## 下一步

- **[了解跑道数据](./runways.md)** - 第一个编码段
- **[理解整体结构](./file-structure.md)** - 段落如何关联
- **[使用解码工具](../tools/)** - 处理编码内容
