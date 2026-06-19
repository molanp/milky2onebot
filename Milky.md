---
title: Milky
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.30"

---

# 通信

Milky 的协议端实现需要开启一个 HTTP 服务器，在不同的端点提供两种网络服务：
- `/api` 端点，提供 API 调用服务，应用端向协议端发起请求，协议端继而完成响应操作；
- `/event` 端点，提供事件推送服务，协议端向应用端主动推送事件。

> [!warning]
>
> 由于 Milky 协议要求协议端提供 HTTP 服务，因此请务必注重网络安全，避免协议端被恶意访问。建议将协议端部署在内网环境中。如果必须要在公网环境中部署协议端，请**务必**使用防火墙等手段限制访问，并且设置 `access_token` 以保证安全性，并且 `access_token` 不应当过于简单，建议使用随机字符串。下文介绍了如何使用 `access_token`。

同时，如果用户配置了 WebHook 地址，协议端还会向配置的地址推送事件。可以给定多个 WebHook 地址。

所有服务传输的数据都应当使用 UTF-8 编码。

## API 调用

接受路径为 `/api/:api` 的 API 请求。请求使用 POST 方法，在请求体中通过 JSON 传递参数。为保证安全性，可以在配置文件中设置 `access_token`，协议端需要在请求头中检查 `Authorization` 字段，格式为 `Bearer {access_token}`。

示例如下：

```http
POST /api/send_private_message
Content-Type: application/json
Authorization: Bearer 123456

{
  "user_id": 123456789,
  "message": [
    {
      "type": "text",
      "data": {
        "text": "Hello, world!"
      }
    }
  ]
}
```

注意，即使请求的 API 无输入参数，也必须传入一个空的 JSON 对象 `{}`，例如：

```http
POST /api/get_login_info
Content-Type: application/json
Authorization: Bearer 123456

{}
```

收到 API 请求并处理后，协议端会返回一个 HTTP 响应，根据具体错误类型不同，HTTP 状态码不同：

- `401`：鉴权凭据未提供或不匹配。
- `404`：请求的 API 不存在。
- `415`：POST 请求的 Content-Type 不支持。

剩下的所有情况，无论操作实际成功与否，状态码**都是 `200`**，同时返回 JSON 格式的响应，示例如下：

```jsonc
// 成功响应示例
{
  "status": "ok",
  "retcode": 0, // 成功时的 retcode 为 0
  "data": {
    "message_seq": 23333,
    "time": 1234567890
  }
}
```

```jsonc
// 失败响应示例 0
{
  "status": "failed",
  "retcode": -403, // 协议端未处于登录状态时，retcode 为 -403
  "message": "未处于登录状态"
}
```

```jsonc
// 失败响应示例 1
{
  "status": "failed",
  "retcode": -400, // 参数解析失败时，retcode 为 -400
  "message": "user_id (-1) 不是一个合法的 QQ 号"
}
```

```jsonc
// 失败响应示例 2
{
  "status": "failed",
  "retcode": -404, // 其余错误情况的 retcode 由协议端自行决定
  "message": "user_id 对应的好友不存在"
}
```

同样，即使响应的 API 无输出参数，也必须返回一个空的 JSON 对象 `{}`，例如：

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {}
}
```

## 事件推送

事件推送服务支持三种方式：Server-Sent Events（SSE）、 WebSocket 和 WebHook。

> [!tip]
>
> 由于 SSE 和 WebSocket 都是由 HTTP GET 请求升级而来，协议端在确定应当提供哪种连接时，应当优先检查应用端请求中的 `Upgrade` 头，如果存在且值为 `websocket`，则视为 WebSocket 连接请求，否则视为 SSE 连接请求。

### SSE 连接

接受路径为 `/event` 的 HTTP GET 请求，在建立连接后推送事件。为保证安全性，可以在配置文件中设置 `access_token`，协议端需要在请求头中检查 `Authorization` 字段，格式为 `Bearer {access_token}`。

示例如下：

```http
GET /event
Authorization: Bearer 123456
```

> [!tip]
>
> 在不支持提供自定义 Header 的环境中，应用端还可以通过在 query 中携带 `access_token` 参数来提供 `access_token`，例如：
> 
> ```http
> GET /event?access_token=123456
> ```

协议端需要给出 `Content-Type` 为 `text/event-stream` 的响应，且一直保持连接。产生事件时，协议端会推送一条内容格式是 JSON 的 SSE 消息，内容格式见 [Event](https://milky.ntqqrev.org/struct/Event)。示例如下：

```plain
event: milky_event
data: {
data:   "time": 1234567890,
data:   "self_id": 123456789,
data:   "event_type": "message_receive",
data:   "data": {
data:     "message_scene": "friend",
data:     "peer_id": 123456789,
data:     "message_seq": 23333,
data:     "sender_id": 123456789,
data:     "time": 1234567890,
data:     "segments": [
data:       {
data:         "type": "text",
data:         "data": {
data:           "text": "Hello, world!"
data:         }
data:       }
data:     ]
data:   }
data: }
// 必须以空行结尾，表示消息结束，这是 SSE 的要求
```

### WebSocket 连接

接受路径为 `/event` 的 WebSocket 连接请求，在建立连接后推送事件。连接 URL 为：

```
ws://{IP}:{端口}/event
```

为保证安全性，可以在配置文件中设置 `access_token`，协议端需要在请求头中检查 `Authorization` 字段，格式为 `Bearer {access_token}`。

> [!tip]
>
> 在不支持提供自定义 Header 的环境中，应用端还可以通过在 query 中携带 `access_token` 参数来提供 `access_token`，例如：
>
> ```
> ws://{IP}:{端口}/event?access_token=123456
> ```

产生事件时，协议端会推送一条 JSON 格式的消息，格式见 [Event](../struct/Event.md)。示例如下：

```json
{
  "time": 1234567890,
  "self_id": 123456789,
  "event_type": "message_receive",
  "data": {
    "message_scene": "friend",
    "peer_id": 123456789,
    "message_seq": 23333,
    "sender_id": 123456789,
    "time": 1234567890,
    "segments": [
      {
        "type": "text",
        "data": {
          "text": "Hello, world!"
        }
      }
    ]
  }
}
```

### WebHook 推送

以 POST 方式向给定的 WebHook 地址推送事件。为保证安全性，可以在**协议端**的配置文件中设置 `access_token`。应用端需要在请求头中检查 `Authorization` 字段，格式为 `Bearer {access_token}`。POST 请求的 body 与 WebSocket 推送的格式相同。示例如下：

```http
POST http://example.com/webhook
Content-Type: application/json

