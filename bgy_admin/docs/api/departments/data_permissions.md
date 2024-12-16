# 部门数据权限

## 1. 获取数据权限配置

### 接口说明

获取指定部门的数据权限配置。

### 请求信息

- 请求路径: `/api/departments/{id}/data_permissions/`
- 请求方法: GET
- 请求头: `Authorization: Bearer {access_token}`

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

## 注意事项

1. 数据范围

   - 合理设置数据范围
   - 避免过大的数据权限
   - 定期审查数据权限

2. 性能优化
   - 使用缓存减少查询
   - 避免频繁变更配置
   - 合理使用数据过滤
