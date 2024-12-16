# 部门统计

## 获取部门统计数据

### 接口说明

获取部门相关的统计数据。

### 请求信息

- 请求路径: `/api/departments/statistics/`
- 请求方法: GET
- 请求头: `Authorization: Bearer {access_token}`

### 请求参数

| 参数名     | 类型    | 必填 | 说明     | 示例       |
| ---------- | ------- | ---- | -------- | ---------- |
| department | integer | 否   | 部门 ID  | 1          |
| start_date | string  | 否   | 开始日期 | 2024-01-01 |
| end_date   | string  | 否   | 结束日期 | 2024-01-10 |

### 响应参数

| 参数名                  | 类型    | 说明           |
| ----------------------- | ------- | -------------- |
| code                    | integer | 状态码         |
| message                 | string  | 状态信息       |
| data                    | object  | 统计数据       |
| ├─overview              | object  | 概览数据       |
| │ ├─total_departments   | integer | 部门总数       |
| │ ├─active_departments  | integer | 活跃部门数     |
| │ ├─total_users         | integer | 用户总数       |
| │ └─active_users        | integer | 活跃用户数     |
| ├─level_distribution    | array   | 层级分布       |
| │ ├─level               | integer | 层级           |
| │ └─count               | integer | 数量           |
| ├─top_departments       | array   | 人数最多的部门 |
| │ ├─name                | string  | 部门名称       |
| │ └─user_count          | integer | 用户数量       |
| └─daily_new_departments | array   | 每日新增部门   |
| &nbsp;&nbsp;├─date      | string  | 日期           |
| &nbsp;&nbsp;└─count     | integer | 新增数量       |

### 响应示例

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "overview": {
      "total_departments": 100,
      "active_departments": 95,
      "total_users": 500,
      "active_users": 480
    },
    "level_distribution": [
      {
        "level": 0,
        "count": 1
      },
      {
        "level": 1,
        "count": 10
      },
      {
        "level": 2,
        "count": 89
      }
    ],
    "top_departments": [
      {
        "name": "技术部",
        "user_count": 100
      },
      {
        "name": "销售部",
        "user_count": 80
      }
    ],
    "daily_new_departments": [
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

## 注意事项

1. 数据统计

   - 统计数据会有一定的延迟
   - 建议使用缓存提高性能
   - 大量数据时考虑异步计算

2. 权限控制

   - 需要统计权限
   - 只统计有权限的部门数据
   - 某些敏感数据可能需要更高权限

3. 性能优化
   - 合理使用缓存
   - 避免复杂的统计查询
   - 考虑使用异步任务
