"""
AI工具箱CMS数据库初始化脚本

此脚本用于初始化数据库并添加示例数据
"""
from app import create_app, db
from app.models.user import User
from app.models.category import Category
from app.models.tool import Tool

# 创建应用上下文
app = create_app('production')

def init_database():
    """初始化数据库并添加示例数据"""
    with app.app_context():
        # 创建所有表
        db.create_all()
        
        # 检查是否已有数据
        if Category.query.count() > 0:
            print("数据库中已有数据，跳过初始化")
            return
        
        # 创建管理员用户
        admin = User(
            username='admin',
            email='admin@example.com',
            is_admin=True
        )
        admin.password = 'admin123'  # 设置密码
        db.session.add(admin)
        
        # 创建示例分类
        categories = [
            Category(name='热门推荐', slug='hot', description='热门AI工具推荐', display_order=0),
            Category(name='AI聊天', slug='chat', description='各类AI聊天工具', display_order=1),
            Category(name='AI绘画', slug='art', description='AI艺术与绘画工具', display_order=2),
            Category(name='AI写作', slug='writing', description='AI辅助写作工具', display_order=3),
            Category(name='AI编程', slug='coding', description='AI编程助手工具', display_order=4),
            Category(name='AI音频', slug='audio', description='AI语音与音频工具', display_order=5),
            Category(name='AI视频', slug='video', description='AI视频创作与编辑工具', display_order=6)
        ]
        
        for category in categories:
            db.session.add(category)
        
        # 提交分类数据以获取ID
        db.session.commit()
        
        # 获取分类ID
        cat_dict = {cat.slug: cat.id for cat in Category.query.all()}
        
        # 创建示例工具
        tools = [
            # 聊天工具
            Tool(name='ChatGPT', description='OpenAI开发的大型语言模型聊天机器人', 
                 url='https://chat.openai.com', icon_class='fab fa-connectdevelop', 
                 category_id=cat_dict['chat'], is_hot=True, display_order=0),
                 
            Tool(name='Claude', description='Anthropic开发的AI助手，专注于有帮助、无害和诚实的对话', 
                 url='https://claude.ai', icon_class='fas fa-robot', 
                 category_id=cat_dict['chat'], is_hot=True, display_order=1),
                 
            Tool(name='Bard', description='Google开发的对话式人工智能服务', 
                 url='https://bard.google.com', icon_class='fab fa-google', 
                 category_id=cat_dict['chat'], display_order=2),
            
            # 绘画工具
            Tool(name='Midjourney', description='AI图像生成工具，通过文本提示创建高质量艺术作品', 
                 url='https://www.midjourney.com', icon_class='fas fa-paint-brush', 
                 category_id=cat_dict['art'], is_hot=True, display_order=0),
                 
            Tool(name='DALL-E', description='OpenAI的AI图像生成系统，可以从文本描述创建图像', 
                 url='https://openai.com/dall-e-3', icon_class='fas fa-image', 
                 category_id=cat_dict['art'], is_hot=True, display_order=1),
                 
            Tool(name='Stable Diffusion', description='开源的深度学习文本到图像模型', 
                 url='https://stability.ai', icon_class='fas fa-layer-group', 
                 category_id=cat_dict['art'], display_order=2),
            
            # 写作工具
            Tool(name='Jasper', description='AI写作助手，可以生成各种类型的文本内容', 
                 url='https://www.jasper.ai', icon_class='fas fa-pencil-alt', 
                 category_id=cat_dict['writing'], is_hot=True, display_order=0),
                 
            Tool(name='Copy.ai', description='使用AI生成营销文案和内容', 
                 url='https://www.copy.ai', icon_class='fas fa-copy', 
                 category_id=cat_dict['writing'], display_order=1),
            
            # 编程工具
            Tool(name='GitHub Copilot', description='AI编程助手，由GitHub和OpenAI合作开发', 
                 url='https://github.com/features/copilot', icon_class='fab fa-github', 
                 category_id=cat_dict['coding'], is_hot=True, display_order=0),
                 
            Tool(name='Cursor', description='AI增强的代码编辑器，帮助开发者更快地编写代码', 
                 url='https://cursor.sh', icon_class='fas fa-terminal', 
                 category_id=cat_dict['coding'], display_order=1),
            
            # 音频工具
            Tool(name='ElevenLabs', description='AI语音合成工具，可以创建逼真的AI语音', 
                 url='https://elevenlabs.io', icon_class='fas fa-microphone', 
                 category_id=cat_dict['audio'], is_hot=True, display_order=0),
                 
            Tool(name='Descript', description='音频和视频编辑工具，具有AI语音合成功能', 
                 url='https://www.descript.com', icon_class='fas fa-headphones', 
                 category_id=cat_dict['audio'], display_order=1),
            
            # 视频工具
            Tool(name='Runway', description='AI视频创作平台，可以生成和编辑视频', 
                 url='https://runwayml.com', icon_class='fas fa-film', 
                 category_id=cat_dict['video'], is_hot=True, display_order=0),
                 
            Tool(name='D-ID', description='AI数字人视频创作平台，可以从静态图像创建会说话的头像', 
                 url='https://www.d-id.com', icon_class='fas fa-user-tie', 
                 category_id=cat_dict['video'], display_order=1)
        ]
        
        for tool in tools:
            db.session.add(tool)
        
        # 提交所有更改
        db.session.commit()
        
        print("数据库初始化完成，添加了以下内容：")
        print(f"- 1名管理员用户")
        print(f"- {len(categories)}个工具分类")
        print(f"- {len(tools)}个AI工具")

if __name__ == "__main__":
    init_database() 