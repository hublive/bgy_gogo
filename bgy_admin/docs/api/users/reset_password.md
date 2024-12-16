# 重置用户密码

## 接口说明

重置指定用户的登录密码

## 请求信息

- 请求路径: `/api/users/{id}/reset_password/`
- 请求方法: POST
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

| 参数名   | 类型   | 必填 | 说明   | 示例         |
| -------- | ------ | ---- | ------ | ------------ |
| password | string | 是   | 新密码 | Password123! |

## 请求示例

```json
{
  "password": "Password123!"
}
```

## 响应参数

| 参数名  | 类型    | 说明     |
| ------- | ------- | -------- |
| code    | integer | 状态码   |
| message | string  | 状态信息 |
| data    | null    | 无       |

## 响应示例

```json
{
  "code": 200,
  "message": "密码重置成功",
  "data": null
}
```

## 错误响应

```json
{
  "code": 400,
  "message": "密码不能为空",
  "data": null
}
```

## 权限要 ��

- 需要登录
- 需要以下权限之一：
  - `users.change_user_password`
  - `users.change_all_users_password`
