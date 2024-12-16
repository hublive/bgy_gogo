# 在线用户管理

## 获取在线用户列表

### 接口说明

获取当前在线的用户列表。

### 请求信息

- 请求路径: `/api/users/online_users/`
- 请求方法: GET
- 请求头:
  ```
  Authorization: Bearer {access_token}
  ```

### 响应参数

| 参数名          | 类型    | 说明         |
| --------------- | ------- | ------------ |
| code            | integer | 状态码       |
| message         | string  | 状态信息     |
| data            | array   | 在线用户列表 |
| ├─id            | integer | 用户 ID      |
| ├─username      | string  | 用户名       |
| ├─nickname      | string  | 昵称         |
| ├─ip_address    | string  | IP 地址      |
| ├─user_agent    | string  | 浏览器标识   |
| ├─login_time    | string  | 登录时间     |
| └─last_activity | string  | 最后活动时间 |

### 响应示例

#### 成功响应

```json
{
  "code": 200,
  "message": "success",
  "data": [
    {
      "id": 1,
      "username": "admin",
      "nickname": "管理员",
      "ip_address": "127.0.0.1",
      "user_agent": "Mozilla/5.0 ...",
      "login_time": "2024-01-09T10:00:00Z",
      "last_activity": "2024-01-09T10:30:00Z"
    }
  ]
}
```

### 权限要求

- 需要登录
- 需要以下权限之一：
  - `users.view_online_users`
  - `users.view_all_online_users`

## 强制用户下线

### 接口说明

强制指定用户退出登录。

### 请求信息

- 请求路径: `/api/users/{id}/force_logout/`
- 请求方法: POST
- 请求头:
  ```
  Authorization: Bearer {access_token}
  ```

### 路径参数

| 参数名 | 类型    | 必填 | 说明    | 示例 |
| ------ | ------- | ---- | ------- | ---- |
| id     | integer | 是   | 用户 ID | 1    |

### 响应参数

| 参数名             | 类型    | 说明         |
| ------------------ | ------- | ------------ |
| code               | integer | 状态码       |
| message            | string  | 状态信息     |
| data               | object  | 响应数据     |
| └─deleted_sessions | integer | 删除的会话数 |

### 响应示例

#### 成功响应

```json
{
  "code": 200,
  "message": "已强制下线用户 admin",
  "data": {
    "deleted_sessions": 1
  }
}
```

#### 错误响应

```json
{
  "code": 404,
  "message": "用户不存在",
  "data": null
}
```

### 权限要求

- 需要登录
- 需要以下权限之一：
  - `users.force_logout`
  - `users.force_logout_all`

### 注意事项

1. 在线判断：

   - 最近 30 分钟内有活动的用户视为在线
   - 超过 30 分钟未活动的会话自动清理

2. 强制下线：
   - 会删除用户的所有会话记录
   - 用户需要重新登录才能访问系统
   - 不能强制下线自己
