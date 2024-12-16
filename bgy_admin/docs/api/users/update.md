# 更新用户

## 接口说明

更新指定用户的信息。

## 请求信息

- 请求路径: `/api/users/{id}/`
- 请求方法: PUT/PATCH
- 请求头:
  ```
  Authorization: Bearer {access_token}
  Content-Type: application/json
  ```

## 路径参数

| 参数名 | 类型    | 必填 | 说明    | 示例 |
| ------ | ------- | ---- | ------- | ---- |
| id     | integer | 是   | 用户 ID | 1    |

## 请求参数

| 参数名     | 类型    | 必填 | 说明                   | 示例              |
| ---------- | ------- | ---- | ---------------------- | ----------------- |
| email      | string  | 否   | 邮箱                   | admin@example.com |
| phone      | string  | 否   | 手机号                 | 13800138000       |
| nickname   | string  | 否   | 昵称                   | 管理员            |
| gender     | integer | 否   | 性别(0:未知 1:男 2:女) | 1                 |
| role       | integer | 否   | 角色 ID                | 1                 |
| department | integer | 否   | 部门 ID                | 1                 |
| is_active  | boolean | 否   | 是否启用               | true              |

## 请求示例

```json
{
  "email": "admin@example.com",
  "phone": "13800138000",
  "nickname": "管理员",
  "gender": 1,
  "role": 1,
  "department": 1,
  "is_active": true
}
```

## 响应参数

| 参数名        | 类型    | 说明                   |
| ------------- | ------- | ---------------------- |
| code          | integer | 状态码                 |
| message       | string  | 状态信息               |
| data          | object  | 用户信息               |
| ├─id          | integer | 用户 ID                |
| ├─username    | string  | 用户名                 |
| ├─nickname    | string  | 昵称                   |
| ├─email       | string  | 邮箱                   |
| ├─phone       | string  | 手机号                 |
| ├─gender      | integer | 性别(0:未知 1:男 2:女) |
| ├─avatar      | string  | 头像 URL               |
| ├─role        | object  | 角色信息               |
| │ ├─id        | integer | 角色 ID                |
| │ └─name      | string  | 角色名称               |
| ├─department  | object  | 部门信息               |
| │ ├─id        | integer | 部门 ID                |
| │ └─name      | string  | 部门名称               |
| ├─is_active   | boolean | 是否启用               |
| └─date_joined | string  | 注册时间               |

## 响应示例

### 成功响应

```json
{
  "code": 200,
  "message": "用户更新成功",
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
    "date_joined": "2024-01-01T00:00:00Z"
  }
}
```

### 错误响应

```json
{
  "code": 400,
  "message": "该手机号已被使用",
  "data": null
}
```

## 权限要求

- 需要登录
- 需要以下权限之一：
  - `users.change_user`
  - `users.change_all_users`

## 注意事项

1. 请求方法说明：

   - PUT：需要提供所有必填字段
   - PATCH：只需提供要更新的字段

2. 手机号要求：

   - 必须是有效的中国大陆手机号
   - 不能与其他用户重复

3. 邮箱要求：

   - 必须是有效的邮箱格式
   - 不能与其他用户重复

4. 权限说明：
   - 普通用户只能修改自己的信息
   - 管理员可以修改所有用户的信息
