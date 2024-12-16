# 上传头像

## 接口说明

上传或更新用户的头像图片。

## 请求信息

- 请求路径: `/api/users/{id}/avatar/`
- 请求方法: POST
- 请求头:
  ```
  Authorization: Bearer {access_token}
  Content-Type: multipart/form-data
  ```

## 路径参数

| 参数名 | 类型    | 必填 | 说明    | 示例 |
| ------ | ------- | ---- | ------- | ---- |
| id     | integer | 是   | 用户 ID | 1    |

## 请求参数

| 参数名 | 类型 | 必填 | 说明     | 示例       |
| ------ | ---- | ---- | -------- | ---------- |
| avatar | file | 是   | 头像文件 | avatar.jpg |

## 响应参数

| 参数名  | 类型    | 说明         |
| ------- | ------- | ------------ |
| code    | integer | 状态码       |
| message | string  | 状态信息     |
| data    | object  | 响应数据     |
| └─url   | string  | 头像访问 URL |

## 响应示例

### 成功响应

```json
{
  "code": 200,
  "message": "头像上传成功",
  "data": {
    "url": "http://example.com/media/avatars/1.jpg"
  }
}
```

### 错误响应

```json
{
  "code": 400,
  "message": "图片大小不能超过2MB",
  "data": null
}
```

## 权限要求

- 需要登录
- 需要以下权限之一：
  - `users.change_avatar`（修改自己的头像）
  - `users.change_all_avatars`（修改任何用户的头像）

## 注意事项

1. 文件要求：

   - 仅支持图片文件（jpg、jpeg、png、gif）
   - 文件大小不超过 2MB
   - 建议图片尺寸为 200x200 像素

2. 存储说明：

   - 旧头像文件会被自动删除
   - 头像文件按日期目录存储
   - 文件名会被自动重命名

3. 访问说明：
   - 返回的 URL 为完整的访问地址
   - 支持 CDN 加速访问
   - 可以通过浏览器直接访问
