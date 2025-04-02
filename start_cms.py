"""
AI工具箱CMS系统启动脚本
"""
import os
import subprocess
import sys

def main():
    print("=" * 40)
    print("    AI工具箱CMS系统启动脚本")
    print("=" * 40)
    print()
    
    # 检查Python版本
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("[错误] Python版本必须是3.8或更高版本")
        sys.exit(1)
    
    # 检查虚拟环境是否存在
    venv_path = "venv"
    if not os.path.exists(venv_path):
        print("[信息] 创建虚拟环境...")
        subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)
    
    # 在Windows上激活虚拟环境
    if os.name == "nt":
        activate_script = os.path.join(venv_path, "Scripts", "activate.bat")
        pip_path = os.path.join(venv_path, "Scripts", "pip")
        python_path = os.path.join(venv_path, "Scripts", "python")
    else:
        activate_script = os.path.join(venv_path, "bin", "activate")
        pip_path = os.path.join(venv_path, "bin", "pip")
        python_path = os.path.join(venv_path, "bin", "python")
    
    # 直接安装依赖，无需检查
    print("[信息] 安装依赖...")
    
    # 定义项目所需的依赖列表
    dependencies = [
        "flask==2.3.3",
        "flask-sqlalchemy==3.1.1",
        "flask-login==0.6.2",
        "flask-wtf==1.2.1",
        "pymysql==1.1.0",
        "email-validator==2.0.0",
        "python-dotenv==1.0.0",
        "bcrypt==4.0.1",
        "gunicorn==21.2.0",
        "Werkzeug==2.3.7"
    ]
    
    # 安装每个依赖
    for dependency in dependencies:
        print(f"[信息] 安装 {dependency}...")
        subprocess.run([pip_path, "install", dependency], check=True)
    
    # 启动应用
    print("[信息] 启动AI工具箱CMS系统...")
    print("[信息] 请访问 http://localhost:9999")
    
    # 设置PORT环境变量为9999
    env = os.environ.copy()
    env["PORT"] = "9999"
    
    # 启动应用
    subprocess.run([python_path, "app.py"], env=env)

if __name__ == "__main__":
    main() 