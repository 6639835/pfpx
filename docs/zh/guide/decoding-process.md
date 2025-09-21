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

RWY 00AN03   04517060030ASP+59088889-156463889
RWY 00AN21   04517060210ASP+59098056-156447778
......
RWY ZYYJ09   08530148092ASP+42881175+129435625
RWY ZYYJ27   08530148272ASP+42884531+129467125

WPT ENOE QAT0ENOEA1P 1CA1TROLL AIRFIELD                003733     -71956667+002453333+0412509843ENOR    18000
WPT NZFX    0NZFXA1P 1PA1PHOENIX                       011402     -77957092+166745389+0003710006NZZO    18000
......
WPT ZYTX SHE0ZYTXZYP 1CZYTAOXIAN                       016367     +41641667+123485000+0019810499ZYSH    
WPT ZYYJ YNJ0ZYYJZYP 1CZYCHAOYANGCHUAN                 016368     +42881667+129450000+0062208530ZYSH    9490

WPT AARON   6AARONA1E0 A1AARON                         016368     -79384500-110927167+0000000000NZZO         
WPT ANGIE   6ANGIEA1E0 A1ANGIE                         016369     -89754667-176959167+0000000000NZZO       
......
WPT LJ      5LJZYP   0 ZYSANJIAZI QIQIHAR              27493901770+47195903+123944392+0000000000ZYSH         
WPT JA      5JAZYP   0 ZYDEXIN YANJI                   27494003320+42871356+129341022+0000000000ZYSH            

AWY A1    SA32690940745071+33447742+135794494+33364503+13544151408000UNLTD0
AWY A1    SA30745070749101+33364503+135441514+33248769+13499722208000UNLTD0
......
AWY Z999  SO30223222639891+47559389+010305583+47745775+01034983309500FL6601
AWY Z999  SA22639890222801+47745775+010349833+47929603+01074995606500FL2451

SID 0ID211   000001099539FLNGJYOYYU1      +44255928-1134392501
SID 0ID211   000002034960YOYYUYOYYU1      +43948250-1133553641
......
SID ZYYJ27   164665263457YJ401WQG19D      +43242778+1297413891
SID ZYYJ27   164666271707WQG  WQG19D      +43293333+1297850001

STR 06FAALL  164667050581BISKSCLMNT2BISKS +27981592-0796214061
STR 06FAALL  164668051894HEMSICLMNT2BISKS +27640356-0797136671
......
STR ZYYJ27   330409263457YJ401WQG19A      +43242778+1297413891
STR ZYYJ27   330410263468YJ604WQG19A      +43017778+1296950001
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

## 下一步

- **[探索数据段](./runways.md)** - 了解特定数据格式
- **[使用 Python 工具](../tools/python-decoder.md)** - 自动化过程
- **[查看示例](../tools/examples.md)** - 实际使用场景
