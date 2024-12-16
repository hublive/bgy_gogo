# 获取角色列表

## 接口说明

获取系统中的角色列表，支持分页、搜索和过滤。

## 请求信息

- 请求路径: `/api/roles/`
- 请求方法: GET
- 请求头: `Authorization: Bearer {access_token}`

## 请求参数

| 参数名    | 类型    | 必填 | 说明     | 示例   |
| --------- | ------- | ---- | -------- | ------ |
| page      | integer | 否   | 页码     | 1      |
| page_size | integer | 否   | 每页数量 | 10     |
| name      | string  | 否   | 角色名称 | 管理员 |
| key       | string  | 否   | 角色标识 | admin  |
| is_active | boolean | 否   | 是否启用 | true   |

## 响应参数

| 参数名        | 类型    | 说明     |
| ------------- | ------- | -------- |
| code          | integer | 状态码   |
| message       | string  | 状态信息 |
| data          | object  | 响应数据 |
| ├─count       | integer | 总记录数 |
| ├─results     | array   | 角色列表 |
| ├─name        | string  | 角色名称 |
| ├─key         | string  | 角色标识 |
| ├─desc        | string  | 角色描述 |
| ├─permissions | array   | 权限列表 |
| ├─menus       | array   | 菜单权限 |
| ├─data_scope  | string  | 数据范围 |
| └─is_active   | boolean | 是否启用 |

## 响应示例

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "count": 2,
    "results": [
      {
        "id": 1,
        "name": "超级管理员",
        "key": "super_admin",
        "desc": "系统超级管理员",
        "permissions": ["*"],
        "menus": ["*"],
        "data_scope": "ALL",
        "is_active": true
      }
    ]
  }
}
```
