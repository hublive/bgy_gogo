# 用户导入导出

## 导出用户

### 接口说明

导出用户数据为 Excel 文件。

### 请求信息

- 请求路径: `/api/users/export/`
- 请求方法: GET
- 请求头:
  ```
  Authorization: Bearer {access_token}
  ```

### 查询参数

支持与用户列表相同的过滤参数：

| 参数名     | 类型    | 必填 | 说明         | 示例              |
| ---------- | ------- | ---- | ------------ | ----------------- |
| username   | string  | 否   | 用户名过滤   | admin             |
| nickname   | string  | 否   | 昵称过滤     | 管理员            |
| email      | string  | 否   | 邮箱过滤     | admin@example.com |
| phone      | string  | 否   | 手机号过滤   | 13800138000       |
| role       | integer | 否   | 角色 ID 过滤 | 1                 |
| department | integer | 否   | 部门 ID 过滤 | 1                 |
| is_active  | boolean | 否   | 是否启用     | true              |

### 响应说明

- 响应类型: `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- 文件名: `users.xlsx`

### 导出字段

1. 用户名
2. 昵称
3. 邮箱
4. 手机号
5. 性别
6. 角色
7. 部门
8. 状态
9. 注册时间
10. 最后登录

### 权限要求

- 需要登录
- 需要以下权限之一：
  - `users.export_user`
  - `users.export_all_users`

## 导入用户

### 接口说明

从 Excel 文件导入用户数据。

### 请求信息

- 请求路径: `/api/users/import_users/`
- 请求方法: POST
- 请求头:
  ```
  Authorization: Bearer {access_token}
  Content-Type: multipart/form-data
  ```

### 请求参数

| 参数名 | 类型 | 必填 | 说明       | 示例       |
| ------ | ---- | ---- | ---------- | ---------- |
| file   | file | 是   | Excel 文件 | users.xlsx |

### 响应参数

| 参数名          | 类型    | 说明         |
| --------------- | ------- | ------------ |
| code            | integer | 状态码       |
| message         | string  | 状态信息     |
| data            | object  | 响应数据     |
| ├─success_count | integer | 成功数量     |
| ├─error_count   | integer | 失败数量     |
| └─error_msgs    | array   | 错误信息列表 |

### 响应示例

#### 成功响应

```json
{
  "code": 200,
  "message": "导入完成: 成功 3 条，失败 1 条",
  "data": {
    "success_count": 3,
    "error_count": 1,
    "error_msgs": ["第 3 行: 用户名已存在"]
  }
}
```

#### 错误响应

```json
{
  "code": 400,
  "message": "请选择要导入的文件",
  "data": null
}
```

### 权限要求

- 需要登录
- 需要以下权限之一：
  - `users.import_user`
  - `users.import_all_users`

### 注意事项

1. 文件要求：

   - 仅支持 Excel 文件（.xlsx）
   - 文件大小不超过 10MB
   - 必须包含必填字段：用户名、密码

2. 导入规则：

   - 如果用户名已存在，则更新用户信息
   - 如果用户名不存在，则创建新用户
   - 密码必须符合系统密码强度要求

3. 字段说明：
   - 用户名：必填，4-30 位字符
   - 密码：必填，符合密码强度要求
   - 昵称：选填，最多 50 位字符
   - 邮箱：选填，必须是有效邮箱格式
   - 手机号：选填，必须是有效的手机号
