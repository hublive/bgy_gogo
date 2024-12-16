# 修改密码

## 接口说明

修改指定用户的登录密码。

## 请求信息

- 请求路径: `/api/users/{id}/change_password/`
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

| 参数名           | 类型   | 必填 | 说明     | 示例        |
| ---------------- | ------ | ---- | -------- | ----------- |
| old_password     | string | 是   | 原密码   | OldPass123! |
| new_password     | string | 是   | 新密码   | NewPass123! |
| confirm_password | string | 是   | 确认密码 | NewPass123! |

## 请求示例

```json
{
  "old_password": "OldPass123!",
  "new_password": "NewPass123!",
  "confirm_password": "NewPass123!"
}
```

## 响应参数

| 参数名  | 类型    | 说明     |
| ------- | ------- | -------- |
| code    | integer | 状态码   |
| message | string  | 状态信息 |
| data    | null    | 无       |

## 响应示例

### 成功响应

```json
{
  "code": 200,
  "message": "密码修改成功",
  "data": null
}
```

### 错误响应

```json
{
  "code": 400,
  "message": "原密码错误",
  "data": null
}
```

## 权限要求

- 需要登录
- 需要以下权限之一：
  - `users.change_password`（修改自己的密码）
  - `users.change_all_passwords`（修改任何用户的密码）

## 注意事项

1. 密码要求：

   - 长度至少 8 位
   - 必须包含大小写字母和数字
   - 可以包含特殊字符
   - 不能与最近使用过的密码相同

2. 安全建议：

   - 建议定期更换密码
   - 不要使用易猜测的密码
   - 不要在不安全的网络中修改密码

3. 修改后影响：
   - 修改密码后会自动登出所有设备
   - 需要使用新密码重新登录
   - 所有已颁发的 Token 将失效
