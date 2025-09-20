# 使用示例

使用我们的 Python 解码器处理 PFPX 导航数据文件的实际示例和工作流程。

## 入门示例

### 您的第一次解码

```bash
# 将导航数据文件下载到工作目录
# 运行解码器
python nav_decoder.py decode navdata.nav decoded_output.txt

# 查看结果
head -20 decoded_output.txt
```

预期输出：
```
PFPX NAVDATA
NG2509
2025/09/04
2025/10/01
NAVIGRAPH

RWY ZBAA01   12467197359ASP+40058914+116617658
RWY ZBAA19   12467197179ASP+40073556+116598889
...
```

### 自动处理工作流程

```bash
# 设置标准文件名
cp your_navdata.nav wait2decode.nav

# 运行自动处理
python nav_decoder.py auto

# 结果自动出现
ls -la already_decode.txt
```

## 数据分析示例

### 提取跑道信息

```python
#!/usr/bin/env python3
"""从 PFPX 导航数据文件中提取跑道数据。"""

from tools.nav_decoder import NavCodec
import re
from pathlib import Path

def extract_runways(navdata_file, output_file):
    """将所有跑道记录提取到单独的文件中。"""
    
    # 解码导航数据文件
    codec = NavCodec()
    decoded_file = "temp_decoded.txt"
    codec.decode_file(Path(navdata_file), Path(decoded_file))
    
    # 提取跑道记录
    runways = []
    with open(decoded_file, 'r') as f:
        for line in f:
            if line.startswith('RWY'):
                runways.append(line.strip())
    
    # 写入跑道数据
    with open(output_file, 'w') as f:
        f.write(f"找到 {len(runways)} 条跑道\n")
        f.write("=" * 50 + "\n")
        for runway in runways:
            f.write(runway + "\n")
    
    print(f"提取了 {len(runways)} 条跑道到 {output_file}")

# 使用方法
extract_runways("navdata.nav", "runways_only.txt")
```

### 机场分析

```python
#!/usr/bin/env python3
"""分析机场及其跑道。"""

from tools.nav_decoder import NavCodec
from collections import defaultdict
import re

def analyze_airports(navdata_file):
    """分析机场数据和跑道数量。"""
    
    # 解码文件
    codec = NavCodec()
    decoded_file = "temp_decoded.txt"
    codec.decode_file(navdata_file, decoded_file)
    
    # 统计每个机场的跑道
    airport_runways = defaultdict(list)
    
    with open(decoded_file, 'r') as f:
        for line in f:
            if line.startswith('RWY'):
                # 解析：RWY ICAO## ...
                parts = line.split()
                if len(parts) >= 2:
                    icao_runway = parts[1]  # 例如："ZBAA01"
                    icao = icao_runway[:4]  # "ZBAA"
                    runway = icao_runway[4:] # "01"
                    airport_runways[icao].append(runway)
    
    # 显示结果
    print(f"机场分析（{len(airport_runways)} 个机场）")
    print("=" * 50)
    
    for icao in sorted(airport_runways.keys())[:10]:  # 前 10 个
        runways = airport_runways[icao]
        print(f"{icao}: {len(runways)} 条跑道 - {', '.join(runways)}")

# 使用方法
analyze_airports("navdata.nav")
```

## 批量处理示例

### 处理多个文件

```python
#!/usr/bin/env python3
"""批量处理多个导航数据文件。"""

from tools.nav_decoder import NavCodec
from pathlib import Path
import sys

def batch_decode(input_dir, output_dir):
    """解码目录中的所有 .nav 文件。"""
    
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # 创建输出目录
    output_path.mkdir(exist_ok=True)
    
    # 查找所有 .nav 文件
    nav_files = list(input_path.glob("*.nav"))
    if not nav_files:
        print(f"在 {input_dir} 中没有找到 .nav 文件")
        return
    
    print(f"找到 {len(nav_files)} 个文件需要处理")
    
    codec = NavCodec()
    successful = 0
    failed = 0
    
    for nav_file in nav_files:
        output_file = output_path / f"{nav_file.stem}_decoded.txt"
        
        try:
            codec.decode_file(nav_file, output_file)
            print(f"✓ {nav_file.name}")
            successful += 1
        except Exception as e:
            print(f"✗ {nav_file.name}: {e}")
            failed += 1
    
    print(f"\n结果：{successful} 成功，{failed} 失败")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法：python batch_decode.py <输入目录> <输出目录>")
        sys.exit(1)
    
    batch_decode(sys.argv[1], sys.argv[2])
```

