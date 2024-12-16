# 用户管理接口

## 接口列表

### 1. 用户基础操作

- [获取用户列表](./list.md)
- [获取用户详情](./detail.md)
- [创建用户](./create.md)
- [更新用户](./update.md)
- [删除用户](./delete.md)

### 2. 用户扩展操作

- [重置用户密码](./reset_password.md)
- [修改个人信息](./profile.md)
- [上传用户头像](./avatar.md)

## 数据结构

### 用户对象

```json
{
  "id": 1,
  "username": "admin",
  "nickname": "管理员",
  "email": "admin@example.com",
  "phone": "13800138000",
  "gender": 1,
  "avatar": "http://example.com/media/avatars/1.jpg",
  "role": {
    "id": 1,
    "name": "超级管理员"
  },
  "department": {
    "id": 1,
    "name": "技术部"
  },
  "is_active": true,
  "last_login": "2024-01-08T10:00:00Z",
  "date_joined": "2024-01-01T00:00:00Z"
}
```

### 字段说明

| 字段名      | 类型    | 说明                        |
| ----------- | ------- | --------------------------- |
| id          | integer | 用户 ID                     |
| username    | string  | 用户名                      |
| nickname    | string  | 昵称                        |
| email       | string  | 邮箱                        |
| phone       | string  | 手机号                      |
| gender      | integer | 性别(0:未知 1:男 2:女)      |
| avatar      | string  | 头像 URL                    |
| role        | object  | 角色信息                    |
| department  | object  | 部门信息                    |
| is_active   | boolean | 是否启用                    |
| last_login  | string  | 最后登录时间(ISO 8601 格式) |
| date_joined | string  | 注册时间(ISO 8601 格式)     |
