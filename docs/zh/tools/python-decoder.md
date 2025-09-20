# Python 解码器

一个用于编码和解码 PFPX 导航数据文件的综合 Python 工具，具有高级功能和自动化能力。

## 安装

### 要求
- **Python 3.6+**
- 无需额外依赖（仅使用标准库）

### 设置
1. 从 `tools/` 目录下载解码器
2. 使其可执行（Unix/Linux）：
   ```bash
   chmod +x nav_decoder.py
   ```

## 基本用法

### 命令行界面

```bash
# 解码导航数据文件
python nav_decoder.py decode input.nav output.txt

# 将文本文件编码回导航数据格式
python nav_decoder.py encode input.txt output.nav

# 自动处理标准名称的文件
python nav_decoder.py auto
```

### 自动处理模式

自动模式在当前目录中查找这些文件：

| 输入文件 | 输出文件 | 操作 |
|------------|-------------|-----------|
| `wait2decode.nav` | `already_decode.txt` | 解码 |
| `wait2encode.txt` | `already_encode.nav` | 编码 |

## 高级选项

### 自定义 XOR 密钥
```bash
# 使用不同的 XOR 密钥（默认是 0x85）
python nav_decoder.py -k 0xFF decode input.nav output.txt

# 十六进制格式
python nav_decoder.py --xor-key 0x90 decode input.nav output.txt
```

### 工作目录
```bash
# 在不同目录中处理文件
python nav_decoder.py -d /path/to/files auto
```

### 详细输出
```bash
# 启用详细日志记录
python nav_decoder.py -v decode input.nav output.txt
```

## Python API

### 基本用法

```python
from pathlib import Path
from tools.nav_decoder import NavCodec

# 创建编解码器实例
codec = NavCodec()

# 解码文件
codec.decode_file(Path("navdata.nav"), Path("decoded.txt"))

# 编码文件
codec.encode_file(Path("input.txt"), Path("encoded.nav"))
```

### 自定义配置

```python
from tools.nav_decoder import NavCodec, CodecConfig

# 自定义配置
config = CodecConfig(
    xor_key=0xFF,           # 不同的 XOR 密钥
    progress_steps=50,      # 更多进度更新
    encoding='utf-8'        # 文本编码
)

codec = NavCodec(config)
```

## 配置选项

`CodecConfig` 类提供这些设置：

| 参数 | 默认值 | 描述 |
|-----------|---------|-------------|
| `xor_key` | `0x85` | 编码/解码的 XOR 密钥 |
| `header_threshold` | `128` | 头部检测的字节阈值 |
| `content_line_threshold` | `30` | 内容检测的行长度阈值 |
| `progress_steps` | `20` | 进度更新次数 |
| `encoding` | `utf-8` | 文本文件编码 |

## 性能特性

### 进度跟踪
```
2025-01-15 10:30:15 - INFO - 开始解码操作: navdata.nav -> output.txt
2025-01-15 10:30:20 - INFO - 进度: 5%
2025-01-15 10:30:25 - INFO - 进度: 10%
...
2025-01-15 10:32:45 - INFO - 解码成功完成。输出: output.txt
```

### 内存优化
- **流式处理**：处理大文件而不将所有内容加载到内存中
- **分块处理**：以可管理的块处理数据
- **进度检查点**：长时间操作的定期进度更新

## 批量处理

### 处理多个文件

```python
from pathlib import Path
from tools.nav_decoder import NavCodec

codec = NavCodec()
input_dir = Path("navdata_files")
output_dir = Path("decoded_files")

# 创建输出目录
output_dir.mkdir(exist_ok=True)

# 处理所有 .nav 文件
for nav_file in input_dir.glob("*.nav"):
    output_file = output_dir / f"{nav_file.stem}.txt"
    try:
        codec.decode_file(nav_file, output_file)
        print(f"✓ {nav_file.name} 解码成功")
    except Exception as e:
        print(f"✗ {nav_file.name} 失败: {e}")
```

## 故障排除

### 常见问题

| 问题 | 原因 | 解决方案 |
|-------|-------|----------|
| "找不到输入文件" | 文件路径错误 | 检查文件路径和权限 |
| "输入文件为空" | 文件损坏 | 验证文件完整性 |
| "解码失败" | XOR 密钥错误 | 尝试不同的 XOR 密钥值 |
| 内存错误 | 文件太大 | 使用流模式或分块处理 |

## 下一步

- **[查看使用示例](./examples.md)** - 实际场景和工作流程
- **[了解数据格式](../guide/)** - 理解解码后的内容
- **[探索集成选项](./examples.md#integration)** - 与其他工具配合使用
