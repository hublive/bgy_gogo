# 用户登录

## 接口说明

使用用户名和密码登录系统。

## 请求信息

- 请求路径: `/api/auth/login/`
- 请求方法: POST
- 请求头:
  - Content-Type: application/json

## 请求参数

| 参数名   | 类型   | 必填 | 说明     | 示例   |
| -------- | ------ | ---- | -------- | ------ |
| username | string | 是   | 登录账号 | admin  |
| password | string | 是   | 登录密码 | 123456 |

## 响应参数

| 参数名          | 类型    | 说明              |
| --------------- | ------- | ----------------- |
| code            | integer | 状态码 (200 成功) |
| message         | string  | 状态信息          |
| data            | object  | 响应数据          |
| ├─access_token  | string  | 访问令牌          |
| ├─refresh_token | string  | 刷新令牌          |
| ├─token_type    | string  | 令牌类型 (Bearer) |
| ├─expires_in    | integer | 过期时间(秒)      |
| └─user          | object  | 用户信息          |
| ├─id            | integer | 用户 ID           |
| ├─username      | string  | 用户名            |
| ├─nickname      | string  | 用户昵称          |
| ├─avatar        | string  | 头像 URL          |
| ├─roles         | array   | 角色列表          |
| │ ├─id          | integer | 角色 ID           |
| │ └─name        | string  | 角色名称          |
| └─permissions   | array   | 权限列表          |

## 请求示例

```json
{
  "username": "admin",
  "password": "123456"
}
```

## 响应示例

### 成功响应

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "token_type": "Bearer",
    "expires_in": 3600,
    "user": {
      "id": 1,
      "username": "admin",
      "nickname": "管理员",
      "avatar": null,
      "roles": [
        {
          "id": 1,
          "name": "超级管理员"
        }
      ],
      "permissions": ["*"]
    }
  }
}
```

### 错误响应

```json
{
  "code": 400,
  "message": "用户名或密码错误"
}
```

```json
{
  "code": 400,
  "message": "用户已被禁用"
}
```

## 错误码说明

| 错误码 | 说明       |
| ------ | ---------- |
| 200    | 成功       |
| 400    | 参数错误   |
| 401    | 未授权     |
| 500    | 服务器错误 |
