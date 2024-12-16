# 登录日志查询

## 接口说明

查询用户的登录日志记录。

## 请求信息

- 请求路径: `/api/users/login_logs/`
- 请求方法: GET
- 请求头:
  ```
  Authorization: Bearer {access_token}
  ```

## 查询参数

| 参数名     | 类型    | 必填 | 说明     | 示例       |
| ---------- | ------- | ---- | -------- | ---------- |
| page       | integer | 否   | 页码     | 1          |
| page_size  | integer | 否   | 每页数量 | 10         |
| username   | string  | 否   | 用户名   | admin      |
| status     | string  | 否   | 状态     | success    |
| login_type | string  | 否   | 登录方式 | username   |
| start_time | string  | 否   | 开始时间 | 2024-01-01 |
| end_time   | string  | 否   | 结束时间 | 2024-01-31 |
| ip_address | string  | 否   | IP 地址  | 127.0.0.1  |

## 响应参数

| 参数名                   | 类型    | 说明       |
| ------------------------ | ------- | ---------- |
| code                     | integer | 状态码     |
| message                  | string  | 状态信息   |
| data                     | object  | 响应数据   |
| ├─count                  | integer | 总记录数   |
| ├─next                   | string  | 下一页 URL |
| ├─previous               | string  | 上一页 URL |
| └─results                | array   | 日志列表   |
| &nbsp;&nbsp;├─id         | integer | 日志 ID    |
| &nbsp;&nbsp;├─username   | string  | 用户名     |
| &nbsp;&nbsp;├─login_type | string  | 登录方式   |
| &nbsp;&nbsp;├─status     | string  | 状态       |
| &nbsp;&nbsp;├─ip_address | string  | IP 地址    |
| &nbsp;&nbsp;├─user_agent | string  | 浏览器标识 |
| &nbsp;&nbsp;├─message    | string  | 消息       |
| &nbsp;&nbsp;└─created_at | string  | 创建时间   |

## 响应示例

### 成功响应

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "count": 100,
    "next": "http://example.com/api/users/login_logs/?page=2",
    "previous": null,
    "results": [
      {
        "id": 1,
        "username": "admin",
        "login_type": "username",
        "status": "success",
        "ip_address": "127.0.0.1",
        "user_agent": "Mozilla/5.0 ...",
        "message": "登录成功",
        "created_at": "2024-01-09T10:00:00Z"
      }
    ]
  }
}
```

## 权限要求

- 需要登录
- 需要以下权限之一：
  - `users.view_login_logs`
  - `users.view_all_login_logs`

## 注意事项

1. 登录方式：

   - username: 用户名登录
   - email: 邮箱登录
   - phone: 手机号登录
   - social: 社交账号登录

2. 状态说明：

   - success: 登录成功
   - failed: 登录失败

3. 查询说明：
   - 时间范围最大支持 90 天
   - IP 地址支持模糊匹配
   - 用户名支持模糊匹配
