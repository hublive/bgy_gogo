# 分配角色

## 接口说明

为指定用户分配角色列表，会覆盖原有的角色关联关系。

## 请求信息

- 请求路径: `/api/users/{id}/assign_roles/`
- 请求方法: POST
- 请求头: `Authorization: Bearer {access_token}`

## 请求参数

| 参数名   | 类型  | 必填 | 说明         | 示例      |
| -------- | ----- | ---- | ------------ | --------- |
| role_ids | array | 是   | 角色 ID 列表 | [1, 2, 3] |

## 响应参数

| 参数名  | 类型    | 说明     |
| ------- | ------- | -------- |
| code    | integer | 状态码   |
| message | string  | 状态信息 |

## 响应示例

```json
{
  "code": 200,
  "message": "分配角色成功"
}
```

## 错误响应

```json
{
  "code": 400,
  "message": "部分角色不存在"
}
```