## 集成示例

### Flask Web 服务

```python
#!/usr/bin/env python3
"""用于导航数据解码的 Web 服务。"""

from flask import Flask, request, jsonify, send_file
from tools.nav_decoder import NavCodec
import tempfile
import os
from pathlib import Path

app = Flask(__name__)
codec = NavCodec()

@app.route('/api/decode', methods=['POST'])
def decode_api():
    """解码导航数据文件的 API 端点。"""
    
    if 'file' not in request.files:
        return jsonify({'error': '未提供文件'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '未选择文件'}), 400
    
    # 创建临时文件
    with tempfile.NamedTemporaryFile(suffix='.nav', delete=False) as input_temp:
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as output_temp:
            try:
                # 保存上传的文件
                file.save(input_temp.name)
                
                # 解码
                codec.decode_file(Path(input_temp.name), Path(output_temp.name))
                
                # 返回解码后的文件
                return send_file(
                    output_temp.name,
                    as_attachment=True,
                    download_name='decoded_navdata.txt'
                )
                
            except Exception as e:
                return jsonify({'error': str(e)}), 500
            
            finally:
                # 清理
                try:
                    os.unlink(input_temp.name)
                    os.unlink(output_temp.name)
                except:
                    pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

## 高级工作流程

### 带监控的自动化处理

```python
#!/usr/bin/env python3
"""监控目录中的新导航数据文件并自动处理。"""

import time
from pathlib import Path
from tools.nav_decoder import NavCodec
import logging

class NavdataMonitor:
    """监控目录中的新导航数据文件。"""
    
    def __init__(self, watch_dir, output_dir, check_interval=60):
        self.watch_dir = Path(watch_dir)
        self.output_dir = Path(output_dir)
        self.check_interval = check_interval
        self.codec = NavCodec()
        self.processed_files = set()
        
        # 设置日志记录
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def process_new_files(self):
        """检查并处理新的 .nav 文件。"""
        nav_files = set(self.watch_dir.glob("*.nav"))
        new_files = nav_files - self.processed_files
        
        for nav_file in new_files:
            output_file = self.output_dir / f"{nav_file.stem}_decoded.txt"
            
            try:
                self.logger.info(f"处理中：{nav_file.name}")
                self.codec.decode_file(nav_file, output_file)
                self.logger.info(f"完成：{nav_file.name}")
                self.processed_files.add(nav_file)
                
            except Exception as e:
                self.logger.error(f"处理 {nav_file.name} 失败：{e}")
    
    def run(self):
        """启动监控循环。"""
        self.logger.info(f"启动监控：{self.watch_dir}")
        self.logger.info(f"输出目录：{self.output_dir}")
        self.logger.info(f"检查间隔：{self.check_interval}秒")
        
        self.output_dir.mkdir(exist_ok=True)
        
        try:
            while True:
                self.process_new_files()
                time.sleep(self.check_interval)
                
        except KeyboardInterrupt:
            self.logger.info("用户停止监控")

# 使用方法
if __name__ == "__main__":
    monitor = NavdataMonitor("input_files", "decoded_files", 30)
    monitor.run()
```

## 下一步

- **[了解数据格式](../guide/)** - 理解解码数据包含的内容
- **[探索 Python 解码器](./python-decoder.md)** - 高级功能和配置
- **[研究特定数据段](../guide/runways.md)** - 详细格式规范
