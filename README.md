# AI工具箱 CMS系统

AI工具箱是一个一站式AI工具导航平台，收集和分类各种前沿AI工具，帮助用户发现和使用最新最热门的AI技术。现已升级为CMS系统，支持通过后台管理内容。

## 系统特点

- **内容管理系统**：通过后台轻松管理AI工具和分类
- **分类浏览**：AI工具按照功能和用途进行分类，方便用户查找
- **一键直达**：点击工具卡片即可直接访问对应的AI工具
- **简洁介绍**：每个工具都有简短的功能介绍，帮助用户了解工具用途
- **响应式设计**：适配各种设备屏幕，提供良好的移动端体验

## 已收录分类

- 热门AI工具推荐
- AI视频工具
- AI编程助手
- AI写作工具
- AI图像生成
- AI设计工具
- AI音频工具
- AI办公套件
- AI大模型
- 等等

## 安装和使用

### 系统要求
- Python 3.8+
- MySQL 5.7+

### 安装步骤

1. 克隆本项目到本地
2. 配置.env文件（或直接使用默认配置）:
   ```
   # 复制示例配置
   cp .env.example .env
   
   # 编辑配置文件
   # 默认已配置使用远程MySQL服务器：172.31.46.204:9998
   ```
3. 安装依赖和启动应用：
   ```
   # 使用启动脚本（推荐）
   python start_cms.py
   
   # 或手动安装和启动
   pip install -r requirements.txt
   python app.py
   ```
4. 在浏览器中访问 `http://localhost:5000`

### 管理员登录

- 默认管理员账号：admin
- 默认管理员密码：admin123
- 管理后台地址：`http://localhost:5000/admin`

## 数据库配置

当前系统配置使用远程MySQL数据库：
- 主机: 
- 端口: 9998
- 用户名: root
- 密码: HA4z4tJMKXzy5hwm
- 数据库名: ai_toolkit_cms

## 技术栈

- Python 3.8+
- Flask 框架
- SQLAlchemy ORM
- MySQL 数据库
- HTML5/CSS3/JavaScript
- Bootstrap 5
- Font Awesome 图标

## 目录结构

```
ai-toolkit-cms/
  ├── app/                # 应用目录
  │   ├── models/         # 数据库模型
  │   ├── routes/         # 路由和视图
  │   ├── forms/          # 表单类
  │   ├── static/         # 静态资源
  │   └── templates/      # HTML模板
  ├── config.py           # 配置文件
  ├── app.py              # 应用入口
  ├── start_cms.py        # 启动脚本
  ├── requirements.txt    # 依赖列表
  └── database_schema.sql # 数据库架构
```

## 许可证

MIT License

## 联系方式
