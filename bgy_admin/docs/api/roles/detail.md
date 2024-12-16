# 获取角色详情

## 接口说明

获取指定角色的详细信息，包括权限列表和关联的菜单等。

## 请求信息

- 请求路径: `/api/roles/{id}/`
- 请求方法: GET
- 请求头: `Authorization: Bearer {access_token}`

## 请求参数

| 参数名 | 类型    | 必填 | 说明    | 示例 |
| ------ | ------- | ---- | ------- | ---- |
| id     | integer | 是   | 角色 ID | 1    |

## 响应参数

| 参数名        | 类型    | 说明         |
| ------------- | ------- | ------------ |
| code          | integer | 状态码       |
| message       | string  | 状态信息     |
| data          | object  | 角色详细信息 |
| ├─id          | integer | 角色 ID      |
| ├─name        | string  | 角色名称     |
| ├─key         | string  | 角色标识     |
| ├─desc        | string  | 角色描述     |
| ├─permissions | array   | 权限列表     |
| ├─menus       | array   | 菜单权限     |
| ├─data_scope  | string  | 数据范围     |
| ├─order       | integer | 显示顺序     |
| └─is_active   | boolean | 是否启用     |

## 响应示例

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 1,
    "name": "超级管理员",
    "key": "super_admin",
    "desc": "系统超级管理员",
    "permissions": ["*"],
    "menus": ["*"],
    "data_scope": "ALL",
    "order": 1,
    "is_active": true,
    "created_at": "2024-01-11T10:00:00Z",
    "updated_at": "2024-01-11T10:00:00Z"
  }
}
```
