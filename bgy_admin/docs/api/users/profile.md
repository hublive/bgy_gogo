# 修改个人信息

## 接口说明

修改当前登录用户的个人信息

## 请求信息

- 请求路径: `/api/users/profile/`
- 请求方法: PUT/PATCH
- 请求头:
  ```
  Authorization: Bearer {access_token}
  Content-Type: application/json
  ```

## 请求参数

| 参数名   | 类型    | 必填 | 说明                   | 示例         |
| -------- | ------- | ---- | ---------------------- | ------------ |
| nickname | string  | 否   | 昵称                   | John Doe     |
| email    | string  | 否   | 邮箱                   | john@doe.com |
| phone    | string  | 否   | 手机号                 | 13800138000  |
| gender   | integer | 否   | 性别(0:未知 1:男 2:女) | 1            |

## 请求示例

```json
{
  "nickname": "John Doe",
  "email": "john@doe.com",
  "phone": "13800138000",
  "gender": 1
}
```

## 响应参数

| 参数名  | 类型    | 说明                           |
| ------- | ------- | ------------------------------ |
| code    | integer | 状态码                         |
| message | string  | 状态信息                       |
| data    | object  | 用户详情(参考用户对象数据结构) |

## 响应示例

```json
{
  "code": 200,
  "message": "更新成功",
  "data": {
    "id": 2,
    "username": "john_doe",
    "nickname": "John Doe",
    "email": "john@doe.com",
    "phone": "13800138000",
    "gender": 1,
    "avatar": null,
    "role": {
      "id": 1,
      "name": "普通用户"
    },
    "department": {
      "id": 1,
      "name": "技术部"
    },
    "is_active": true,
    "last_login": "2024-01-09T10:30:00Z",
    "date_joined": "2024-01-09T10:30:00Z"
  }
}
```

## 错误响应

```json
{
  "code": 400,
  "message": "邮箱格式不正确",
  "data": null
}
```

## 权限要求

- 需要登录
