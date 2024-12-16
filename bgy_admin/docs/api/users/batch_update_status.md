# 批量更新用户状态

## 接口说明

批量修改多个用户的启用状态。

## 请求信息

- 请求路径: `/api/users/batch_update_status/`
- 请求方法: POST
- 请求头:
  ```
  Authorization: Bearer {access_token}
  Content-Type: application/json
  ```

## 请求参数

| 参数名    | 类型    | 必填 | 说明         | 示例      |
| --------- | ------- | ---- | ------------ | --------- |
| ids       | array   | 是   | 用户 ID 列表 | [1, 2, 3] |
| is_active | boolean | 是   | 启用状态     | true      |

## 请求示例

```json
{
  "ids": [1, 2, 3],
  "is_active": true
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
  "message": "成功启用3个用户",
  "data": null
}
```

### 错误响应

```json
{
  "code": 400,
  "message": "请选择要操作的用户",
  "data": null
}
```

## 权限要求

- 需要登录
- 需要以下权限之一：
  - `users.change_user`
  - `users.change_all_users`

## 注意事项

1. 状态说明：

   - true：启用用户
   - false：禁用用户

2. 权限说明：

   - 普通用户不能修改用户状态
   - 管理员可以修改除自己以外的所有用户状态
   - 超级管理员可以修改任何用户状态

3. 操作建议：
   - 建议每次批量操作不超过 100 个用户
   - 禁用用户后，用户将无法登录系统
   - 可以随时重新启用被禁用的用户
