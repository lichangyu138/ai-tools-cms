import os
from app import create_app, db
from app.models.user import User
from app.models.category import Category
from app.models.tool import Tool

# 从环境变量获取配置
env = os.environ.get('FLASK_ENV', 'production')
app = create_app(env)

@app.shell_context_processor
def make_shell_context():
    """为Flask shell提供上下文"""
    return {
        'db': db, 
        'User': User, 
        'Category': Category, 
        'Tool': Tool
    }

if __name__ == '__main__':
    # 生产环境使用0.0.0.0主机，允许外部访问
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    debug = env != 'production'
    
    app.run(host=host, port=port, debug=debug) 