{
  "time": 1234567890,
  "self_id": 123456789,
  "event_type": "message_receive",
  "data": {
    "message_scene": "friend",
    "peer_id": 123456789,
    "message_seq": 23333,
    "sender_id": 123456789,
    "time": 1234567890,
    "segments": [
      {
        "type": "text",
        "data": {
          "text": "Hello, world!"
        }
      }
    ]
  }
}
```

# Milky

Milky 协议 API 与事件定义（v1.0）

Base URLs:

# Authentication

- HTTP Authentication, scheme: bearer<br/>在 Authorization 头中携带：Bearer {access_token}

# 系统 API

<a id="opIdget_login_info"></a>

## POST 获取登录信息

POST /api/get_login_info

> Body 请求参数

```json
{}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|[ApiEmptyObject](#schemaapiemptyobject)| 是 |none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "uin": 10001,
    "nickname": "string"
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdget_impl_info"></a>

## POST 获取协议端信息

POST /api/get_impl_info

> Body 请求参数

```json
{}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|[ApiEmptyObject](#schemaapiemptyobject)| 是 |none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "impl_name": "string",
    "impl_version": "string",
    "qq_protocol_version": "string",
    "qq_protocol_type": "windows",
    "milky_version": "string"
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|
|qq_protocol_type|windows|
|qq_protocol_type|linux|
|qq_protocol_type|macos|
|qq_protocol_type|android_pad|
|qq_protocol_type|android_phone|
|qq_protocol_type|ipad|
|qq_protocol_type|iphone|
|qq_protocol_type|harmony|
|qq_protocol_type|watch|

<a id="opIdget_user_profile"></a>

## POST 获取用户个人信息

POST /api/get_user_profile

> Body 请求参数

```json
{
  "user_id": 10001
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetUserProfileInput](#schemagetuserprofileinput)| 是 | get_user_profile 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "nickname": "string",
    "qid": "string",
    "age": 9007199254740991,
    "sex": "male",
    "remark": "string",
    "bio": "string",
    "level": 9007199254740991,
    "country": "string",
    "city": "string",
    "school": "string"
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|
|sex|male|
|sex|female|
|sex|unknown|

<a id="opIdget_friend_list"></a>

## POST 获取好友列表

POST /api/get_friend_list

> Body 请求参数

```json
{
  "no_cache": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetFriendListInput](#schemagetfriendlistinput)| 是 | get_friend_list 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "friends": [
      {}
    ]
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|
|sex|male|
|sex|female|
|sex|unknown|

<a id="opIdget_friend_info"></a>

## POST 获取好友信息

POST /api/get_friend_info

> Body 请求参数

```json
{
  "user_id": 10001,
  "no_cache": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetFriendInfoInput](#schemagetfriendinfoinput)| 是 | get_friend_info 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "friend": {
      "user_id": null,
      "nickname": null,
      "sex": null,
      "qid": null,
      "remark": null,
      "category": null
    }
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|
|sex|male|
|sex|female|
|sex|unknown|

<a id="opIdget_group_list"></a>

## POST 获取群列表

POST /api/get_group_list

> Body 请求参数

```json
{
  "no_cache": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetGroupListInput](#schemagetgrouplistinput)| 是 | get_group_list 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "groups": [
      {}
    ]
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdget_group_info"></a>

## POST 获取群信息

POST /api/get_group_info

> Body 请求参数

```json
{
  "group_id": 10001,
  "no_cache": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetGroupInfoInput](#schemagetgroupinfoinput)| 是 | get_group_info 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "group": {
      "group_id": null,
      "group_name": null,
      "member_count": null,
      "max_member_count": null,
      "remark": null,
      "created_time": null,
      "description": null,
      "question": null,
      "announcement": null
    }
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdget_group_member_list"></a>

## POST 获取群成员列表

POST /api/get_group_member_list

> Body 请求参数

```json
{
  "group_id": 10001,
  "no_cache": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetGroupMemberListInput](#schemagetgroupmemberlistinput)| 是 | get_group_member_list 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "members": [
      {}
    ]
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|
|sex|male|
|sex|female|
|sex|unknown|
|role|owner|
|role|admin|
|role|member|

<a id="opIdget_group_member_info"></a>

## POST 获取群成员信息

POST /api/get_group_member_info

> Body 请求参数

```json
{
  "group_id": 10001,
  "user_id": 10001,
  "no_cache": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetGroupMemberInfoInput](#schemagetgroupmemberinfoinput)| 是 | get_group_member_info 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "member": {
      "user_id": null,
      "nickname": null,
      "sex": null,
      "group_id": null,
      "card": null,
      "title": null,
      "level": null,
      "role": null,
      "join_time": null,
      "last_sent_time": null,
      "shut_up_end_time": null
    }
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|
|sex|male|
|sex|female|
|sex|unknown|
|role|owner|
|role|admin|
|role|member|

<a id="opIdget_peer_pins"></a>

## POST 获取置顶的好友和群列表

POST /api/get_peer_pins

> Body 请求参数

```json
{}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[ApiEmptyObject](#schemaapiemptyobject)| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "friends": [
      {}
    ],
    "groups": [
      {}
    ]
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|
|sex|male|
|sex|female|
|sex|unknown|

<a id="opIdset_peer_pin"></a>

## POST 设置好友或群的置顶状态

POST /api/set_peer_pin

> Body 请求参数

```json
{
  "message_scene": "friend",
  "peer_id": 10001,
  "is_pinned": true
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SetPeerPinInput](#schemasetpeerpininput)| 是 | set_peer_pin 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdset_avatar"></a>

## POST 设置 QQ 账号头像

POST /api/set_avatar

> Body 请求参数

```json
{
  "uri": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SetAvatarInput](#schemasetavatarinput)| 是 | set_avatar 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdset_nickname"></a>

## POST 设置 QQ 账号昵称

POST /api/set_nickname

> Body 请求参数

```json
{
  "new_nickname": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SetNicknameInput](#schemasetnicknameinput)| 是 | set_nickname 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdset_bio"></a>

## POST 设置 QQ 账号个性签名

POST /api/set_bio

> Body 请求参数

```json
{
  "new_bio": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SetBioInput](#schemasetbioinput)| 是 | set_bio 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdget_custom_face_url_list"></a>

## POST 获取自定义表情 URL 列表

POST /api/get_custom_face_url_list

> Body 请求参数

```json
{}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[ApiEmptyObject](#schemaapiemptyobject)| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "urls": [
      "string"
    ]
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdget_cookies"></a>

## POST 获取 Cookies

POST /api/get_cookies

> Body 请求参数

```json
{
  "domain": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetCookiesInput](#schemagetcookiesinput)| 是 | get_cookies 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "cookies": "string"
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdget_csrf_token"></a>

## POST 获取 CSRF Token

POST /api/get_csrf_token

> Body 请求参数

```json
{}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[ApiEmptyObject](#schemaapiemptyobject)| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "csrf_token": "string"
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

# 消息 API

<a id="opIdsend_private_message"></a>

## POST 发送私聊消息

POST /api/send_private_message

> Body 请求参数

```json
{
  "user_id": 10001,
  "message": [
    {
      "type": "[",
      "data": {}
    }
  ]
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SendPrivateMessageInput](#schemasendprivatemessageinput)| 是 | send_private_message 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "message_seq": 9007199254740991,
    "time": 9007199254740991
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdsend_group_message"></a>

## POST 发送群聊消息

POST /api/send_group_message

> Body 请求参数

```json
{
  "group_id": 10001,
  "message": [
    {
      "type": "[",
      "data": {}
    }
  ]
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SendGroupMessageInput](#schemasendgroupmessageinput)| 是 | send_group_message 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "message_seq": 9007199254740991,
    "time": 9007199254740991
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdrecall_private_message"></a>

## POST 撤回私聊消息

POST /api/recall_private_message

> Body 请求参数

```json
{
  "user_id": 10001,
  "message_seq": 9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[RecallPrivateMessageInput](#schemarecallprivatemessageinput)| 是 | recall_private_message 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdrecall_group_message"></a>

## POST 撤回群聊消息

POST /api/recall_group_message

> Body 请求参数

```json
{
  "group_id": 10001,
  "message_seq": 9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[RecallGroupMessageInput](#schemarecallgroupmessageinput)| 是 | recall_group_message 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdget_message"></a>

## POST 获取消息

POST /api/get_message

> Body 请求参数

```json
{
  "message_scene": "friend",
  "peer_id": 10001,
  "message_seq": 9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetMessageInput](#schemagetmessageinput)| 是 | get_message 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "message": {}
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|
|message_scene|friend|
|type|text|
|type|mention|
|type|mention_all|
|type|face|
|type|reply|
|type|image|
|sub_type|normal|
|sub_type|sticker|
|type|record|
|type|video|
|type|file|
|type|forward|
|type|market_face|
|type|light_app|
|type|xml|
|sex|male|
|sex|female|
|sex|unknown|
|message_scene|group|
|sex|male|
|sex|female|
|sex|unknown|
|role|owner|
|role|admin|
|role|member|
|message_scene|temp|

<a id="opIdget_history_messages"></a>

## POST 获取历史消息列表

POST /api/get_history_messages

> Body 请求参数

```json
{
  "message_scene": "friend",
  "peer_id": 10001,
  "start_message_seq": 9007199254740991,
  "limit": 20
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetHistoryMessagesInput](#schemagethistorymessagesinput)| 是 | get_history_messages 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "messages": [
      {}
    ],
    "next_message_seq": 9007199254740991
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|
|message_scene|friend|
|type|text|
|type|mention|
|type|mention_all|
|type|face|
|type|reply|
|type|image|
|sub_type|normal|
|sub_type|sticker|
|type|record|
|type|video|
|type|file|
|type|forward|
|type|market_face|
|type|light_app|
|type|xml|
|sex|male|
|sex|female|
|sex|unknown|
|message_scene|group|
|sex|male|
|sex|female|
|sex|unknown|
|role|owner|
|role|admin|
|role|member|
|message_scene|temp|

<a id="opIdget_resource_temp_url"></a>

## POST 获取临时资源链接

POST /api/get_resource_temp_url

> Body 请求参数

```json
{
  "resource_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetResourceTempUrlInput](#schemagetresourcetempurlinput)| 是 | get_resource_temp_url 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "url": "string"
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdget_forwarded_messages"></a>

## POST 获取合并转发消息内容

POST /api/get_forwarded_messages

> Body 请求参数

```json
{
  "forward_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetForwardedMessagesInput](#schemagetforwardedmessagesinput)| 是 | get_forwarded_messages 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "messages": [
      {}
    ]
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|
|type|text|
|type|mention|
|type|mention_all|
|type|face|
|type|reply|
|type|image|
|sub_type|normal|
|sub_type|sticker|
|type|record|
|type|video|
|type|file|
|type|forward|
|type|market_face|
|type|light_app|
|type|xml|

<a id="opIdmark_message_as_read"></a>

## POST 标记消息为已读

POST /api/mark_message_as_read

> Body 请求参数

```json
{
  "message_scene": "friend",
  "peer_id": 10001,
  "message_seq": 9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[MarkMessageAsReadInput](#schemamarkmessageasreadinput)| 是 | mark_message_as_read 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

# 好友 API

<a id="opIdsend_friend_nudge"></a>

## POST 发送好友戳一戳

POST /api/send_friend_nudge

> Body 请求参数

```json
{
  "user_id": 10001,
  "is_self": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SendFriendNudgeInput](#schemasendfriendnudgeinput)| 是 | send_friend_nudge 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdsend_profile_like"></a>

## POST 发送名片点赞

POST /api/send_profile_like

> Body 请求参数

```json
{
  "user_id": 10001,
  "count": 1
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SendProfileLikeInput](#schemasendprofilelikeinput)| 是 | send_profile_like 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIddelete_friend"></a>

## POST 删除好友

POST /api/delete_friend

> Body 请求参数

```json
{
  "user_id": 10001
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[DeleteFriendInput](#schemadeletefriendinput)| 是 | delete_friend 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdget_friend_requests"></a>

## POST 获取好友请求列表

POST /api/get_friend_requests

> Body 请求参数

```json
{
  "limit": 20,
  "is_filtered": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetFriendRequestsInput](#schemagetfriendrequestsinput)| 是 | get_friend_requests 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "requests": [
      {}
    ]
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|
|state|pending|
|state|accepted|
|state|rejected|
|state|ignored|

<a id="opIdaccept_friend_request"></a>

## POST 同意好友请求

POST /api/accept_friend_request

> Body 请求参数

```json
{
  "initiator_uid": "string",
  "is_filtered": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[AcceptFriendRequestInput](#schemaacceptfriendrequestinput)| 是 | accept_friend_request 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdreject_friend_request"></a>

## POST 拒绝好友请求

POST /api/reject_friend_request

> Body 请求参数

```json
{
  "initiator_uid": "string",
  "is_filtered": false,
  "reason": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[RejectFriendRequestInput](#schemarejectfriendrequestinput)| 是 | reject_friend_request 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

# 群聊 API

<a id="opIdset_group_name"></a>

## POST 设置群名称

POST /api/set_group_name

> Body 请求参数

```json
{
  "group_id": 10001,
  "new_group_name": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SetGroupNameInput](#schemasetgroupnameinput)| 是 | set_group_name 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdset_group_avatar"></a>

## POST 设置群头像

POST /api/set_group_avatar

> Body 请求参数

```json
{
  "group_id": 10001,
  "image_uri": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SetGroupAvatarInput](#schemasetgroupavatarinput)| 是 | set_group_avatar 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdset_group_member_card"></a>

## POST 设置群名片

POST /api/set_group_member_card

> Body 请求参数

```json
{
  "group_id": 10001,
  "user_id": 10001,
  "card": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SetGroupMemberCardInput](#schemasetgroupmembercardinput)| 是 | set_group_member_card 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdset_group_member_special_title"></a>

## POST 设置群成员专属头衔

POST /api/set_group_member_special_title

> Body 请求参数

```json
{
  "group_id": 10001,
  "user_id": 10001,
  "special_title": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SetGroupMemberSpecialTitleInput](#schemasetgroupmemberspecialtitleinput)| 是 | set_group_member_special_title 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdset_group_member_admin"></a>

## POST 设置群管理员

POST /api/set_group_member_admin

> Body 请求参数

```json
{
  "group_id": 10001,
  "user_id": 10001,
  "is_set": true
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SetGroupMemberAdminInput](#schemasetgroupmemberadmininput)| 是 | set_group_member_admin 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdset_group_member_mute"></a>

## POST 设置群成员禁言

POST /api/set_group_member_mute

> Body 请求参数

```json
{
  "group_id": 10001,
  "user_id": 10001,
  "duration": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SetGroupMemberMuteInput](#schemasetgroupmembermuteinput)| 是 | set_group_member_mute 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdset_group_whole_mute"></a>

## POST 设置群全员禁言

POST /api/set_group_whole_mute

> Body 请求参数

```json
{
  "group_id": 10001,
  "is_mute": true
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SetGroupWholeMuteInput](#schemasetgroupwholemuteinput)| 是 | set_group_whole_mute 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdkick_group_member"></a>

## POST 踢出群成员

POST /api/kick_group_member

> Body 请求参数

```json
{
  "group_id": 10001,
  "user_id": 10001,
  "reject_add_request": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[KickGroupMemberInput](#schemakickgroupmemberinput)| 是 | kick_group_member 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdget_group_announcements"></a>

## POST 获取群公告列表

POST /api/get_group_announcements

> Body 请求参数

```json
{
  "group_id": 10001
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetGroupAnnouncementsInput](#schemagetgroupannouncementsinput)| 是 | get_group_announcements 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "announcements": [
      {}
    ]
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdsend_group_announcement"></a>

## POST 发送群公告

POST /api/send_group_announcement

> Body 请求参数

```json
{
  "group_id": 10001,
  "content": "string",
  "image_uri": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SendGroupAnnouncementInput](#schemasendgroupannouncementinput)| 是 | send_group_announcement 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIddelete_group_announcement"></a>

## POST 删除群公告

POST /api/delete_group_announcement

> Body 请求参数

```json
{
  "group_id": 10001,
  "announcement_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[DeleteGroupAnnouncementInput](#schemadeletegroupannouncementinput)| 是 | delete_group_announcement 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdget_group_essence_messages"></a>

## POST 获取群精华消息列表

POST /api/get_group_essence_messages

> Body 请求参数

```json
{
  "group_id": 10001,
  "page_index": 9007199254740991,
  "page_size": 9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetGroupEssenceMessagesInput](#schemagetgroupessencemessagesinput)| 是 | get_group_essence_messages 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "messages": [
      {}
    ],
    "is_end": true
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|
|type|text|
|type|mention|
|type|mention_all|
|type|face|
|type|reply|
|type|image|
|sub_type|normal|
|sub_type|sticker|
|type|record|
|type|video|
|type|file|
|type|forward|
|type|market_face|
|type|light_app|
|type|xml|

<a id="opIdset_group_essence_message"></a>

## POST 设置群精华消息

POST /api/set_group_essence_message

> Body 请求参数

```json
{
  "group_id": 10001,
  "message_seq": 9007199254740991,
  "is_set": true
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SetGroupEssenceMessageInput](#schemasetgroupessencemessageinput)| 是 | set_group_essence_message 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdquit_group"></a>

## POST 退出群

POST /api/quit_group

> Body 请求参数

```json
{
  "group_id": 10001
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[QuitGroupInput](#schemaquitgroupinput)| 是 | quit_group 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdsend_group_message_reaction"></a>

## POST 发送群消息表情回应

POST /api/send_group_message_reaction

> Body 请求参数

```json
{
  "group_id": 10001,
  "message_seq": 9007199254740991,
  "reaction": "string",
  "reaction_type": "face",
  "is_add": true
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SendGroupMessageReactionInput](#schemasendgroupmessagereactioninput)| 是 | send_group_message_reaction 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdsend_group_nudge"></a>

## POST 发送群戳一戳

POST /api/send_group_nudge

> Body 请求参数

```json
{
  "group_id": 10001,
  "user_id": 10001
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[SendGroupNudgeInput](#schemasendgroupnudgeinput)| 是 | send_group_nudge 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdget_group_notifications"></a>

## POST 获取群通知列表

POST /api/get_group_notifications

> Body 请求参数

```json
{
  "start_notification_seq": 9007199254740991,
  "is_filtered": false,
  "limit": 20
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetGroupNotificationsInput](#schemagetgroupnotificationsinput)| 是 | get_group_notifications 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "notifications": [
      null
    ],
    "next_notification_seq": 9007199254740991
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|
|type|join_request|
|state|pending|
|state|accepted|
|state|rejected|
|state|ignored|
|type|admin_change|
|type|kick|
|type|quit|
|type|invited_join_request|
|state|pending|
|state|accepted|
|state|rejected|
|state|ignored|

<a id="opIdaccept_group_request"></a>

## POST 同意入群/邀请他人入群请求

POST /api/accept_group_request

> Body 请求参数

```json
{
  "notification_seq": 9007199254740991,
  "notification_type": "join_request",
  "group_id": 10001,
  "is_filtered": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[AcceptGroupRequestInput](#schemaacceptgrouprequestinput)| 是 | accept_group_request 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdreject_group_request"></a>

## POST 拒绝入群/邀请他人入群请求

POST /api/reject_group_request

> Body 请求参数

```json
{
  "notification_seq": 9007199254740991,
  "notification_type": "join_request",
  "group_id": 10001,
  "is_filtered": false,
  "reason": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[RejectGroupRequestInput](#schemarejectgrouprequestinput)| 是 | reject_group_request 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdaccept_group_invitation"></a>

## POST 同意他人邀请自身入群

POST /api/accept_group_invitation

> Body 请求参数

```json
{
  "group_id": 10001,
  "invitation_seq": 9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[AcceptGroupInvitationInput](#schemaacceptgroupinvitationinput)| 是 | accept_group_invitation 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdreject_group_invitation"></a>

## POST 拒绝他人邀请自身入群

POST /api/reject_group_invitation

> Body 请求参数

```json
{
  "group_id": 10001,
  "invitation_seq": 9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[RejectGroupInvitationInput](#schemarejectgroupinvitationinput)| 是 | reject_group_invitation 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

# 文件 API

<a id="opIdupload_private_file"></a>

## POST 上传私聊文件

POST /api/upload_private_file

> Body 请求参数

```json
{
  "user_id": 10001,
  "file_uri": "string",
  "file_name": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[UploadPrivateFileInput](#schemauploadprivatefileinput)| 是 | upload_private_file 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "file_id": "string"
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdupload_group_file"></a>

## POST 上传群文件

POST /api/upload_group_file

> Body 请求参数

```json
{
  "group_id": 10001,
  "parent_folder_id": "/",
  "file_uri": "string",
  "file_name": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[UploadGroupFileInput](#schemauploadgroupfileinput)| 是 | upload_group_file 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "file_id": "string"
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdget_private_file_download_url"></a>

## POST 获取私聊文件下载链接

POST /api/get_private_file_download_url

> Body 请求参数

```json
{
  "user_id": 10001,
  "file_id": "string",
  "file_hash": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetPrivateFileDownloadUrlInput](#schemagetprivatefiledownloadurlinput)| 是 | get_private_file_download_url 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "download_url": "string"
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdget_group_file_download_url"></a>

## POST 获取群文件下载链接

POST /api/get_group_file_download_url

> Body 请求参数

```json
{
  "group_id": 10001,
  "file_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetGroupFileDownloadUrlInput](#schemagetgroupfiledownloadurlinput)| 是 | get_group_file_download_url 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "download_url": "string"
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdget_group_files"></a>

## POST 获取群文件列表

POST /api/get_group_files

> Body 请求参数

```json
{
  "group_id": 10001,
  "parent_folder_id": "/"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[GetGroupFilesInput](#schemagetgroupfilesinput)| 是 | get_group_files 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "files": [
      {}
    ],
    "folders": [
      {}
    ]
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdmove_group_file"></a>

## POST 移动群文件

POST /api/move_group_file

> Body 请求参数

```json
{
  "group_id": 10001,
  "file_id": "string",
  "parent_folder_id": "/",
  "target_folder_id": "/"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[MoveGroupFileInput](#schemamovegroupfileinput)| 是 | move_group_file 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdrename_group_file"></a>

## POST 重命名群文件

POST /api/rename_group_file

> Body 请求参数

```json
{
  "group_id": 10001,
  "file_id": "string",
  "parent_folder_id": "/",
  "new_file_name": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[RenameGroupFileInput](#schemarenamegroupfileinput)| 是 | rename_group_file 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIddelete_group_file"></a>

## POST 删除群文件

POST /api/delete_group_file

> Body 请求参数

```json
{
  "group_id": 10001,
  "file_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[DeleteGroupFileInput](#schemadeletegroupfileinput)| 是 | delete_group_file 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdcreate_group_folder"></a>

## POST 创建群文件夹

POST /api/create_group_folder

> Body 请求参数

```json
{
  "group_id": 10001,
  "folder_name": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[CreateGroupFolderInput](#schemacreategroupfolderinput)| 是 | create_group_folder 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "folder_id": "string"
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIdrename_group_folder"></a>

## POST 重命名群文件夹

POST /api/rename_group_folder

> Body 请求参数

```json
{
  "group_id": 10001,
  "folder_id": "string",
  "new_folder_name": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[RenameGroupFolderInput](#schemarenamegroupfolderinput)| 是 | rename_group_folder 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<a id="opIddelete_group_folder"></a>

## POST 删除群文件夹

POST /api/delete_group_folder

> Body 请求参数

```json
{
  "group_id": 10001,
  "folder_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[DeleteGroupFolderInput](#schemadeletegroupfolderinput)| 是 | delete_group_folder 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|None|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|None|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

# 数据模型

<h2 id="tocS_Event">Event</h2>

<a id="schemaevent"></a>
<a id="schema_Event"></a>
<a id="tocSevent"></a>
<a id="tocsevent"></a>

```json
{
  "event_type": "bot_offline",
  "time": 9007199254740991,
  "self_id": 10001,
  "data": {
    "reason": "string"
  }
}

```

事件

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|事件|any|false|none|事件|事件|

oneOf

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|机器人离线事件|机器人离线事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||机器人离线事件|
|»» reason|string|true|none||下线原因|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|消息接收事件|消息接收事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|[IncomingMessage](#schemaincomingmessage)|true|none||消息接收事件|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|消息撤回事件|消息撤回事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||消息撤回事件|
|»» message_scene|string|true|none||消息场景|
|»» peer_id|integer|true|none||好友 QQ 号或群号|
|»» message_seq|integer|true|none||消息序列号|
|»» sender_id|integer|true|none||被撤回的消息的发送者 QQ 号|
|»» operator_id|integer|true|none||操作者 QQ 号|
|»» display_suffix|string|true|none||撤回提示的后缀文本|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|会话置顶变更事件|会话置顶变更事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||会话置顶变更事件|
|»» message_scene|string|true|none||发生改变的会话的消息场景|
|»» peer_id|integer|true|none||发生改变的好友 QQ 号或群号|
|»» is_pinned|boolean|true|none||是否被置顶, `false` 表示取消置顶|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|好友请求事件|好友请求事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||好友请求事件|
|»» initiator_id|integer|true|none||申请好友的用户 QQ 号|
|»» initiator_uid|string|true|none||用户 UID|
|»» comment|string|true|none||申请附加信息|
|»» via|string|true|none||申请来源|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|入群请求事件|入群请求事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||入群请求事件|
|»» group_id|integer|true|none||群号|
|»» notification_seq|integer|true|none||请求对应的通知序列号|
|»» is_filtered|boolean|true|none||请求是否被过滤（发起自风险账户）|
|»» initiator_id|integer|true|none||申请入群的用户 QQ 号|
|»» comment|string|true|none||申请附加信息|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|群成员邀请他人入群请求事件|群成员邀请他人入群请求事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||群成员邀请他人入群请求事件|
|»» group_id|integer|true|none||群号|
|»» notification_seq|integer|true|none||请求对应的通知序列号|
|»» initiator_id|integer|true|none||邀请者 QQ 号|
|»» target_user_id|integer|true|none||被邀请者 QQ 号|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|他人邀请自身入群事件|他人邀请自身入群事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||他人邀请自身入群事件|
|»» group_id|integer|true|none||群号|
|»» invitation_seq|integer|true|none||邀请序列号|
|»» initiator_id|integer|true|none||邀请者 QQ 号|
|»» source_group_id|integer,null|false|none||来源群号，如果是通过 QQ 群邀请|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|好友戳一戳事件|好友戳一戳事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||好友戳一戳事件|
|»» user_id|integer|true|none||好友 QQ 号|
|»» is_self_send|boolean|true|none||是否是自己发送的戳一戳|
|»» is_self_receive|boolean|true|none||是否是自己接收的戳一戳|
|»» display_action|string|true|none||戳一戳提示的动作文本|
|»» display_suffix|string|true|none||戳一戳提示的后缀文本|
|»» display_action_img_url|string|true|none||戳一戳提示的动作图片 URL，用于取代动作提示文本|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|好友文件上传事件|好友文件上传事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||好友文件上传事件|
|»» user_id|integer|true|none||好友 QQ 号|
|»» file_id|string|true|none||文件 ID|
|»» file_name|string|true|none||文件名称|
|»» file_size|integer|true|none||文件大小（字节）|
|»» file_hash|string|true|none||文件的 TriSHA1 哈希值|
|»» is_self|boolean|true|none||是否是自己发送的文件|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|群管理员变更事件|群管理员变更事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||群管理员变更事件|
|»» group_id|integer|true|none||群号|
|»» user_id|integer|true|none||发生变更的用户 QQ 号|
|»» operator_id|integer|true|none||操作者 QQ 号|
|»» is_set|boolean|true|none||是否被设置为管理员，`false` 表示被取消管理员|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|群精华消息变更事件|群精华消息变更事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||群精华消息变更事件|
|»» group_id|integer|true|none||群号|
|»» message_seq|integer|true|none||发生变更的消息序列号|
|»» operator_id|integer|true|none||操作者 QQ 号|
|»» is_set|boolean|true|none||是否被设置为精华，`false` 表示被取消精华|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|群成员增加事件|群成员增加事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||群成员增加事件|
|»» group_id|integer|true|none||群号|
|»» user_id|integer|true|none||发生变更的用户 QQ 号|
|»» operator_id|integer,null|false|none||管理员 QQ 号，如果是管理员同意入群|
|»» invitor_id|integer,null|false|none||邀请者 QQ 号，如果是邀请入群|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|群成员减少事件|群成员减少事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||群成员减少事件|
|»» group_id|integer|true|none||群号|
|»» user_id|integer|true|none||发生变更的用户 QQ 号|
|»» operator_id|integer,null|false|none||管理员 QQ 号，如果是管理员踢出|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|群名称变更事件|群名称变更事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||群名称变更事件|
|»» group_id|integer|true|none||群号|
|»» new_group_name|string|true|none||新的群名称|
|»» operator_id|integer|true|none||操作者 QQ 号|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|群消息表情回应事件|群消息表情回应事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||群消息表情回应事件|
|»» group_id|integer|true|none||群号|
|»» user_id|integer|true|none||发送回应者 QQ 号|
|»» message_seq|integer|true|none||消息序列号|
|»» face_id|string|true|none||表情 ID|
|»» reaction_type|string|true|none||收到的回应类型|
|»» is_add|boolean|true|none||是否为添加，`false` 表示取消回应|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|群禁言事件|群禁言事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||群禁言事件|
|»» group_id|integer|true|none||群号|
|»» user_id|integer|true|none||发生变更的用户 QQ 号|
|»» operator_id|integer|true|none||操作者 QQ 号|
|»» duration|integer|true|none||禁言时长（秒），为 0 表示取消禁言|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|群全体禁言事件|群全体禁言事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||群全体禁言事件|
|»» group_id|integer|true|none||群号|
|»» operator_id|integer|true|none||操作者 QQ 号|
|»» is_mute|boolean|true|none||是否全员禁言，`false` 表示取消全员禁言|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|群戳一戳事件|群戳一戳事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||群戳一戳事件|
|»» group_id|integer|true|none||群号|
|»» sender_id|integer|true|none||发送者 QQ 号|
|»» receiver_id|integer|true|none||接收者 QQ 号|
|»» display_action|string|true|none||戳一戳提示的动作文本|
|»» display_suffix|string|true|none||戳一戳提示的后缀文本|
|»» display_action_img_url|string|true|none||戳一戳提示的动作图片 URL，用于取代动作提示文本|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|群文件上传事件|群文件上传事件|
|» event_type|string|true|none||none|
|» time|integer|true|none||事件 Unix 时间戳（秒）|
|» self_id|integer|true|none||机器人 QQ 号|
|» data|object|true|none||群文件上传事件|
|»» group_id|integer|true|none||群号|
|»» user_id|integer|true|none||发送者 QQ 号|
|»» file_id|string|true|none||文件 ID|
|»» file_name|string|true|none||文件名称|
|»» file_size|integer|true|none||文件大小（字节）|

#### 枚举值

|属性|值|
|---|---|
|event_type|bot_offline|
|event_type|message_receive|
|event_type|message_recall|
|message_scene|friend|
|message_scene|group|
|message_scene|temp|
|event_type|peer_pin_change|
|message_scene|friend|
|message_scene|group|
|message_scene|temp|
|event_type|friend_request|
|event_type|group_join_request|
|event_type|group_invited_join_request|
|event_type|group_invitation|
|event_type|friend_nudge|
|event_type|friend_file_upload|
|event_type|group_admin_change|
|event_type|group_essence_message_change|
|event_type|group_member_increase|
|event_type|group_member_decrease|
|event_type|group_name_change|
|event_type|group_message_reaction|
|reaction_type|face|
|reaction_type|emoji|
|event_type|group_mute|
|event_type|group_whole_mute|
|event_type|group_nudge|
|event_type|group_file_upload|

<h2 id="tocS_FriendEntity">FriendEntity</h2>

<a id="schemafriendentity"></a>
<a id="schema_FriendEntity"></a>
<a id="tocSfriendentity"></a>
<a id="tocsfriendentity"></a>

```json
{
  "user_id": 10001,
  "nickname": "string",
  "sex": "male",
  "qid": "string",
  "remark": "string",
  "category": {
    "category_id": 9007199254740991,
    "category_name": "string"
  }
}

```

好友实体

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||用户 QQ 号|
|nickname|string|true|none||用户昵称|
|sex|string|true|none||用户性别|
|qid|string|true|none||用户 QID|
|remark|string|true|none||好友备注|
|category|[FriendCategoryEntity](#schemafriendcategoryentity)|true|none||好友分组|

#### 枚举值

|属性|值|
|---|---|
|sex|male|
|sex|female|
|sex|unknown|

<h2 id="tocS_FriendCategoryEntity">FriendCategoryEntity</h2>

<a id="schemafriendcategoryentity"></a>
<a id="schema_FriendCategoryEntity"></a>
<a id="tocSfriendcategoryentity"></a>
<a id="tocsfriendcategoryentity"></a>

```json
{
  "category_id": 9007199254740991,
  "category_name": "string"
}

```

好友分组实体

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|category_id|integer|true|none||好友分组 ID|
|category_name|string|true|none||好友分组名称|

<h2 id="tocS_GroupEntity">GroupEntity</h2>

<a id="schemagroupentity"></a>
<a id="schema_GroupEntity"></a>
<a id="tocSgroupentity"></a>
<a id="tocsgroupentity"></a>

```json
{
  "group_id": 10001,
  "group_name": "string",
  "member_count": 9007199254740991,
  "max_member_count": 9007199254740991,
  "remark": "string",
  "created_time": 9007199254740991,
  "description": "string",
  "question": "string",
  "announcement": "string"
}

```

群实体

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|group_name|string|true|none||群名称|
|member_count|integer|true|none||群成员数量|
|max_member_count|integer|true|none||群容量|
|remark|string|true|none||群备注|
|created_time|integer|true|none||群创建时间，Unix 时间戳（秒）|
|description|string|true|none||群简介|
|question|string|true|none||加群验证问题|
|announcement|string|true|none||群公告预览|

<h2 id="tocS_GroupMemberEntity">GroupMemberEntity</h2>

<a id="schemagroupmemberentity"></a>
<a id="schema_GroupMemberEntity"></a>
<a id="tocSgroupmemberentity"></a>
<a id="tocsgroupmemberentity"></a>

```json
{
  "user_id": 10001,
  "nickname": "string",
  "sex": "male",
  "group_id": 10001,
  "card": "string",
  "title": "string",
  "level": 9007199254740991,
  "role": "owner",
  "join_time": 9007199254740991,
  "last_sent_time": 9007199254740991,
  "shut_up_end_time": 9007199254740991
}

```

群成员实体

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||用户 QQ 号|
|nickname|string|true|none||用户昵称|
|sex|string|true|none||用户性别|
|group_id|integer|true|none||群号|
|card|string|true|none||成员备注|
|title|string|true|none||专属头衔|
|level|integer|true|none||群等级，注意和 QQ 等级区分|
|role|string|true|none||权限等级|
|join_time|integer|true|none||入群时间，Unix 时间戳（秒）|
|last_sent_time|integer|true|none||最后发言时间，Unix 时间戳（秒）|
|shut_up_end_time|integer,null|false|none||禁言结束时间，Unix 时间戳（秒）|

#### 枚举值

|属性|值|
|---|---|
|sex|male|
|sex|female|
|sex|unknown|
|role|owner|
|role|admin|
|role|member|

<h2 id="tocS_GroupAnnouncementEntity">GroupAnnouncementEntity</h2>

<a id="schemagroupannouncemententity"></a>
<a id="schema_GroupAnnouncementEntity"></a>
<a id="tocSgroupannouncemententity"></a>
<a id="tocsgroupannouncemententity"></a>

```json
{
  "group_id": 10001,
  "announcement_id": "string",
  "user_id": 10001,
  "time": 9007199254740991,
  "content": "string",
  "image_url": "string"
}

```

群公告实体

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|announcement_id|string|true|none||公告 ID|
|user_id|integer|true|none||发送者 QQ 号|
|time|integer|true|none||Unix 时间戳（秒）|
|content|string|true|none||公告内容|
|image_url|string,null|false|none||公告图片 URL|

<h2 id="tocS_GroupFileEntity">GroupFileEntity</h2>

<a id="schemagroupfileentity"></a>
<a id="schema_GroupFileEntity"></a>
<a id="tocSgroupfileentity"></a>
<a id="tocsgroupfileentity"></a>

```json
{
  "group_id": 10001,
  "file_id": "string",
  "file_name": "string",
  "parent_folder_id": "string",
  "file_size": 9007199254740991,
  "uploaded_time": 9007199254740991,
  "expire_time": 9007199254740991,
  "uploader_id": 10001,
  "downloaded_times": 9007199254740991
}

```

群文件实体

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|file_id|string|true|none||文件 ID|
|file_name|string|true|none||文件名称|
|parent_folder_id|string|true|none||父文件夹 ID|
|file_size|integer|true|none||文件大小（字节）|
|uploaded_time|integer|true|none||上传时的 Unix 时间戳（秒）|
|expire_time|integer,null|false|none||过期时的 Unix 时间戳（秒）|
|uploader_id|integer|true|none||上传者 QQ 号|
|downloaded_times|integer|true|none||下载次数|

<h2 id="tocS_GroupFolderEntity">GroupFolderEntity</h2>

<a id="schemagroupfolderentity"></a>
<a id="schema_GroupFolderEntity"></a>
<a id="tocSgroupfolderentity"></a>
<a id="tocsgroupfolderentity"></a>

```json
{
  "group_id": 10001,
  "folder_id": "string",
  "parent_folder_id": "string",
  "folder_name": "string",
  "created_time": 9007199254740991,
  "last_modified_time": 9007199254740991,
  "creator_id": 10001,
  "file_count": 9007199254740991
}

```

群文件夹实体

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|folder_id|string|true|none||文件夹 ID|
|parent_folder_id|string|true|none||父文件夹 ID|
|folder_name|string|true|none||文件夹名称|
|created_time|integer|true|none||创建时的 Unix 时间戳（秒）|
|last_modified_time|integer|true|none||最后修改时的 Unix 时间戳（秒）|
|creator_id|integer|true|none||创建者 QQ 号|
|file_count|integer|true|none||文件数量|

<h2 id="tocS_FriendRequest">FriendRequest</h2>

<a id="schemafriendrequest"></a>
<a id="schema_FriendRequest"></a>
<a id="tocSfriendrequest"></a>
<a id="tocsfriendrequest"></a>

```json
{
  "time": 9007199254740991,
  "initiator_id": 10001,
  "initiator_uid": "string",
  "target_user_id": 10001,
  "target_user_uid": "string",
  "state": "pending",
  "comment": "string",
  "via": "string",
  "is_filtered": true
}

```

好友请求实体

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||请求发起时的 Unix 时间戳（秒）|
|initiator_id|integer|true|none||请求发起者 QQ 号|
|initiator_uid|string|true|none||请求发起者 UID|
|target_user_id|integer|true|none||目标用户 QQ 号|
|target_user_uid|string|true|none||目标用户 UID|
|state|string|true|none||请求状态|
|comment|string|true|none||申请附加信息|
|via|string|true|none||申请来源|
|is_filtered|boolean|true|none||请求是否被过滤（发起自风险账户）|

#### 枚举值

|属性|值|
|---|---|
|state|pending|
|state|accepted|
|state|rejected|
|state|ignored|

<h2 id="tocS_GroupNotification">GroupNotification</h2>

<a id="schemagroupnotification"></a>
<a id="schema_GroupNotification"></a>
<a id="tocSgroupnotification"></a>
<a id="tocsgroupnotification"></a>

```json
{
  "type": "join_request",
  "group_id": 10001,
  "notification_seq": 9007199254740991,
  "is_filtered": true,
  "initiator_id": 10001,
  "state": "pending",
  "operator_id": 9007199254740991,
  "comment": "string"
}

```

群通知实体

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|群通知实体|any|false|none|群通知实体|群通知实体|

oneOf

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|用户入群请求|用户入群请求|
|» type|string|true|none||none|
|» group_id|integer|true|none||群号|
|» notification_seq|integer|true|none||通知序列号|
|» is_filtered|boolean|true|none||请求是否被过滤（发起自风险账户）|
|» initiator_id|integer|true|none||发起者 QQ 号|
|» state|string|true|none||请求状态|
|» operator_id|integer,null|false|none||处理请求的管理员 QQ 号|
|» comment|string|true|none||入群请求附加信息|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|群管理员变更通知|群管理员变更通知|
|» type|string|true|none||none|
|» group_id|integer|true|none||群号|
|» notification_seq|integer|true|none||通知序列号|
|» target_user_id|integer|true|none||被设置/取消用户 QQ 号|
|» is_set|boolean|true|none||是否被设置为管理员，`false` 表示被取消管理员|
|» operator_id|integer|true|none||操作者（群主）QQ 号|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|群成员被移除通知|群成员被移除通知|
|» type|string|true|none||none|
|» group_id|integer|true|none||群号|
|» notification_seq|integer|true|none||通知序列号|
|» target_user_id|integer|true|none||被移除用户 QQ 号|
|» operator_id|integer|true|none||移除用户的管理员 QQ 号|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|群成员退群通知|群成员退群通知|
|» type|string|true|none||none|
|» group_id|integer|true|none||群号|
|» notification_seq|integer|true|none||通知序列号|
|» target_user_id|integer|true|none||退群用户 QQ 号|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|群成员邀请他人入群请求|群成员邀请他人入群请求|
|» type|string|true|none||none|
|» group_id|integer|true|none||群号|
|» notification_seq|integer|true|none||通知序列号|
|» initiator_id|integer|true|none||邀请者 QQ 号|
|» target_user_id|integer|true|none||被邀请用户 QQ 号|
|» state|string|true|none||请求状态|
|» operator_id|integer,null|false|none||处理请求的管理员 QQ 号|

#### 枚举值

|属性|值|
|---|---|
|type|join_request|
|state|pending|
|state|accepted|
|state|rejected|
|state|ignored|
|type|admin_change|
|type|kick|
|type|quit|
|type|invited_join_request|
|state|pending|
|state|accepted|
|state|rejected|
|state|ignored|

<h2 id="tocS_IncomingMessage">IncomingMessage</h2>

<a id="schemaincomingmessage"></a>
<a id="schema_IncomingMessage"></a>
<a id="tocSincomingmessage"></a>
<a id="tocsincomingmessage"></a>

```json
{
  "message_scene": "friend",
  "peer_id": 10001,
  "message_seq": 9007199254740991,
  "sender_id": 10001,
  "time": 9007199254740991,
  "segments": [
    {
      "type": "text",
      "data": {
        "text": "[unknown]"
      }
    }
  ],
  "friend": {
    "user_id": 10001,
    "nickname": "string",
    "sex": "male",
    "qid": "string",
    "remark": "string",
    "category": null
  }
}

```

接收消息

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|接收消息|any|false|none|接收消息|接收消息|

oneOf

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|好友消息|好友消息|
|» message_scene|string|true|none||none|
|» peer_id|integer|true|none||好友 QQ 号或群号|
|» message_seq|integer|true|none||消息序列号|
|» sender_id|integer|true|none||发送者 QQ 号|
|» time|integer|true|none||消息 Unix 时间戳（秒）|
|» segments|[allOf]|true|none||消息段列表|
|» friend|[FriendEntity](#schemafriendentity)|true|none||好友信息|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|群消息|群消息|
|» message_scene|string|true|none||none|
|» peer_id|integer|true|none||好友 QQ 号或群号|
|» message_seq|integer|true|none||消息序列号|
|» sender_id|integer|true|none||发送者 QQ 号|
|» time|integer|true|none||消息 Unix 时间戳（秒）|
|» segments|[allOf]|true|none||消息段列表|
|» group|[GroupEntity](#schemagroupentity)|true|none||群信息|
|» group_member|[GroupMemberEntity](#schemagroupmemberentity)|true|none||群成员信息|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|临时会话消息|临时会话消息|
|» message_scene|string|true|none||none|
|» peer_id|integer|true|none||好友 QQ 号或群号|
|» message_seq|integer|true|none||消息序列号|
|» sender_id|integer|true|none||发送者 QQ 号|
|» time|integer|true|none||消息 Unix 时间戳（秒）|
|» segments|[allOf]|true|none||消息段列表|
|» group|[GroupEntity](#schemagroupentity)|false|none||临时会话发送者的所在的群信息|

#### 枚举值

|属性|值|
|---|---|
|message_scene|friend|
|message_scene|group|
|message_scene|temp|

<h2 id="tocS_IncomingForwardedMessage">IncomingForwardedMessage</h2>

<a id="schemaincomingforwardedmessage"></a>
<a id="schema_IncomingForwardedMessage"></a>
<a id="tocSincomingforwardedmessage"></a>
<a id="tocsincomingforwardedmessage"></a>

```json
{
  "message_seq": 9007199254740991,
  "sender_name": "string",
  "avatar_url": "string",
  "time": 9007199254740991,
  "segments": [
    {
      "type": "text",
      "data": {
        "text": "[unknown]"
      }
    }
  ]
}

```

接收转发消息

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|message_seq|integer|true|none||消息序列号|
|sender_name|string|true|none||发送者名称|
|avatar_url|string|true|none||发送者头像 URL|
|time|integer|true|none||消息 Unix 时间戳（秒）|
|segments|[allOf]|true|none||消息段列表|

<h2 id="tocS_GroupEssenceMessage">GroupEssenceMessage</h2>

<a id="schemagroupessencemessage"></a>
<a id="schema_GroupEssenceMessage"></a>
<a id="tocSgroupessencemessage"></a>
<a id="tocsgroupessencemessage"></a>

```json
{
  "group_id": 10001,
  "message_seq": 9007199254740991,
  "message_time": 9007199254740991,
  "sender_id": 10001,
  "sender_name": "string",
  "operator_id": 10001,
  "operator_name": "string",
  "operation_time": 9007199254740991,
  "segments": [
    {
      "type": "text",
      "data": {
        "text": "[unknown]"
      }
    }
  ]
}

```

群精华消息

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|message_seq|integer|true|none||消息序列号|
|message_time|integer|true|none||消息发送时的 Unix 时间戳（秒）|
|sender_id|integer|true|none||发送者 QQ 号|
|sender_name|string|true|none||发送者名称|
|operator_id|integer|true|none||设置精华的操作者 QQ 号|
|operator_name|string|true|none||设置精华的操作者名称|
|operation_time|integer|true|none||消息被设置精华时的 Unix 时间戳（秒）|
|segments|[allOf]|true|none||消息段列表|

<h2 id="tocS_IncomingSegment">IncomingSegment</h2>

<a id="schemaincomingsegment"></a>
<a id="schema_IncomingSegment"></a>
<a id="tocSincomingsegment"></a>
<a id="tocsincomingsegment"></a>

```json
{
  "type": "text",
  "data": {
    "text": "[unknown]"
  }
}

```

接收消息段

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|接收消息段|any|false|none|接收消息段|接收消息段|

oneOf

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|文本消息段|文本消息段|
|» type|string|true|none||none|
|» data|object|true|none||文本消息段|
|»» text|string|true|none||文本内容|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|提及消息段|提及消息段|
|» type|string|true|none||none|
|» data|object|true|none||提及消息段|
|»» user_id|integer|true|none||提及的 QQ 号|
|»» name|string|true|none||去掉 `@` 前缀的提及的名称|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|提及全体消息段|提及全体消息段|
|» type|string|true|none||none|
|» data|object|true|none||提及全体消息段|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|表情消息段|表情消息段|
|» type|string|true|none||none|
|» data|object|true|none||表情消息段|
|»» face_id|string|true|none||表情 ID|
|»» is_large|boolean|true|none||是否为超级表情|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|回复消息段|回复消息段|
|» type|string|true|none||none|
|» data|object|true|none||回复消息段|
|»» message_seq|integer|true|none||被引用的消息序列号|
|»» sender_id|integer|true|none||被引用的消息发送者 QQ 号|
|»» sender_name|string,null|false|none||被引用的消息发送者名称，仅在合并转发中能够获取|
|»» time|integer|true|none||被引用的消息的 Unix 时间戳（秒）|
|»» segments|[allOf]|true|none||回复消息内容|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|图片消息段|图片消息段|
|» type|string|true|none||none|
|» data|object|true|none||图片消息段|
|»» resource_id|string|true|none||资源 ID|
|»» temp_url|string|true|none||临时 URL|
|»» width|integer|true|none||图片宽度|
|»» height|integer|true|none||图片高度|
|»» summary|string|true|none||图片预览文本|
|»» sub_type|string|true|none||图片类型|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|语音消息段|语音消息段|
|» type|string|true|none||none|
|» data|object|true|none||语音消息段|
|»» resource_id|string|true|none||资源 ID|
|»» temp_url|string|true|none||临时 URL|
|»» duration|integer|true|none||语音时长（秒）|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|视频消息段|视频消息段|
|» type|string|true|none||none|
|» data|object|true|none||视频消息段|
|»» resource_id|string|true|none||资源 ID|
|»» temp_url|string|true|none||临时 URL|
|»» width|integer|true|none||视频宽度|
|»» height|integer|true|none||视频高度|
|»» duration|integer|true|none||视频时长（秒）|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|文件消息段|文件消息段|
|» type|string|true|none||none|
|» data|object|true|none||文件消息段|
|»» file_id|string|true|none||文件 ID|
|»» file_name|string|true|none||文件名称|
|»» file_size|integer|true|none||文件大小（字节）|
|»» file_hash|string,null|false|none||文件的 TriSHA1 哈希值，仅在私聊文件中存在|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|合并转发消息段|合并转发消息段|
|» type|string|true|none||none|
|» data|object|true|none||合并转发消息段|
|»» forward_id|string|true|none||合并转发 ID|
|»» title|string|true|none||合并转发标题|
|»» preview|[string]|true|none||合并转发预览文本|
|»» summary|string|true|none||合并转发摘要|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|市场表情消息段|市场表情消息段|
|» type|string|true|none||none|
|» data|object|true|none||市场表情消息段|
|»» emoji_package_id|integer|true|none||市场表情包 ID|
|»» emoji_id|string|true|none||市场表情 ID|
|»» key|string|true|none||市场表情 Key|
|»» summary|string|true|none||市场表情预览文本|
|»» url|string|true|none||市场表情 URL|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|小程序消息段|小程序消息段|
|» type|string|true|none||none|
|» data|object|true|none||小程序消息段|
|»» app_name|string|true|none||小程序名称|
|»» json_payload|string|true|none||小程序 JSON 数据|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|XML 消息段|XML 消息段|
|» type|string|true|none||none|
|» data|object|true|none||XML 消息段|
|»» service_id|integer|true|none||服务 ID|
|»» xml_payload|string|true|none||XML 数据|

#### 枚举值

|属性|值|
|---|---|
|type|text|
|type|mention|
|type|mention_all|
|type|face|
|type|reply|
|type|image|
|sub_type|normal|
|sub_type|sticker|
|type|record|
|type|video|
|type|file|
|type|forward|
|type|market_face|
|type|light_app|
|type|xml|

<h2 id="tocS_OutgoingForwardedMessage">OutgoingForwardedMessage</h2>

<a id="schemaoutgoingforwardedmessage"></a>
<a id="schema_OutgoingForwardedMessage"></a>
<a id="tocSoutgoingforwardedmessage"></a>
<a id="tocsoutgoingforwardedmessage"></a>

```json
{
  "user_id": 10001,
  "sender_name": "string",
  "segments": [
    {
      "type": "[",
      "data": {}
    }
  ]
}

```

发送转发消息

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||发送者 QQ 号|
|sender_name|string|true|none||发送者名称|
|segments|[allOf]|true|none||消息段列表|

<h2 id="tocS_OutgoingSegment">OutgoingSegment</h2>

<a id="schemaoutgoingsegment"></a>
<a id="schema_OutgoingSegment"></a>
<a id="tocSoutgoingsegment"></a>
<a id="tocsoutgoingsegment"></a>

```json
{
  "type": "text",
  "data": {
    "text": "string"
  }
}

```

发送消息段

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|发送消息段|any|false|none|发送消息段|发送消息段|

oneOf

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|文本消息段|文本消息段|
|» type|string|true|none||none|
|» data|object|true|none||文本消息段|
|»» text|string|true|none||文本内容|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|提及消息段|提及消息段|
|» type|string|true|none||none|
|» data|object|true|none||提及消息段|
|»» user_id|integer|true|none||提及的 QQ 号|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|提及全体消息段|提及全体消息段|
|» type|string|true|none||none|
|» data|object|true|none||提及全体消息段|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|表情消息段|表情消息段|
|» type|string|true|none||none|
|» data|object|true|none||表情消息段|
|»» face_id|string|true|none||表情 ID|
|»» is_large|boolean,null|false|none||是否为超级表情|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|回复消息段|回复消息段|
|» type|string|true|none||none|
|» data|object|true|none||回复消息段|
|»» message_seq|integer|true|none||被引用的消息序列号|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|图片消息段|图片消息段|
|» type|string|true|none||none|
|» data|object|true|none||图片消息段|
|»» uri|string|true|none||文件 URI，支持 `file://` `http(s)://` `base64://` 三种格式|
|»» sub_type|string,null|false|none||图片类型|
|»» summary|string,null|false|none||图片预览文本|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|语音消息段|语音消息段|
|» type|string|true|none||none|
|» data|object|true|none||语音消息段|
|»» uri|string|true|none||文件 URI，支持 `file://` `http(s)://` `base64://` 三种格式|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|视频消息段|视频消息段|
|» type|string|true|none||none|
|» data|object|true|none||视频消息段|
|»» uri|string|true|none||文件 URI，支持 `file://` `http(s)://` `base64://` 三种格式|
|»» thumb_uri|string,null|false|none||封面图片 URI|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|合并转发消息段|合并转发消息段|
|» type|string|true|none||none|
|» data|object|true|none||合并转发消息段|
|»» messages|[allOf]|true|none||转发消息内容|
|»» title|string,null|false|none||合并转发标题|
|»» preview|array,null|false|none||合并转发预览文本，若提供，至少 1 条，至多 4 条|
|»» summary|string,null|false|none||合并转发摘要|
|»» prompt|string,null|false|none||合并转发的预览外显文本，仅对移动端 QQ 有效|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|小程序消息段|小程序消息段|
|» type|string|true|none||none|
|» data|object|true|none||小程序消息段|
|»» json_payload|string|true|none||小程序 JSON 数据|

#### 枚举值

|属性|值|
|---|---|
|type|text|
|type|mention|
|type|mention_all|
|type|face|
|type|reply|
|type|image|
|sub_type|normal|
|sub_type|sticker|
|type|record|
|type|video|
|type|forward|
|type|light_app|

<h2 id="tocS_ApiResponse">ApiResponse</h2>

<a id="schemaapiresponse"></a>
<a id="schema_ApiResponse"></a>
<a id="tocSapiresponse"></a>
<a id="tocsapiresponse"></a>

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string"
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|status|string|true|none||none|
|retcode|integer|true|none||业务状态码，0 表示成功|
|data|any|false|none||none|
|message|string,null|false|none||错误消息，仅失败时返回|

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

<h2 id="tocS_ApiEmptyObject">ApiEmptyObject</h2>

<a id="schemaapiemptyobject"></a>
<a id="schema_ApiEmptyObject"></a>
<a id="tocSapiemptyobject"></a>
<a id="tocsapiemptyobject"></a>

```json
{}

```

空对象，用于无输入/输出的 API

### 属性

*None*

<h2 id="tocS_GetLoginInfoOutput">GetLoginInfoOutput</h2>

<a id="schemagetlogininfooutput"></a>
<a id="schema_GetLoginInfoOutput"></a>
<a id="tocSgetlogininfooutput"></a>
<a id="tocsgetlogininfooutput"></a>

```json
{
  "uin": 10001,
  "nickname": "string"
}

```

get_login_info 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|uin|integer|true|none||登录 QQ 号|
|nickname|string|true|none||登录昵称|

<h2 id="tocS_GetImplInfoOutput">GetImplInfoOutput</h2>

<a id="schemagetimplinfooutput"></a>
<a id="schema_GetImplInfoOutput"></a>
<a id="tocSgetimplinfooutput"></a>
<a id="tocsgetimplinfooutput"></a>

```json
{
  "impl_name": "string",
  "impl_version": "string",
  "qq_protocol_version": "string",
  "qq_protocol_type": "windows",
  "milky_version": "string"
}

```

get_impl_info 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|impl_name|string|true|none||协议端名称|
|impl_version|string|true|none||协议端版本|
|qq_protocol_version|string|true|none||协议端使用的 QQ 协议版本|
|qq_protocol_type|string|true|none||协议端使用的 QQ 协议平台|
|milky_version|string|true|none||协议端实现的 Milky 协议版本，目前为 "1.2"|

#### 枚举值

|属性|值|
|---|---|
|qq_protocol_type|windows|
|qq_protocol_type|linux|
|qq_protocol_type|macos|
|qq_protocol_type|android_pad|
|qq_protocol_type|android_phone|
|qq_protocol_type|ipad|
|qq_protocol_type|iphone|
|qq_protocol_type|harmony|
|qq_protocol_type|watch|

<h2 id="tocS_GetUserProfileInput">GetUserProfileInput</h2>

<a id="schemagetuserprofileinput"></a>
<a id="schema_GetUserProfileInput"></a>
<a id="tocSgetuserprofileinput"></a>
<a id="tocsgetuserprofileinput"></a>

```json
{
  "user_id": 10001
}

```

get_user_profile 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||用户 QQ 号|

<h2 id="tocS_GetUserProfileOutput">GetUserProfileOutput</h2>

<a id="schemagetuserprofileoutput"></a>
<a id="schema_GetUserProfileOutput"></a>
<a id="tocSgetuserprofileoutput"></a>
<a id="tocsgetuserprofileoutput"></a>

```json
{
  "nickname": "string",
  "qid": "string",
  "age": 9007199254740991,
  "sex": "male",
  "remark": "string",
  "bio": "string",
  "level": 9007199254740991,
  "country": "string",
  "city": "string",
  "school": "string"
}

```

get_user_profile 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|nickname|string|true|none||昵称|
|qid|string|true|none||QID|
|age|integer|true|none||年龄|
|sex|string|true|none||性别|
|remark|string|true|none||备注|
|bio|string|true|none||个性签名|
|level|integer|true|none||QQ 等级|
|country|string|true|none||国家或地区|
|city|string|true|none||城市|
|school|string|true|none||学校|

#### 枚举值

|属性|值|
|---|---|
|sex|male|
|sex|female|
|sex|unknown|

<h2 id="tocS_GetFriendListInput">GetFriendListInput</h2>

<a id="schemagetfriendlistinput"></a>
<a id="schema_GetFriendListInput"></a>
<a id="tocSgetfriendlistinput"></a>
<a id="tocsgetfriendlistinput"></a>

```json
{
  "no_cache": false
}

```

get_friend_list 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|no_cache|boolean,null|false|none||是否强制不使用缓存|

<h2 id="tocS_GetFriendListOutput">GetFriendListOutput</h2>

<a id="schemagetfriendlistoutput"></a>
<a id="schema_GetFriendListOutput"></a>
<a id="tocSgetfriendlistoutput"></a>
<a id="tocsgetfriendlistoutput"></a>

```json
{
  "friends": [
    {
      "user_id": 10001,
      "nickname": "string",
      "sex": "male",
      "qid": "string",
      "remark": "string",
      "category": {}
    }
  ]
}

```

get_friend_list 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|friends|[allOf]|true|none||好友列表|

<h2 id="tocS_GetFriendInfoInput">GetFriendInfoInput</h2>

<a id="schemagetfriendinfoinput"></a>
<a id="schema_GetFriendInfoInput"></a>
<a id="tocSgetfriendinfoinput"></a>
<a id="tocsgetfriendinfoinput"></a>

```json
{
  "user_id": 10001,
  "no_cache": false
}

```

get_friend_info 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||好友 QQ 号|
|no_cache|boolean,null|false|none||是否强制不使用缓存|

<h2 id="tocS_GetFriendInfoOutput">GetFriendInfoOutput</h2>

<a id="schemagetfriendinfooutput"></a>
<a id="schema_GetFriendInfoOutput"></a>
<a id="tocSgetfriendinfooutput"></a>
<a id="tocsgetfriendinfooutput"></a>

```json
{
  "friend": {
    "user_id": 10001,
    "nickname": "string",
    "sex": "male",
    "qid": "string",
    "remark": "string",
    "category": {
      "category_id": null,
      "category_name": null
    }
  }
}

```

get_friend_info 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|friend|[FriendEntity](#schemafriendentity)|true|none||好友信息|

<h2 id="tocS_GetGroupListInput">GetGroupListInput</h2>

<a id="schemagetgrouplistinput"></a>
<a id="schema_GetGroupListInput"></a>
<a id="tocSgetgrouplistinput"></a>
<a id="tocsgetgrouplistinput"></a>

```json
{
  "no_cache": false
}

```

get_group_list 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|no_cache|boolean,null|false|none||是否强制不使用缓存|

<h2 id="tocS_GetGroupListOutput">GetGroupListOutput</h2>

<a id="schemagetgrouplistoutput"></a>
<a id="schema_GetGroupListOutput"></a>
<a id="tocSgetgrouplistoutput"></a>
<a id="tocsgetgrouplistoutput"></a>

```json
{
  "groups": [
    {
      "group_id": 10001,
      "group_name": "string",
      "member_count": 9007199254740991,
      "max_member_count": 9007199254740991,
      "remark": "string",
      "created_time": 9007199254740991,
      "description": "string",
      "question": "string",
      "announcement": "string"
    }
  ]
}

```

get_group_list 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|groups|[allOf]|true|none||群列表|

<h2 id="tocS_GetGroupInfoInput">GetGroupInfoInput</h2>

<a id="schemagetgroupinfoinput"></a>
<a id="schema_GetGroupInfoInput"></a>
<a id="tocSgetgroupinfoinput"></a>
<a id="tocsgetgroupinfoinput"></a>

```json
{
  "group_id": 10001,
  "no_cache": false
}

```

get_group_info 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|no_cache|boolean,null|false|none||是否强制不使用缓存|

<h2 id="tocS_GetGroupInfoOutput">GetGroupInfoOutput</h2>

<a id="schemagetgroupinfooutput"></a>
<a id="schema_GetGroupInfoOutput"></a>
<a id="tocSgetgroupinfooutput"></a>
<a id="tocsgetgroupinfooutput"></a>

```json
{
  "group": {
    "group_id": 10001,
    "group_name": "string",
    "member_count": 9007199254740991,
    "max_member_count": 9007199254740991,
    "remark": "string",
    "created_time": 9007199254740991,
    "description": "string",
    "question": "string",
    "announcement": "string"
  }
}

```

get_group_info 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group|[GroupEntity](#schemagroupentity)|true|none||群信息|

<h2 id="tocS_GetGroupMemberListInput">GetGroupMemberListInput</h2>

<a id="schemagetgroupmemberlistinput"></a>
<a id="schema_GetGroupMemberListInput"></a>
<a id="tocSgetgroupmemberlistinput"></a>
<a id="tocsgetgroupmemberlistinput"></a>

```json
{
  "group_id": 10001,
  "no_cache": false
}

```

get_group_member_list 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|no_cache|boolean,null|false|none||是否强制不使用缓存|

<h2 id="tocS_GetGroupMemberListOutput">GetGroupMemberListOutput</h2>

<a id="schemagetgroupmemberlistoutput"></a>
<a id="schema_GetGroupMemberListOutput"></a>
<a id="tocSgetgroupmemberlistoutput"></a>
<a id="tocsgetgroupmemberlistoutput"></a>

```json
{
  "members": [
    {
      "user_id": 10001,
      "nickname": "string",
      "sex": "male",
      "group_id": 10001,
      "card": "string",
      "title": "string",
      "level": 9007199254740991,
      "role": "owner",
      "join_time": 9007199254740991,
      "last_sent_time": 9007199254740991,
      "shut_up_end_time": 9007199254740991
    }
  ]
}

```

get_group_member_list 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|members|[allOf]|true|none||群成员列表|

<h2 id="tocS_GetGroupMemberInfoInput">GetGroupMemberInfoInput</h2>

<a id="schemagetgroupmemberinfoinput"></a>
<a id="schema_GetGroupMemberInfoInput"></a>
<a id="tocSgetgroupmemberinfoinput"></a>
<a id="tocsgetgroupmemberinfoinput"></a>

```json
{
  "group_id": 10001,
  "user_id": 10001,
  "no_cache": false
}

```

get_group_member_info 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||群成员 QQ 号|
|no_cache|boolean,null|false|none||是否强制不使用缓存|

<h2 id="tocS_GetGroupMemberInfoOutput">GetGroupMemberInfoOutput</h2>

<a id="schemagetgroupmemberinfooutput"></a>
<a id="schema_GetGroupMemberInfoOutput"></a>
<a id="tocSgetgroupmemberinfooutput"></a>
<a id="tocsgetgroupmemberinfooutput"></a>

```json
{
  "member": {
    "user_id": 10001,
    "nickname": "string",
    "sex": "male",
    "group_id": 10001,
    "card": "string",
    "title": "string",
    "level": 9007199254740991,
    "role": "owner",
    "join_time": 9007199254740991,
    "last_sent_time": 9007199254740991,
    "shut_up_end_time": 9007199254740991
  }
}

```

get_group_member_info 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|member|[GroupMemberEntity](#schemagroupmemberentity)|true|none||群成员信息|

<h2 id="tocS_GetPeerPinsOutput">GetPeerPinsOutput</h2>

<a id="schemagetpeerpinsoutput"></a>
<a id="schema_GetPeerPinsOutput"></a>
<a id="tocSgetpeerpinsoutput"></a>
<a id="tocsgetpeerpinsoutput"></a>

```json
{
  "friends": [
    {
      "user_id": 10001,
      "nickname": "string",
      "sex": "male",
      "qid": "string",
      "remark": "string",
      "category": {}
    }
  ],
  "groups": [
    {
      "group_id": 10001,
      "group_name": "string",
      "member_count": 9007199254740991,
      "max_member_count": 9007199254740991,
      "remark": "string",
      "created_time": 9007199254740991,
      "description": "string",
      "question": "string",
      "announcement": "string"
    }
  ]
}

```

get_peer_pins 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|friends|[allOf]|true|none||置顶的好友列表|
|groups|[allOf]|true|none||置顶的群列表|

<h2 id="tocS_SetPeerPinInput">SetPeerPinInput</h2>

<a id="schemasetpeerpininput"></a>
<a id="schema_SetPeerPinInput"></a>
<a id="tocSsetpeerpininput"></a>
<a id="tocssetpeerpininput"></a>

```json
{
  "message_scene": "friend",
  "peer_id": 10001,
  "is_pinned": true
}

```

set_peer_pin 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|message_scene|string|true|none||要设置的会话的消息场景|
|peer_id|integer|true|none||要设置的好友 QQ 号或群号|
|is_pinned|boolean,null|false|none||是否置顶, `false` 表示取消置顶|

#### 枚举值

|属性|值|
|---|---|
|message_scene|friend|
|message_scene|group|
|message_scene|temp|

<h2 id="tocS_SetAvatarInput">SetAvatarInput</h2>

<a id="schemasetavatarinput"></a>
<a id="schema_SetAvatarInput"></a>
<a id="tocSsetavatarinput"></a>
<a id="tocssetavatarinput"></a>

```json
{
  "uri": "string"
}

```

set_avatar 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|uri|string|true|none||头像文件 URI，支持 `file://` `http(s)://` `base64://` 三种格式|

<h2 id="tocS_SetNicknameInput">SetNicknameInput</h2>

<a id="schemasetnicknameinput"></a>
<a id="schema_SetNicknameInput"></a>
<a id="tocSsetnicknameinput"></a>
<a id="tocssetnicknameinput"></a>

```json
{
  "new_nickname": "string"
}

```

set_nickname 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|new_nickname|string|true|none||新昵称|

<h2 id="tocS_SetBioInput">SetBioInput</h2>

<a id="schemasetbioinput"></a>
<a id="schema_SetBioInput"></a>
<a id="tocSsetbioinput"></a>
<a id="tocssetbioinput"></a>

```json
{
  "new_bio": "string"
}

```

set_bio 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|new_bio|string|true|none||新个性签名|

<h2 id="tocS_GetCustomFaceUrlListOutput">GetCustomFaceUrlListOutput</h2>

<a id="schemagetcustomfaceurllistoutput"></a>
<a id="schema_GetCustomFaceUrlListOutput"></a>
<a id="tocSgetcustomfaceurllistoutput"></a>
<a id="tocsgetcustomfaceurllistoutput"></a>

```json
{
  "urls": [
    "string"
  ]
}

```

get_custom_face_url_list 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|urls|[string]|true|none||自定义表情 URL 列表|

<h2 id="tocS_GetCookiesInput">GetCookiesInput</h2>

<a id="schemagetcookiesinput"></a>
<a id="schema_GetCookiesInput"></a>
<a id="tocSgetcookiesinput"></a>
<a id="tocsgetcookiesinput"></a>

```json
{
  "domain": "string"
}

```

get_cookies 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|domain|string|true|none||需要获取 Cookies 的域名|

<h2 id="tocS_GetCookiesOutput">GetCookiesOutput</h2>

<a id="schemagetcookiesoutput"></a>
<a id="schema_GetCookiesOutput"></a>
<a id="tocSgetcookiesoutput"></a>
<a id="tocsgetcookiesoutput"></a>

```json
{
  "cookies": "string"
}

```

get_cookies 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|cookies|string|true|none||域名对应的 Cookies 字符串|

<h2 id="tocS_GetCSRFTokenOutput">GetCSRFTokenOutput</h2>

<a id="schemagetcsrftokenoutput"></a>
<a id="schema_GetCSRFTokenOutput"></a>
<a id="tocSgetcsrftokenoutput"></a>
<a id="tocsgetcsrftokenoutput"></a>

```json
{
  "csrf_token": "string"
}

```

get_csrf_token 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|csrf_token|string|true|none||CSRF Token|

<h2 id="tocS_SendPrivateMessageInput">SendPrivateMessageInput</h2>

<a id="schemasendprivatemessageinput"></a>
<a id="schema_SendPrivateMessageInput"></a>
<a id="tocSsendprivatemessageinput"></a>
<a id="tocssendprivatemessageinput"></a>

```json
{
  "user_id": 10001,
  "message": [
    {
      "type": "[",
      "data": {}
    }
  ]
}

```

send_private_message 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||好友 QQ 号|
|message|[allOf]|true|none||消息内容|

<h2 id="tocS_SendPrivateMessageOutput">SendPrivateMessageOutput</h2>

<a id="schemasendprivatemessageoutput"></a>
<a id="schema_SendPrivateMessageOutput"></a>
<a id="tocSsendprivatemessageoutput"></a>
<a id="tocssendprivatemessageoutput"></a>

```json
{
  "message_seq": 9007199254740991,
  "time": 9007199254740991
}

```

send_private_message 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|message_seq|integer|true|none||消息序列号|
|time|integer|true|none||消息发送时间|

<h2 id="tocS_SendGroupMessageInput">SendGroupMessageInput</h2>

<a id="schemasendgroupmessageinput"></a>
<a id="schema_SendGroupMessageInput"></a>
<a id="tocSsendgroupmessageinput"></a>
<a id="tocssendgroupmessageinput"></a>

```json
{
  "group_id": 10001,
  "message": [
    {
      "type": "[",
      "data": {}
    }
  ]
}

```

send_group_message 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|message|[allOf]|true|none||消息内容|

<h2 id="tocS_SendGroupMessageOutput">SendGroupMessageOutput</h2>

<a id="schemasendgroupmessageoutput"></a>
<a id="schema_SendGroupMessageOutput"></a>
<a id="tocSsendgroupmessageoutput"></a>
<a id="tocssendgroupmessageoutput"></a>

```json
{
  "message_seq": 9007199254740991,
  "time": 9007199254740991
}

```

send_group_message 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|message_seq|integer|true|none||消息序列号|
|time|integer|true|none||消息发送时间|

<h2 id="tocS_RecallPrivateMessageInput">RecallPrivateMessageInput</h2>

<a id="schemarecallprivatemessageinput"></a>
<a id="schema_RecallPrivateMessageInput"></a>
<a id="tocSrecallprivatemessageinput"></a>
<a id="tocsrecallprivatemessageinput"></a>

```json
{
  "user_id": 10001,
  "message_seq": 9007199254740991
}

```

recall_private_message 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||好友 QQ 号|
|message_seq|integer|true|none||消息序列号|

<h2 id="tocS_RecallGroupMessageInput">RecallGroupMessageInput</h2>

<a id="schemarecallgroupmessageinput"></a>
<a id="schema_RecallGroupMessageInput"></a>
<a id="tocSrecallgroupmessageinput"></a>
<a id="tocsrecallgroupmessageinput"></a>

```json
{
  "group_id": 10001,
  "message_seq": 9007199254740991
}

```

recall_group_message 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|message_seq|integer|true|none||消息序列号|

<h2 id="tocS_GetMessageInput">GetMessageInput</h2>

<a id="schemagetmessageinput"></a>
<a id="schema_GetMessageInput"></a>
<a id="tocSgetmessageinput"></a>
<a id="tocsgetmessageinput"></a>

```json
{
  "message_scene": "friend",
  "peer_id": 10001,
  "message_seq": 9007199254740991
}

```

get_message 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|message_scene|string|true|none||消息场景|
|peer_id|integer|true|none||好友 QQ 号或群号|
|message_seq|integer|true|none||消息序列号|

#### 枚举值

|属性|值|
|---|---|
|message_scene|friend|
|message_scene|group|
|message_scene|temp|

<h2 id="tocS_GetMessageOutput">GetMessageOutput</h2>

<a id="schemagetmessageoutput"></a>
<a id="schema_GetMessageOutput"></a>
<a id="tocSgetmessageoutput"></a>
<a id="tocsgetmessageoutput"></a>

```json
{
  "message": {
    "message_scene": "friend",
    "peer_id": 10001,
    "message_seq": 9007199254740991,
    "sender_id": 10001,
    "time": 9007199254740991,
    "segments": [
      null
    ],
    "friend": null
  }
}

```

get_message 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|message|[IncomingMessage](#schemaincomingmessage)|true|none||消息内容|

<h2 id="tocS_GetHistoryMessagesInput">GetHistoryMessagesInput</h2>

<a id="schemagethistorymessagesinput"></a>
<a id="schema_GetHistoryMessagesInput"></a>
<a id="tocSgethistorymessagesinput"></a>
<a id="tocsgethistorymessagesinput"></a>

```json
{
  "message_scene": "friend",
  "peer_id": 10001,
  "start_message_seq": 9007199254740991,
  "limit": 20
}

```

get_history_messages 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|message_scene|string|true|none||消息场景|
|peer_id|integer|true|none||好友 QQ 号或群号|
|start_message_seq|integer,null|false|none||起始消息序列号，由此开始从新到旧查询，不提供则从最新消息开始|
|limit|integer,null|false|none||期望获取到的消息数量，最多 30 条|

#### 枚举值

|属性|值|
|---|---|
|message_scene|friend|
|message_scene|group|
|message_scene|temp|

<h2 id="tocS_GetHistoryMessagesOutput">GetHistoryMessagesOutput</h2>

<a id="schemagethistorymessagesoutput"></a>
<a id="schema_GetHistoryMessagesOutput"></a>
<a id="tocSgethistorymessagesoutput"></a>
<a id="tocsgethistorymessagesoutput"></a>

```json
{
  "messages": [
    {
      "message_scene": "[",
      "peer_id": 10001,
      "message_seq": 9007199254740991,
      "sender_id": 10001,
      "time": 9007199254740991,
      "segments": [
        null
      ],
      "friend": null
    }
  ],
  "next_message_seq": 9007199254740991
}

```

get_history_messages 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|messages|[allOf]|true|none||获取到的消息（message_seq 升序排列），部分消息可能不存在，如撤回的消息|
|next_message_seq|integer,null|false|none||下一页起始消息序列号|

<h2 id="tocS_GetResourceTempUrlInput">GetResourceTempUrlInput</h2>

<a id="schemagetresourcetempurlinput"></a>
<a id="schema_GetResourceTempUrlInput"></a>
<a id="tocSgetresourcetempurlinput"></a>
<a id="tocsgetresourcetempurlinput"></a>

```json
{
  "resource_id": "string"
}

```

get_resource_temp_url 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|resource_id|string|true|none||资源 ID|

<h2 id="tocS_GetResourceTempUrlOutput">GetResourceTempUrlOutput</h2>

<a id="schemagetresourcetempurloutput"></a>
<a id="schema_GetResourceTempUrlOutput"></a>
<a id="tocSgetresourcetempurloutput"></a>
<a id="tocsgetresourcetempurloutput"></a>

```json
{
  "url": "string"
}

```

get_resource_temp_url 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|url|string|true|none||临时资源链接|

<h2 id="tocS_GetForwardedMessagesInput">GetForwardedMessagesInput</h2>

<a id="schemagetforwardedmessagesinput"></a>
<a id="schema_GetForwardedMessagesInput"></a>
<a id="tocSgetforwardedmessagesinput"></a>
<a id="tocsgetforwardedmessagesinput"></a>

```json
{
  "forward_id": "string"
}

```

get_forwarded_messages 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|forward_id|string|true|none||转发消息 ID|

<h2 id="tocS_GetForwardedMessagesOutput">GetForwardedMessagesOutput</h2>

<a id="schemagetforwardedmessagesoutput"></a>
<a id="schema_GetForwardedMessagesOutput"></a>
<a id="tocSgetforwardedmessagesoutput"></a>
<a id="tocsgetforwardedmessagesoutput"></a>

```json
{
  "messages": [
    {
      "message_seq": 9007199254740991,
      "sender_name": "string",
      "avatar_url": "string",
      "time": 9007199254740991,
      "segments": [
        null
      ]
    }
  ]
}

```

get_forwarded_messages 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|messages|[allOf]|true|none||转发消息内容|

<h2 id="tocS_MarkMessageAsReadInput">MarkMessageAsReadInput</h2>

<a id="schemamarkmessageasreadinput"></a>
<a id="schema_MarkMessageAsReadInput"></a>
<a id="tocSmarkmessageasreadinput"></a>
<a id="tocsmarkmessageasreadinput"></a>

```json
{
  "message_scene": "friend",
  "peer_id": 10001,
  "message_seq": 9007199254740991
}

```

mark_message_as_read 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|message_scene|string|true|none||消息场景|
|peer_id|integer|true|none||好友 QQ 号或群号|
|message_seq|integer|true|none||标为已读的消息序列号，该消息及更早的消息将被标记为已读|

#### 枚举值

|属性|值|
|---|---|
|message_scene|friend|
|message_scene|group|
|message_scene|temp|

<h2 id="tocS_SendFriendNudgeInput">SendFriendNudgeInput</h2>

<a id="schemasendfriendnudgeinput"></a>
<a id="schema_SendFriendNudgeInput"></a>
<a id="tocSsendfriendnudgeinput"></a>
<a id="tocssendfriendnudgeinput"></a>

```json
{
  "user_id": 10001,
  "is_self": false
}

```

send_friend_nudge 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||好友 QQ 号|
|is_self|boolean,null|false|none||是否戳自己|

<h2 id="tocS_SendProfileLikeInput">SendProfileLikeInput</h2>

<a id="schemasendprofilelikeinput"></a>
<a id="schema_SendProfileLikeInput"></a>
<a id="tocSsendprofilelikeinput"></a>
<a id="tocssendprofilelikeinput"></a>

```json
{
  "user_id": 10001,
  "count": 1
}

```

send_profile_like 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||好友 QQ 号|
|count|integer,null|false|none||点赞数量|

<h2 id="tocS_DeleteFriendInput">DeleteFriendInput</h2>

<a id="schemadeletefriendinput"></a>
<a id="schema_DeleteFriendInput"></a>
<a id="tocSdeletefriendinput"></a>
<a id="tocsdeletefriendinput"></a>

```json
{
  "user_id": 10001
}

```

delete_friend 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||好友 QQ 号|

<h2 id="tocS_GetFriendRequestsInput">GetFriendRequestsInput</h2>

<a id="schemagetfriendrequestsinput"></a>
<a id="schema_GetFriendRequestsInput"></a>
<a id="tocSgetfriendrequestsinput"></a>
<a id="tocsgetfriendrequestsinput"></a>

```json
{
  "limit": 20,
  "is_filtered": false
}

```

get_friend_requests 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|limit|integer,null|false|none||获取的最大请求数量|
|is_filtered|boolean,null|false|none||`true` 表示只获取被过滤（由风险账号发起）的通知，`false` 表示只获取未被过滤的通知|

<h2 id="tocS_GetFriendRequestsOutput">GetFriendRequestsOutput</h2>

<a id="schemagetfriendrequestsoutput"></a>
<a id="schema_GetFriendRequestsOutput"></a>
<a id="tocSgetfriendrequestsoutput"></a>
<a id="tocsgetfriendrequestsoutput"></a>

```json
{
  "requests": [
    {
      "time": 9007199254740991,
      "initiator_id": 10001,
      "initiator_uid": "string",
      "target_user_id": 10001,
      "target_user_uid": "string",
      "state": "pending",
      "comment": "string",
      "via": "string",
      "is_filtered": true
    }
  ]
}

```

get_friend_requests 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|requests|[allOf]|true|none||好友请求列表|

<h2 id="tocS_AcceptFriendRequestInput">AcceptFriendRequestInput</h2>

<a id="schemaacceptfriendrequestinput"></a>
<a id="schema_AcceptFriendRequestInput"></a>
<a id="tocSacceptfriendrequestinput"></a>
<a id="tocsacceptfriendrequestinput"></a>

```json
{
  "initiator_uid": "string",
  "is_filtered": false
}

```

accept_friend_request 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|initiator_uid|string|true|none||请求发起者 UID|
|is_filtered|boolean,null|false|none||是否是被过滤的请求|

<h2 id="tocS_RejectFriendRequestInput">RejectFriendRequestInput</h2>

<a id="schemarejectfriendrequestinput"></a>
<a id="schema_RejectFriendRequestInput"></a>
<a id="tocSrejectfriendrequestinput"></a>
<a id="tocsrejectfriendrequestinput"></a>

```json
{
  "initiator_uid": "string",
  "is_filtered": false,
  "reason": "string"
}

```

reject_friend_request 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|initiator_uid|string|true|none||请求发起者 UID|
|is_filtered|boolean,null|false|none||是否是被过滤的请求|
|reason|string,null|false|none||拒绝理由|

<h2 id="tocS_SetGroupNameInput">SetGroupNameInput</h2>

<a id="schemasetgroupnameinput"></a>
<a id="schema_SetGroupNameInput"></a>
<a id="tocSsetgroupnameinput"></a>
<a id="tocssetgroupnameinput"></a>

```json
{
  "group_id": 10001,
  "new_group_name": "string"
}

```

set_group_name 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|new_group_name|string|true|none||新群名称|

<h2 id="tocS_SetGroupAvatarInput">SetGroupAvatarInput</h2>

<a id="schemasetgroupavatarinput"></a>
<a id="schema_SetGroupAvatarInput"></a>
<a id="tocSsetgroupavatarinput"></a>
<a id="tocssetgroupavatarinput"></a>

```json
{
  "group_id": 10001,
  "image_uri": "string"
}

```

set_group_avatar 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|image_uri|string|true|none||头像文件 URI，支持 `file://` `http(s)://` `base64://` 三种格式|

<h2 id="tocS_SetGroupMemberCardInput">SetGroupMemberCardInput</h2>

<a id="schemasetgroupmembercardinput"></a>
<a id="schema_SetGroupMemberCardInput"></a>
<a id="tocSsetgroupmembercardinput"></a>
<a id="tocssetgroupmembercardinput"></a>

```json
{
  "group_id": 10001,
  "user_id": 10001,
  "card": "string"
}

```

set_group_member_card 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||被设置的群成员 QQ 号|
|card|string|true|none||新群名片|

<h2 id="tocS_SetGroupMemberSpecialTitleInput">SetGroupMemberSpecialTitleInput</h2>

<a id="schemasetgroupmemberspecialtitleinput"></a>
<a id="schema_SetGroupMemberSpecialTitleInput"></a>
<a id="tocSsetgroupmemberspecialtitleinput"></a>
<a id="tocssetgroupmemberspecialtitleinput"></a>

```json
{
  "group_id": 10001,
  "user_id": 10001,
  "special_title": "string"
}

```

set_group_member_special_title 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||被设置的群成员 QQ 号|
|special_title|string|true|none||新专属头衔|

<h2 id="tocS_SetGroupMemberAdminInput">SetGroupMemberAdminInput</h2>

<a id="schemasetgroupmemberadmininput"></a>
<a id="schema_SetGroupMemberAdminInput"></a>
<a id="tocSsetgroupmemberadmininput"></a>
<a id="tocssetgroupmemberadmininput"></a>

```json
{
  "group_id": 10001,
  "user_id": 10001,
  "is_set": true
}

```

set_group_member_admin 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||被设置的 QQ 号|
|is_set|boolean,null|false|none||是否设置为管理员，`false` 表示取消管理员|

<h2 id="tocS_SetGroupMemberMuteInput">SetGroupMemberMuteInput</h2>

<a id="schemasetgroupmembermuteinput"></a>
<a id="schema_SetGroupMemberMuteInput"></a>
<a id="tocSsetgroupmembermuteinput"></a>
<a id="tocssetgroupmembermuteinput"></a>

```json
{
  "group_id": 10001,
  "user_id": 10001,
  "duration": 0
}

```

set_group_member_mute 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||被设置的 QQ 号|
|duration|integer,null|false|none||禁言持续时间（秒），设为 `0` 为取消禁言|

<h2 id="tocS_SetGroupWholeMuteInput">SetGroupWholeMuteInput</h2>

<a id="schemasetgroupwholemuteinput"></a>
<a id="schema_SetGroupWholeMuteInput"></a>
<a id="tocSsetgroupwholemuteinput"></a>
<a id="tocssetgroupwholemuteinput"></a>

```json
{
  "group_id": 10001,
  "is_mute": true
}

```

set_group_whole_mute 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|is_mute|boolean,null|false|none||是否开启全员禁言，`false` 表示取消全员禁言|

<h2 id="tocS_KickGroupMemberInput">KickGroupMemberInput</h2>

<a id="schemakickgroupmemberinput"></a>
<a id="schema_KickGroupMemberInput"></a>
<a id="tocSkickgroupmemberinput"></a>
<a id="tocskickgroupmemberinput"></a>

```json
{
  "group_id": 10001,
  "user_id": 10001,
  "reject_add_request": false
}

```

kick_group_member 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||被踢的 QQ 号|
|reject_add_request|boolean,null|false|none||是否拒绝加群申请，`false` 表示不拒绝|

<h2 id="tocS_GetGroupAnnouncementsInput">GetGroupAnnouncementsInput</h2>

<a id="schemagetgroupannouncementsinput"></a>
<a id="schema_GetGroupAnnouncementsInput"></a>
<a id="tocSgetgroupannouncementsinput"></a>
<a id="tocsgetgroupannouncementsinput"></a>

```json
{
  "group_id": 10001
}

```

get_group_announcements 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|

<h2 id="tocS_GetGroupAnnouncementsOutput">GetGroupAnnouncementsOutput</h2>

<a id="schemagetgroupannouncementsoutput"></a>
<a id="schema_GetGroupAnnouncementsOutput"></a>
<a id="tocSgetgroupannouncementsoutput"></a>
<a id="tocsgetgroupannouncementsoutput"></a>

```json
{
  "announcements": [
    {
      "group_id": 10001,
      "announcement_id": "string",
      "user_id": 10001,
      "time": 9007199254740991,
      "content": "string",
      "image_url": "string"
    }
  ]
}

```

get_group_announcements 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|announcements|[allOf]|true|none||群公告列表|

<h2 id="tocS_SendGroupAnnouncementInput">SendGroupAnnouncementInput</h2>

<a id="schemasendgroupannouncementinput"></a>
<a id="schema_SendGroupAnnouncementInput"></a>
<a id="tocSsendgroupannouncementinput"></a>
<a id="tocssendgroupannouncementinput"></a>

```json
{
  "group_id": 10001,
  "content": "string",
  "image_uri": "string"
}

```

send_group_announcement 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|content|string|true|none||公告内容|
|image_uri|string,null|false|none||公告附带图像文件 URI，支持 `file://` `http(s)://` `base64://` 三种格式|

<h2 id="tocS_DeleteGroupAnnouncementInput">DeleteGroupAnnouncementInput</h2>

<a id="schemadeletegroupannouncementinput"></a>
<a id="schema_DeleteGroupAnnouncementInput"></a>
<a id="tocSdeletegroupannouncementinput"></a>
<a id="tocsdeletegroupannouncementinput"></a>

```json
{
  "group_id": 10001,
  "announcement_id": "string"
}

```

delete_group_announcement 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|announcement_id|string|true|none||公告 ID|

<h2 id="tocS_GetGroupEssenceMessagesInput">GetGroupEssenceMessagesInput</h2>

<a id="schemagetgroupessencemessagesinput"></a>
<a id="schema_GetGroupEssenceMessagesInput"></a>
<a id="tocSgetgroupessencemessagesinput"></a>
<a id="tocsgetgroupessencemessagesinput"></a>

```json
{
  "group_id": 10001,
  "page_index": 9007199254740991,
  "page_size": 9007199254740991
}

```

get_group_essence_messages 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|page_index|integer|true|none||页码索引，从 0 开始|
|page_size|integer|true|none||每页包含的精华消息数量|

<h2 id="tocS_GetGroupEssenceMessagesOutput">GetGroupEssenceMessagesOutput</h2>

<a id="schemagetgroupessencemessagesoutput"></a>
<a id="schema_GetGroupEssenceMessagesOutput"></a>
<a id="tocSgetgroupessencemessagesoutput"></a>
<a id="tocsgetgroupessencemessagesoutput"></a>

```json
{
  "messages": [
    {
      "group_id": 10001,
      "message_seq": 9007199254740991,
      "message_time": 9007199254740991,
      "sender_id": 10001,
      "sender_name": "string",
      "operator_id": 10001,
      "operator_name": "string",
      "operation_time": 9007199254740991,
      "segments": [
        null
      ]
    }
  ],
  "is_end": true
}

```

get_group_essence_messages 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|messages|[allOf]|true|none||精华消息列表|
|is_end|boolean|true|none||是否已到最后一页|

<h2 id="tocS_SetGroupEssenceMessageInput">SetGroupEssenceMessageInput</h2>

<a id="schemasetgroupessencemessageinput"></a>
<a id="schema_SetGroupEssenceMessageInput"></a>
<a id="tocSsetgroupessencemessageinput"></a>
<a id="tocssetgroupessencemessageinput"></a>

```json
{
  "group_id": 10001,
  "message_seq": 9007199254740991,
  "is_set": true
}

```

set_group_essence_message 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|message_seq|integer|true|none||消息序列号|
|is_set|boolean,null|false|none||是否设置为精华消息，`false` 表示取消精华|

<h2 id="tocS_QuitGroupInput">QuitGroupInput</h2>

<a id="schemaquitgroupinput"></a>
<a id="schema_QuitGroupInput"></a>
<a id="tocSquitgroupinput"></a>
<a id="tocsquitgroupinput"></a>

```json
{
  "group_id": 10001
}

```

quit_group 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|

<h2 id="tocS_SendGroupMessageReactionInput">SendGroupMessageReactionInput</h2>

<a id="schemasendgroupmessagereactioninput"></a>
<a id="schema_SendGroupMessageReactionInput"></a>
<a id="tocSsendgroupmessagereactioninput"></a>
<a id="tocssendgroupmessagereactioninput"></a>

```json
{
  "group_id": 10001,
  "message_seq": 9007199254740991,
  "reaction": "string",
  "reaction_type": "face",
  "is_add": true
}

```

send_group_message_reaction 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|message_seq|integer|true|none||要回应的消息序列号|
|reaction|string|true|none||发送的回应的表情 ID|
|reaction_type|string,null|false|none||发送的回应类型|
|is_add|boolean,null|false|none||是否添加表情，`false` 表示取消|

#### 枚举值

|属性|值|
|---|---|
|reaction_type|face|
|reaction_type|emoji|

<h2 id="tocS_SendGroupNudgeInput">SendGroupNudgeInput</h2>

<a id="schemasendgroupnudgeinput"></a>
<a id="schema_SendGroupNudgeInput"></a>
<a id="tocSsendgroupnudgeinput"></a>
<a id="tocssendgroupnudgeinput"></a>

```json
{
  "group_id": 10001,
  "user_id": 10001
}

```

send_group_nudge 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||被戳的群成员 QQ 号|

<h2 id="tocS_GetGroupNotificationsInput">GetGroupNotificationsInput</h2>

<a id="schemagetgroupnotificationsinput"></a>
<a id="schema_GetGroupNotificationsInput"></a>
<a id="tocSgetgroupnotificationsinput"></a>
<a id="tocsgetgroupnotificationsinput"></a>

```json
{
  "start_notification_seq": 9007199254740991,
  "is_filtered": false,
  "limit": 20
}

```

get_group_notifications 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|start_notification_seq|integer,null|false|none||起始通知序列号|
|is_filtered|boolean,null|false|none||`true` 表示只获取被过滤（由风险账号发起）的通知，`false` 表示只获取未被过滤的通知|
|limit|integer,null|false|none||获取的最大通知数量|

<h2 id="tocS_GetGroupNotificationsOutput">GetGroupNotificationsOutput</h2>

<a id="schemagetgroupnotificationsoutput"></a>
<a id="schema_GetGroupNotificationsOutput"></a>
<a id="tocSgetgroupnotificationsoutput"></a>
<a id="tocsgetgroupnotificationsoutput"></a>

```json
{
  "notifications": [
    null
  ],
  "next_notification_seq": 9007199254740991
}

```

get_group_notifications 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|notifications|[allOf]|true|none||获取到的群通知（notification_seq 降序排列），序列号不一定连续|
|next_notification_seq|integer,null|false|none||下一页起始通知序列号|

<h2 id="tocS_AcceptGroupRequestInput">AcceptGroupRequestInput</h2>

<a id="schemaacceptgrouprequestinput"></a>
<a id="schema_AcceptGroupRequestInput"></a>
<a id="tocSacceptgrouprequestinput"></a>
<a id="tocsacceptgrouprequestinput"></a>

```json
{
  "notification_seq": 9007199254740991,
  "notification_type": "join_request",
  "group_id": 10001,
  "is_filtered": false
}

```

accept_group_request 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|notification_seq|integer|true|none||请求对应的通知序列号|
|notification_type|string|true|none||请求对应的通知类型|
|group_id|integer|true|none||请求所在的群号|
|is_filtered|boolean,null|false|none||是否是被过滤的请求|

#### 枚举值

|属性|值|
|---|---|
|notification_type|join_request|
|notification_type|invited_join_request|

<h2 id="tocS_RejectGroupRequestInput">RejectGroupRequestInput</h2>

<a id="schemarejectgrouprequestinput"></a>
<a id="schema_RejectGroupRequestInput"></a>
<a id="tocSrejectgrouprequestinput"></a>
<a id="tocsrejectgrouprequestinput"></a>

```json
{
  "notification_seq": 9007199254740991,
  "notification_type": "join_request",
  "group_id": 10001,
  "is_filtered": false,
  "reason": "string"
}

```

reject_group_request 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|notification_seq|integer|true|none||请求对应的通知序列号|
|notification_type|string|true|none||请求对应的通知类型|
|group_id|integer|true|none||请求所在的群号|
|is_filtered|boolean,null|false|none||是否是被过滤的请求|
|reason|string,null|false|none||拒绝理由|

#### 枚举值

|属性|值|
|---|---|
|notification_type|join_request|
|notification_type|invited_join_request|

<h2 id="tocS_AcceptGroupInvitationInput">AcceptGroupInvitationInput</h2>

<a id="schemaacceptgroupinvitationinput"></a>
<a id="schema_AcceptGroupInvitationInput"></a>
<a id="tocSacceptgroupinvitationinput"></a>
<a id="tocsacceptgroupinvitationinput"></a>

```json
{
  "group_id": 10001,
  "invitation_seq": 9007199254740991
}

```

accept_group_invitation 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|invitation_seq|integer|true|none||邀请序列号|

<h2 id="tocS_RejectGroupInvitationInput">RejectGroupInvitationInput</h2>

<a id="schemarejectgroupinvitationinput"></a>
<a id="schema_RejectGroupInvitationInput"></a>
<a id="tocSrejectgroupinvitationinput"></a>
<a id="tocsrejectgroupinvitationinput"></a>

```json
{
  "group_id": 10001,
  "invitation_seq": 9007199254740991
}

```

reject_group_invitation 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|invitation_seq|integer|true|none||邀请序列号|

<h2 id="tocS_UploadPrivateFileInput">UploadPrivateFileInput</h2>

<a id="schemauploadprivatefileinput"></a>
<a id="schema_UploadPrivateFileInput"></a>
<a id="tocSuploadprivatefileinput"></a>
<a id="tocsuploadprivatefileinput"></a>

```json
{
  "user_id": 10001,
  "file_uri": "string",
  "file_name": "string"
}

```

upload_private_file 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||好友 QQ 号|
|file_uri|string|true|none||文件 URI，支持 `file://` `http(s)://` `base64://` 三种格式|
|file_name|string|true|none||文件名称|

<h2 id="tocS_UploadPrivateFileOutput">UploadPrivateFileOutput</h2>

<a id="schemauploadprivatefileoutput"></a>
<a id="schema_UploadPrivateFileOutput"></a>
<a id="tocSuploadprivatefileoutput"></a>
<a id="tocsuploadprivatefileoutput"></a>

```json
{
  "file_id": "string"
}

```

upload_private_file 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|file_id|string|true|none||文件 ID|

<h2 id="tocS_UploadGroupFileInput">UploadGroupFileInput</h2>

<a id="schemauploadgroupfileinput"></a>
<a id="schema_UploadGroupFileInput"></a>
<a id="tocSuploadgroupfileinput"></a>
<a id="tocsuploadgroupfileinput"></a>

```json
{
  "group_id": 10001,
  "parent_folder_id": "/",
  "file_uri": "string",
  "file_name": "string"
}

```

upload_group_file 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|parent_folder_id|string,null|false|none||目标文件夹 ID|
|file_uri|string|true|none||文件 URI，支持 `file://` `http(s)://` `base64://` 三种格式|
|file_name|string|true|none||文件名称|

<h2 id="tocS_UploadGroupFileOutput">UploadGroupFileOutput</h2>

<a id="schemauploadgroupfileoutput"></a>
<a id="schema_UploadGroupFileOutput"></a>
<a id="tocSuploadgroupfileoutput"></a>
<a id="tocsuploadgroupfileoutput"></a>

```json
{
  "file_id": "string"
}

```

upload_group_file 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|file_id|string|true|none||文件 ID|

<h2 id="tocS_GetPrivateFileDownloadUrlInput">GetPrivateFileDownloadUrlInput</h2>

<a id="schemagetprivatefiledownloadurlinput"></a>
<a id="schema_GetPrivateFileDownloadUrlInput"></a>
<a id="tocSgetprivatefiledownloadurlinput"></a>
<a id="tocsgetprivatefiledownloadurlinput"></a>

```json
{
  "user_id": 10001,
  "file_id": "string",
  "file_hash": "string"
}

```

get_private_file_download_url 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||好友 QQ 号|
|file_id|string|true|none||文件 ID|
|file_hash|string|true|none||文件的 TriSHA1 哈希值|

<h2 id="tocS_GetPrivateFileDownloadUrlOutput">GetPrivateFileDownloadUrlOutput</h2>

<a id="schemagetprivatefiledownloadurloutput"></a>
<a id="schema_GetPrivateFileDownloadUrlOutput"></a>
<a id="tocSgetprivatefiledownloadurloutput"></a>
<a id="tocsgetprivatefiledownloadurloutput"></a>

```json
{
  "download_url": "string"
}

```

get_private_file_download_url 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|download_url|string|true|none||文件下载链接|

<h2 id="tocS_GetGroupFileDownloadUrlInput">GetGroupFileDownloadUrlInput</h2>

<a id="schemagetgroupfiledownloadurlinput"></a>
<a id="schema_GetGroupFileDownloadUrlInput"></a>
<a id="tocSgetgroupfiledownloadurlinput"></a>
<a id="tocsgetgroupfiledownloadurlinput"></a>

```json
{
  "group_id": 10001,
  "file_id": "string"
}

```

get_group_file_download_url 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|file_id|string|true|none||文件 ID|

<h2 id="tocS_GetGroupFileDownloadUrlOutput">GetGroupFileDownloadUrlOutput</h2>

<a id="schemagetgroupfiledownloadurloutput"></a>
<a id="schema_GetGroupFileDownloadUrlOutput"></a>
<a id="tocSgetgroupfiledownloadurloutput"></a>
<a id="tocsgetgroupfiledownloadurloutput"></a>

```json
{
  "download_url": "string"
}

```

get_group_file_download_url 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|download_url|string|true|none||文件下载链接|

<h2 id="tocS_GetGroupFilesInput">GetGroupFilesInput</h2>

<a id="schemagetgroupfilesinput"></a>
<a id="schema_GetGroupFilesInput"></a>
<a id="tocSgetgroupfilesinput"></a>
<a id="tocsgetgroupfilesinput"></a>

```json
{
  "group_id": 10001,
  "parent_folder_id": "/"
}

```

get_group_files 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|parent_folder_id|string,null|false|none||父文件夹 ID|

<h2 id="tocS_GetGroupFilesOutput">GetGroupFilesOutput</h2>

<a id="schemagetgroupfilesoutput"></a>
<a id="schema_GetGroupFilesOutput"></a>
<a id="tocSgetgroupfilesoutput"></a>
<a id="tocsgetgroupfilesoutput"></a>

```json
{
  "files": [
    {
      "group_id": 10001,
      "file_id": "string",
      "file_name": "string",
      "parent_folder_id": "string",
      "file_size": 9007199254740991,
      "uploaded_time": 9007199254740991,
      "expire_time": 9007199254740991,
      "uploader_id": 10001,
      "downloaded_times": 9007199254740991
    }
  ],
  "folders": [
    {
      "group_id": 10001,
      "folder_id": "string",
      "parent_folder_id": "string",
      "folder_name": "string",
      "created_time": 9007199254740991,
      "last_modified_time": 9007199254740991,
      "creator_id": 10001,
      "file_count": 9007199254740991
    }
  ]
}

```

get_group_files 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|files|[allOf]|true|none||文件列表|
|folders|[allOf]|true|none||文件夹列表|

<h2 id="tocS_MoveGroupFileInput">MoveGroupFileInput</h2>

<a id="schemamovegroupfileinput"></a>
<a id="schema_MoveGroupFileInput"></a>
<a id="tocSmovegroupfileinput"></a>
<a id="tocsmovegroupfileinput"></a>

```json
{
  "group_id": 10001,
  "file_id": "string",
  "parent_folder_id": "/",
  "target_folder_id": "/"
}

```

move_group_file 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|file_id|string|true|none||文件 ID|
|parent_folder_id|string,null|false|none||文件所在的文件夹 ID|
|target_folder_id|string,null|false|none||目标文件夹 ID|

<h2 id="tocS_RenameGroupFileInput">RenameGroupFileInput</h2>

<a id="schemarenamegroupfileinput"></a>
<a id="schema_RenameGroupFileInput"></a>
<a id="tocSrenamegroupfileinput"></a>
<a id="tocsrenamegroupfileinput"></a>

```json
{
  "group_id": 10001,
  "file_id": "string",
  "parent_folder_id": "/",
  "new_file_name": "string"
}

```

rename_group_file 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|file_id|string|true|none||文件 ID|
|parent_folder_id|string,null|false|none||文件所在的文件夹 ID|
|new_file_name|string|true|none||新文件名称|

<h2 id="tocS_DeleteGroupFileInput">DeleteGroupFileInput</h2>

<a id="schemadeletegroupfileinput"></a>
<a id="schema_DeleteGroupFileInput"></a>
<a id="tocSdeletegroupfileinput"></a>
<a id="tocsdeletegroupfileinput"></a>

```json
{
  "group_id": 10001,
  "file_id": "string"
}

```

delete_group_file 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|file_id|string|true|none||文件 ID|

<h2 id="tocS_CreateGroupFolderInput">CreateGroupFolderInput</h2>

<a id="schemacreategroupfolderinput"></a>
<a id="schema_CreateGroupFolderInput"></a>
<a id="tocScreategroupfolderinput"></a>
<a id="tocscreategroupfolderinput"></a>

```json
{
  "group_id": 10001,
  "folder_name": "string"
}

```

create_group_folder 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|folder_name|string|true|none||文件夹名称|

<h2 id="tocS_CreateGroupFolderOutput">CreateGroupFolderOutput</h2>

<a id="schemacreategroupfolderoutput"></a>
<a id="schema_CreateGroupFolderOutput"></a>
<a id="tocScreategroupfolderoutput"></a>
<a id="tocscreategroupfolderoutput"></a>

```json
{
  "folder_id": "string"
}

```

create_group_folder 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|folder_id|string|true|none||文件夹 ID|

<h2 id="tocS_RenameGroupFolderInput">RenameGroupFolderInput</h2>

<a id="schemarenamegroupfolderinput"></a>
<a id="schema_RenameGroupFolderInput"></a>
<a id="tocSrenamegroupfolderinput"></a>
<a id="tocsrenamegroupfolderinput"></a>

```json
{
  "group_id": 10001,
  "folder_id": "string",
  "new_folder_name": "string"
}

```

rename_group_folder 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|folder_id|string|true|none||文件夹 ID|
|new_folder_name|string|true|none||新文件夹名|

<h2 id="tocS_DeleteGroupFolderInput">DeleteGroupFolderInput</h2>

<a id="schemadeletegroupfolderinput"></a>
<a id="schema_DeleteGroupFolderInput"></a>
<a id="tocSdeletegroupfolderinput"></a>
<a id="tocsdeletegroupfolderinput"></a>

```json
{
  "group_id": 10001,
  "folder_id": "string"
}

```

delete_group_folder 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|folder_id|string|true|none||文件夹 ID|

