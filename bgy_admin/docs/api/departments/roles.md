# 部门角色管理

## 1. 获取部门角色列表

### 接口说明

获取指定部门下的角色列表。

### 请求信息

- 请求路径: `/api/departments/{id}/roles/`
- 请求方法: GET
- 请求头: `Authorization: Bearer {access_token}`

### 请求参数

| 参数名    | 类型    | 必填 | 说明     | 示例   |
| --------- | ------- | ---- | -------- | ------ |
| page      | integer | 否   | 页码     | 1      |
| page_size | integer | 否   | 每页数量 | 10     |
| name      | string  | 否   | 角色名称 | 管理员 |
| is_active | boolean | 否   | 是否启用 | true   |

### 响应参数

| 参数名               | 类型    | 说明       |
| -------------------- | ------- | ---------- |
| code                 | integer | 状态码     |
| message              | string  | 状态信息   |
| data                 | object  | 响应数据   |
| ├─id                 | integer | 配置 ID    |
| ├─department         | object  | 部门信息   |
| ├─data_scope         | string  | 数据范围   |
| ├─custom_departments | array   | 自定义部门 |
| └─created_at         | string  | 创建时间   |

### 响应示例

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 1,
    "department": {
      "id": 1,
      "name": "技术部"
    },
    "data_scope": "custom",
    "custom_departments": [2, 3, 4],
    "created_at": "2024-01-10T10:00:00Z"
  }
}
```

## 注意事项

1. 角色管理

   - 角色代码全局唯一
   - 角色名称在部门内唯一
   - 角色删除前需要解除关联关系

2. 数据校验
   - 角色代码只能包含字母、数字和下划线
   - 角色名称长度不超过 32 个字符
   - 备注说明长度不超过 128 个字符
