# 分配部门

## 接口说明

为指定用户分配部门。

## 请求信息

- 请求路径: `/api/users/{id}/assign_department/`
- 请求方法: POST
- 请求头: `Authorization: Bearer {access_token}`

## 请求参数

| 参数名        | 类型    | 必填 | 说明    | 示例 |
| ------------- | ------- | ---- | ------- | ---- |
| department_id | integer | 是   | 部门 ID | 1    |

## 响应参数

| 参数名  | 类型    | 说明     |
| ------- | ------- | -------- |
| code    | integer | 状态码   |
| message | string  | 状态信息 |

## 响应示例

```json
{
  "code": 200,
  "message": "分配部门成功"
}
```

## 错误响应

```json
{
  "code": 400,
  "message": "部门不存在"
}
```
