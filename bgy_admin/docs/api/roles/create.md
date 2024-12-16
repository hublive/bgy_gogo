# 创建角色

## 接口说明

创建新的角色，需要管理员权限。

## 请求信息

- 请求路径: `/api/roles/`
- 请求方法: POST
- 请求头: `Authorization: Bearer {access_token}`

## 请求参数

| 参数名      | 类型    | 必填 | 说明     | 示例          |
| ----------- | ------- | ---- | -------- | ------------- |
| name        | string  | 是   | 角色名称 | 部门管理员    |
| key         | string  | 是   | 角色标识 | dept_admin    |
| desc        | string  | 否   | 角色描述 | 部门管理角色  |
| permissions | array   | 否   | 权限列表 | ["view_user"] |
| menus       | array   | 否   | 菜单权限 | [1, 2, 3]     |
| data_scope  | string  | 否   | 数据范围 | "DEPT"        |
| order       | integer | 否   | 显示顺序 | 1             |
| is_active   | boolean | 否   | 是否启用 | true          |

## 响应参数

| 参数名  | 类型    | 说明     |
| ------- | ------- | -------- |
| code    | integer | 状态码   |
| message | string  | 状态信息 |
| data    | object  | 角色信息 |

## 响应示例

```json
{
  "code": 200,
  "message": "创建成功",
  "data": {
    "id": 2,
    "name": "部门管理员",
    "key": "dept_admin",
    "desc": "部门管理角色",
    "permissions": ["view_user"],
    "menus": [1, 2, 3],
    "data_scope": "DEPT",
    "order": 1,
    "is_active": true
  }
}
```
