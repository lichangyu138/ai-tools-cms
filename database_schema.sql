-- AI工具箱CMS数据库架构

CREATE DATABASE IF NOT EXISTS ai_toolkit_cms CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE ai_toolkit_cms;

-- 用户表
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 工具类别表
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    slug VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    display_order INT DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 工具表
CREATE TABLE tools (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    url VARCHAR(255) NOT NULL,
    icon_class VARCHAR(50),  -- Font Awesome图标类名
    icon_path VARCHAR(255),  -- 自定义图标路径
    color_class VARCHAR(20), -- 颜色类名
    category_id INT NOT NULL,
    is_hot BOOLEAN DEFAULT FALSE,  -- 是否热门工具
    is_active BOOLEAN DEFAULT TRUE,
    display_order INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- 初始数据：管理员账户
INSERT INTO users (username, password, email, is_admin) 
VALUES ('admin', '$2b$12$eVQQMEFyU2dRZUc4Umh3VORm1iCDu85zq/ZxV5vELhj2LXSy0xfZW', 'admin@example.com', TRUE);
-- 默认密码: admin123 (已加密)

-- 初始数据：默认类别
INSERT INTO categories (name, slug, description, display_order) VALUES 
('热门推荐', 'hot', '热门AI工具推荐', 1),
('AI视频工具', 'video', 'AI视频生成和编辑工具', 2),
('AI编程助手', 'coding', 'AI辅助编程和开发工具', 3),
('AI写作', 'writing', 'AI写作和内容创作工具', 4),
('AI图像生成', 'image', 'AI图像生成和处理工具', 5),
('AI设计工具', 'design', 'AI辅助设计工具', 6),
('AI音频工具', 'audio', 'AI音频生成和处理工具', 7),
('AI办公套件', 'office', 'AI办公和生产力工具', 8),
('AI大模型', 'model', '开放的AI大模型', 9),
('AI数字人', 'avatar', 'AI数字人和虚拟形象', 10),
('AI翻译助手', 'translation', 'AI翻译和语言处理工具', 11),
('AI营销工具', 'marketing', 'AI营销和推广工具', 12),
('AI搜索引擎', 'search', 'AI搜索和信息检索工具', 13); 