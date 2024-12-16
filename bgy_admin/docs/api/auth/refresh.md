# 刷新访问令牌

## 接口说明

通过刷新令牌(refresh_token)获取新的访问令牌(access_token)

## 请求信息

- 请求路径: `/api/auth/refresh/`
- 请求方法: POST
- 请求头:
  ```
  Content-Type: application/json
  ```

## 请求参数

| 参数名  | 类型   | 必填 | 说明                                              | 示例    |
| ------- | ------ | ---- | ------------------------------------------------- | ------- |
| refresh | string | 是   | 刷新令牌(之前获取 token 接口返回的 refresh_token) | eyJ0... |

## 请求示例

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

## 响应参数

| 参数名         | 类型    | 说明                 | 示例    |
| -------------- | ------- | -------------------- | ------- |
| code           | integer | 状态码               | 200     |
| message        | string  | 状态信息             | success |
| data           | object  | 响应数据             |         |
| ├─access_token | string  | 新的访问令牌         | eyJ0... |
| ├─token_type   | string  | 令牌类型             | Bearer  |
| └─expires_in   | integer | ��� 问令牌有效期(秒) | 3600    |

## 响应示例

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "token_type": "Bearer",
    "expires_in": 3600
  }
}
```

## 错误响应

```json
{
  "code": 401,
  "message": "无效的刷新令牌",
  "data": null
}
```

## 使用场景

当 access_token 过期时，使用 refresh_token 获取新的 access_token，避免重新登录
