import os
import chardet
import codecs

def check_and_fix_encoding(directory):
    """检查目录下所有HTML文件的编码，并转换为UTF-8无BOM格式"""
    print(f"正在检查目录: {directory}")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.html', '.htm')):
                file_path = os.path.join(root, file)
                fix_file_encoding(file_path)

def fix_file_encoding(file_path):
    """检查文件编码并转换为UTF-8无BOM"""
    # 先读取文件内容并检测编码
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    
    # 检测文件的编码
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    confidence = result['confidence']
    
    # 输出检测结果
    print(f"文件: {file_path}")
    print(f"检测编码: {encoding}, 置信度: {confidence:.2f}")
    
    # 检查是否有BOM标记
    has_bom = False
    if raw_data.startswith(codecs.BOM_UTF8):
        has_bom = True
        print("检测到UTF-8 BOM标记")
    elif raw_data.startswith(b'\xff\xfe') or raw_data.startswith(b'\xfe\xff'):
        has_bom = True
        print("检测到UTF-16 BOM标记")
    
    # 如果需要修复编码
    if has_bom or encoding.lower() != 'utf-8':
        print("正在转换为UTF-8无BOM格式...")
        
        # 尝试解码文件内容
        try:
            if has_bom and encoding.lower() == 'utf-8':
                # UTF-8 with BOM
                content = raw_data.decode('utf-8-sig')
            else:
                # 其他编码
                content = raw_data.decode(encoding)
                
            # 保存为UTF-8无BOM
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print("文件已转换为UTF-8无BOM格式")
        except Exception as e:
            print(f"转换失败: {e}")
    else:
        print("文件编码正确，无需修复")
    
    print("-" * 50)

if __name__ == "__main__":
    templates_dir = "app/templates"
    check_and_fix_encoding(templates_dir)
    print("编码检查和修复完成") 