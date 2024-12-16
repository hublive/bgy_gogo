# 开发指南

## 1. 环境准备

### 1.1 Python 环境

- Python 3.8+
- pip 或 poetry

### 1.2 数据库

- MySQL 8.0+
- Redis 6.0+

### 1.3 开发工具

- VS Code 或 PyCharm
- Git

## 2. 项目设置

### 2.1 克隆项目

```bash
git clone https://github.com/your-repo/byg-admin.git
cd byg-admin
```

### 2.2 安装依赖

```bash
pip install -r requirements.txt
```

### 2.3 配置环境变量

创建 .env 文件:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=byg_admin
DB_USER=root
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=3306
```

### 2.4 数据库迁移

```bash
python manage.py migrate
```

## 3. 开发规范

### 3.1 代码风格

- 遵循 PEP 8 规范
- 使用 4 个空格缩进
- 行长度不超过 120 字符

### 3.2 API 开发

- 使用 ViewSet 组织视图
- 使用序列化器验证数据
- 统一使用 APIResponse 返回数据
- 添加适当的权限控制

### 3.3 文档规范

- 为所有接口添加文档字符串
- 使用 drf-spectacular 生成 API 文档
- 及时更新 README 和开发文档

## 4. 测试

### 4.1 单元测试

```bash
python manage.py test
```

### 4.2 代码覆盖率

```bash
coverage run manage.py test
coverage report
```

## 5. 部署

### 5.1 生产环境配置

- 禁用 DEBUG 模式
- 配置安全的 SECRET_KEY
- 使用 HTTPS
- 配置跨域白名单

### 5.2 性能优化

- 使用缓存减少查询
- 优化数据库查询
- 使用异步任务处理耗时操作
