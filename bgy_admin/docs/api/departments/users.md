# 部门用户管理

## 1. 获取部门用户列表

### 接口说明

获取指定部门下的用户列表。

### 请求信息

- 请求路径: `/api/departments/{id}/users/`
- 请求方法: GET
- 请求头: `Authorization: Bearer {access_token}`

### 请求参数

| 参数名      | 类型    | 必填 | 说明               | 示例  |
| ----------- | ------- | ---- | ------------------ | ----- |
| page        | integer | 否   | 页码               | 1     |
| page_size   | integer | 否   | 每页数量           | 10    |
| username    | string  | 否   | 用户名(模糊搜索)   | admin |
| nickname    | string  | 否   | 昵称(模糊搜索)     | 张三  |
| role        | integer | 否   | 角色 ID            | 1     |
| is_active   | boolean | 否   | 是否启用           | true  |
| include_sub | boolean | 否   | 是否包含子部门用户 | true  |

### 响应参数

| 参数名                  | 类型    | 说明       |
| ----------------------- | ------- | ---------- |
| code                    | integer | 状态码     |
| message                 | string  | 状态信 ��  |
| data                    | object  | 响应数据   |
| ├─count                 | integer | 总记录数   |
| ├─next                  | string  | 下一页 URL |
| ├─previous              | string  | 上一页 URL |
| └─results               | array   | 用户列表   |
| &nbsp;&nbsp;├─id        | integer | 用户 ID    |
| &nbsp;&nbsp;├─username  | string  | 用户名     |
| &nbsp;&nbsp;├─nickname  | string  | 昵称       |
| &nbsp;&nbsp;├─email     | string  | 邮箱       |
| &nbsp;&nbsp;├─phone     | string  | 手机号     |
| &nbsp;&nbsp;├─role      | object  | 角色信息   |
| &nbsp;&nbsp;└─is_active | boolean | 是否启用   |

### 响应示例

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "count": 100,
    "next": "http://example.com/api/departments/1/users/?page=2",
    "previous": null,
    "results": [
      {
        "id": 1,
        "username": "zhangsan",
        "nickname": "张三",
        "email": "zhangsan@example.com",
        "phone": "13800138000",
        "role": {
          "id": 1,
          "name": "管理员"
        },
        "is_active": true
      }
    ]
  }
}
```

## 2. 添加部门用户

### 接口说明

向指定部门添加用户。

### 请求信息

- 请求路径: `/api/departments/{id}/add_users/`
- 请求方法: POST
- 请求头: `Authorization: Bearer {access_token}`

### 请求参数

| 参数名   | 类型  | 必填 | 说明         | 示例      |
| -------- | ----- | ---- | ------------ | --------- |
| user_ids | array | 是   | 用户 ID 列表 | [1, 2, 3] |

### 响应示例

```json
{
  "code": 200,
  "message": "添加成功",
  "data": {
    "success_count": 2,
    "error_count": 1,
    "error_msgs": ["用户 3 已在其他部门"]
  }
}
```

## 3. 移除部门用户

### 接口说明

从指定部门移除用户。

### 请求信息

- 请求路径: `/api/departments/{id}/remove_users/`
- 请求方法: POST
- 请求头: `Authorization: Bearer {access_token}`

### 请求参数

| 参数名   | 类型  | 必填 | 说明         | 示例      |
| -------- | ----- | ---- | ------------ | --------- |
| user_ids | array | 是   | 用户 ID 列表 | [1, 2, 3] |

### 响应示例

```json
{
  "code": 200,
  "message": "移除成功",
  "data": null
}
```

## 注意事项

1. 用户管理

   - 一个用户只能属于一个部门
   - 添加用户时会自动从原部门移除
   - 移除用户时需要考虑关联数据

2. 权限控制
   - 需要相应的用户管理权限
   - 只能管理有权限 ��� 部门用户
   - 某些操作可能需要更高权限
