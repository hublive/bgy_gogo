# 部门列表

## 接口说明

获取部门列表数据，支持树形结构。

## 请求信息

- 请求路径: `/api/departments/`
- 请求方法: GET
- 请求头:
  ```
  Authorization: Bearer {access_token}
  ```

## 查询参数

| 参数名    | 类型    | 必填 | 说明       | 示例   |
| --------- | ------- | ---- | ---------- | ------ |
| page      | integer | 否   | 页码       | 1      |
| page_size | integer | 否   | 每页数量   | 10     |
| name      | string  | 否   | 部门名称   | 技术部 |
| leader    | integer | 否   | 负责人 ID  | 1      |
| is_active | boolean | 否   | 是否启用   | true   |
| tree      | boolean | 否   | 树形结构   | true   |
| search    | string  | 否   | 搜索关键词 | 技术   |
| ordering  | string  | 否   | 排序字段   | order  |

## 响应参数

| 参数名           | 类型    | 说明       |
| ---------------- | ------- | ---------- |
| code             | integer | 状态码     |
| message          | string  | 状态信息   |
| data             | array   | 部门列表   |
| ├─id             | integer | 部门 ID    |
| ��─name          | string  | 部门名称   |
| ├─parent         | integer | 父部门 ID  |
| ├─parent_name    | string  | 父部门名称 |
| ├─leader         | integer | 负责人 ID  |
| ├─leader_name    | string  | 负责人名称 |
| ├─order          | integer | 显示顺序   |
| ├─is_active      | boolean | 是否启用   |
| ├─children_count | integer | 子部门数量 |
| ├─member_count   | integer | 部门人数   |
| ├─created_at     | string  | 创建时间   |
| └─updated_at     | string  | 更新时间   |

## 响应示例

```json
{
  "code": 200,
  "message": "success",
  "data": [
    {
      "id": 1,
      "name": "技术部",
      "parent": null,
      "parent_name": null,
      "leader": 1,
      "leader_name": "张三",
      "order": 1,
      "is_active": true,
      "children_count": 2,
      "member_count": 10,
      "created_at": "2024-01-09T10:00:00Z",
      "updated_at": "2024-01-09T10:00:00Z"
    }
  ]
}
```

## 权限要求

- 需要登录
- 需要以下权限之一：
  - `departments.view_department`
  - `departments.view_all_departments`
