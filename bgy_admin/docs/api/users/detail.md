# 获取用户详情

## 接口说明

获取指定用户的详细信息。

## 请求信息

- 请求路径: `/api/users/{id}/`
- 请求方法: GET
- 请求头:
  ```
  Authorization: Bearer {access_token}
  ```

## 路径参数

| 参数名 | 类型    | 必填 | 说明    | 示例 |
| ------ | ------- | ---- | ------- | ---- |
| id     | integer | 是   | 用户 ID | 1    |

## 响应参数

| 参数名          | 类型    | 说明                   |
| --------------- | ------- | ---------------------- |
| code            | integer | 状态码                 |
| message         | string  | 状态信息               |
| data            | object  | 用户信息               |
| ├─id            | integer | 用户 ID                |
| ├─username      | string  | 用户名                 |
| ├─nickname      | string  | 昵称                   |
| ├─email         | string  | 邮箱                   |
| ├─phone         | string  | 手机号                 |
| ├─gender        | integer | 性别(0:未知 1:男 2:女) |
| ├─avatar        | string  | 头像 URL               |
| ├─role          | object  | 角色信息               |
| │ ├─id          | integer | 角色 ID                |
| │ └─name        | string  | 角色名称               |
| ├─department    | object  | 部门信息               |
| │ ├─id          | integer | 部门 ID                |
| │ └─name        | string  | 部门名称               |
| ├─is_active     | boolean | 是否启用               |
| ├─last_login    | string  | 最后登录时间           |
| ├─date_joined   | string  | 注册时间               |
| ├─login_count   | integer | 登录次数               |
| └─last_login_ip | string  | 最后登录 IP            |

## 响应示例

### 成功响应

```json
{
  "code": 200,
  "message": "success",
  "data": {
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
    "last_login": "2024-01-09T10:30:00Z",
    "date_joined": "2024-01-01T00:00:00Z",
    "login_count": 10,
    "last_login_ip": "127.0.0.1"
  }
}
```

### 错误响应

```json
{
  "code": 404,
  "message": "用户不存在",
  "data": null
}
```

## 权限要求

- 需要登录
- 需要以下权限之一：
  - `users.view_user`
  - `users.view_all_users`
