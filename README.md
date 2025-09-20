# PFPX Navdata Documentation | PFPX 导航数据文档

[![English](https://img.shields.io/badge/Language-English-blue)](#english) [![中文](https://img.shields.io/badge/语言-中文-red)](#中文)

---

## English

Complete guide and tools for working with PFPX navigation data files.

### Overview

This project provides comprehensive documentation and Python tools for understanding and working with PFPX (Professional Flight Planner X) navigation database files. The navdata files use a proprietary binary format with XOR encryption that this project helps decode and analyze.

### Features

- 📚 **Complete Documentation** - Detailed analysis of file format and data structures
- 🔧 **Python Decoder Tool** - Automated encoding/decoding with progress tracking
- 📊 **Data Analysis** - Tools for extracting and analyzing navigation data
- 🗺️ **Format Specifications** - Detailed breakdown of runways, waypoints, airways, and procedures
- ⚡ **Batch Processing** - Handle multiple files efficiently

### Quick Start

#### View Documentation

```bash
# Install dependencies
npm install

# Start development server
npm run docs:dev

# Visit http://localhost:5173
```

The documentation is available in multiple languages:
- **English**: http://localhost:5173/ (default)
- **简体中文**: http://localhost:5173/zh/

#### Use Python Decoder

```bash
# Basic decoding
python tools/nav_decoder.py decode navdata.nav output.txt

# Auto-processing mode
python tools/nav_decoder.py auto

# See all options
python tools/nav_decoder.py --help
```

### Documentation Structure

```
docs/
├── guide/                  # Main documentation
│   ├── getting-started.md  # Introduction and setup
│   ├── file-structure.md   # Overall file organization
│   ├── encoding-table.md   # Character encoding details
│   ├── decoding-process.md # How to decode files
│   ├── file-header.md      # Header format specification
│   ├── runways.md          # Runway data format
│   ├── waypoints.md        # Navigation points and facilities
│   ├── airways.md          # Route and airway information
│   ├── sid-procedures.md   # Standard Instrument Departures
│   └── star-procedures.md  # Standard Terminal Arrivals
├── tools/                  # Tool documentation
│   ├── python-decoder.md   # Python tool reference
│   └── examples.md         # Usage examples and workflows
└── index.md               # Home page
```

### Tools

#### Python Decoder (`tools/nav_decoder.py`)

A comprehensive tool for working with PFPX navdata files:

**Features:**
- Decode `.nav` files to readable text
- Encode text files back to `.nav` format  
- Auto-processing mode for batch operations
- Progress tracking for large files
- Configurable XOR keys and parameters
- Error handling and validation

**Usage:**
```bash
# Decode a file
python tools/nav_decoder.py decode input.nav output.txt

# Encode a file  
python tools/nav_decoder.py encode input.txt output.nav

# Auto-process with standard naming
python tools/nav_decoder.py auto
```

### File Format Overview

PFPX navdata files contain:

1. **Header** (plaintext) - Database metadata and validity dates
2. **Runway Data** (encoded) - Airport runway specifications
3. **Waypoint Data** (encoded) - Navigation points, airports, VOR/NDB facilities  
4. **Airway Data** (encoded) - Route segments and connections
5. **SID Data** (encoded) - Standard departure procedures
6. **STAR Data** (encoded) - Standard arrival procedures

All sections except the header use XOR encryption with key `0x85`.

### Data Sources

Navigation data typically comes from:
- **Navigraph** - Primary commercial provider
- **Aerosoft** - Alternative data source
- Follows AIRAC 28-day update cycles

### Development

#### Prerequisites
- Node.js 16+ (for documentation)
- Python 3.6+ (for tools)

#### Setup
```bash
# Clone repository
git clone https://github.com/6639835/pfpx
cd pfpx

# Install documentation dependencies
npm install

# Make Python tool executable
chmod +x tools/nav_decoder.py
```

#### Build Documentation
```bash
# Development server
npm run docs:dev

# Build static site
npm run docs:build

# Preview production build
npm run docs:preview
```

### Contributing

This project is based on reverse engineering and community research. Contributions are welcome:

1. **Documentation improvements** - Clarify existing content or add missing details
2. **Tool enhancements** - Improve Python decoder or add new utilities
3. **Format analysis** - Help decode additional data fields or sections
4. **Examples and workflows** - Share practical usage scenarios

### Disclaimer

⚠️ **Important Notice**: This documentation is based on personal analysis and reverse engineering. Neither Aerosoft nor Navigraph have published official specifications for the PFPX data format. Use at your own risk and verify results independently.

### License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.

### Acknowledgments

- Community researchers who contributed to format analysis
- PFPX users who provided sample files and feedback
- Aviation professionals who verified data interpretations

---

## 中文

PFPX 导航数据文件的完整指南和工具。

### 概述

本项目为理解和处理 PFPX（专业飞行计划器 X）导航数据库文件提供了全面的文档和 Python 工具。这些导航数据文件使用专有的二进制格式和 XOR 加密，本项目帮助解码和分析这些文件。

### 特性

- 📚 **完整文档** - 详细分析文件格式和数据结构
- 🔧 **Python 解码工具** - 自动化编码/解码，支持进度跟踪
- 📊 **数据分析** - 提取和分析导航数据的工具
- 🗺️ **格式规范** - 跑道、航路点、航路和程序的详细解析
- ⚡ **批量处理** - 高效处理多个文件

### 快速开始

#### 查看文档

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run docs:dev

# 访问 http://localhost:5173
```

文档提供多种语言版本：
- **English**: http://localhost:5173/ (默认)
- **简体中文**: http://localhost:5173/zh/

#### 使用 Python 解码器

```bash
# 基本解码
python tools/nav_decoder.py decode navdata.nav output.txt

# 自动处理模式
python tools/nav_decoder.py auto

# 查看所有选项
python tools/nav_decoder.py --help
```

### 文档结构

```
docs/
├── guide/                  # 主要文档
│   ├── getting-started.md  # 介绍和设置
│   ├── file-structure.md   # 整体文件组织
│   ├── encoding-table.md   # 字符编码详情
│   ├── decoding-process.md # 如何解码文件
│   ├── file-header.md      # 文件头格式规范
│   ├── runways.md          # 跑道数据格式
│   ├── waypoints.md        # 导航点和设施
│   ├── airways.md          # 航路和航线信息
│   ├── sid-procedures.md   # 标准仪表离场程序
│   └── star-procedures.md  # 标准终端进场航线
├── tools/                  # 工具文档
│   ├── python-decoder.md   # Python 工具参考
│   └── examples.md         # 使用示例和工作流
└── index.md               # 首页
```

### 工具

#### Python 解码器 (`tools/nav_decoder.py`)

处理 PFPX 导航数据文件的综合工具：

**功能：**
- 将 `.nav` 文件解码为可读文本
- 将文本文件编码回 `.nav` 格式
- 批量操作的自动处理模式
- 大文件的进度跟踪
- 可配置的 XOR 密钥和参数
- 错误处理和验证

**用法：**
```bash
# 解码文件
python tools/nav_decoder.py decode input.nav output.txt

# 编码文件
python tools/nav_decoder.py encode input.txt output.nav

# 使用标准命名的自动处理
python tools/nav_decoder.py auto
```

### 文件格式概述

PFPX 导航数据文件包含：

1. **文件头**（明文）- 数据库元数据和有效日期
2. **跑道数据**（编码）- 机场跑道规格
3. **航路点数据**（编码）- 导航点、机场、VOR/NDB 设施
4. **航路数据**（编码）- 航线段和连接
5. **SID 数据**（编码）- 标准离场程序
6. **STAR 数据**（编码）- 标准进场程序

除文件头外，所有部分都使用密钥 `0x85` 进行 XOR 加密。

### 数据源

导航数据通常来自：
- **Navigraph** - 主要商业提供商
- **Aerosoft** - 替代数据源
- 遵循 AIRAC 28 天更新周期

### 开发

#### 先决条件
- Node.js 16+（用于文档）
- Python 3.6+（用于工具）

#### 设置
```bash
# 克隆仓库
git clone https://github.com/6639835/pfpx
cd pfpx

# 安装文档依赖
npm install

# 使 Python 工具可执行
chmod +x tools/nav_decoder.py
```

#### 构建文档
```bash
# 开发服务器
npm run docs:dev

# 构建静态站点
npm run docs:build

# 预览生产构建
npm run docs:preview
```

### 贡献

本项目基于逆向工程和社区研究。欢迎贡献：

1. **文档改进** - 澄清现有内容或添加缺失细节
2. **工具增强** - 改进 Python 解码器或添加新实用程序
3. **格式分析** - 帮助解码额外的数据字段或部分
4. **示例和工作流** - 分享实际使用场景

### 免责声明

⚠️ **重要声明**：本文档基于个人分析和逆向工程。Aerosoft 和 Navigraph 都未发布 PFPX 数据格式的官方规范。请自行承担风险使用，并独立验证结果。

### 许可证

本项目根据 MIT 许可证发布。详见 [LICENSE](LICENSE)。

### 致谢

- 为格式分析做出贡献的社区研究人员
- 提供样本文件和反馈的 PFPX 用户
- 验证数据解释的航空专业人员

---

**访问[完整文档](docs/)获取详细指南、规范和示例。**
