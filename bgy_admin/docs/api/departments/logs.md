# 部门日志查询

## 获取部门操作日志

### 接口说明

查询部门相关的操作日志记录。

### 请求信息

- 请求路径: `/api/departments/logs/`
- 请求方法: GET
- 请求头: `Authorization: Bearer {access_token}`

### 请求参数

| 参数名     | 类型    | 必填 | 说明      | 示例       |
| ---------- | ------- | ---- | --------- | ---------- |
| page       | integer | 否   | 页码      | 1          |
| page_size  | integer | 否   | 每页数量  | 10         |
| department | integer | 否   | 部门 ID   | 1          |
| action     | string  | 否   | 操作类型  | create     |
| operator   | integer | 否   | 操作人 ID | 1          |
| start_date | string  | 否   | 开始日期  | 2024-01-01 |
| end_date   | string  | 否   | 结束日期  | 2024-01-10 |

### 响应参数

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
| &nbsp;&nbsp;├─department | object  | 部门信息   |
| &nbsp;&nbsp;├─action     | string  | 操作类型   |
| &nbsp;&nbsp;├─operator   | object  | 操作人信息 |
| &nbsp;&nbsp;├─detail     | object  | 操作详情   |
| &nbsp;&nbsp;└─created_at | string  | 操作时间   |

### 响应示例

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "count": 100,
    "next": "http://example.com/api/departments/logs/?page=2",
    "previous": null,
    "results": [
      {
        "id": 1,
        "department": {
          "id": 1,
          "name": "技术部"
        },
        "action": "create",
        "operator": {
          "id": 1,
          "nickname": "张三"
        },
        "detail": {
          "name": "技术部",
          "parent": null,
          "leader": 1
        },
        "created_at": "2024-01-10T10:00:00Z"
      }
    ]
  }
}
```

## 注意事项

1. 日志记录

   - ��� 录所有关键操作
   - 包含操作前后的数据
   - 记录操作人信息

2. 数据权限

   - 只能查看有权限的部门日志
   - 某些敏感信息可能需要更高权限
   - 支持按角色过滤日志

3. 性能优化
   - 使用异步任务记录日志
   - 定期归档历史日志
   - 合理使用索引提升查询性能
