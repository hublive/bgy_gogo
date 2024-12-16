# 部门导入导出

## 1. 导出部门数据

### 接口说明

将部门数据导出为 Excel 文件。

### 请求信息

- 请求路径: `/api/departments/export/`
- 请求方法: GET
- 请求头: `Authorization: Bearer {access_token}`

### 请求参数

| 参数名      | 类型    | 必填 | 说明       | 示例       |
| ----------- | ------- | ---- | ---------- | ---------- |
| department  | integer | 否   | 部门 ID    | 1          |
| include_sub | boolean | 否   | 包含子部门 | true       |
| start_date  | string  | 否   | 开始日期   | 2024-01-01 |
| end_date    | string  | 否   | 结束日期   | 2024-01-10 |

### 响应信息

- Content-Type: application/vnd.ms-excel
- Content-Disposition: attachment; filename="departments.xlsx"

### 导出字段

| 字段名   | 说明     | 示例     |
| -------- | -------- | -------- |
| 部门名称 | 部门名称 | 技术部   |
| 父部门   | 上级部门 | 研发中心 |
| 负责人   | 部门主管 | 张三     |
| 排序号   | 显示顺序 | 1        |
| 状态     | 启用状态 | 启用     |
| 备注     | 备注说明 | 无       |

## 2. 导入部门数据

### 接口说明

从 Excel 文件导入部门数据。

### 请求信息

- 请求路径: `/api/departments/import/`
- 请求方法: POST
- 请求头:
  - `Authorization: Bearer {access_token}`
  - `Content-Type: multipart/form-data`

### 请求参数

| 参数名 | 类型 | 必填 | 说明       | 示例             |
| ------ | ---- | ---- | ---------- | ---------------- |
| file   | file | 是   | Excel 文件 | departments.xlsx |

### 响应参数

| 参数名          | 类型    | 说明         |
| --------------- | ------- | ------------ |
| code            | integer | 状态码       |
| message         | string  | 状态信息     |
| data            | object  | 导入结果     |
| ├─success_count | integer | 成功数量     |
| ├─error_count   | integer | 失败数量     |
| └─error_msgs    | array   | 错误信息列表 |

### 响应示例

```json
{
  "code": 200,
  "message": "导入完成: 成功 2 条，失败 1 条",
  "data": {
    "success_count": 2,
    "error_count": 1,
    "error_msgs": ["第3行: 父部门 市场部 不存在"]
  }
}
```

## 3. 下载导入模板

### 接口说明

下载部门导入的 Excel 模板文件。

### 请求信息

- 请求路径: `/api/departments/template/`
- 请求方法: GET
- 请求头: `Authorization: Bearer {access_token}`

### 响应信息

- Content-Type: application/vnd.ms-excel
- Content-Disposition: attachment; filename="department_template.xlsx"

## 注意事项

1. 导入规则

   - 必须使用系统提供的模板文件
   - 部门名称不能重复
   - 父部门必须已存在
   - 负责人必须是系统中的用户

2. 数据验证

   - 导入前会进行数据格式验证
   - 验证失败的数据会记录在错误信息中
   - 支持部分数据导入成功

3. 性能优化
   - 大量数据导入时使用异步任务
   - 导出数据时分批次处理
   - 适当使用缓存机制
