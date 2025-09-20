# 解码过程

本指南解释如何将编码的 PFPX 导航数据文件转换为可读的文本格式。

## 概述

PFPX 导航数据文件使用带有自定义字符映射的 XOR 加密。解码过程逆转这种加密以显示原始导航数据。

## 手动解码方法

### 要求
- **Notepad++** 及其转换器插件
- PFPX 导航数据文件（`.nav`）
- 时间和耐心（处理大文件）

### 分步过程

1. **在 Notepad 中打开文件**
   ```
   文件 → 打开 → navdata.nav
   ```
   您将看到明文头部，然后是编码内容。

2. **切换到 Notepad++**
   - 在 Notepad++ 中打开同一文件
   - 您将看到相同的头部 + 编码段

3. **选择编码内容**
   - 从第 9 行开始（跳过明文头部）
   - 选择您要解码的内容
   - **重要**：一次不要选择超过 3,000-4,000 行

4. **转换为十六进制**
   ```
   菜单 → 插件 → 转换器 → ASCII 转十六进制
   ```

5. **应用字符映射**
   - 使用[编码表](./encoding-table.md)转换十六进制码
   - 每对十六进制字符代表一个原始字符

### 重要注意事项

::: warning 文件处理
- **绝不直接修改原始文件**
- **始终在副本上工作**
- **保存新文件时使用 ANSI 编码**
- **分小块处理**以避免错误
:::

## 自动化解码方法

我们的 Python 解码器自动化了整个过程：

### 基本用法

```bash
# 解码导航数据文件
python nav_decoder.py decode navdata.nav output.txt

# 将文本文件编码回导航数据格式  
python nav_decoder.py encode input.txt navdata.nav
```

### 自动处理模式

```bash
# 自动处理标准名称的文件
python nav_decoder.py auto
```

这会查找：
- `wait2decode.nav` → 创建 `already_decode.txt`
- `wait2encode.txt` → 创建 `already_encode.nav`

## 理解输出

解码后，您将看到可读的导航数据：

```txt
PFPX NAVDATA
NG2509
2025/09/04
2025/10/01
NAVIGRAPH

RWY ZBAA01   12467197359ASP+40058914+116617658
RWY ZBAA19   12467197179ASP+40073556+116598889
...

WPT ZBAA PEK0ZBAAZBP 1CZBCAPITAL                       016256     +40073333+116598333+0011612467ZBPE    9850
WPT AVBOX   6AVBOXZBE0 ZBAVBOX                         097808     +38647778+116378056+0000000000ZBPE   
...
```

## 验证

解码后，验证您的结果：

1. **检查头部** - 应与原始文件相同
2. **验证记录格式** - 每行应遵循预期模式
3. **计算记录数** - 与预期数量比较
4. **测试编码** - 重新编码并与原始文件比较

## 故障排除

### 常见问题

| 问题 | 原因 | 解决方案 |
|---------|-------|----------|
| 转换器插件缺失 | Notepad++ 安装问题 | 安装转换器插件 |
| "错误"消息 | 处理行数过多 | 减少选择大小 |
| 输出乱码 | 编码错误 | 使用 ANSI 编码 |
| 字符缺失 | 选择不完整 | 包含完整行范围 |

### 性能提示

- **分块处理**：一次处理 3,000-4,000 行
- **进度跟踪**：对大文件使用自动化工具
- **内存管理**：对大型操作关闭其他应用程序
- **备份策略**：始终保持原始文件安全

## 集成选项

### 脚本化
```python
from nav_codec import NavCodec

codec = NavCodec()
codec.decode_file("navdata.nav", "output.txt")
```

### 批量处理
```bash
# 处理多个文件
for file in *.nav; do
    python nav_decoder.py decode "$file" "${file%.nav}.txt"
done
```

### 自定义应用程序
解码器可以集成到更大的应用程序中用于：
- 飞行计划工具
- 导航数据库分析
- 数据验证和确认
- 格式转换实用程序

## 下一步

- **[探索数据段](./runways.md)** - 了解特定数据格式
- **[使用 Python 工具](../tools/python-decoder.md)** - 自动化过程
- **[查看示例](../tools/examples.md)** - 实际使用场景
