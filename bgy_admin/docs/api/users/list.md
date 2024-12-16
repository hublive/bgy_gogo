# 获取用户列表

## 接口说明

获取系统中的用户列表，支持分页、搜索、过滤和排序。

## 请求信息

- 请求路径: `/api/users/`
- 请求方法: GET
- 请求头:
  ```
  Authorization: Bearer {access_token}
  ```

## 查询参数

| 参数名             | 类型    | 必填 | 说明             | 示例              |
| ------------------ | ------- | ---- | ---------------- | ----------------- |
| page               | integer | 否   | 页码             | 1                 |
| page_size          | integer | 否   | 每页数量         | 10                |
| search             | string  | 否   | 搜索关键词       | admin             |
| ordering           | string  | 否   | 排序字段         | -date_joined      |
| username           | string  | 否   | 用户名过滤       | admin             |
| nickname           | string  | 否   | 昵称过滤         | 管理员            |
| email              | string  | 否   | 邮箱过滤         | admin@example.com |
| phone              | string  | 否   | 手机号过滤       | 13800138000       |
| role               | integer | 否   | 角色 ID 过滤     | 1                 |
| department         | integer | 否   | 部门 ID 过滤     | 1                 |
| is_active          | boolean | 否   | 是否启用         | true              |
| date_joined_after  | date    | 否   | 注册时间起始日期 | 2024-01-01        |
| date_joined_before | date    | 否   | 注册时间结束日期 | 2024-01-31        |

## 响应参数

| 参数名                   | 类型    | 说明                   |
| ------------------------ | ------- | ---------------------- |
| code                     | integer | 状态码                 |
| message                  | string  | 状态信息               |
| data                     | object  | 响应数据               |
| ├─count                  | integer | 总记录数               |
| ├─next                   | string  | 下一页 URL             |
| ├─previous               | string  | 上一页 URL             |
| └─results                | array   | 用户列表               |
| &nbsp;&nbsp;├─id         | integer | 用户 ID                |
| &nbsp;&nbsp;├─username   | string  | 用户名                 |
| &nbsp;&nbsp;├─nickname   | string  | 昵称                   |
| &nbsp;&nbsp;├─email      | string  | 邮箱                   |
| &nbsp;&nbsp;├─phone      | string  | 手机号                 |
| &nbsp;&nbsp;├─gender     | integer | 性别(0:未知 1:男 2:女) |
| &nbsp;&nbsp;├─avatar     | string  | 头像 URL               |
| &nbsp;&nbsp;├─is_active  | boolean | 是否启用               |
| &nbsp;&nbsp;└─last_login | string  | 最后登录时间           |

## 响应示例

### 成功响应

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "count": 100,
    "next": "http://example.com/api/users/?page=2",
    "previous": null,
    "results": [
      {
        "id": 1,
        "username": "admin",
        "nickname": "管理员",
        "email": "admin@example.com",
        "phone": "13800138000",
        "gender": 1,
        "avatar": "http://example.com/media/avatars/1.jpg",
        "is_active": true,
        "last_login": "2024-01-09T10:30:00Z"
      }
    ]
  }
}
```

### 错误响应

```json
{
  "code": 401,
  "message": "认证失败",
  "data": null
}
```

## 权限要求

- 需要登录
- 需要以下权限之一：
  - `users.view_user`
  - `users.view_all_users`

## 注意事项

1. 排序字段说明：

   - 支持的排序字段：id、username、date_joined、last_login
   - 降序排序需要在字段前添加减号，如 -date_joined

2. 搜索说明：

   - search 参数会在 username、nickname、email、phone 字段中进行模糊匹配
   - 支持中文搜索

3. 过滤说明：
   - 日期过滤支持 ISO 格式：YYYY-MM-DD
   - 手机号和邮箱支持精确匹配
   - 用户名和昵称支持模糊匹配
