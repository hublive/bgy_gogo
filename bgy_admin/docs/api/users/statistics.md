# 用户数据统计

## 接口说明

获取用户相关的统计数据。

## 请求信息

- 请求路径: `/api/users/statistics/`
- 请求方法: GET
- 请求头:
  ```
  Authorization: Bearer {access_token}
  ```

## 响应参数

| 参数名                    | 类型    | 说明               |
| ------------------------- | ------- | ------------------ |
| code                      | integer | 状态码             |
| message                   | string  | 状态信息           |
| data                      | object  | 统计数据           |
| ├─overview                | object  | 概览数据           |
| │ ├─total_users           | integer | 总用户数           |
| │ ├─active_users          | integer | 活跃用户数         |
| │ ├─today_logins          | integer | 今日登录数         |
| │ └─new_users_30d         | integer | 近 30 天新增用户数 |
| ├─role_distribution       | array   | 角色分布           |
| │ ├─role\_\_name          | string  | 角色名称           |
| │ └���count               | integer | 用户数量           |
| ├─department_distribution | array   | 部门分布           |
| │ ├─department\_\_name    | string  | 部门名称           |
| │ └─count                 | integer | 用户数量           |
| ├─gender_distribution     | array   | 性别分布           |
| │ ├─gender                | integer | 性别代码           |
| │ ├─gender_name           | string  | 性别名称           |
| │ └─count                 | integer | 用户数量           |
| └─daily_new_users         | array   | 每日新增用户       |
| &nbsp;&nbsp;├─date        | string  | 日期               |
| &nbsp;&nbsp;└─count       | integer | 新增用户数         |

## 响应示例

### 成功响应

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "overview": {
      "total_users": 100,
      "active_users": 80,
      "today_logins": 50,
      "new_users_30d": 30
    },
    "role_distribution": [
      {
        "role__name": "管理员",
        "count": 5
      },
      {
        "role__name": "普通用户",
        "count": 95
      }
    ],
    "department_distribution": [
      {
        "department__name": "��术部",
        "count": 40
      },
      {
        "department__name": "市场部",
        "count": 30
      }
    ],
    "gender_distribution": [
      {
        "gender": 0,
        "gender_name": "未知",
        "count": 20
      },
      {
        "gender": 1,
        "gender_name": "男",
        "count": 50
      },
      {
        "gender": 2,
        "gender_name": "女",
        "count": 30
      }
    ],
    "daily_new_users": [
      {
        "date": "2024-01-01",
        "count": 5
      },
      {
        "date": "2024-01-02",
        "count": 3
      }
    ]
  }
}
```

## 权限要求

- 需要登录
- 需要以下权限之一：
  - `users.view_statistics`
  - `users.view_all_statistics`

## 注意事项

1. 统计范围：

   - 活跃用户：最近 30 天有登录记录的用户
   - 今日登录：当天 00:00 至现在登录的用户数
   - 新增用户：最近 30 天注册的用户数

2. 数据说明：
   - 角色分布：按角色统计的用户数量
   - 部门分布：按部门统计的用户数量
   - 性别分布：按性别统计的用户数量
   - 每日新增：最近 30 天每天新增的用户数量
