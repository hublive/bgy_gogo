# BYG Admin API 文档

## 简介

BYG Admin 后台管理系统 API 文档，包含了所有接口的详细说明。

## 接口规范

### 请求格式

- 接口基础路径: `/api`
- 请求方法: GET, POST, PUT, DELETE
- Content-Type: application/json

### 响应格式

```json
{
  "code": 200, // 状态码
  "message": "success", // 状态信息
  "data": {} // 响应数据
}
```

### 认证方式

- Bearer Token 认证
- 在请求头中添加: `Authorization: Bearer {access_token}`

### 错误码说明

- 200: 成功
- 400: 请求参数错误
- 401: 未认证或认证失败
- 403: 权限不足
- 404: 资源不存在
- 500: 服务器内部错误

## 接口目录

1. [认证相关](./auth/README.md)
   - [登录获取 token](./auth/login.md)
   - [刷新 token](./auth/refresh.md)
2. [用户管理](./users/README.md)
   - [获取用户列表](./users/list.md)
   - [创建用户](./users/create.md)
   - [重置用户密码](./users/reset_password.md)
