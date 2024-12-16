# 部门基础管理

## 1. 获取部门列表

### 接口说明

获取部门列表,支持分页、搜索和过滤。

### 请求信息

- 请求路径: `/api/departments/`
- 请求方法: GET
- 请求头: `Authorization: Bearer {access_token}`

### 请求参数

| 参数名    | 类型    | 必填 | 说明     | 示例   |
| --------- | ------- | ---- | -------- | ------ |
| page      | integer | 否   | 页码     | 1      |
| page_size | integer | 否   | 每页数量 | 10     |
| name      | string  | 否   | 部门名称 | 技术部 |
| is_active | boolean | 否   | 是否启用 | true   |

### 响应参数

| 参数名           | 类型    | 说明       |
| ---------------- | ------- | ---------- |
| code             | integer | 状态码     |
| message          | string  | 状态信息   |
| data             | object  | 响应数据   |
| ├─id             | integer | 部门 ID    |
| ├─name           | string  | 部门名称   |
| ├─parent         | object  | 父部门信息 |
| ├─leader         | object  | 负责人信息 |
| ├─order          | integer | 显示顺序   |
| ├─is_active      | boolean | 是否启用   |
| └─children_count | integer | 子部门数量 |

### 响应示例

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "count": 10,
    "next": null,
    "previous": null,
    "results": [
      {
        "id": 1,
        "name": "技术部",
        "parent": null,
        "leader": {
          "id": 1,
          "name": "张三"
        },
        "order": 1,
        "is_active": true,
        "children_count": 2
      }
    ]
  }
}
```

## 2. 创建部门

### 接口说明

创建新的部门。

### 请求信息

- 请求路径: `/api/departments/`
- 请求方法: POST
- 请求头: `Authorization: Bearer {access_token}`

### 请求参数

| 参数名    | 类型    | 必填 | 说明      | 示例   |
| --------- | ------- | ---- | --------- | ------ |
| name      | string  | 是   | 部门名称  | 技术部 |
| parent    | integer | 否   | 父部门 ID | 1      |
| leader    | integer | 否   | 负责人 ID | 1      |
| order     | integer | 否   | 显示顺序  | 1      |
| is_active | boolean | 否   | 是否启用  | true   |

## 注意事项

1. 部门管理

   - 部门名称不能重复
   - 不能选择自己作为父部门
   - 不能选择子部门作为父部门

2. 数据校验
   - 部门名称长度不超过 50 个字符
   - 显示顺序必须大于等于 0
