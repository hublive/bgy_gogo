# 部门树形结构

## 获取部门树

### 接口说明

获取完整的部门层级树形结构。

### 请求信息

- 请求路径: `/api/departments/tree/`
- 请求方法: GET
- 请求头: `Authorization: Bearer {access_token}`

### 请求参数

| 参数名    | 类型    | 必填 | 说明           | 示例 |
| --------- | ------- | ---- | -------------- | ---- |
| is_active | boolean | 否   | 是否只返回启用 | true |

### 响应参数

| 参数名        | 类型    | 说明         |
| ------------- | ------- | ------------ |
| code          | integer | 状态码       |
| message       | string  | 状态信息     |
| data          | array   | 部门树形数据 |
| ├─id          | integer | 部门 ID      |
| ├─name        | string  | 部门名称     |
| ├─parent      | object  | 父部门信息   |
| ├─leader      | object  | 负责人信息   |
| ├─order       | integer | 显示顺序     |
| ├─level       | integer | 层级深度     |
| ├─is_active   | boolean | 是否启用     |
| ├─child_count | integer | 子部门数量   |
| ├─user_count  | integer | 用户数量     |
| └─children    | array   | 子部门列表   |

### 响应示例

```json
{
  "code": 200,
  "message": "success",
  "data": [
    {
      "id": 1,
      "name": "总公司",
      "parent": null,
      "leader": {
        "id": 1,
        "nickname": "张三"
      },
      "order": 1,
      "level": 0,
      "is_active": true,
      "child_count": 2,
      "user_count": 5,
      "children": [
        {
          "id": 2,
          "name": "技术部",
          "parent": 1,
          "leader": {
            "id": 2,
            "nickname": "李四"
          },
          "order": 1,
          "level": 1,
          "is_active": true,
          "child_count": 1,
          "user_count": 10,
          "children": [
            {
              "id": 3,
              "name": "研发组",
              "parent": 2,
              "leader": {
                "id": 3,
                "nickname": "王五"
              },
              "order": 1,
              "level": 2,
              "is_active": true,
              "child_count": 0,
              "user_count": 5,
              "children": []
            }
          ]
        }
      ]
    }
  ]
}
```

## 注意事项

1. 性能优化

   - 使用缓存减少数据库查询
   - 避免过深的层级嵌套
   - 按需加载子节点数据

2. 数据权限
   - 只返回用户有权限访问的部门
   - 支持按角色过滤部门树
   - 继承上级部门的访问权限
