# 部门审计报告

## 1. 获取审计报告

### 接口说明

获取部门的审计报告数据。

### 请求信息

- 请求路径: `/api/departments/{id}/audit/`
- 请求方法: GET
- 请求头: `Authorization: Bearer {access_token}`

### 请求参数

| 参数名     | 类型   | 必填 | 说明     | 示例       |
| ---------- | ------ | ---- | -------- | ---------- |
| start_date | string | 是   | 开始日期 | 2024-01-01 |
| end_date   | string | 是   | 结束日期 | 2024-01-10 |
| type       | string | 否   | 报告类型 | summary    |
| format     | string | 否   | 导出格式 | pdf        |

### 响应参数

| 参数名                  | 类型    | 说明     |
| ----------------------- | ------- | -------- |
| code                    | integer | 状态码   |
| message                 | string  | 状态信息 |
| data                    | object  | 响应数据 |
| ├─basic_info            | object  | 基本信息 |
| ├─permission_changes    | array   | 权限变更 |
| ├─user_changes          | array   | 人员变动 |
| ├��operation_statistics | object  | 操作统计 |
| └─risk_warnings         | array   | 风险预警 |

### 响应示例

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "basic_info": {
      "department_name": "技术部",
      "audit_period": "2024-01-01 至 2024-01-10",
      "generated_at": "2024-01-11T10:00:00Z"
    },
    "permission_changes": [
      {
        "date": "2024-01-02",
        "type": "add",
        "operator": "张三",
        "detail": "添加查看权限"
      }
    ],
    "user_changes": [
      {
        "date": "2024-01-03",
        "type": "join",
        "user": "李四",
        "position": "开发工程师"
      }
    ],
    "operation_statistics": {
      "total_operations": 100,
      "high_risk_operations": 5,
      "abnormal_operations": 2
    },
    "risk_warnings": [
      {
        "level": "high",
        "type": "permission",
        "description": "发现异常权限提升",
        "suggestion": "建议及时审查"
      }
    ]
  }
}
```

## 2. 导出审计报告

### 接口说明

导出部门审计报告文件。

### 请求信息

- 请求路径: `/api/departments/{id}/audit/export/`
- 请求方法: GET
- 请求头: `Authorization: Bearer {access_token}`

### 请求参数

| 参数名     | 类型   | 必填 | 说明     | 示例       |
| ---------- | ------ | ---- | -------- | ---------- |
| start_date | string | 是   | 开始日期 | 2024-01-01 |
| end_date   | string | 是   | 结束日期 | 2024-01-10 |
| format     | string | 否   | 文件格式 | pdf        |

### 响应信息

- Content-Type: application/pdf
- Content-Disposition: attachment; filename="audit_report.pdf"

## 注意事项

1. 报告生成

   - 支持多种导出格式
   - 大报告异步生成
   - 缓存常用报告

2. 数据安全

   - 敏感信息脱敏
   - 访问权限控制
   - 操作留痕审计

3. 性能优化
   - 使用异步任务
   - 分批处理数据
   - 合理使用缓存
