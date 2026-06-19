---
title: 默认模块
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

目前包括四种通信方式：

- **HTTP**：OneBot 作为 HTTP 服务端，提供 API 调用服务
- **HTTP POST**：OneBot 作为 HTTP 客户端，向用户配置的 URL 推送事件，并处理用户返回的响应
- **正向 WebSocket**：OneBot 作为 WebSocket 服务端，接受用户连接，提供 API 调用和事件推送服务
- **反向 WebSocket**：OneBot 作为 WebSocket 客户端，主动连接用户配置的 URL，提供 API 调用和事件推送服务

所有通信方式传输的数据都使用 UTF-8 编码。

# 默认模块

Base URLs:

* <a href="http://127.0.0.1:3000">开发环境: http://127.0.0.1:3000</a>

# Authentication

- HTTP Authentication, scheme: bearer

# OneBot 11/接口列表/用户

## POST 点赞

POST /send_like

> Body 请求参数

```json
{
  "user_id": 0,
  "times": 1
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» user_id|body|integer| 是 |对方 QQ 号|
|» times|body|integer| 否 |赞的次数|

> 返回示例

```json
{
    "status": "failed",
    "retcode": 200,
    "data": null,
    "message": "点赞失败 今日同一好友点赞数已达 SVIP 上限",
    "wording": "点赞失败 今日同一好友点赞数已达 SVIP 上限",
    "echo": null
}
```

```json
{
    "status": "ok",
    "retcode": 0,
    "data": null,
    "message": "",
    "wording": "",
    "echo": null
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|null|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 好友列表

POST /get_friend_list

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": [
    {
      "user_id": 0,
      "nickname": "string",
      "remark": "string",
      "sex": "string",
      "birthday_year": 0,
      "birthday_month": 0,
      "birthday_day": 0,
      "age": 0,
      "qid": "string",
      "long_nick": "string"
    }
  ],
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|[object]|true|none||none|
|»» user_id|integer|true|none||QQ 号|
|»» nickname|string|true|none||昵称|
|»» remark|string|true|none||备注名|
|»» sex|string|true|none||性别，male 或 female 或 unknown|
|»» birthday_year|integer|true|none||出生年份|
|»» birthday_month|integer|true|none||出生月份|
|»» birthday_day|integer|true|none||出生日|
|»» age|integer|true|none||年龄|
|»» qid|string|true|none||QID|
|»» long_nick|string|true|none||个性签名|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## GET 好友列表（带分组）

GET /get_friends_with_category

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": [
        {
            "categoryId": 13,
            "categorySortId": 0,
            "categoryName": "分组1",
            "categoryMbCount": 2,
            "onlineCount": 2,
            "buddyList": [
                {
                    "user_id": 2053541842,
                    "nickname": "林雨辰的猫猫",
                    "remark": "林雨辰的猫猫",
                    "sex": "unknown",
                    "birthday_year": 0,
                    "birthday_month": 0,
                    "birthday_day": 0,
                    "age": 0,
                    "qid": "",
                    "long_nick": "",
                    "level": 0,
                    "longNick": "",
                    "eMail": "",
                    "uid": "u_YLNHzMqI7HwqKEpwwzC4aA",
                    "categoryId": 13,
                    "richTime": 0
                }                
            ]
        }
    ],
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|[object]|true|none||none|
|»» categoryId|integer|true|none||none|
|»» categorySortId|integer|true|none||none|
|»» categoryName|string|true|none||none|
|»» categoryMbCount|integer|true|none||none|
|»» onlineCount|integer|true|none||none|
|»» buddyList|[object]|true|none||none|
|»»» user_id|integer|true|none||none|
|»»» nickname|string|true|none||none|
|»»» remark|string|true|none||none|
|»»» sex|string|true|none||none|
|»»» birthday_year|integer|true|none||none|
|»»» birthday_month|integer|true|none||none|
|»»» birthday_day|integer|true|none||none|
|»»» age|integer|true|none||none|
|»»» qid|string|true|none||none|
|»»» long_nick|string|true|none||none|
|»»» level|integer|true|none||none|
|»»» longNick|string|true|none||none|
|»»» eMail|string|true|none||none|
|»»» uid|string|true|none||none|
|»»» categoryId|integer|true|none||none|
|»»» richTime|integer|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 删除好友

POST /delete_friend

> Body 请求参数

```json
{
    "user_id": 379450326
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» user_id|body|integer| 是 |好友 QQ 号|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 处理好友申请

POST /set_friend_add_request

> Body 请求参数

```json
{
  "flag": "string",
  "approve": true,
  "remark": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» flag|body|string| 是 | 请求id|none|
|» approve|body|boolean| 是 | 是否同意|none|
|» remark|body|string| 是 | 好友备注|none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 设置好友备注

POST /set_friend_remark

> Body 请求参数

```json
{
  "user_id": 0,
  "remark": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» user_id|body|integer| 是 ||好友 QQ 号|
|» remark|body|string| 否 ||备注名|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 获取陌生人信息

POST /get_stranger_info

> Body 请求参数

```json
{
  "user_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» user_id|body|integer| 是 ||QQ 号|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": {
    "user_id": 0,
    "nickname": "string",
    "sex": "string",
    "age": 0,
    "qid": "string",
    "level": 0,
    "login_days": 0,
    "reg_time": 0,
    "long_nick": "string",
    "city": "string",
    "country": "string",
    "birthday_year": 0,
    "birthday_month": 0,
    "birthday_day": 0,
    "labels": [
      "string"
    ],
    "is_vip": true,
    "is_years_vip": true,
    "vip_level": 0,
    "remark": "string"
  },
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» user_id|integer|true|none||QQ 号|
|»» nickname|string|true|none||昵称|
|»» sex|string|true|none||性别，male 或 female 或 unknown|
|»» age|integer|true|none||年龄|
|»» qid|string|true|none||qid ID 身份卡|
|»» level|integer|true|none||等级|
|»» login_days|integer|true|none||登录天数|
|»» reg_time|integer|true|none||注册时间|
|»» long_nick|string|true|none||个性签名|
|»» city|string|true|none||城市|
|»» country|string|true|none||国家|
|»» birthday_year|integer|true|none||出生年份|
|»» birthday_month|integer|true|none||出生月份|
|»» birthday_day|integer|true|none||出生日|
|»» labels|[string]|true|none||个性标签|
|»» is_vip|boolean|true|none||是否会员|
|»» is_years_vip|boolean|true|none||是否年费会员|
|»» vip_level|integer|true|none||会员等级|
|»» remark|string|true|none||备注|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 设置个人头像

POST /set_qq_avatar

> Body 请求参数

```json
{
    // 支持三种形式:
    // file://d:/1.png
    // http://baidu.com/xxxx/1.png
    // base64://xxxxxxxx
    "file": "file://d:\\1.png"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» file|body|string| 是 ||支持三种形式: |

#### 详细说明

**» file**: 支持三种形式: 

* file://d:/1.png 

* http://baidu.com/xxxx/1.png 

* base64://xxxxxxxx

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 好友戳一戳（双击头像）

POST /friend_poke

> Body 请求参数

```json
{
    "user_id": 1231311
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» user_id|body|integer| 是 ||对方 QQ 号|
|» target_id|body|integer| 否 ||目标 QQ 号|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 获取我赞过谁列表

POST /get_profile_like

> Body 请求参数

```json
{
  "start": 0,
  "count": 20
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» start|body|integer| 否 ||从0开始，-1表示获取全部，获取全部的时候非好友nick可能为空|
|» count|body|integer| 否 ||一页的数量，最多30|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "users": [
            {
                "uid": "u_WuwZOz_Hdk4HBUlSGw",
                "src": 71,
                "latestTime": 1735032386,
                "count": 1,
                "giftCount": 0,
                "customId": 2721,
                "lastCharged": 0,
                "bAvailableCnt": 0,
                "bTodayVotedCnt": 1,
                "nick": "xxx",
                "gender": 1,
                "age": 27,
                "isFriend": false,
                "isvip": true,
                "isSvip": true,
                "uin": 1123123
            }
        ],
        "nextStart": 1
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» users|[object]|true|none||none|
|»»» uid|string|true|none||none|
|»»» src|integer|true|none||none|
|»»» latestTime|integer|true|none||none|
|»»» count|integer|true|none||none|
|»»» giftCount|integer|true|none||none|
|»»» customId|integer|true|none||none|
|»»» lastCharged|integer|true|none||none|
|»»» bAvailableCnt|integer|true|none||none|
|»»» bTodayVotedCnt|integer|true|none||none|
|»»» nick|string|true|none||none|
|»»» gender|integer|true|none||none|
|»»» age|integer|true|none||none|
|»»» isFriend|boolean|true|none||none|
|»»» isvip|boolean|true|none||none|
|»»» isSvip|boolean|true|none||none|
|»»» uin|integer|true|none||none|
|»» nextStart|integer|true|none|下一页的start，-1表示没有下一页了|none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取谁赞过我列表

POST /get_profile_like_me

> Body 请求参数

```json
{
  "start": 0,
  "count": 20
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» start|body|integer| 否 ||从0开始，-1表示获取全部，获取全部的时候非好友nick可能为空|
|» count|body|integer| 否 ||一页的数量，最多30|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "users": [
            {
                "uid": "u_KzF6I-tgzAe7l3qW1S",
                "src": 66,
                "latestTime": 1734883223,
                "count": 10,
                "giftCount": 0,
                "customId": 0,
                "lastCharged": 0,
                "bAvailableCnt": 0,
                "bTodayVotedCnt": 0,
                "nick": "AI bot",
                "gender": 255,
                "age": 0,
                "isFriend": true,
                "isvip": false,
                "isSvip": false,
                "uin": 123123123
            }
        ],
        "nextStart": 2
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» users|[object]|true|none||none|
|»»» uid|string|false|none||none|
|»»» src|integer|false|none||none|
|»»» latestTime|integer|false|none||none|
|»»» count|integer|false|none|点赞次数|none|
|»»» giftCount|integer|false|none||none|
|»»» customId|integer|false|none||none|
|»»» lastCharged|integer|false|none||none|
|»»» bAvailableCnt|integer|false|none||none|
|»»» bTodayVotedCnt|integer|false|none||none|
|»»» nick|string|false|none||none|
|»»» gender|integer|false|none||none|
|»»» age|integer|false|none||none|
|»»» isFriend|boolean|false|none||none|
|»»» isvip|boolean|false|none||none|
|»»» isSvip|boolean|false|none||none|
|»»» uin|integer|false|none|QQ号|none|
|»» nextStart|integer|true|none|下一页的start，-1则表示没有下一页|none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## GET 获取官方机器人QQ号范围

GET /get_robot_uin_range

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": [
        {
            "minUin": "3328144510",
            "maxUin": "3328144510"
        },
        {
            "minUin": "2854196301",
            "maxUin": "2854216399"
        },
        {
            "minUin": "66600000",
            "maxUin": "66600000"
        },
        {
            "minUin": "3889000000",
            "maxUin": "3889999999"
        },
        {
            "minUin": "4010000000",
            "maxUin": "4019999999"
        }
    ],
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|[object]|true|none||none|
|»» minUin|string|true|none||none|
|»» maxUin|string|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 移动好友分组

POST /set_friend_category

> Body 请求参数

```json
{
    "user_id": 12321313,
    "category_id": 9999
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» user_id|body|integer| 是 ||好友 QQ 号|
|» category_id|body|integer| 是 ||分组 ID|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 获取QQ或QQ群头像

POST /get_qq_avatar

> Body 请求参数

```json
{
  "user_id": 0,
  "group_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» user_id|body|integer| 否 ||QQ 号|
|» group_id|body|integer| 否 ||none|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "url": "https://thirdqq.qlogo.cn/g?b=qq&nk=&s=640"
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» url|string|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取被过滤好友请求

POST /get_doubt_friends_add_request

此 API 需要 LLOneBot 6.2.0 及以上版本

> Body 请求参数

```json
{
  "count": 50
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 是 ||none|
|» count|body|integer| 否 ||好友请求数量|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": [
    {
      "flag": "string",
      "uin": "string",
      "nick": "string",
      "source": "string",
      "reason": "string",
      "msg": "string",
      "group_code": "string",
      "time": "string",
      "type": "string"
    }
  ],
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|[object]|true|none||none|
|»» flag|string|true|none||none|
|»» uin|string|true|none||none|
|»» nick|string|true|none||none|
|»» source|string|true|none||none|
|»» reason|string|true|none||none|
|»» msg|string|true|none||none|
|»» group_code|string|true|none||none|
|»» time|string|true|none||none|
|»» type|string|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 处理被过滤好友请求

POST /set_doubt_friends_add_request

此 API 需要 LLOneBot 6.2.0 及以上版本

> Body 请求参数

```json
{
  "flag": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 是 ||none|
|» flag|body|string| 是 ||加好友请求的 flag（需从 get_doubt_friends_add_request API 中获得）|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|null|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 设置登录号资料

POST /set_qq_profile

> Body 请求参数

```json
{
  "nickname": "string",
  "personal_note": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 是 ||none|
|» nickname|body|string| 否 ||名称|
|» personal_note|body|string| 否 ||个人说明|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": null,
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|null|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 设置输入状态

POST /set_input_status

此 API 需要 LLBot 7.12.3 及以上版本

> Body 请求参数

```json
{
  "user_id": 0,
  "event_type": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 是 ||none|
|» user_id|body|integer| 是 ||对方 QQ 号|
|» event_type|body|integer| 是 ||事件类型（为 `0` 时表示「对方正在说话...」，为 `1` 时表示「对方正在输入...」）|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": null,
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|null|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

# OneBot 11/接口列表/群组

## POST 获取群列表

POST /get_group_list

> Body 请求参数

```json
{
  "no_cache": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» no_cache|body|boolean| 否 ||是否不使用缓存|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": [
    {
      "group_id": 0,
      "group_name": "string",
      "group_memo": "string",
      "group_create_time": 0,
      "member_count": 0,
      "max_member_count": 0,
      "remark_name": "string",
      "avatar_url": "string",
      "owner_id": 0,
      "is_top": true,
      "shut_up_all_timestamp": 0,
      "shut_up_me_timestamp": 0
    }
  ],
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|[object]|true|none||none|
|»» group_id|integer|true|none||群号|
|»» group_name|string|true|none||群名称|
|»» group_memo|string|true|none||群介绍|
|»» group_create_time|integer|true|none||群创建时间|
|»» member_count|integer|true|none||成员数|
|»» max_member_count|integer|true|none||最大成员数（群容量）|
|»» remark_name|string|true|none||群备注|
|»» avatar_url|string|true|none||群头像|
|»» owner_id|integer|true|none||群主 QQ 号|
|»» is_top|boolean|true|none||群是否顶置|
|»» shut_up_all_timestamp|integer|true|none||全员禁言结束时间|
|»» shut_up_me_timestamp|integer|true|none||自身禁言结束时间|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取群信息

POST /get_group_info

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "group_id": 1009098331,
        "group_name": "测试",
        "group_memo": "",
        "group_create_time": 1766228302,
        "member_count": 3,
        "max_member_count": 200,
        "remark_name": "",
        "avatar_url": "https://p.qlogo.cn/gh/1009098331/1009098331/0",
        // 以下字段需要 LLBot 7.8 以上版本
        "owner_id": 1234567,
        "is_top": false,
        "shut_up_all_timestamp": 0,
        "shut_up_me_timestamp": 1770360153,
        "is_freeze": false,
        "active_member_count": 0
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» group_id|integer|true|none||群号|
|»» group_name|string|true|none||群名称|
|»» group_memo|string|true|none||群介绍|
|»» group_create_time|integer|true|none||群创建时间|
|»» member_count|integer|true|none||成员数|
|»» max_member_count|integer|true|none||最大成员数（群容量）|
|»» remark_name|string|true|none||群备注|
|»» avatar_url|string|true|none||群头像|
|»» owner_id|integer|true|none||群主 QQ 号|
|»» is_top|boolean|true|none||群是否顶置|
|»» shut_up_all_timestamp|integer|true|none||全员禁言结束时间|
|»» shut_up_me_timestamp|integer|true|none||自身禁言结束时间|
|»» is_freeze|boolean|true|none||群是否被冻结|
|»» active_member_count|integer|true|none||活跃成员数|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取群成员列表

POST /get_group_member_list

> Body 请求参数

```json
{
  "group_id": 0,
  "no_cache": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» no_cache|body|boolean| 否 ||是否不使用缓存|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": [
    {
      "group_id": 0,
      "user_id": 0,
      "nickname": "string",
      "card": "string",
      "card_or_nickname": "string",
      "sex": "string",
      "age": 0,
      "area": "string",
      "level": "string",
      "qq_level": 0,
      "join_time": 0,
      "last_sent_time": 0,
      "title_expire_time": 0,
      "unfriendly": true,
      "card_changeable": true,
      "is_robot": true,
      "shut_up_timestamp": 0,
      "role": "string",
      "title": "string"
    }
  ],
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|[object]|true|none||none|
|»» group_id|integer|true|none||群号|
|»» user_id|integer|true|none||QQ 号|
|»» nickname|string|true|none||昵称|
|»» card|string|true|none||群名片／备注|
|»» card_or_nickname|string|true|none||群名片或昵称|
|»» sex|string|true|none||性别, male 或 female 或 unknown|
|»» age|integer|true|none||年龄|
|»» area|string|true|none||地区|
|»» level|string|true|none||成员等级|
|»» qq_level|integer|true|none||QQ 等级|
|»» join_time|integer|true|none||加群时间戳|
|»» last_sent_time|integer|true|none||最后发言时间戳|
|»» title_expire_time|integer|true|none||专属头衔过期时间戳|
|»» unfriendly|boolean|true|none||是否不良记录成员|
|»» card_changeable|boolean|true|none||是否允许修改群名片|
|»» is_robot|boolean|true|none||是否为机器人|
|»» shut_up_timestamp|integer|true|none||禁言到期时间|
|»» role|string|true|none||角色, owner 或 admin 或 member|
|»» title|string|true|none||专属头衔|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取群成员信息

POST /get_group_member_info

> Body 请求参数

```json
{
  "group_id": 0,
  "user_id": 0,
  "no_cache": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» user_id|body|integer| 是 ||QQ 号|
|» no_cache|body|boolean| 否 ||是否不使用缓存|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": {
    "group_id": 0,
    "user_id": 0,
    "nickname": "string",
    "card": "string",
    "card_or_nickname": "string",
    "sex": "string",
    "age": 0,
    "area": "string",
    "level": "string",
    "qq_level": 0,
    "join_time": 0,
    "last_sent_time": 0,
    "title_expire_time": 0,
    "unfriendly": true,
    "card_changeable": true,
    "is_robot": true,
    "shut_up_timestamp": 0,
    "role": "string",
    "title": "string"
  },
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» group_id|integer|true|none||群号|
|»» user_id|integer|true|none||QQ 号|
|»» nickname|string|true|none||昵称|
|»» card|string|true|none||群名片／备注|
|»» card_or_nickname|string|true|none||群名片或昵称|
|»» sex|string|true|none||性别, male 或 female 或 unknown|
|»» age|integer|true|none||年龄|
|»» area|string|true|none||地区|
|»» level|string|true|none||成员等级|
|»» qq_level|integer|true|none||QQ 等级|
|»» join_time|integer|true|none||加群时间戳|
|»» last_sent_time|integer|true|none||最后发言时间戳|
|»» title_expire_time|integer|true|none||专属头衔过期时间戳|
|»» unfriendly|boolean|true|none||是否不良记录成员|
|»» card_changeable|boolean|true|none||是否允许修改群名片|
|»» is_robot|boolean|true|none||是否为机器人|
|»» shut_up_timestamp|integer|true|none||禁言到期时间|
|»» role|string|true|none||角色, owner 或 admin 或 member|
|»» title|string|true|none||专属头衔|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 群员戳一戳（双击头像）

POST /group_poke

> Body 请求参数

```json
{
    "group_id": 1232112,
    "user_id": 15123123
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» user_id|body|integer| 是 ||QQ 号|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## GET 获取群系统消息

GET /get_group_system_msg

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "invited_requests": [
            {
                "request_id": 1729175034613589,
                "invitor_uin": 379450326,
                "invitor_nick": "--",
                "group_id": 518662028,
                "group_name": "LLOneBot",
                "checked": true,
                "actor": 379450326
            }
        ],
        "join_requests": [
            {
                "request_id": 1730027829687169,
                "requester_uin": 379450326,
                "requester_nick": "不",
                "message": "问题：你为什么要加群？\n答案：加群测试",
                "group_id": 518662028,
                "group_name": "test",
                "checked": false,
                "actor": 0
            }
        ]
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» invited_requests|[object]|true|none||邀请加群申请|
|»»» request_id|integer|false|none||none|
|»»» invitor_uin|integer|false|none||none|
|»»» invitor_nick|string|false|none||none|
|»»» group_id|integer|false|none||none|
|»»» group_name|string|false|none||none|
|»»» checked|boolean|false|none||none|
|»»» actor|integer|false|none||none|
|»» join_requests|[object]|true|none||加群申请|
|»»» request_id|integer|false|none||none|
|»»» requester_uin|integer|false|none||none|
|»»» requester_nick|string|false|none||none|
|»»» message|string|false|none||none|
|»»» group_id|integer|false|none||none|
|»»» group_name|string|false|none||none|
|»»» checked|boolean|false|none||none|
|»»» actor|integer|false|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 处理加群请求

POST /set_group_add_request

> Body 请求参数

```json
{
  "flag": "string",
  "approve": true,
  "reason": " "
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» flag|body|string| 是 ||加群请求的 flag|
|» approve|body|boolean| 否 ||是否同意请求／邀请|
|» reason|body|string| 否 ||拒绝理由（仅在拒绝时有效）|

> 返回示例

> 200 Response

```json
{"status":"ok","retcode":0,"data":null,"message":"","wording":""}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|null|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 退群

POST /set_group_leave

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 设置群管理员

POST /set_group_admin

> Body 请求参数

```json
{
  "group_id": 0,
  "user_id": 0,
  "enable": true
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 | 群号|none|
|» user_id|body|integer| 是 | 群员号|none|
|» enable|body|boolean| 是 | 设置/取消|none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 设置群名片

POST /set_group_card

> Body 请求参数

```json
{
  "group_id": 0,
  "user_id": 0,
  "card": " "
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» user_id|body|integer| 是 ||要设置的 QQ 号|
|» card|body|string| 否 ||群名片内容，为空则取消群名片|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 群禁言

POST /set_group_ban

> Body 请求参数

```json
{
  "group_id": 0,
  "user_id": 0,
  "duration": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» user_id|body|integer| 是 ||要禁言的 QQ 号|
|» duration|body|integer| 是 ||禁言时长(秒)，0为取消禁言|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 群全体禁言

POST /set_group_whole_ban

> Body 请求参数

```json
{
  "group_id": 0,
  "enable": true
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» enable|body|boolean| 否 ||是否禁言|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 获取被禁言群员列表

POST /get_group_shut_list

> Body 请求参数

```json
{
    "group_id": 123123
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": [
        {
            "uid": "u_snYxnE123a-12313RQ",
            "qid": "",
            "uin": "1231231",
            "nick": "林雨辰的猫找到了",
            "remark": "",
            "cardType": 0,
            "cardName": "猫猫2",
            "role": 2,
            "avatarPath": "",
            "shutUpTime": 1750385481,
            "isDelete": false,
            "isSpecialConcerned": false,
            "isSpecialShield": false,
            "isRobot": false,
            "groupHonor": {
                "0": 16,
                "1": 43
            },
            "memberRealLevel": 43,
            "memberLevel": 1,
            "globalGroupLevel": 8,
            "globalGroupPoint": 3023,
            "memberTitleId": 10315,
            "memberSpecialTitle": "猫猫33",
            "specialTitleExpireTime": "4294967295",
            "userShowFlag": 0,
            "userShowFlagNew": 0,
            "richFlag": 17,
            "mssVipType": 339,
            "bigClubLevel": 0,
            "bigClubFlag": 0,
            "autoRemark": "",
            "creditLevel": 0,
            "joinTime": 1716003859,
            "lastSpeakTime": 1750060936,
            "memberFlag": 0,
            "memberFlagExt": 9,
            "memberMobileFlag": 2,
            "memberFlagExt2": 0,
            "isSpecialShielded": false,
            "cardNameId": 0
        }
    ],
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 设置群名

POST /set_group_name

> Body 请求参数

```json
{
  "group_id": 0,
  "group_name": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» group_name|body|string| 是 ||新群名|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 批量踢出群成员

POST /batch_delete_group_member

需要 5.6.0 及以上版本

> Body 请求参数

```json
{
    "group_id": 1232131,
    "user_ids": [
        1234,
        1231231
    ]
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» user_ids|body|[integer]| 是 ||QQ 号|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": null,
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|null|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 群踢人

POST /set_group_kick

> Body 请求参数

```json
{
  "group_id": 0,
  "user_id": 0,
  "reject_add_request": true
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» user_id|body|integer| 是 ||要踢的 QQ 号|
|» reject_add_request|body|boolean| 是 ||是否禁止再次加群|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 设置群头衔

POST /set_group_special_title

> Body 请求参数

```json
{
  "group_id": 0,
  "user_id": 0,
  "special_title": " "
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» user_id|body|integer| 是 ||要设置的 QQ 号|
|» special_title|body|string| 否 ||专属头衔，为空则表示去掉群头衔|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 群荣誉

POST /get_group_honor_info

> Body 请求参数

```json
{
  "group_id": 0,
  "type": "all"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» type|body|string| 否 ||要获取的群荣誉类型, 可传入 talkative、performer、legend、strong_newbie、emotion 以分别获取单个类型的群荣誉数据, 或传入 all 获取所有数据|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "group_id": "860105388",
        "current_talkative": {
            "user_id": 379450326,
            "avatar": "http://thirdqq.qlogo.cn/g?b=oidb&k=XHbicicZFicicaHzVQjNkvbXhQ&kti=ZxjvpxHhVOA&s=640",
            "nickname": "猫猫12",
            "day_count": 0,
            "description": "34天，最长蝉联7天"
        },
        "talkative_list": [
            {
                "user_id": 379450326,
                "avatar": "http://thirdqq.qlogo.cn/g?b=oidb&k=XHbicicZFicicaHzVQjNkvbXhQ&kti=ZxjvpxHhVOA&s=640",
                "description": "34天，最长蝉联7天",
                "day_count": 0,
                "nickname": "猫猫12"
            },
            {
                "user_id": 721011692,
                "avatar": "http://thirdqq.qlogo.cn/g?b=oidb&k=W9hP20Q154QbbtdqvCn9bA&kti=ZxjvpxHhVOA&s=640",
                "description": "28天，最长蝉联4天",
                "day_count": 0,
                "nickname": "--"
            }
        ],
        "performer_list": [
            {
                "user_id": 379450326,
                "nickname": "猫猫12",
                "avatar": "http://thirdqq.qlogo.cn/g?b=oidb&k=A4xBJupoDSCXt2bqJD9J5w&kti=ZxjvpxHhVOE&s=640",
                "description": "连续发消息8天"
            },
            {
                "user_id": 721011692,
                "nickname": "--",
                "avatar": "http://thirdqq.qlogo.cn/g?b=oidb&k=apofEU0DVaujicHWNHfFh7Q&kti=ZxjvpxHhVOI&s=640",
                "description": "连续发消息8天"
            }
        ],
        "legend_list": [],
        "emotion_list": [],
        "strong_newbie_list": []
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» group_id|string|true|none||none|
|»» current_talkative|object|true|none||当前龙王|
|»»» user_id|integer|true|none||none|
|»»» avatar|string|true|none||none|
|»»» nickname|string|true|none||none|
|»»» day_count|integer|true|none||none|
|»»» description|string|true|none||none|
|»» talkative_list|[object]|true|none||历史龙王|
|»»» user_id|integer|true|none||none|
|»»» avatar|string|true|none||none|
|»»» description|string|true|none||none|
|»»» day_count|integer|true|none||none|
|»»» nickname|string|true|none||none|
|»» performer_list|[object]|true|none||群聊之火|
|»»» user_id|integer|true|none||none|
|»»» nickname|string|true|none||none|
|»»» avatar|string|true|none||none|
|»»» description|string|true|none||none|
|»» legend_list|[string]|true|none||群聊炽焰|
|»» emotion_list|[string]|true|none||快乐之源|
|»» strong_newbie_list|[string]|true|none||冒尖小春笋|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取群精华消息

POST /get_essence_msg_list

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": [
        {
            "sender_id": 1513935547,
            "sender_nick": "喵",
            "sender_time": 1758034945,
            "operator_id": 379450326,
            "operator_nick": "猫",
            "operator_time": 1758034948,
            "message_id": 1606116643
        }
    ],
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|[object]|true|none||none|
|»» sender_id|integer|true|none||none|
|»» sender_nick|string|true|none||none|
|»» sender_time|integer|true|none||none|
|»» operator_id|integer|true|none||none|
|»» operator_nick|string|true|none||none|
|»» operator_time|integer|true|none||none|
|»» message_id|integer|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 设置群精华消息

POST /set_essence_msg

> Body 请求参数

```json
{
    "message_id": 854234234
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» message_id|body|integer| 是 ||消息 ID|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 删除群精华消息

POST /delete_essence_msg

> Body 请求参数

```json
{
    "message_id": 854234234
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» message_id|body|integer| 是 ||消息 ID|

> 返回示例

> 200 Response

```json
{"status":"ok","retcode":0,"data":{"errCode":0,"errMsg":"success","result":{"wording":"","digestUin":"0","digestTime":0,"msg":{"groupCode":"0","msgSeq":0,"msgRandom":0,"msgContent":[],"textSize":"0","picSize":"0","videoSize":"0","senderUin":"0","senderTime":0,"addDigestUin":"0","addDigestTime":0,"startTime":0,"latestMsgSeq":0,"opType":0},"errorCode":0}},"message":"","wording":""}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 获取群 @全体成员 剩余次数

POST /get_group_at_all_remain

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|

> 返回示例

> 200 Response

```json
{"status":"ok","retcode":0,"data":{"can_at_all":true,"remain_at_all_count_for_group":20,"remain_at_all_count_for_uin":10},"message":"","wording":""}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» can_at_all|boolean|true|none|是否可以 @全体成员|none|
|»» remain_at_all_count_for_group|integer|true|none|群内所有管理当天剩余 @全体成员 次数|none|
|»» remain_at_all_count_for_uin|integer|true|none|Bot 当天剩余 @全体成员 次数|none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 发送群公告

POST /_send_group_notice

> Body 请求参数

```json
{
    "group_id": 545402644,
    "content": "公告测试",
    "image": "http://i0.hdslb.com/bfs/archive/c8fd97a40bf79f03e7b76cbc87236f612caef7b2.png"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» content|body|string| 是 ||公告内容|
|» image|body|string| 否 ||图片路径，支持 http://、file://、base64://|
|» pinned|body|boolean| 否 ||是否置顶|
|» confirm_required|body|boolean| 否 ||是否需要确认收到|
|» is_show_edit_card|body|boolean| 否 ||是否引导修改群昵称|
|» tip_window|body|boolean| 否 ||是否使用弹窗展示公告|
|» send_new_member|body|boolean| 否 ||是否发送给新成员|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 获取群公告

POST /_get_group_notice

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": [
    {
      "notice_id": "string",
      "sender_id": 0,
      "publish_time": 0,
      "message": {
        "text": "string",
        "images": [
          {
            "height": null,
            "width": null,
            "id": null
          }
        ]
      },
      "settings": {
        "is_show_edit_card": true,
        "tip_window": true,
        "confirm_required": true,
        "pinned": true,
        "send_new_member": true
      }
    }
  ],
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|[object]|true|none||none|
|»» notice_id|string|true|none||公告 ID|
|»» sender_id|integer|true|none||公告发表者|
|»» publish_time|integer|true|none||公告发表时间|
|»» message|object|true|none||公告内容|
|»»» text|string|true|none||公告内容|
|»»» images|[object]|true|none||公告图片|
|»»»» height|string|false|none||图片高度|
|»»»» width|string|false|none||图片宽度|
|»»»» id|string|false|none||图片 ID，图片 URL 为 https://gdynamic.qpic.cn/gdynamic/(id)/0|
|»» settings|object|true|none||设置项|
|»»» is_show_edit_card|boolean|true|none||是否引导修改群昵称|
|»»» tip_window|boolean|true|none||是否使用弹窗展示公告|
|»»» confirm_required|boolean|true|none||是否需要确认收到|
|»»» pinned|boolean|true|none||是否置顶|
|»»» send_new_member|boolean|true|none||是否发送给新成员|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 群打卡

POST /send_group_sign

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 设置群消息接收方式

POST /set_group_msg_mask

> Body 请求参数

```json
{
    "group_id": 123213,
    "mask": 1 // 1 接收并提醒，2 收进群助手，3 屏蔽，4 接收不提醒
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» mask|body|integer| 是 ||接收方式|

#### 枚举值

|属性|值|
|---|---|
|» mask|1|
|» mask|2|
|» mask|3|
|» mask|4|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 设置群备注

POST /set_group_remark

> Body 请求参数

```json
{
  "group_id": 0,
  "remark": " "
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» remark|body|string| 否 ||备注名，为空则取消备注|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 获取已过滤的加群通知

POST /get_group_ignore_add_request

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 上传群相册

POST /upload_group_album

> Body 请求参数

```json
{
    "group_id": 123456,
    "album_id": "V64bCpRO1qoERF1jMbrk3mA8aW0DEkIu",
    "files": [
        "file:///D:/temp/1.png"
    ]
    // base64
    //"files": ["base64://abcabcabca=="]
    // http
    // "files": ["http://a.com/a.png"]
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» album_id|body|string| 是 ||相册 ID|
|» files|body|[string]| 是 ||文件路径|

> 返回示例

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "success_count": 1,
        "fail_count": 0,
        "fail_indexes": []
    },
    "message": "",
    "wording": ""
}
```

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "success_count": 0,
        "fail_count": 1,
        "fail_indexes": [
            0
        ]
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» success_count|integer|true|none||none|
|»» fail_count|integer|true|none||none|
|»» fail_indexes|[string]|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取群相册列表

POST /get_group_album_list

> Body 请求参数

```json
{
    "group_id": 24123123
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|

> 返回示例

```json
{
    "status": "ok",
    "retcode": 0,
    "data": [
        {
            "album_id": "V64bCpRO1qoERF1jMbrk3mA8aW0DEkIu",
            "owner": "164461995",
            "name": "test",
            "desc": " ",
            "create_time": "1761912301",
            "modify_time": "1762322311",
            "last_upload_time": "1762322310",
            "upload_number": "34",
            "cover": {
                "type": 0,
                "image": {
                    "name": "",
                    "sloc": "",
                    "lloc": "V5bCQAxNjQ0NjE5OTWG5wppe.2HEg!!",
                    "photo_url": [
                        {
                            "spec": 3,
                            "url": {
                                "url": "https://qungz.photo.store.qq.com/qun-qungz/V64bCpRO1qoERF1jMbrk3mA8aW0DEkIu/V5bCQAxNjQ0NjE5OTWG5wppe.2HEg!!/200?ek=1&kp=1&w5=0&h5=0&pt=7#sce=110-3-3",
                                "width": 0,
                                "height": 0
                            }
                        },
                        {
                            "spec": 5,
                            "url": {
                                "url": "https://qungz.photo.store.qq.com/qun-qungz/V64bCpRO1qoERF1jMbrk3mA8aW0DEkIu/V5bCQAxNjQ0NjE5OTWG5wppe.2HEg!!/640?ek=1&kp=1&w5=0&h5=0&pt=7#sce=110-11-2",
                                "width": 0,
                                "height": 0
                            }
                        },
                        {
                            "spec": 6,
                            "url": {
                                "url": "https://qungz.photo.store.qq.com/qun-qungz/V64bCpRO1qoERF1jMbrk3mA8aW0DEkIu/V5bCQAxNjQ0NjE5OTWG5wppe.2HEg!!/0?ek=1&kp=1&w5=0&h5=0&pt=7#sce=110-0-0",
                                "width": 0,
                                "height": 0
                            }
                        },
                        {
                            "spec": 1,
                            "url": {
                                "url": "https://qungz.photo.store.qq.com/qun-qungz/V64bCpRO1qoERF1jMbrk3mA8aW0DEkIu/V5bCQAxNjQ0NjE5OTWG5wppe.2HEg!!/800?ek=1&kp=1&w5=0&h5=0&pt=7#sce=110-1-1",
                                "width": 0,
                                "height": 0
                            }
                        },
                        {
                            "spec": 2,
                            "url": {
                                "url": "https://qungz.photo.store.qq.com/qun-qungz/V64bCpRO1qoERF1jMbrk3mA8aW0DEkIu/V5bCQAxNjQ0NjE5OTWG5wppe.2HEg!!/640?ek=1&kp=1&w5=0&h5=0&pt=7#sce=110-2-2",
                                "width": 0,
                                "height": 0
                            }
                        }
                    ],
                    "default_url": {
                        "url": "https://qungz.photo.store.qq.com/qun-qungz/V64bCpRO1qoERF1jMbrk3mA8aW0DEkIu/V5bCQAxNjQ0NjE5OTWG5wppe.2HEg!!/640?ek=1&kp=1&w5=0&h5=0&pt=7#sce=110-11-2",
                        "width": 0,
                        "height": 0
                    },
                    "is_gif": false,
                    "has_raw": false
                },
                "video": null,
                "desc": "",
                "lbs": null,
                "uploader": "",
                "batch_id": "0",
                "upload_time": "0",
                "upload_order": 0,
                "like": null,
                "comment": null,
                "upload_user": null,
                "ext": [],
                "shoot_time": "0",
                "link_id": "0",
                "op_mask": [],
                "lbs_source": 0
            },
            "creator": {
                "uid": "",
                "nick": "猫",
                "yellow_info": null,
                "star_info": null,
                "is_sweet": false,
                "is_special": false,
                "is_super_like": false,
                "custom_id": "",
                "poly_id": "",
                "portrait": "",
                "can_follow": 0,
                "isfollowed": 0,
                "uin": "379450326",
                "ditto_uin": ""
            },
            "top_flag": "0",
            "busi_type": 0,
            "status": 0,
            "permission": null,
            "allow_share": false,
            "is_subscribe": false,
            "bitmap": "",
            "is_share_album": false,
            "share_album": null,
            "qz_album_type": 0,
            "family_album": null,
            "lover_album": null,
            "cover_type": 2,
            "travel_album": null,
            "visitor_info": null,
            "default_desc": "",
            "op_info": null,
            "active_album": null,
            "memory_info": null,
            "sort_type": 0
        },
        {
            "album_id": "V64bCpRO1qoERF1jMbrk08oVsx3qLkbk",
            "owner": "164461995",
            "name": "aaa",
            "desc": "",
            "create_time": "1762319245",
            "modify_time": "1762319245",
            "last_upload_time": "1762319245",
            "upload_number": "0",
            "cover": {
                "type": 0,
                "image": {
                    "name": "",
                    "sloc": "",
                    "lloc": "",
                    "photo_url": [
                        {
                            "spec": 5,
                            "url": {
                                "url": "",
                                "width": 0,
                                "height": 0
                            }
                        }
                    ],
                    "default_url": {
                        "url": "",
                        "width": 0,
                        "height": 0
                    },
                    "is_gif": false,
                    "has_raw": false
                },
                "video": null,
                "desc": "",
                "lbs": null,
                "uploader": "",
                "batch_id": "0",
                "upload_time": "0",
                "upload_order": 0,
                "like": null,
                "comment": null,
                "upload_user": null,
                "ext": [],
                "shoot_time": "0",
                "link_id": "0",
                "op_mask": [],
                "lbs_source": 0
            },
            "creator": {
                "uid": "",
                "nick": "--",
                "yellow_info": null,
                "star_info": null,
                "is_sweet": false,
                "is_special": false,
                "is_super_like": false,
                "custom_id": "",
                "poly_id": "",
                "portrait": "",
                "can_follow": 0,
                "isfollowed": 0,
                "uin": "721011692",
                "ditto_uin": ""
            },
            "top_flag": "0",
            "busi_type": 0,
            "status": 0,
            "permission": null,
            "allow_share": false,
            "is_subscribe": false,
            "bitmap": "",
            "is_share_album": false,
            "share_album": null,
            "qz_album_type": 0,
            "family_album": null,
            "lover_album": null,
            "cover_type": 0,
            "travel_album": null,
            "visitor_info": null,
            "default_desc": "",
            "op_info": null,
            "active_album": null,
            "memory_info": null,
            "sort_type": 0
        }
    ],
    "message": "",
    "wording": ""
}
```

```json
{
    "status": "failed",
    "retcode": 200,
    "data": null,
    "message": "获取群相册列表失败 Not member, can not read",
    "wording": "获取群相册列表失败 Not member, can not read"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|[object]|true|none||none|
|»» album_id|string|true|none||none|
|»» owner|string|true|none||none|
|»» name|string|true|none||none|
|»» desc|string|true|none||none|
|»» create_time|string|true|none||none|
|»» modify_time|string|true|none||none|
|»» last_upload_time|string|true|none||none|
|»» upload_number|string|true|none||none|
|»» cover|object|true|none||none|
|»»» type|integer|true|none||none|
|»»» image|object|true|none||none|
|»»»» name|string|true|none||none|
|»»»» sloc|string|true|none||none|
|»»»» lloc|string|true|none||none|
|»»»» photo_url|[object]|true|none||none|
|»»»»» spec|integer|true|none||none|
|»»»»» url|object|true|none||none|
|»»»»»» url|string|true|none||none|
|»»»»»» width|integer|true|none||none|
|»»»»»» height|integer|true|none||none|
|»»»» default_url|object|true|none||none|
|»»»»» url|string|true|none||none|
|»»»»» width|integer|true|none||none|
|»»»»» height|integer|true|none||none|
|»»»» is_gif|boolean|true|none||none|
|»»»» has_raw|boolean|true|none||none|
|»»» video|null|true|none||none|
|»»» desc|string|true|none||none|
|»»» lbs|null|true|none||none|
|»»» uploader|string|true|none||none|
|»»» batch_id|string|true|none||none|
|»»» upload_time|string|true|none||none|
|»»» upload_order|integer|true|none||none|
|»»» like|null|true|none||none|
|»»» comment|null|true|none||none|
|»»» upload_user|null|true|none||none|
|»»» ext|[string]|true|none||none|
|»»» shoot_time|string|true|none||none|
|»»» link_id|string|true|none||none|
|»»» op_mask|[string]|true|none||none|
|»»» lbs_source|integer|true|none||none|
|»» creator|object|true|none||none|
|»»» uid|string|true|none||none|
|»»» nick|string|true|none||none|
|»»» yellow_info|null|true|none||none|
|»»» star_info|null|true|none||none|
|»»» is_sweet|boolean|true|none||none|
|»»» is_special|boolean|true|none||none|
|»»» is_super_like|boolean|true|none||none|
|»»» custom_id|string|true|none||none|
|»»» poly_id|string|true|none||none|
|»»» portrait|string|true|none||none|
|»»» can_follow|integer|true|none||none|
|»»» isfollowed|integer|true|none||none|
|»»» uin|string|true|none||none|
|»»» ditto_uin|string|true|none||none|
|»» top_flag|string|true|none||none|
|»» busi_type|integer|true|none||none|
|»» status|integer|true|none||none|
|»» permission|null|true|none||none|
|»» allow_share|boolean|true|none||none|
|»» is_subscribe|boolean|true|none||none|
|»» bitmap|string|true|none||none|
|»» is_share_album|boolean|true|none||none|
|»» share_album|null|true|none||none|
|»» qz_album_type|integer|true|none||none|
|»» family_album|null|true|none||none|
|»» lover_album|null|true|none||none|
|»» cover_type|integer|true|none||none|
|»» travel_album|null|true|none||none|
|»» visitor_info|null|true|none||none|
|»» default_desc|string|true|none||none|
|»» op_info|null|true|none||none|
|»» active_album|null|true|none||none|
|»» memory_info|null|true|none||none|
|»» sort_type|integer|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 创建群相册

POST /create_group_album

> Body 请求参数

```json
{
    "group_id": {{group_id}},
    "name": "test",
    "desc": ""
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» name|body|string| 是 ||相册名称|
|» desc|body|string| 否 ||相册描述|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "album_id": "V64bCpRO1qoERF1jMbrk2WBM3G3iXXMo",
        "owner": "164461995",
        "name": "test",
        "desc": "",
        "create_time": "0",
        "modify_time": "0",
        "last_upload_time": "0",
        "upload_number": "0",
        "cover": null,
        "creator": null,
        "top_flag": "0",
        "busi_type": 0,
        "status": 0,
        "permission": null,
        "allow_share": false,
        "is_subscribe": false,
        "bitmap": "",
        "is_share_album": false,
        "share_album": null,
        "qz_album_type": 0,
        "family_album": null,
        "lover_album": null,
        "cover_type": 0,
        "travel_album": null,
        "visitor_info": null,
        "default_desc": "",
        "op_info": null,
        "active_album": null,
        "memory_info": null,
        "sort_type": 0
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» album_id|string|true|none||none|
|»» owner|string|true|none||none|
|»» name|string|true|none||none|
|»» desc|string|true|none||none|
|»» create_time|string|true|none||none|
|»» modify_time|string|true|none||none|
|»» last_upload_time|string|true|none||none|
|»» upload_number|string|true|none||none|
|»» cover|null|true|none||none|
|»» creator|null|true|none||none|
|»» top_flag|string|true|none||none|
|»» busi_type|integer|true|none||none|
|»» status|integer|true|none||none|
|»» permission|null|true|none||none|
|»» allow_share|boolean|true|none||none|
|»» is_subscribe|boolean|true|none||none|
|»» bitmap|string|true|none||none|
|»» is_share_album|boolean|true|none||none|
|»» share_album|null|true|none||none|
|»» qz_album_type|integer|true|none||none|
|»» family_album|null|true|none||none|
|»» lover_album|null|true|none||none|
|»» cover_type|integer|true|none||none|
|»» travel_album|null|true|none||none|
|»» visitor_info|null|true|none||none|
|»» default_desc|string|true|none||none|
|»» op_info|null|true|none||none|
|»» active_album|null|true|none||none|
|»» memory_info|null|true|none||none|
|»» sort_type|integer|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 删除群相册

POST /delete_group_album

> Body 请求参数

```json
{
    "group_id": 1232131,
    "album_id": "V64bCpRO1qoERF1jMbrk3mA8aW0DEkIu"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» album_id|body|string| 是 ||相册 ID|

> 返回示例

```json
{
    "status": "ok",
    "retcode": 0,
    "data": null,
    "message": "",
    "wording": ""
}
```

```json
{
    "status": "failed",
    "retcode": 200,
    "data": null,
    "message": "CreateGroupAlbum failed: 相册不存在",
    "wording": "CreateGroupAlbum failed: 相册不存在"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|null|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取群相册媒体列表

POST /get_group_album_media_list

此 API 需要 LLBot 7.12.3 及以上版本

> Body 请求参数

```json
{
  "group_id": 0,
  "album_id": "string",
  "attach_info": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 是 ||none|
|» group_id|body|integer| 是 ||群号|
|» album_id|body|string| 是 ||相册 ID|
|» attach_info|body|string| 否 ||附加信息（用于分页）|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": {
    "album": {
      "album_id": "string",
      "owner": "string",
      "name": "string",
      "desc": "string",
      "create_time": "string",
      "modify_time": "string",
      "last_upload_time": "string",
      "upload_number": "string",
      "cover": {
        "type": 0,
        "image": {
          "name": null,
          "sloc": null,
          "lloc": null,
          "photo_url": null,
          "default_url": null,
          "is_gif": null,
          "has_raw": null
        },
        "video": null,
        "desc": "string",
        "lbs": null,
        "uploader": "string",
        "batch_id": "string",
        "upload_time": "string",
        "upload_order": 0,
        "like": null,
        "comment": null,
        "upload_user": null,
        "ext": [
          "string"
        ],
        "shoot_time": "string",
        "link_id": "string",
        "op_mask": [
          "string"
        ],
        "lbs_source": 0
      },
      "creator": {
        "uid": "string",
        "nick": "string",
        "yellow_info": null,
        "star_info": null,
        "is_sweet": true,
        "is_special": true,
        "is_super_like": true,
        "custom_id": "string",
        "poly_id": "string",
        "portrait": "string",
        "can_follow": 0,
        "isfollowed": 0,
        "uin": "string",
        "ditto_uin": "string"
      },
      "top_flag": "string",
      "busi_type": 0,
      "status": 0,
      "permission": null,
      "allow_share": true,
      "is_subscribe": true,
      "bitmap": "string",
      "is_share_album": true,
      "share_album": null,
      "qz_album_type": 0,
      "family_album": null,
      "lover_album": null,
      "cover_type": 0,
      "travel_album": null,
      "visitor_info": null,
      "default_desc": "string",
      "op_info": null,
      "active_album": null,
      "memory_info": null,
      "sort_type": 0
    },
    "media_list": [
      {
        "type": 0,
        "image": {
          "name": "string",
          "sloc": "string",
          "lloc": "string",
          "photo_url": [
            null
          ],
          "default_url": {},
          "is_gif": true,
          "has_raw": true
        },
        "video": null,
        "desc": "string",
        "lbs": {
          "gps": {},
          "location": "string",
          "lbsId": "string",
          "address": "string"
        },
        "uploader": "string",
        "batch_id": "string",
        "upload_time": "string",
        "upload_order": 0,
        "like": {
          "key": "string",
          "num": 0,
          "liked": true
        },
        "comment": {
          "num": 0
        },
        "upload_user": {
          "uid": "string",
          "nick": "string",
          "yellow_info": null,
          "star_info": null,
          "is_sweet": true,
          "is_special": true,
          "is_super_like": true,
          "custom_id": "string",
          "poly_id": "string",
          "portrait": "string",
          "can_follow": 0,
          "isfollowed": 0,
          "uin": "string",
          "ditto_uin": "string"
        },
        "ext": [
          "string"
        ],
        "shoot_time": "string",
        "link_id": "string",
        "op_mask": [
          "string"
        ],
        "lbs_source": 0
      }
    ],
    "next_attach_info": "string",
    "next_has_more": true
  },
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» album|object|true|none||none|
|»»» album_id|string|true|none||none|
|»»» owner|string|true|none||none|
|»»» name|string|true|none||none|
|»»» desc|string|true|none||none|
|»»» create_time|string|true|none||none|
|»»» modify_time|string|true|none||none|
|»»» last_upload_time|string|true|none||none|
|»»» upload_number|string|true|none||none|
|»»» cover|object|true|none||none|
|»»»» type|integer|true|none||none|
|»»»» image|object|true|none||none|
|»»»»» name|string|true|none||none|
|»»»»» sloc|string|true|none||none|
|»»»»» lloc|string|true|none||none|
|»»»»» photo_url|[object]|true|none||none|
|»»»»»» spec|integer|true|none||none|
|»»»»»» url|object|true|none||none|
|»»»»»»» url|string|true|none||none|
|»»»»»»» width|integer|true|none||none|
|»»»»»»» height|integer|true|none||none|
|»»»»» default_url|object|true|none||none|
|»»»»»» url|string|true|none||none|
|»»»»»» width|integer|true|none||none|
|»»»»»» height|integer|true|none||none|
|»»»»» is_gif|boolean|true|none||none|
|»»»»» has_raw|boolean|true|none||none|
|»»»» video|null|true|none||none|
|»»»» desc|string|true|none||none|
|»»»» lbs|null|true|none||none|
|»»»» uploader|string|true|none||none|
|»»»» batch_id|string|true|none||none|
|»»»» upload_time|string|true|none||none|
|»»»» upload_order|integer|true|none||none|
|»»»» like|null|true|none||none|
|»»»» comment|null|true|none||none|
|»»»» upload_user|null|true|none||none|
|»»»» ext|[string]|true|none||none|
|»»»» shoot_time|string|true|none||none|
|»»»» link_id|string|true|none||none|
|»»»» op_mask|[string]|true|none||none|
|»»»» lbs_source|integer|true|none||none|
|»»» creator|object|true|none||none|
|»»»» uid|string|true|none||none|
|»»»» nick|string|true|none||none|
|»»»» yellow_info|null|true|none||none|
|»»»» star_info|null|true|none||none|
|»»»» is_sweet|boolean|true|none||none|
|»»»» is_special|boolean|true|none||none|
|»»»» is_super_like|boolean|true|none||none|
|»»»» custom_id|string|true|none||none|
|»»»» poly_id|string|true|none||none|
|»»»» portrait|string|true|none||none|
|»»»» can_follow|integer|true|none||none|
|»»»» isfollowed|integer|true|none||none|
|»»»» uin|string|true|none||none|
|»»»» ditto_uin|string|true|none||none|
|»»» top_flag|string|true|none||none|
|»»» busi_type|integer|true|none||none|
|»»» status|integer|true|none||none|
|»»» permission|null|true|none||none|
|»»» allow_share|boolean|true|none||none|
|»»» is_subscribe|boolean|true|none||none|
|»»» bitmap|string|true|none||none|
|»»» is_share_album|boolean|true|none||none|
|»»» share_album|null|true|none||none|
|»»» qz_album_type|integer|true|none||none|
|»»» family_album|null|true|none||none|
|»»» lover_album|null|true|none||none|
|»»» cover_type|integer|true|none||none|
|»»» travel_album|null|true|none||none|
|»»» visitor_info|null|true|none||none|
|»»» default_desc|string|true|none||none|
|»»» op_info|null|true|none||none|
|»»» active_album|null|true|none||none|
|»»» memory_info|null|true|none||none|
|»»» sort_type|integer|true|none||none|
|»» media_list|[object]|true|none||none|
|»»» type|integer|false|none||none|
|»»» image|object|false|none||none|
|»»»» name|string|true|none||none|
|»»»» sloc|string|true|none||none|
|»»»» lloc|string|true|none||none|
|»»»» photo_url|[object]|true|none||none|
|»»»»» spec|integer|true|none||none|
|»»»»» url|object|true|none||none|
|»»»»»» url|string|true|none||none|
|»»»»»» width|integer|true|none||none|
|»»»»»» height|integer|true|none||none|
|»»»» default_url|object|true|none||none|
|»»»»» url|string|true|none||none|
|»»»»» width|integer|true|none||none|
|»»»»» height|integer|true|none||none|
|»»»» is_gif|boolean|true|none||none|
|»»»» has_raw|boolean|true|none||none|
|»»» video|null|false|none||none|
|»»» desc|string|false|none||none|
|»»» lbs|object|false|none||none|
|»»»» gps|object|true|none||none|
|»»»»» lat|string|true|none||none|
|»»»»» lon|string|true|none||none|
|»»»»» e_type|string|true|none||none|
|»»»»» alt|string|true|none||none|
|»»»» location|string|true|none||none|
|»»»» lbsId|string|true|none||none|
|»»»» address|string|true|none||none|
|»»» uploader|string|false|none||none|
|»»» batch_id|string|false|none||none|
|»»» upload_time|string|false|none||none|
|»»» upload_order|integer|false|none||none|
|»»» like|object|false|none||none|
|»»»» key|string|true|none||none|
|»»»» num|integer|true|none||none|
|»»»» liked|boolean|true|none||none|
|»»» comment|object|false|none||none|
|»»»» num|integer|true|none||none|
|»»» upload_user|object|false|none||none|
|»»»» uid|string|true|none||none|
|»»»» nick|string|true|none||none|
|»»»» yellow_info|null|true|none||none|
|»»»» star_info|null|true|none||none|
|»»»» is_sweet|boolean|true|none||none|
|»»»» is_special|boolean|true|none||none|
|»»»» is_super_like|boolean|true|none||none|
|»»»» custom_id|string|true|none||none|
|»»»» poly_id|string|true|none||none|
|»»»» portrait|string|true|none||none|
|»»»» can_follow|integer|true|none||none|
|»»»» isfollowed|integer|true|none||none|
|»»»» uin|string|true|none||none|
|»»»» ditto_uin|string|true|none||none|
|»»» ext|[string]|false|none||none|
|»»» shoot_time|string|false|none||none|
|»»» link_id|string|false|none||none|
|»»» op_mask|[string]|false|none||none|
|»»» lbs_source|integer|false|none||none|
|»» next_attach_info|string|true|none||none|
|»» next_has_more|boolean|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 删除群公告

POST /_delete_group_notice

> Body 请求参数

```json
{
  "group_id": 0,
  "notice_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 是 ||none|
|» group_id|body|integer| 是 ||群号|
|» notice_id|body|string| 是 ||公告 ID|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|null|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 设置群头像

POST /set_group_portrait

> Body 请求参数

```json
{
  "group_id": 0,
  "file": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 是 ||none|
|» group_id|body|integer| 是 ||群号|
|» file|body|string| 是 ||头像文件 URI|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": null,
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|null|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

# OneBot 11/接口列表/消息

## GET 长连接接收消息

GET /_events

HTTP SSE 的方式接收消息 

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 转发单条好友消息

POST /forward_friend_single_msg

> Body 请求参数

```json
{
  "message_id": 0,
  "user_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» message_id|body|integer| 是 ||消息 ID|
|» user_id|body|integer| 是 ||对方 QQ 号|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": {
    "message_id": 0
  },
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» message_id|integer|true|none||消息 ID|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 转发单条群消息

POST /forward_group_single_msg

> Body 请求参数

```json
{
  "message_id": 0,
  "group_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» message_id|body|integer| 是 ||消息 ID|
|» group_id|body|integer| 是 ||群号|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": {
    "message_id": 0
  },
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» message_id|integer|true|none||消息 ID|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取消息详情

POST /get_msg

> Body 请求参数

```json
{
  "message_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» message_id|body|integer| 是 ||消息 ID|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": {
    "self_id": 0,
    "user_id": 0,
    "time": 0,
    "message_id": 0,
    "real_id": 0,
    "message_seq": 0,
    "message_type": "string",
    "sender": {
      "user_id": 0,
      "nickname": "string",
      "card": "string",
      "role": "string",
      "title": "string"
    },
    "raw_message": "string",
    "font": 0,
    "sub_type": "string",
    "message": [
      {
        "type": "string",
        "data": {
          "text": "string"
        }
      }
    ],
    "message_format": "string",
    "post_type": "string",
    "group_id": 0,
    "status": "normal"
  },
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» self_id|integer|true|none||none|
|»» user_id|integer|true|none||none|
|»» time|integer|true|none||none|
|»» message_id|integer|true|none||none|
|»» real_id|integer|true|none||none|
|»» message_seq|integer|true|none||none|
|»» message_type|string|true|none||none|
|»» sender|object|true|none||none|
|»»» user_id|integer|true|none||none|
|»»» nickname|string|true|none||none|
|»»» card|string|true|none||none|
|»»» role|string|true|none||none|
|»»» title|string|true|none||none|
|»» raw_message|string|true|none||none|
|»» font|integer|true|none||none|
|»» sub_type|string|true|none||none|
|»» message|[object]|true|none||none|
|»»» type|string|false|none||none|
|»»» data|object|false|none||none|
|»»»» text|string|true|none||none|
|»» message_format|string|true|none||none|
|»» post_type|string|true|none||none|
|»» group_id|integer|true|none||none|
|»» status|string|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

#### 枚举值

|属性|值|
|---|---|
|status|normal|
|status|deleted|

## POST 撤回消息

POST /delete_msg

> Body 请求参数

```json
{
  "message_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» message_id|body|integer| 是 ||消息 ID|

> 返回示例

```json
{"status":"ok","retcode":0,"message":"","wording":""}
```

```json
{"status":"failed","retcode":200,"data":null,"message":"Error: 消息-966671988不存在","wording":"Error: 消息-966671988不存在"}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取消息文件详情

POST /get_file

> Body 请求参数

```json
{
  "file": "string",
  "download": true
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» file|body|string| 是 ||收到的文件名|
|» download|body|boolean| 否 ||是否下载文件到 QQ 目录|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "file": "C:\\Users\\linyuchen\\Documents\\Downloads\\~.jpg",
        "url": "http://xxxx",
        "file_size": "59635",
        "file_name": "~.jpg",
        "base64": "/9j/4AAQSkZJRgABAQEASxxxx" // 文件的 base64 编码, 需要在 LLOneBot 的配置文件中开启 文件转base64
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» file|string|true|none||文件路径|
|»» url|string|true|none||文件网址|
|»» file_size|string|true|none||文件大小|
|»» file_name|string|true|none||文件名|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取消息图片详情

POST /get_image

> Body 请求参数

```json
{
  "file": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» file|body|string| 是 ||收到的图片文件名|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "file": "E:\\SystemDocuments\\QQ\\721011692\\nt_qq\\nt_data\\Pic\\2024-10\\Ori\\982eac0e63f48aa524afeaab4a0454fb.gif",
        "url": "https://multimedia.nt.qq.com.cn/download?appid=1407&fileid=EhQUF44jzJ2UpXQ5wgCbzSDrXE6fwBiq1Qog_woozb_H76qkiQMyBHByb2RQgL2jAVoQ-4KUwjXwnPw5XThLD-tL1w&spec=0&rkey=CAESKBkcro_MGujo_-Kh0dsVOliftm4gzNtIFmtigHMTCIkVQRLhdZqOhp8",
        "file_size": "174762",
        "file_name": "982EAC0E63F48AA524AFEAAB4A0454FB.gif"
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» file|string|true|none||none|
|»» url|string|true|none||none|
|»» file_size|string|true|none||none|
|»» file_name|string|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取消息语音详情

POST /get_record

> Body 请求参数

```json
{
  "file": "string",
  "out_format": "mp3"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» file|body|string| 是 ||收到的语音文件名|
|» out_format|body|string| 否 ||要转换到的格式|

#### 枚举值

|属性|值|
|---|---|
|» out_format|mp3|
|» out_format|amr|
|» out_format|wma|
|» out_format|m4a|
|» out_format|spx|
|» out_format|ogg|
|» out_format|wav|
|» out_format|flac|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": {
    "file": "string",
    "file_size": "string",
    "file_name": "string",
    "base64": "string"
  },
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» file|string|true|none||转换后的语音文件路径|
|»» file_size|string|true|none||转换后的语音文件大小|
|»» file_name|string|true|none||转换后的语音文件名称|
|»» base64|string|false|none||转换后的语音文件 Base64|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 表情回应消息

POST /set_msg_emoji_like

只支持群聊消息

> Body 请求参数

```json
{
  "message_id": 0,
  "emoji_id": 0,
  "set": true
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» message_id|body|integer| 是 ||消息 ID|
|» emoji_id|body|integer| 是 ||表情 ID，参考 https://bot.q.qq.com/wiki/develop/api-v2/openapi/emoji/model.html#EmojiType|
|» set|body|boolean| 否 ||是否回应|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|null|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取好友历史消息记录

POST /get_friend_msg_history

> Body 请求参数

```json
{
  "user_id": 0,
  "message_seq": 0,
  "count": 20,
  "reverseOrder": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» user_id|body|integer| 是 ||QQ 号|
|» message_seq|body|integer| 否 ||起始消息序号|
|» count|body|integer| 否 ||消息数量|
|» reverseOrder|body|boolean| 否 ||none|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "messages": [
            {
                "self_id": 379450326,
                "user_id": 379450326,
                "time": 1727071003,
                "message_id": 1898394369,
                "real_id": 1898394369,
                "message_seq": 1898394369,
                "message_type": "private",
                "sender": {
                    "user_id": 379450326,
                    "nickname": "--",
                    "card": ""
                },
                "raw_message": "[CQ:image,file=A6ABA306AAE1AF175C0452868A09824B.png,subType=0,url=https://multimedia.nt.qq.com.cn/download?appid=1406&amp;fileid=Cgk3MjEwMTE2OTISFHk2DU4LCJVL55THYAdYFRGBNBTIGLgaIP4KKKrRk-2w2IgDMgRwcm9k&amp;spec=0&amp;rkey=CAQSKAB6JWENi5LM6IC2hBDLIDV-Ozb5pRGcI6HiFqrC-GYi3MfoTVFONyc,file_size=3384]",
                "font": 14,
                "sub_type": "friend",
                "message": [
                    {
                        "type": "image",
                        "data": {
                            "file": "A6ABA306AAE1AF175C0452868A09824B.png",
                            "subType": 0,
                            "url": "https://multimedia.nt.qq.com.cn/download?appid=1406&fileid=Cgk3MjEwMTE2OTISFHk2DU4LCJVL55THYAdYFRGBNBTIGLgaIP4KKKrRk-2w2IgDMgRwcm9k&spec=0&rkey=CAQSKAB6JWENi5LM6IC2hBDLIDV-Ozb5pRGcI6HiFqrC-GYi3MfoTVFONyc",
                            "file_size": "3384"
                        }
                    }
                ],
                "message_format": "array",
                "post_type": "message_sent"
            }
        ]
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» messages|[object]|true|none||none|
|»»» self_id|integer|true|none||none|
|»»» user_id|integer|true|none||none|
|»»» time|integer|true|none||none|
|»»» message_id|integer|true|none||none|
|»»» real_id|integer|true|none||none|
|»»» message_seq|integer|true|none||none|
|»»» message_type|string|true|none||none|
|»»» sender|object|true|none||none|
|»»»» user_id|integer|true|none||none|
|»»»» nickname|string|true|none||none|
|»»»» card|string|true|none||none|
|»»» raw_message|string|true|none||none|
|»»» font|integer|true|none||none|
|»»» sub_type|string|true|none||none|
|»»» message|[object]|true|none||none|
|»»»» type|string|true|none||none|
|»»»» data|object|true|none||none|
|»»»»» file|string|true|none||none|
|»»»»» subType|integer|false|none||none|
|»»»»» url|string|true|none||none|
|»»»»» file_size|string|true|none||none|
|»»»»» data|string|false|none||none|
|»»»»» text|string|false|none||none|
|»»»»» id|string|false|none||none|
|»»»»» path|string|true|none||none|
|»»»»» result|string|false|none||none|
|»»»»» file_id|string|true|none||none|
|»»» message_format|string|true|none||none|
|»»» post_type|string|true|none||none|
|»»» raw|object|true|none||none|
|»»»» msgId|string|true|none||none|
|»»»» msgRandom|string|true|none||none|
|»»»» msgSeq|string|true|none||none|
|»»»» cntSeq|string|true|none||none|
|»»»» chatType|integer|true|none||none|
|»»»» msgType|integer|true|none||none|
|»»»» subMsgType|integer|true|none||none|
|»»»» sendType|integer|true|none||none|
|»»»» senderUid|string|true|none||none|
|»»»» peerUid|string|true|none||none|
|»»»» channelId|string|true|none||none|
|»»»» guildId|string|true|none||none|
|»»»» guildCode|string|true|none||none|
|»»»» fromUid|string|true|none||none|
|»»»» fromAppid|string|true|none||none|
|»»»» msgTime|string|true|none||none|
|»»»» msgMeta|object|true|none||none|
|»»»» sendStatus|integer|true|none||none|
|»»»» sendRemarkName|string|true|none||none|
|»»»» sendMemberName|string|true|none||none|
|»»»» sendNickName|string|true|none||none|
|»»»» guildName|string|true|none||none|
|»»»» channelName|string|true|none||none|
|»»»» elements|[object]|true|none||none|
|»»»»» elementType|integer|true|none||none|
|»»»»» elementId|string|true|none||none|
|»»»»» elementGroupId|integer|true|none||none|
|»»»»» extBufForUI|object|true|none||none|
|»»»»» textElement|object¦null|true|none||none|
|»»»»»» content|string|true|none||none|
|»»»»»» atType|integer|true|none||none|
|»»»»»» atUid|string|true|none||none|
|»»»»»» atTinyId|string|true|none||none|
|»»»»»» atNtUid|string|true|none||none|
|»»»»»» subElementType|integer|true|none||none|
|»»»»»» atChannelId|string|true|none||none|
|»»»»»» linkInfo|null|true|none||none|
|»»»»»» atRoleId|string|true|none||none|
|»»»»»» atRoleColor|integer|true|none||none|
|»»»»»» atRoleName|string|true|none||none|
|»»»»»» needNotify|integer|true|none||none|
|»»»»» faceElement|object¦null|true|none||none|
|»»»»»» faceIndex|integer|true|none||none|
|»»»»»» faceText|string|true|none||none|
|»»»»»» faceType|integer|true|none||none|
|»»»»»» packId|string|true|none||none|
|»»»»»» stickerId|string|true|none||none|
|»»»»»» sourceType|integer|true|none||none|
|»»»»»» stickerType|integer|true|none||none|
|»»»»»» resultId|string|true|none||none|
|»»»»»» surpriseId|string|true|none||none|
|»»»»»» randomType|integer|true|none||none|
|»»»»»» imageType|null|true|none||none|
|»»»»»» pokeType|null|true|none||none|
|»»»»»» spokeSummary|null|true|none||none|
|»»»»»» doubleHit|null|true|none||none|
|»»»»»» vaspokeId|null|true|none||none|
|»»»»»» vaspokeName|null|true|none||none|
|»»»»»» vaspokeMinver|null|true|none||none|
|»»»»»» pokeStrength|null|true|none||none|
|»»»»»» msgType|null|true|none||none|
|»»»»»» faceBubbleCount|null|true|none||none|
|»»»»»» oldVersionStr|null|true|none||none|
|»»»»»» pokeFlag|null|true|none||none|
|»»»»»» chainCount|integer|true|none||none|
|»»»»» marketFaceElement|null|true|none||none|
|»»»»» replyElement|object¦null|true|none||none|
|»»»»»» replayMsgId|string|true|none||none|
|»»»»»» replayMsgSeq|string|true|none||none|
|»»»»»» replayMsgRootSeq|string|true|none||none|
|»»»»»» replayMsgRootMsgId|string|true|none||none|
|»»»»»» replayMsgRootCommentCnt|string|true|none||none|
|»»»»»» sourceMsgIdInRecords|string|true|none||none|
|»»»»»» sourceMsgText|string|true|none||none|
|»»»»»» sourceMsgTextElems|[any]|true|none||none|
|»»»»»» senderUid|string|true|none||none|
|»»»»»» senderUidStr|string|true|none||none|
|»»»»»» replyMsgClientSeq|string|true|none||none|
|»»»»»» replyMsgTime|string|true|none||none|
|»»»»»» replyMsgRevokeType|integer|true|none||none|
|»»»»»» sourceMsgIsIncPic|boolean|true|none||none|
|»»»»»» sourceMsgExpired|boolean|true|none||none|
|»»»»»» anonymousNickName|null|true|none||none|
|»»»»»» originalMsgState|null|true|none||none|
|»»»»» picElement|object¦null|true|none||none|
|»»»»»» picSubType|integer|true|none||none|
|»»»»»» fileName|string|true|none||none|
|»»»»»» fileSize|string|true|none||none|
|»»»»»» picWidth|integer|true|none||none|
|»»»»»» picHeight|integer|true|none||none|
|»»»»»» original|boolean|true|none||none|
|»»»»»» md5HexStr|string|true|none||none|
|»»»»»» sourcePath|string|true|none||none|
|»»»»»» thumbPath|object|true|none||none|
|»»»»»» transferStatus|integer|true|none||none|
|»»»»»» progress|integer|true|none||none|
|»»»»»» picType|integer|true|none||none|
|»»»»»» invalidState|integer|true|none||none|
|»»»»»» fileUuid|string|true|none||none|
|»»»»»» fileSubId|string|true|none||none|
|»»»»»» thumbFileSize|integer|true|none||none|
|»»»»»» fileBizId|null|true|none||none|
|»»»»»» downloadIndex|null|true|none||none|
|»»»»»» summary|string|true|none||none|
|»»»»»» emojiFrom|integer¦null|true|none||none|
|»»»»»» emojiWebUrl|string¦null|true|none||none|
|»»»»»» emojiAd|object|true|none||none|
|»»»»»»» url|string|true|none||none|
|»»»»»»» desc|string|true|none||none|
|»»»»»» emojiMall|object|true|none||none|
|»»»»»»» packageId|integer|true|none||none|
|»»»»»»» emojiId|integer|true|none||none|
|»»»»»» emojiZplan|object|true|none||none|
|»»»»»»» actionId|integer|true|none||none|
|»»»»»»» actionName|string|true|none||none|
|»»»»»»» actionType|integer|true|none||none|
|»»»»»»» playerNumber|integer|true|none||none|
|»»»»»»» peerUid|string|true|none||none|
|»»»»»»» bytesReserveInfo|string|true|none||none|
|»»»»»» originImageMd5|string|true|none||none|
|»»»»»» originImageUrl|string|true|none||none|
|»»»»»» import_rich_media_context|null|true|none||none|
|»»»»»» isFlashPic|boolean¦null|true|none||none|
|»»»»»» storeID|integer|true|none||none|
|»»»»» pttElement|null|true|none||none|
|»»»»» videoElement|object¦null|true|none||none|
|»»»»»» filePath|string|true|none||none|
|»»»»»» fileName|string|true|none||none|
|»»»»»» videoMd5|string|true|none||none|
|»»»»»» thumbMd5|string|true|none||none|
|»»»»»» fileTime|integer|true|none||none|
|»»»»»» thumbSize|integer|true|none||none|
|»»»»»» fileFormat|integer|true|none||none|
|»»»»»» fileSize|string|true|none||none|
|»»»»»» thumbWidth|integer|true|none||none|
|»»»»»» thumbHeight|integer|true|none||none|
|»»»»»» busiType|integer|true|none||none|
|»»»»»» subBusiType|integer|true|none||none|
|»»»»»» thumbPath|object|true|none||none|
|»»»»»» transferStatus|integer|true|none||none|
|»»»»»» progress|integer|true|none||none|
|»»»»»» invalidState|integer|true|none||none|
|»»»»»» fileUuid|string|true|none||none|
|»»»»»» fileSubId|string|true|none||none|
|»»»»»» fileBizId|null|true|none||none|
|»»»»»» originVideoMd5|string|true|none||none|
|»»»»»» import_rich_media_context|null|true|none||none|
|»»»»»» sourceVideoCodecFormat|integer|true|none||none|
|»»»»»» storeID|integer|true|none||none|
|»»»»» grayTipElement|object|true|none||none|
|»»»»»» subElementType|integer|true|none||none|
|»»»»»» revokeElement|null|true|none||none|
|»»»»»» proclamationElement|null|true|none||none|
|»»»»»» emojiReplyElement|null|true|none||none|
|»»»»»» groupElement|null|true|none||none|
|»»»»»» buddyElement|null|true|none||none|
|»»»»»» feedMsgElement|null|true|none||none|
|»»»»»» essenceElement|null|true|none||none|
|»»»»»» groupNotifyElement|null|true|none||none|
|»»»»»» buddyNotifyElement|null|true|none||none|
|»»»»»» xmlElement|null|true|none||none|
|»»»»»» fileReceiptElement|object|true|none||none|
|»»»»»»» fileName|string|true|none||none|
|»»»»»» localGrayTipElement|null|true|none||none|
|»»»»»» blockGrayTipElement|null|true|none||none|
|»»»»»» aioOpGrayTipElement|null|true|none||none|
|»»»»»» jsonGrayTipElement|null|true|none||none|
|»»»»»» walletGrayTipElement|null|true|none||none|
|»»»»» arkElement|object¦null|true|none||none|
|»»»»»» bytesData|string|true|none||none|
|»»»»»» linkInfo|null|true|none||none|
|»»»»»» subElementType|null|true|none||none|
|»»»»» fileElement|object¦null|true|none||none|
|»»»»»» fileMd5|string|true|none||none|
|»»»»»» fileName|string|true|none||none|
|»»»»»» filePath|string|true|none||none|
|»»»»»» fileSize|string|true|none||none|
|»»»»»» picHeight|integer|true|none||none|
|»»»»»» picWidth|integer|true|none||none|
|»»»»»» picThumbPath|object|true|none||none|
|»»»»»» expireTime|string|true|none||none|
|»»»»»» file10MMd5|string|true|none||none|
|»»»»»» fileSha|string|true|none||none|
|»»»»»» fileSha3|string|true|none||none|
|»»»»»» videoDuration|integer|true|none||none|
|»»»»»» transferStatus|integer|true|none||none|
|»»»»»» progress|integer|true|none||none|
|»»»»»» invalidState|integer|true|none||none|
|»»»»»» fileUuid|string|true|none||none|
|»»»»»» fileSubId|string|true|none||none|
|»»»»»» thumbFileSize|integer|true|none||none|
|»»»»»» fileBizId|integer|true|none||none|
|»»»»»» thumbMd5|null|true|none||none|
|»»»»»» folderId|null|true|none||none|
|»»»»»» fileGroupIndex|integer|true|none||none|
|»»»»»» fileTransType|null|true|none||none|
|»»»»»» subElementType|integer|true|none||none|
|»»»»»» storeID|integer|true|none||none|
|»»»»» liveGiftElement|null|true|none||none|
|»»»»» markdownElement|null|true|none||none|
|»»»»» structLongMsgElement|null|true|none||none|
|»»»»» multiForwardMsgElement|null|true|none||none|
|»»»»» giphyElement|null|true|none||none|
|»»»»» walletElement|null|true|none||none|
|»»»»» inlineKeyboardElement|null|true|none||none|
|»»»»» textGiftElement|null|true|none||none|
|»»»»» calendarElement|null|true|none||none|
|»»»»» yoloGameResultElement|null|true|none||none|
|»»»»» avRecordElement|null|true|none||none|
|»»»»» structMsgElement|null|true|none||none|
|»»»»» faceBubbleElement|null|true|none||none|
|»»»»» shareLocationElement|null|true|none||none|
|»»»»» tofuRecordElement|null|true|none||none|
|»»»»» taskTopMsgElement|null|true|none||none|
|»»»»» recommendedMsgElement|null|true|none||none|
|»»»»» actionBarElement|null|true|none||none|
|»»»»» prologueMsgElement|null|true|none||none|
|»»»» records|[string]|true|none||none|
|»»»» emojiLikesList|[string]|true|none||none|
|»»»» commentCnt|string|true|none||none|
|»»»» directMsgFlag|integer|true|none||none|
|»»»» directMsgMembers|[string]|true|none||none|
|»»»» peerName|string|true|none||none|
|»»»» freqLimitInfo|null|true|none||none|
|»»»» editable|boolean|true|none||none|
|»»»» avatarMeta|string|true|none||none|
|»»»» avatarPendant|string|true|none||none|
|»»»» feedId|string|true|none||none|
|»»»» roleId|string|true|none||none|
|»»»» timeStamp|string|true|none||none|
|»»»» clientIdentityInfo|null|true|none||none|
|»»»» isImportMsg|boolean|true|none||none|
|»»»» atType|integer|true|none||none|
|»»»» roleType|integer|true|none||none|
|»»»» fromChannelRoleInfo|object|true|none||none|
|»»»»» roleId|string|true|none||none|
|»»»»» name|string|true|none||none|
|»»»»» color|integer|true|none||none|
|»»»» fromGuildRoleInfo|object|true|none||none|
|»»»»» roleId|string|true|none||none|
|»»»»» name|string|true|none||none|
|»»»»» color|integer|true|none||none|
|»»»» levelRoleInfo|object|true|none||none|
|»»»»» roleId|string|true|none||none|
|»»»»» name|string|true|none||none|
|»»»»» color|integer|true|none||none|
|»»»» recallTime|string|true|none||none|
|»»»» isOnlineMsg|boolean|true|none||none|
|»»»» generalFlags|object|true|none||none|
|»»»» clientSeq|string|true|none||none|
|»»»» fileGroupSize|null|true|none||none|
|»»»» foldingInfo|null|true|none||none|
|»»»» multiTransInfo|null|true|none||none|
|»»»» senderUin|string|true|none||none|
|»»»» peerUin|string|true|none||none|
|»»»» msgAttrs|object|true|none||none|
|»»»» anonymousExtInfo|null|true|none||none|
|»»»» nameType|integer|true|none||none|
|»»»» avatarFlag|integer|true|none||none|
|»»»» extInfoForUI|null|true|none||none|
|»»»» personalMedal|null|true|none||none|
|»»»» categoryManage|integer|true|none||none|
|»»»» msgEventInfo|null|true|none||none|
|»»»» sourceType|integer|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取群历史消息

POST /get_group_msg_history

> Body 请求参数

```json
{
  "group_id": 0,
  "message_seq": 0,
  "count": 20,
  "reverseOrder": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|number| 是 ||群号|
|» message_seq|body|number| 否 ||最新消息序号,填0或者不填表示从最新开始|
|» count|body|integer| 否 ||消息数量|
|» reverseOrder|body|boolean| 否 ||none|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "messages": [
            {
                "self_id": 721011692,
                "user_id": 721011692,
                "time": 1729603046,
                "message_id": 1170696403,
                "real_id": 1170696403,
                "message_seq": 1170696403,
                "message_type": "group",
                "sender": {
                    "user_id": 721011692,
                    "nickname": "--",
                    "card": "",
                    "role": "owner",
                    "title": ""
                },
                "raw_message": "[CQ:image,file=A507E29F9F727D689AE43A575A6B74A0.png,subType=0,url=https://multimedia.nt.qq.com.cn/download?appid=1407&amp;fileid=EhQSdGwB1zdTx3vOFHPIk4LH5klh7hj1lTUg_woowbaBuYmiiQMyBHByb2RQgL2jAVoQpNtWwVRr3APaJXD4AV4i-A&amp;spec=0&amp;rkey=CAMSKMa3OFokB_TlF7FTUNo885mvsACBYlQMuIeT35gwt0_yutJf2r5AaUQ,file_size=871157]",
                "font": 14,
                "sub_type": "normal",
                "message": [
                    {
                        "type": "image",
                        "data": {
                            "file": "A507E29F9F727D689AE43A575A6B74A0.png",
                            "subType": 0,
                            "url": "https://multimedia.nt.qq.com.cn/download?appid=1407&fileid=EhQSdGwB1zdTx3vOFHPIk4LH5klh7hj1lTUg_woowbaBuYmiiQMyBHByb2RQgL2jAVoQpNtWwVRr3APaJXD4AV4i-A&spec=0&rkey=CAMSKMa3OFokB_TlF7FTUNo885mvsACBYlQMuIeT35gwt0_yutJf2r5AaUQ",
                            "file_size": "871157"
                        }
                    }
                ],
                "message_format": "array",
                "post_type": "message_sent",
                "group_id": 860105388
            }
        ]
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» messages|[object]|true|none||none|
|»»» self_id|integer|false|none||none|
|»»» user_id|integer|false|none||none|
|»»» time|integer|false|none||none|
|»»» message_id|integer|false|none||none|
|»»» real_id|integer|false|none||none|
|»»» message_seq|integer|false|none||none|
|»»» message_type|string|false|none||none|
|»»» sender|object|false|none||none|
|»»»» user_id|integer|true|none||none|
|»»»» nickname|string|true|none||none|
|»»»» card|string|true|none||none|
|»»»» role|string|true|none||none|
|»»»» title|string|true|none||none|
|»»» raw_message|string|false|none||none|
|»»» font|integer|false|none||none|
|»»» sub_type|string|false|none||none|
|»»» message|[object]|false|none||none|
|»»»» type|string|false|none||none|
|»»»» data|object|false|none||none|
|»»»»» file|string|true|none||none|
|»»»»» subType|integer|true|none||none|
|»»»»» url|string|true|none||none|
|»»»»» file_size|string|true|none||none|
|»»» message_format|string|false|none||none|
|»»» post_type|string|false|none||none|
|»»» group_id|integer|false|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取转发消息详情

POST /get_forward_msg

> Body 请求参数

```json
{
  "message_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» message_id|body|string| 是 ||llonebot中，message_id为长id，在上报的转发消息中可以拿到|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "messages": [
            {
                "content": [
                    {
                        "type": "text",
                        "data": {
                            "text": "请输入正确的身高（cm）和体重（斤），如：bmi 175 145。"
                        }
                    }
                ],
                "sender": {
                    "nickname": "喵了6个咪",
                    "user_id": 1094950020
                },
                "time": 1729669148,
                "message_format": "array",
                "message_type": "group"
            }
        ]
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» messages|[object]|true|none||none|
|»»» content|[object]|false|none||none|
|»»»» type|string|false|none||none|
|»»»» data|object|false|none||none|
|»»»»» text|string|true|none||none|
|»»» sender|object|false|none||none|
|»»»» nickname|string|true|none||none|
|»»»» user_id|integer|true|none||none|
|»»» time|integer|false|none||none|
|»»» message_format|string|false|none||none|
|»»» message_type|string|false|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 标记消息已读

POST /mark_msg_as_read

> Body 请求参数

```json
{
    "message_id": 422622744
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» message_id|body|integer| 是 ||消息 ID|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 语音消息转文字

POST /voice_msg_to_text

llonebot 5.1 版本才支持此 api

> Body 请求参数

```json
{
    "message_id": 1365471751
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» message_id|body|integer| 是 ||消息 ID|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "text": "这个应该能可以。"
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» text|string|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 发送群 Ai 语音

POST /send_group_ai_record

此 API 需要 LLOneBot 5.6.1 及以上版本

> Body 请求参数

```json
{
    "character": "lucy-voice-suxinjiejie",
    "group_id": 12312313,
    "text": "你好呀"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» character|body|string| 是 ||语音声色，character_id|
|» group_id|body|integer| 是 ||群号|
|» text|body|string| 是 ||语音文本|
|» chat_type|body|integer| 否 ||语音类型|

#### 枚举值

|属性|值|
|---|---|
|» chat_type|1|
|» chat_type|2|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "message_id": 0
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» message_id|integer|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取群 Ai 语音可用声色列表

POST /get_ai_characters

此 API 需要 LLOneBot 5.6.1 及以上版本

> Body 请求参数

```json
{
  "group_id": 42,
  "chat_type": 1
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 否 ||群号|
|» chat_type|body|integer| 否 ||语音类型|

#### 枚举值

|属性|值|
|---|---|
|» chat_type|1|
|» chat_type|2|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": [
        {
            "characters": [
                {
                    "character_id": "lucy-voice-laibixiaoxin",
                    "character_name": "小新",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-laibixiaoxin.wav"
                },
                {
                    "character_id": "lucy-voice-houge",
                    "character_name": "猴哥",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-houge.wav"
                },
                {
                    "character_id": "lucy-voice-silang",
                    "character_name": "四郎",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-silang.wav"
                },
                {
                    "character_id": "lucy-voice-guangdong-f1",
                    "character_name": "东北老妹儿",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-guangdong-f1.wav"
                },
                {
                    "character_id": "lucy-voice-guangxi-m1",
                    "character_name": "广西大表哥",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-guangxi-m1.wav"
                },
                {
                    "character_id": "lucy-voice-daji",
                    "character_name": "妲己",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-daji.wav"
                },
                {
                    "character_id": "lucy-voice-lizeyan",
                    "character_name": "霸道总裁",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-lizeyan-2.wav"
                },
                {
                    "character_id": "lucy-voice-suxinjiejie",
                    "character_name": "酥心御姐",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-suxinjiejie.wav"
                }
            ],
            "type": "推荐"
        },
        {
            "characters": [
                {
                    "character_id": "lucy-voice-laibixiaoxin",
                    "character_name": "小新",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-laibixiaoxin.wav"
                },
                {
                    "character_id": "lucy-voice-houge",
                    "character_name": "猴哥",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-houge.wav"
                },
                {
                    "character_id": "lucy-voice-guangdong-f1",
                    "character_name": "东北老妹儿",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-guangdong-f1.wav"
                },
                {
                    "character_id": "lucy-voice-guangxi-m1",
                    "character_name": "广西大表哥",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-guangxi-m1.wav"
                },
                {
                    "character_id": "lucy-voice-m8",
                    "character_name": "说书先生",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-m8.wav"
                },
                {
                    "character_id": "lucy-voice-male1",
                    "character_name": "憨憨小弟",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-male1.wav"
                },
                {
                    "character_id": "lucy-voice-male3",
                    "character_name": "憨厚老哥",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-male3.wav"
                }
            ],
            "type": "搞怪"
        },
        {
            "characters": [
                {
                    "character_id": "lucy-voice-daji",
                    "character_name": "妲己",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-daji.wav"
                },
                {
                    "character_id": "lucy-voice-silang",
                    "character_name": "四郎",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-silang.wav"
                },
                {
                    "character_id": "lucy-voice-lvbu",
                    "character_name": "吕布",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-lvbu.wav"
                }
            ],
            "type": "古风"
        },
        {
            "characters": [
                {
                    "character_id": "lucy-voice-lizeyan",
                    "character_name": "霸道总裁",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-lizeyan-2.wav"
                },
                {
                    "character_id": "lucy-voice-suxinjiejie",
                    "character_name": "酥心御姐",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-suxinjiejie.wav"
                },
                {
                    "character_id": "lucy-voice-xueling",
                    "character_name": "元气少女",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-xueling.wav"
                },
                {
                    "character_id": "lucy-voice-f37",
                    "character_name": "文艺少女",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-f37.wav"
                },
                {
                    "character_id": "lucy-voice-male2",
                    "character_name": "磁性大叔",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-male2.wav"
                },
                {
                    "character_id": "lucy-voice-female1",
                    "character_name": "邻家小妹",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-female1.wav"
                },
                {
                    "character_id": "lucy-voice-m14",
                    "character_name": "低沉男声",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-m14.wav"
                },
                {
                    "character_id": "lucy-voice-f38",
                    "character_name": "傲娇少女",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-f38.wav"
                },
                {
                    "character_id": "lucy-voice-m101",
                    "character_name": "爹系男友",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-m101.wav"
                },
                {
                    "character_id": "lucy-voice-female2",
                    "character_name": "暖心姐姐",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-female2.wav"
                },
                {
                    "character_id": "lucy-voice-f36",
                    "character_name": "温柔妹妹",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-f36.wav"
                },
                {
                    "character_id": "lucy-voice-f34",
                    "character_name": "书香少女",
                    "preview_url": "https://res.qpt.qq.com/qpilot/tts_sample/group/lucy-voice-f34.wav"
                }
            ],
            "type": "现代"
        }
    ],
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|[object]|true|none||none|
|»» type|string|true|none||none|
|»» characters|[object]|true|none||none|
|»»» character_id|string|true|none||none|
|»»» character_name|string|true|none||none|
|»»» preview_url|string|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 发送戳一戳（双击头像）

POST /send_poke

此 API 需要 LLBot 7.11.3 及以上版本

> Body 请求参数

```json
{
  "group_id": 0,
  "user_id": 0,
  "target_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 是 ||none|
|» group_id|body|integer| 否 ||群号，不填则为私聊戳一戳|
|» user_id|body|integer| 是 ||用户 QQ 号|
|» target_id|body|integer| 否 ||目标 QQ 号，仅在私聊生效|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|null|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

# OneBot 11/接口列表/消息/发送私聊消息

## POST 发送私聊卡片(json)消息

POST /send_private_msg

json内容无法自定义，需要找签好名带token的

> Body 请求参数

```json
{
    "user_id": 370450326,
    "message": [
        {
            "type": "json",
            "data": {
                "data": "{    \"app\": \"com.tencent.music.lua\",    \"bizsrc\": \"qqconnect.sdkshare_music\",    \"config\": {        \"ctime\": 1736390927,        \"forward\": 1,        \"token\": \"9c72f3a00a1587f4b88eb91303c2a96c\",        \"type\": \"normal\"    },    \"extra\": {        \"app_type\": 1,        \"appid\": 100497308,        \"uin\": 3264925726    },    \"meta\": {        \"music\": {            \"app_type\": 1,            \"appid\": 100497308,            \"ctime\": 1736390927,            \"desc\": \" \",            \"jumpUrl\": \"https://mc.kurogames.com/m/\",            \"musicUrl\": \"https://mc.kurogames.com/m/\",            \"preview\": \"https://qq.ugcimg.cn/v1/dp7ec71e9hd5vdmmsv5ot2c9njd2i4n3i25oads477jcpi12h1brjrbrpum1clevmsp9tf77m0bmnd71f4r8jl9t7fntrmaefdah5jo/v697fvf8debh0gec94kh0e8u17c0jlfn8r7f6meo1lslp954nr0g\",            \"tag\": \"QQ音乐\",            \"tagIcon\": \"https://p.qpic.cn/qqconnect/0/app_100497308_1626060999/100?max-age=2592000&t=0\",            \"title\": \"LLOneBot启动！\",            \"uin\": 3264925726        }    },    \"prompt\": \"[分享]LLOneBot启动！\",    \"ver\": \"0.0.0.1\",    \"view\": \"music\"}"
            }
        }
    ]
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» user_id|body|integer| 是 ||对方 QQ 号|
|» message|body|[object]| 是 ||要发送的内容|
|»» type|body|string| 是 ||none|
|»» data|body|object| 是 ||none|
|»»» data|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "message_id": 696124706
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» message_id|integer|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 发送私聊合并转发消息

POST /send_private_forward_msg

> Body 请求参数

```json
{
    "user_id": "379450326",
    "messages": [
        {
            "type": "node",
            "data": {
                "content": [
                    {
                        "type": "text",
                        "data": {
                            "text": "hahahah"
                        }
                    }
                ]
            }
        }
    ]
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» user_id|body|integer| 是 ||对方 QQ 号|
|» messages|body|[object]| 是 ||要发送的内容|
|»» type|body|string| 是 ||none|
|»» data|body|object| 是 ||none|
|»»» id|body|integer| 否 ||转发消息 ID|
|»»» name|body|string| 否 ||发送者显示名字|
|»»» uin|body|integer| 否 ||发送者 QQ 号|
|»»» content|body|[object]| 否 ||具体消息|
|» source|body|string| 否 ||合并转发标题|
|» news|body|[object]| 否 ||合并转发预览文本，若提供，至少 1 条，至多 4 条|
|»» text|body|string| 是 ||none|
|» summary|body|string| 否 ||合并转发摘要|
|» prompt|body|string| 否 ||合并转发的预览外显文本，仅对移动端 QQ 有效|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "message_id": 1934956788
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» message_id|integer|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

# OneBot 11/接口列表/消息/发送群聊消息

## POST 发送群聊卡片(json)消息

POST /send_group_msg

json内容无法自定义，需要找签好名带token的

> Body 请求参数

```json
{
    "group_id": 123123,
    "message": [
        {
            "type": "json",
            "data": {
                "data": "{    \"app\": \"com.tencent.music.lua\",    \"bizsrc\": \"qqconnect.sdkshare_music\",    \"config\": {        \"ctime\": 1736390927,        \"forward\": 1,        \"token\": \"9c72f3a00a1587f4b88eb91303c2a96c\",        \"type\": \"normal\"    },    \"extra\": {        \"app_type\": 1,        \"appid\": 100497308,        \"uin\": 3264925726    },    \"meta\": {        \"music\": {            \"app_type\": 1,            \"appid\": 100497308,            \"ctime\": 1736390927,            \"desc\": \" \",            \"jumpUrl\": \"https://mc.kurogames.com/m/\",            \"musicUrl\": \"https://mc.kurogames.com/m/\",            \"preview\": \"https://qq.ugcimg.cn/v1/dp7ec71e9hd5vdmmsv5ot2c9njd2i4n3i25oads477jcpi12h1brjrbrpum1clevmsp9tf77m0bmnd71f4r8jl9t7fntrmaefdah5jo/v697fvf8debh0gec94kh0e8u17c0jlfn8r7f6meo1lslp954nr0g\",            \"tag\": \"QQ音乐\",            \"tagIcon\": \"https://p.qpic.cn/qqconnect/0/app_100497308_1626060999/100?max-age=2592000&t=0\",            \"title\": \"LLOneBot启动！\",            \"uin\": 3264925726        }    },    \"prompt\": \"[分享]LLOneBot启动！\",    \"ver\": \"0.0.0.1\",    \"view\": \"music\"}"
            }
        }
    ]
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» message|body|[object]| 是 ||要发送的内容|
|»» type|body|string| 是 ||none|
|»» data|body|object| 是 ||none|
|»»» data|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "message_id": 696124706
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» message_id|integer|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 发送群聊合并转发消息

POST /send_group_forward_msg

> Body 请求参数

```json
{
    "group_id": 12345,
    "messages": [
        {
            "type": "node",
            "data": {
                "uin": 379450326,
                "name": "喵喵喵",
                "content": [
                    {
                        "type": "text",
                        "data": {
                            "text": "hahahah"
                        }
                    },
                    {
                        "type": "image",
                        "data": {
                            "file": "http://i0.hdslb.com/bfs/archive/c8fd97a40bf79f03e7b76cbc87236f612caef7b2.png"
                        }
                    }
                ]
            }
        }
    ]
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» messages|body|[object]| 是 ||要发送的内容|
|»» type|body|string| 是 ||none|
|»» data|body|object| 是 ||none|
|»»» id|body|integer| 否 ||转发消息 ID|
|»»» name|body|string| 否 ||发送者显示名字|
|»»» uin|body|integer| 否 ||发送者 QQ 号|
|»»» content|body|[object]| 否 ||具体消息|
|» source|body|string| 否 ||合并转发标题|
|» news|body|[object]| 否 ||合并转发预览文本，若提供，至少 1 条，至多 4 条|
|»» text|body|string| 是 ||none|
|» summary|body|string| 否 ||合并转发摘要|
|» prompt|body|string| 否 ||合并转发的预览外显文本，仅对移动端 QQ 有效|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "message_id": 2026505362,
        "forward_id": "zUfJpEhzJgXxJID2cIwUoiRk7dMLSgnbhwb8yPrPz8iK6IsBn2uUQArcosp4WrNH"
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» message_id|integer|true|none||none|
|»» forward_id|string|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

# OneBot 11/接口列表/文件

## POST 上传群文件

POST /upload_group_file

> Body 请求参数

```json
{
    "group_id": 123123,
    "file": "d:/1.mp3",
    "name": "南红始边根之市.mp3"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» file|body|string| 是 ||文件路径|
|» name|body|string| 否 ||储存名称|
|» folder_id|body|string| 否 ||文件夹 ID，可通过 get_group_root_files 获取|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": {
    "file_id": "string"
  },
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» file_id|string|true|none||文件 ID|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 群文件转永久

POST /set_group_file_forever

需要 6.5.0 之后的版本

> Body 请求参数

```json
{
    "group_id": 164461995,
    "file_id": "/ba3bf4d6-6073-4a07-8bbd-8b0f6dd870b4"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» file_id|body|string| 是 ||文件id|

> 返回示例

> 200 Response

```json
{"status":"ok","retcode":0,"data":null,"message":"","wording":""}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|null|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 删除群文件

POST /delete_group_file

> Body 请求参数

```json
{
    "group_id": 379450326,
    // file_id 在上报的上传文件消息中可以拿到
    "file_id": "/c1c18801-670b-4eda-b02b-89c113ef3379"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» file_id|body|string| 是 ||文件 ID|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 移动群文件

POST /move_group_file

> Body 请求参数

```json
{
  "group_id": 0,
  "file_id": "string",
  "parent_directory": "string",
  "target_directory": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» file_id|body|string| 是 ||文件 ID|
|» parent_directory|body|string| 是 ||当前文件夹 ID|
|» target_directory|body|string| 是 ||目标文件夹 ID|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|null|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 创建群文件文件夹

POST /create_group_file_folder

> Body 请求参数

```json
{
    "group_id": 379450326,
    "name": "新建文件夹"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» name|body|string| 是 ||文件夹名称|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": {
    "folder_id": "string"
  },
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» folder_id|string|true|none||文件夹 ID|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 删除群文件文件夹

POST /delete_group_folder

> Body 请求参数

```json
{
    "group_id": 379450326,
    "folder_id": "/ee47f501-b92b-42a6-bfd1-d49b16a816b7"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» folder_id|body|string| 是 ||文件夹 ID|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 获取群文件系统信息

POST /get_group_file_system_info

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": {
    "file_count": 0,
    "limit_count": 0,
    "used_space": 0,
    "total_space": 0
  },
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» file_count|integer|true|none||文件总数|
|»» limit_count|integer|true|none||文件上限|
|»» used_space|integer|true|none||已使用空间|
|»» total_space|integer|true|none||空间上限|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取群根目录文件列表

POST /get_group_root_files

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": {
    "files": [
      {
        "group_id": 0,
        "file_id": "string",
        "file_name": "string",
        "busid": 0,
        "file_size": 0,
        "upload_time": 0,
        "dead_time": 0,
        "modify_time": 0,
        "download_times": 0,
        "uploader": 0,
        "uploader_name": "string"
      }
    ],
    "folders": [
      {
        "group_id": 0,
        "folder_id": "string",
        "folder_name": "string",
        "create_time": 0,
        "creator": 0,
        "creator_name": "string",
        "total_file_count": 0
      }
    ]
  },
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» files|[[FileEntity](#schemafileentity)]|true|none||none|
|»»» 群文件|[FileEntity](#schemafileentity)|false|none|群文件|none|
|»»»» group_id|integer|true|none||群号|
|»»»» file_id|string|true|none||文件 ID|
|»»»» file_name|string|true|none||文件名|
|»»»» busid|integer|true|none||文件类型|
|»»»» file_size|integer|true|none||文件大小|
|»»»» upload_time|integer|true|none||上传时间|
|»»»» dead_time|integer|true|none||过期时间，永久文件恒为0|
|»»»» modify_time|integer|true|none||最后修改时间|
|»»»» download_times|integer|true|none||下载次数|
|»»»» uploader|integer|true|none||上传者 ID|
|»»»» uploader_name|string|true|none||上传者名字|
|»» folders|[[FolderEntity](#schemafolderentity)]|true|none||none|
|»»» 群文件夹|[FolderEntity](#schemafolderentity)|false|none|群文件夹|none|
|»»»» group_id|integer|true|none||群号|
|»»»» folder_id|string|true|none||文件夹 ID|
|»»»» folder_name|string|true|none||文件名|
|»»»» create_time|integer|true|none||创建时间|
|»»»» creator|integer|true|none||创建者|
|»»»» creator_name|string|true|none||创建者名字|
|»»»» total_file_count|integer|true|none||子文件数量|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取群子目录文件列表

POST /get_group_files_by_folder

> Body 请求参数

```json
{
  "group_id": 0,
  "folder_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» folder_id|body|string| 是 ||文件夹 ID|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": {
    "files": [
      {
        "group_id": 0,
        "file_id": "string",
        "file_name": "string",
        "busid": 0,
        "file_size": 0,
        "upload_time": 0,
        "dead_time": 0,
        "modify_time": 0,
        "download_times": 0,
        "uploader": 0,
        "uploader_name": "string"
      }
    ],
    "folders": [
      {
        "group_id": 0,
        "folder_id": "string",
        "folder_name": "string",
        "create_time": 0,
        "creator": 0,
        "creator_name": "string",
        "total_file_count": 0
      }
    ]
  },
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» files|[[FileEntity](#schemafileentity)]|true|none||none|
|»»» 群文件|[FileEntity](#schemafileentity)|false|none|群文件|none|
|»»»» group_id|integer|true|none||群号|
|»»»» file_id|string|true|none||文件 ID|
|»»»» file_name|string|true|none||文件名|
|»»»» busid|integer|true|none||文件类型|
|»»»» file_size|integer|true|none||文件大小|
|»»»» upload_time|integer|true|none||上传时间|
|»»»» dead_time|integer|true|none||过期时间，永久文件恒为0|
|»»»» modify_time|integer|true|none||最后修改时间|
|»»»» download_times|integer|true|none||下载次数|
|»»»» uploader|integer|true|none||上传者 ID|
|»»»» uploader_name|string|true|none||上传者名字|
|»» folders|[[FolderEntity](#schemafolderentity)]|true|none||none|
|»»» 群文件夹|[FolderEntity](#schemafolderentity)|false|none|群文件夹|none|
|»»»» group_id|integer|true|none||群号|
|»»»» folder_id|string|true|none||文件夹 ID|
|»»»» folder_name|string|true|none||文件名|
|»»»» create_time|integer|true|none||创建时间|
|»»»» creator|integer|true|none||创建者|
|»»»» creator_name|string|true|none||创建者名字|
|»»»» total_file_count|integer|true|none||子文件数量|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 重命名群文件文件夹名

POST /rename_group_file_folder

> Body 请求参数

```json
{
  "group_id": 0,
  "folder_id": "string",
  "new_folder_name": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» folder_id|body|string| 是 ||文件夹 ID|
|» new_folder_name|body|string| 是 ||新文件夹名称|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|null|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 重命名群文件名

POST /rename_group_file

此 API 需要 LLBot 7.10.1 及以上版本

> Body 请求参数

```json
{
  "group_id": 0,
  "file_id": "string",
  "current_parent_directory": "string",
  "new_name": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 是 ||none|
|» group_id|body|integer| 是 ||群号|
|» file_id|body|string| 是 ||文件 ID|
|» current_parent_directory|body|string| 是 ||当前父目录|
|» new_name|body|string| 是 ||新文件名|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|null|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取群文件资源链接

POST /get_group_file_url

> Body 请求参数

```json
{
    "group_id": 90,
    "file_id": "/6744sdfsf-sdfadfsd"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» group_id|body|integer| 是 ||群号|
|» file_id|body|string| 是 ||文件 ID|

> 返回示例

> 200 Response

```json
{"status":"ok","retcode":0,"data":{"url":"file:///C:/Users/linyuchen/Documents/LiteLoaderQQNT/data/LLOneBot/temp/BMjAyMzA1MDExNDQwMjRfODUxMDMzODhfMTAxOTY3MDU5MzIwXzFfMw==_b_B610d398c0f170540e8b16e8b0c738cf5.mp4"},"message":"","wording":""}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» url|string|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取私聊文件资源链接

POST /get_private_file_url

此 API 需要 LLOneBot 5.9.0 及以上版本

> Body 请求参数

```json
{
  "file_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» file_id|body|string| 是 ||文件 ID|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": {
    "url": "string"
  },
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» url|string|true|none||文件下载链接|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 上传私聊文件

POST /upload_private_file

> Body 请求参数

```json
{
    "user_id": 379450326,
    "file": "https://www.yujn.cn/api/heisis.php",
    // 本地文件
    // "file": "file://d:\\1.mp4"
    
    // base64文件
    // "file": "base64://xxxxxxxxxxxxx"
    "name": "好看的.mp4"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» user_id|body|integer| 是 ||对方 QQ 号|
|» file|body|string| 是 ||文件路径|
|» name|body|string| 否 ||文件名称|

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": {
    "file_id": "string"
  },
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» file_id|string|true|none||文件 ID|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 上传闪传文件

POST /upload_flash_file

**此 API 需要 LLOneBot 5.3.0 以上版本**

上传进度会以事件形式上报
```json
"notice_type": "flash_file",
"sub_type": "uploading",  // uploaded 表示上传完成
```

> Body 请求参数

```json
{
    "title": "",
    "paths": [
        "file://d:/temp/1.png",
        "http://qq.com/test/1.mp3",
        "base64://YWRzZmZzZGZzZGY="
    ]
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» title|body|string| 否 ||标题|
|» paths|body|[string]| 是 ||文件路径，支持 file://、http://、base64:// 三种格式|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "file_set_id": "7ddae05e-934e-4bad-a89c-992b7cabb511",
        "share_link": "https://qfile.qq.com/q/l0qGdCLzry",
        "expire_time": 1752222668
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» file_set_id|string|true|none||none|
|»» share_link|string|true|none||none|
|»» expire_time|number|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 下载闪传文件

POST /download_flash_file

**此 API 需要 LLOneBot 5.3.0 以上版本**

下载进度会以事件形式上报
```json
"notice_type": "flash_file",
"sub_type": "downloading",  // downloaded 表示下载完成
```

> Body 请求参数

```json
{
    // "file_set_id": "65",
    "share_link": "https://monstrous-scratch.name/"    
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» share_link|body|string| 否 ||分享链接，和 file_set_id 二选一|
|» file_set_id|body|string| 否 ||文件集 ID|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": null,
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|null|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取闪传文件详情

POST /get_flash_file_info

**此 API 需要 LLOneBot 5.3.0 以上版本**

> Body 请求参数

```json
{
    "share_link": "https://qfile.qq.com/q/l0qGdCLzry"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» share_link|body|string| 否 ||分享链接，和 file_set_id 二选一|
|» file_set_id|body|string| 否 ||文件集 ID|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "file_set_id": "7ddae05e-934e-4bad-a89c-992b7cabb511",
        "title": "",
        "share_link": "https://qfile.qq.com/q/l0qGdCLzry",
        "total_file_size": "1712",
        "files": [
            {
                "name": "1.png",
                "size": 1712
            }
        ]
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» file_set_id|string|true|none||none|
|»» title|string|true|none||none|
|»» share_link|string|true|none||none|
|»» total_file_size|string|true|none|bytes|none|
|»» files|[object]|true|none||none|
|»»» name|string|false|none||none|
|»»» size|integer|false|none|bytes|none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 下载文件到缓存目录

POST /download_file

> Body 请求参数

```json
{
    "url": "https://www.yujn.cn/api/heisis.php",
    "name": "视频.mp4",
    "headers": [
        "User-Agent=YOUR_UA",
        "Referer=https://www.baidu.com"
    ]
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» url|body|string| 否 ||链接地址|
|» base64|body|string| 否 ||Base64 编码|
|» name|body|string| 否 ||文件名|
|» headers|body|[string]| 否 ||自定义请求头|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 重新分享闪传文件

POST /reshare_flash_file

**此 API 需要 LLBot 7.11.0 以上版本**
注意：只能重新分享还没有过期的闪传

> Body 请求参数

```json
{
    "file_set_id": "e8285b87-1b83-4afc-ac1a-c16e9e620fbb"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» file_set_id|body|string| 否 ||none|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "file_set_id": "f0c86396-d351-4cf5-bf2f-a9a22c1cfcae",
        "share_link": "https://qfile.qq.com/q/2pxTid3N56",
        "expire_time": 1774596230
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» file_set_id|string|true|none||none|
|»» share_link|string|true|none||none|
|»» expire_time|integer|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

# OneBot 11/接口列表/系统

## GET 获取登录号信息

GET /get_login_info

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "user_id": 379450326,
        "nickname": "linyuchen"
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» user_id|integer|true|none||none|
|»» nickname|string|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取登录号信息 Copy

POST /get_login_info

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "user_id": 379450326,
        "nickname": "linyuchen"
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» user_id|integer|true|none||none|
|»» nickname|string|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## GET 获取版本信息

GET /get_version_info

> 返回示例

> 200 Response

```json
{"status":"ok","retcode":0,"data":{"app_name":"LLOneBot","protocol_version":"v11","app_version":"4.1.2"},"message":"","wording":""}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» app_name|string|true|none||none|
|»» protocol_version|string|true|none||none|
|»» app_version|string|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST bot状态

POST /get_status

> 返回示例

> 200 Response

```json
{
  "status": "string",
  "retcode": 0,
  "data": {
    "online": true,
    "good": true,
    "stat": {
      "message_received": 0,
      "message_sent": 0,
      "last_message_time": 0,
      "startup_time": 0
    }
  },
  "message": "string",
  "wording": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» online|boolean|true|none||是否在线|
|»» good|boolean|true|none||状态是否良好|
|»» stat|object|true|none||运行统计|
|»»» message_received|integer|true|none||接收信息总数|
|»»» message_sent|integer|true|none||发送信息总数|
|»»» last_message_time|integer|true|none||最后一条消息时间|
|»»» startup_time|integer|true|none||启动时间|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## GET 清理缓存

GET /clean_cache

该 API 在 LLOneBot 5.0+ 之后失效

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 获取cookies

POST /get_cookies

> Body 请求参数

```json
{
    "domain": "qun.qq.com"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» domain|body|string| 是 ||需要获取 cookies 的域名|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "cookies": "pt2gguin=o0721011692; uin=o0721011692; skey=@SYMqFE5pd; pt_recent_uins=6330f7c148af161fd114030b3382c7075df4fed41289056d068fdf1e7e2641092e342182bc6db62bfcd310ed922aefd4a033604bb9dc6fbe; RK=5SXAfi4GP4; ptnick_721011692=2d2d; ptcz=0a61a3b0ac2020652d9727f1f34fb79c6fee28f10e0f74a84a009b742ef95b87; p_uin=o0721011692; pt4_token=5wdevAZtU1VcCrNJyqX1giQR7oq6Tlvaq6UO7WFZBOc_; p_skey=dgW58Yth9jO0KQsRGHUBcWcjI5MCtlaYTqrv*WcniW4_; tgw_l7_route=8842d3050439e5105ea26b0d5af4b071",
        "bkn": "1401060323"
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» cookies|string|true|none||none|
|»» bkn|string|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 设置在线状态

POST /set_online_status

> Body 请求参数

```json
{ "status": 10, "ext_status": 0, "battery_status": 0 }
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» status|body|integer| 是 ||状态|
|» ext_status|body|integer| 是 ||扩展状态|
|» battery_status|body|integer| 是 ||电量|

#### 枚举值

|属性|值|
|---|---|
|» status|10|
|» status|30|
|» status|40|
|» status|50|
|» status|60|
|» status|70|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 重启

POST /set_restart

该 API 在 LLOneBot 5.0+ 之后失效

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

## POST 扫描二维码

POST /scan_qrcode

需要7.2.0及以上版本

> Body 请求参数

```json
{
    "file": "base64://iVBORw0KGgoAAAANSUhEUgAAAlgAAAJYCAYAAAC+ZpjcAAAQAElEQVR4AezYgXLbyI4FUOL9/z9zh8lM1rEtWSLRzUb32XrMOBKJBg7o1K393+7/CBAgQIAAAQIEUgX+t/k/AgQIECAwnICGCNQWELBq70/3BAgQIECAwIACAtaAS9ESgQwBNQgQIEDgPgEB6z57JxMgQIAAAQKTCghYDxfrCwIECBAgQIDAOQEB65ybpwgQIECAwD0CTi0hIGCVWJMmCRAgQIAAgUoCAlalbemVAIEMATUIECDQXEDAak7sAAIECBAgQGA1AQFrtY1nzKsGAQIECBAg8FRAwHrK40sCBAgQIECgisBIfQpYI21DLwQIECBAgMAUAgLWFGs0BAECBDIE1CBAIEtAwMqSVIcAAQIECBAg8K+AgPUvhP8QyBBQgwABAgQIHAIC1qHgIkCAAAECBAgkCgwWsBInU4oAAQIECBAgcJOAgHUTvGMJECBAoJCAVgm8KSBgvQnmdgIECBAgQIDATwIC1k9CvidAIENADQIECCwlIGAttW7DEiBAgAABAj0EBKweyhlnqEGAAAECBAiUERCwyqxKowQIECBAYDwBHX0vIGB97+JTAgQIECBAgMBpAQHrNJ0HCRAgkCGgBgECMwoIWDNu1UwECBAgQIDArQIC1q38Ds8QUIMAAQIECIwmIGCNthH9ECBAgAABAuUF/rdt5WcwAAECBAgQIEBgKAH/H6yh1qEZAgQIEPgj4AcChQUErMLL0zoBAgQIECAwpoCANeZedEUgQ0ANAgQIELhJQMC6Cd6xBAgQIECAwLwCAtaz3fqOAAECBAgQIHBCQMA6geYRAgQIECBwp4CzxxcQsMbfkQ4JECBAgACBYgICVrGFaZcAgQwBNQgQINBWQMBq66s6AQIECBAgsKCAgLXg0jNGVoMAAQIECBB4LCBgPbbxDQECBAgQIFBLYJhuBaxhVqERAgQIECBAYBaBMgErIrYIVwSDiHMG2b+0Eef6iHj8XHaPK9eLeOwcce67Cp4R52aL+Pe5b/6bPXfE47MifBfBIOK5QfY72aJemYDVYng1CRAgQIAAAQItBASsFqpqrixgdgIECBAgsAlYXgICBAgQIECAQLLAeAEreUDlCBAgQIAAAQK9BQSs3uLOI0CAAIGSApom8I6AgPWOlnsJECBAgAABAi8ICFgvILmFAIEMATUIECCwjoCAtc6uTUqAAAECBAh0EhCwOkFnHKMGAQIECBAgUENAwKqxJ10SIECAAIFRBfT1jYCA9Q2KjwgQIECAAAECVwQErCt6niVAgECGgBoECEwnIGBNt1IDESBAgAABAncLCFh3b8D5GQJqECBAgACBoQQErKHWoRkCBAgQIEBgBoHfAWuGScxAgAABAgQIEBhEQMAaZBHaIECAAIGvAj4hUFVAwKq6OX0TIECAAAECwwoIWMOuRmMEMgTUIECAAIE7BASsO9SdSYAAAQIECEwtsHTA2vd9++ny/T1GU//WdR4uIraIsa8WJC1+dyPGdoyIFpQlarbYt5o5//6XeIEaNLl0wGrgqSQBAgQIEOgh4IzBBQSswRekPQIECBAgQKCegIBVb2c6JkAgQ0ANAgQINBQQsBriKk2AAAECBAisKSBgrbn3jKnVIECAAAECBB4ICFgPYHxMgAABAgQIVBQYo2cBa4w96IIAAQIECBCYSEDAmmiZRiFAgECGgBoECFwXELCuG6pAgAABAgQIEPhLQMD6i8NfCGQIqEGAAAECqwsIWKu/AeYnQIAAAQIE0gWGDFjpUypIgAABAgQIEOgoIGB1xHYUAQIECJQW0DyBlwUErJep3EiAAAECBAgQeE1AwHrNyV0ECGQIqEGAAIFFBASsRRZtTAIECBAgQKCfgIDVzzrjJDUIECBAgACBAgICVoElaZEAAQIECIwtoLvPAgLWZxF/J0CAAAECBAhcFBCwLgJ+fDwitoj1ro8Gfr4mEJH//lzr6OvT+75v2VdE/twR+TW/alz75KNj1s/XOvL0R4GI/HcoYvyaHw38fF5AwDpv50kCBAgQIECAwLcCAta3LD6sJ6BjAgQIECAwjoCANc4udEKAAAECBAhMIvAnYE0yjzEIECBAgAABArcLCFi3r0ADBAgQIPBEwFcESgoIWCXXpmkCBAgQIEBgZAEBa+Tt6I1AhoAaBAgQINBdQMDqTu5AAgQIECBAYHYBAevnDbuDAAECBAgQIPCWgID1FpebCRAgQIDAKAL6GFlAwBp5O3ojQIAAAQIESgoIWCXXpmkCBDIE1CBAgEArAQGrlay6BAgQIECAwLICAtayq88YXA0CBAgQIEDgOwEB6zsVnxEgQIAAAQJ1BQboXMAaYAlaIECAAAECBOYSELDm2qdpCBAgkCGgBgECFwUErIuAHidAgAABAgQIfBYQsD6L+DuBDAE1CBAgQGBpAQFr6fUbngABAgQIEGghMGrAajGrmgSWFNj3fcu8ImKLyL0y+/uvVoVlR+Q6RkTqritZVti3HtcSELDW2rdpCRAgQOCSgIcJvCYgYL3m5C4CBAgQIECAwMsCAtbLVG4kQCBDQA0CBAisICBgrbBlMxIgQIAAAQJdBQSsrtwZh6lBgAABAgQIjC4gYI2+If0RIECAAIEKAnr8S0DA+ovDXwgQIECAAAEC1wUErOuGKhAgQCBDQA0CBCYSELAmWqZRCBAgQIAAgTEEBKwx9qCLDAE1CBAgQIDAIAIC1iCL0AYBAgQIECAwj8DHgDXPVCYhQIAAAQIECNwoIGDdiO9oAgQIEHhFwD0E6gkIWPV2pmMCBAgQIEBgcAEBa/AFaY9AhoAaBAgQINBXQMDq6+00AgQIECBAYAEBAeulJbuJAAECBAgQIPC6gID1upU7CRAgQIDAWAK6GVZAwBp2NRojQIAAAQIEqgoIWFU3p28CBDIE1CBAgEATAQGrCauiBM4J7Pu+ZV8RsUXkXdn9HfXOaT1/6qibfT0/8f1vs/s76r3fhScIEGghIGC1UF2pplkJECBAgACBLwIC1hcSHxAgQIAAAQLVBe7uX8C6ewPOJ0CAAAECBKYTELCmW6mBCBAgkCGgBgECVwQErCt6niVAgAABAgQIfCMgYH2D4iMCGQJqECBAgMC6AgLWurs3OQECBAgQINBIYOCA1WhiZQkQIECAAAECjQUErMbAyhMgQIDAZALGIfCCgID1ApJbCBAgQIAAAQLvCAhY72i5lwCBDAE1CBAgML2AgDX9ig1IgAABAgQI9BYQsHqLZ5ynBgECBAgQIDC0gIA19Ho0R4AAAQIE6gjo9P8FBKz/t/ATAQIECBAgQCBFQMBKYVSEAAECGQJqECAwi4CANcsmzUGAAAECBAgMIyBgDbMKjWQIqEGAAAECBEYQELBG2IIeCBAgQIAAgakEPgWsqWbrPsy+79uKV3foQQ5ssetBRnvaRkRsEbnX0wNPfhmR22NEpP9+nxzNY50EWvyOV6jZiXf6YwSs6VdsQAIECEwgYAQCxQQErGIL0y4BAgQIECAwvoCANf6OdEggQ0ANAgQIEOgoIGB1xHYUAQIECBAgsIaAgPXqnt1HgAABAgQIEHhRQMB6EcptBAgQIEBgRAE9jSkgYI25F10RIECAAAEChQUErMLL0zoBAhkCahAgQCBfQMDKN1WRAAECBAgQWFxAwFr8BcgYXw0CBAgQIEDgbwEB628PfyNAgAABAgTmELh1CgHrVn6HEyBAgAABAjMKCFgzbtVMBAgQyBBQgwCB0wIC1mk6DxIgQIAAAQIEvhcQsL538SmBDAE1CBAgQGBRAQFr0cUbmwABAgQIEGgnMHbAaje3ygQIECBAgACBZgICVjNahQkQIEBgVgFzEfhJQMD6Scj3BAgQIECAAIE3BQSsN8HcToBAhoAaBAgQmFtg6YAVEVuEK2I8gwq/dhH5bhXm3vd9y74i8i2zezzqReT22WLfEbk9RkSLNtNrRoR/zwc1SF92kYJLB6wiO/q2TR8SIECAAAEC4woIWOPuRmcECBAgQKCagH7/FRCw/oXwHwIECBAgQIBAloCAlSWpDgECBDIE1CBAYAoBAWuKNRqCAAECBAgQGElAwBppG3rJEFCDAAECBAjcLiBg3b4CDRAgQIAAAQKzCXwNWLNNaB4CBAgQIECAQGcBAaszuOMIECBA4JyApwhUEhCwKm1LrwQIECBAgEAJAQGrxJo0SSBDQA0CBAgQ6CUgYPWSdg4BAgQIECCwjICA9caq3UqAAAECBAgQeEVAwHpFyT0ECBAgQGBcAZ0NKCBgDbgULREgQIAAAQK1BQSs2vvTPQECGQJqECBAIFlAwEoGVY4AAQIECBAgIGB5BzIE1CBAgAABAgQ+CAhYHzD8SIAAAQIECMwkcN8sAtZ99k4mQIAAAQIEJhUoE7D2fd9cDK68A5P+Dk8x1pW9Pno2IraI3GsK7DeHaHH7o5353L/xr74DLd7L7JplAlb24OoRIECAAAECBFoJCFitZNUl8EvAHwQIECCwooCAteLWzUyAAAECBAg0FRg+YDWdXnECBAgQIECAQAMBAasBqpIECBAgML2AAQk8FRCwnvL4kgABAgQIECDwvoCA9b6ZJwgQyBBQgwABAhMLCFgTL9doBAgQIECAwD0CAtY97hmnqkGAAAECBAgMKiBgDboYbREgQIAAgZoCuj4EBKxDwUWAAAECBAgQSBQQsBIxlSJAgECGgBoECNQXELDq79AEBAgQIECAwGACAtZgC9FOhoAaBAgQIEDgXgEB615/pxMgQIAAAQITCnwbsCac00gECBAgQIAAgW4CAlY3agcRIECAwEUBjxMoIyBglVmVRgkQIECAAIEqAgJWlU3pk0CGgBoECBAg0EVg6YAVEVvE2FeLtyAid+YKPUbkzhwR277v6VfE+H1G5PfY4h1qsZ/sPiPyLVedO3s3R72I/P1EqBlx3eDYz+jX0gHrxHI8QoAAAQIECBD4UUDA+pHIDQQIECBAYHQB/Y0mIGCNthH9ECBAgAABAuUFBKzyKzQAAQIZAmoQIEAgU0DAytRUiwABAgQIECDwj4CA9Q+C/2UIqEGAAAECBAj8JyBg/SfhvwQIECBAgMB8AjdNJGDdBO9YAgQIECBAYF4BAWve3ZqMAAECGQJqECBwQkDAOoHmEQIECBAgQIDAMwEB65mO7whkCKhBgAABAssJCFjLrdzABAgQIECAQGuBCgGrtYH6BAgQIECAAIFUAQErlVMxAgQIEFhHwKQEHgsIWI9tfEOAAAECBAgQOCUgYJ1i8xABAhkCahAgQGBWAQFr1s2aiwABAgQIELhNQMC6jT7jYDUIECBAgACBEQUErBG3oicCBAgQIFBZQO+bgOUlIECAAAECBAgkC5QJWBGxReReyZZNykXkzhwR6X1GRPpu9n3fsq/0wRUk0E5gqMoRub/jLYaLyO0xItL/Dcr+N61KvRb7rlCzTMCqgKlHAgQIECBAgMAhIGAdCq75BExEgAABAgRuFBCwbsR3TEp1/QAAEABJREFUNAECBAgQIDCnwKOANee0piJAgAABAgQIdBAQsDogO4IAAQIEsgTUIVBDQMCqsSddEiBAgAABAoUEBKxCy9IqgQwBNQgQIECgvYCA1d7YCQQIECBAgMBiAgLW2wv3AAECBAgQIEDguYCA9dzHtwQIECBAoIaALocSELCGWodmCBAgQIAAgRkEBKwZtmgGAgQyBNQgQIBAmoCAlUapEAECBAgQIEDgt4CA9dvBnxkCahAgQIAAAQK/BASsXwz+IECAAAECBGYVuGMuAesOdWcSIECAAAECUwsIWFOv13AECBDIEFCDAIF3BQSsd8XcT4AAAQIECBD4QUDA+gHI1wQyBNQgQIAAgbUEBKy19m1aAgQIECBAoINAkYC1bfu+D3912FfKERUsI2KLyL2y547I7S8imrzjKS/NhyLZjke9iHzLiPyaR6+jXx9WNeyPLQxbDBuR+w5V6DEid+aIaDF2iZplAlYJTU0SIECAwFoCpiXwQEDAegDjYwIECBAgQIDAWQEB66yc5wgQyBBQgwABAlMKCFhTrtVQBAgQIECAwJ0CAtad+hlnq0GAAAECBAgMJyBgDbcSDREgQIAAgfoCq08gYK3+BpifAAECBAgQSBcQsNJJFSRAgECGgBoECFQWELAqb0/vBAgQIECAwJACAtaQa9FUhoAaBAgQIEDgLgEB6y555xIgQIAAAQLTCjwJWNPObDACBAgQIECAQFMBAaspr+IECBAgkC6gIIECAgJWgSVpkQABAgQIEKglIGDV2pduCWQIqEGAAAECjQUErMbAyhMgQIAAAQLrCQhYZ3buGQIECBAgQIDAEwEB6wmOrwgQIECAQCUBvY4jIGCNswudECBAgAABApMICFiJi9z3fcu+EttrVioitojcK9vxqJcNcNTMvrJ7POpF5O7mqJl9ZTuer/f8dzh77ojc3UREdotN6kVE+r8ZLRrNfo8q9HjMnN3nUTP7yu6xRT0Bq4WqmgQIECBAgMDSAgLW0uvPH15FAgQIECBAYNsELG8BAQIECBAgMLtA9/kErO7kDiRAgAABAgRmFxCwZt+w+QgQIJAhoAYBAm8JCFhvcbmZAAECBAgQIPCzgID1s5E7CGQIqEGAAAECCwkIWAst26gECBAgQIBAH4E6AauPh1MIECBAgAABApcFBKzLhAoQIECAwMoCZifwnYCA9Z2KzwgQIECAAAECFwQErAt4HiVAIENADQIECMwnIGDNt1MTESBAgAABAjcLCFg3LyDjeDUIECBAgACBsQQErLH2oRsCBAgQIDCLwNJzCFhLr9/wBAgQIECAQAsBAauFqpoECBDIEFCDAIGyAgJW2dVpnAABAgQIEBhVQMAadTP6yhBQgwABAgQI3CIgYN3C7lACBAgQIEBgZoHnAWugySNiixj7asG17/uWfbXoM7tmxNi7jojskX/Vi4j09/xX4cQ/IvJ7jMivmThys1LZv9tHvYg1LZstKbFwxJq7iVhz7jIBK/EdV4oAAQIEigton8DoAgLW6BvSHwECBAgQIFBOQMAqtzINE8gQUIMAAQIEWgoIWC111SZAgAABAgSWFBCwTq7dYwQIECBAgACBRwIC1iMZnxMgQIAAgXoCOh5EQMAaZBHaIECAAAECBOYRELDm2aVJCBDIEFCDAAECCQICVgKiEgQIECBAgACBjwIC1kcNP2cIqEGAAAECBJYXELCWfwUAECBAgACBFQT6zihg9fV2GgECBAgQILCAgIC1wJKNSIAAgQwBNQgQeF1AwHrdyp0ECBAgQIAAgZcEBKyXmNxEIENADQIECBBYRUDAWmXT5iRAgAABAgS6CZQKWN1UHESAAAECBAgQuCAgYF3A8ygBAgQIENi2DQKBLwIC1hcSHxAgQIAAAQIErgkIWNf8PE2AQIaAGgQIEJhMoEzA2vd9y74m2+VU42Tv+qhXAejoM/sy97gCEbFF5F7jTtu2s+zfm6Ne247HrX7MnnmNO2nbzsoErLYM5asbgAABAgQIEBhIQMAaaBlaIUCAAAECcwmsO42Ate7uTU6AAAECBAg0EhCwGsEqS4AAgQwBNQgQqCkgYNXcm64JECBAgACBgQUErIGXo7UMATUIECBAgEB/AQGrv7kTCRAgQIAAgckFfgxYk89vPAIECBAgQIBAuoCAlU6qIAECBAh0EHAEgaEFBKyh16M5AgQIECBAoKKAgFVxa3omkCGgBgECBAg0ExCwmtEqTIAAAQIECKwqIGCd37wnCRAgQIAAAQLfCghY37L4kAABAgQIVBXQ9wgCAtYIW9ADAQIECBAgMJWAgDXVOg1DgECGgBoECBC4KiBgXRX0PAECBAgQIEDgk4CA9QnEXzME1CBAgAABAmsLCFhr79/0BAgQIEBgHYGOkwpYHbEdRYAAAQIECKwhUCZgRcQWkXvt+75lXlVemYixHY+dROT2GBGpuz56rLLv7D6P2bOv7B5b1YvIfS9b9Zld98O+U36Psvs76kXk7iYiv16241EvIr/PiNyax35WvMoErBWXY2YCBAgQIECgpoCAVXNvuq4qoG8CBAgQWEJAwFpizYYkQIAAAQIEegpUC1g9bZxFgAABAgQIEDglIGCdYvMQAQIECBD4KOBnAn8LCFh/e/gbAQIECBAgQOCygIB1mVABAgQyBNQgQIDATAIC1kzbNAsBAgQIECAwhICANcQaMppQgwABAgQIEBhFQMAaZRP6IECAAAECMwosOpOAtejijU2AAAECBAi0ExCw2tmqTIAAgQwBNQgQKCggYBVcmpYJECBAgACBsQUErLH3o7sMATUIECBAgEBnAQGrM7jjCBAgQIAAgfkFXglY8yuYkAABAgQIECCQKCBgJWIqRYAAAQI9BZxFYFwBAWvc3eiMAAECBAgQKCogYBVdnLYJZAioQYAAAQJtBMoErH3ft+wrIraI9a42r1Ju1exdH/Ui1tt1ROQuplG1iEj/XWzUamrZ473MvlIbXLxY9m4i8t/z7B6PetlrP2pmX9k9tqhXJmC1GP56TRUIECBAgAABAl8FBKyvJj4hQIAAAQK1BXR/u4CAdfsKNECAAAECBAjMJiBgzbZR8xAgkCGgBgECBC4JCFiX+DxMgAABAgQIEPgqIGB9NfFJhoAaBAgQIEBgYQEBa+HlG50AAQIECKwm0GteAauXtHMIECBAgACBZQQErGVWbVACBAhkCKhBgMArAgLWK0ruIUCAAAECBAi8ISBgvYHlVgIZAmoQIECAwPwCAtb8OzYhAQIECBAg0FmgYMDqLOQ4AgQIECBAgMCbAgLWm2BuJ0CAAAEC3wr4kMAHAQHrA4YfCRAgQIAAAQIZAgJWhqIaBAhkCKhBgACBaQQErGlWaRACBAgQIEBgFAEBa5RNZPShBgECBAgQIDCEgIA1xBo0QYAAAQIE5hVYcTIBa8Wtm5kAAQIECBBoKlAmYEXEFpF77fu+rXg1faOSikfk7joikjqrVyb7Ha8iEBHp/2Zkzx7xao+v35fd41Ev4vXzI36+96hZ4Yr4eZaI1++pMPPR46r/ZhyzZ15lAlbm0GoRIECAAAECBFoKCFgtddUeRkAjBAgQIECgp4CA1VPbWQQIECBAgMASAi8GrCUsDEmAAAECBAgQSBEQsFIYFSFAgACBWwQcSmBQAQFr0MVoiwABAgQIEKgrIGDV3Z3OCWQIqEGAAAECDQQErAaoShIgQIAAAQJrCwhYV/fveQIECBAgQIDAJwEB6xOIvxIgQIAAgRkEzHCvgIB1r7/TCRAgQIAAgQkFBKwJl2okAgQyBNQgQIDAeQEB67ydJwkQIECAAAEC3woIWN+y+DBDQA0CBAgQILCqgIC16ubNTYAAAQIE1hToMrWA1YXZIQQIECBAgMBKAgLWSts2KwECBDIE1CBA4EcBAetHIjcQIECAAAECBN4TELDe83I3gQwBNQgQIEBgcgEBa/IFG48AAQIECBDoL1AmYO37vv25kn7uzz3GiRUcs3tsUW+Mbeqip0D2e9Sz9ytnZc9dpd4Vs17PRsQWsd7Vy/fKOWUC1pUhPUuAAAECBHoIOIPAfwIC1n8S/kuAAAECBAgQSBIQsJIglSFAIENADQIECMwhIGDNsUdTECBAgAABAgMJCFgDLSOjFTUIECBAgACB+wUErPt3oAMCBAgQIDC7wHLzCVjLrdzABAgQIECAQGsBAau1sPoECBDIEFCDAIFSAgJWqXVplgABAgQIEKggIGBV2JIeMwTUIECAAAEC3QQErG7UDiJAgAABAgRWEXg9YK0iYk4CBAgQIECAwEUBAesioMcJECBA4F4BpxMYUUDAGnEreiJAgAABAgRKCwhYpdeneQIZAmoQIECAQLaAgJUtqh4BAgQIECCwvICAlfAKKEGAAAECBAgQ+CggYH3U8DMBAgQIEJhHwCQ3CghYN+I7mgABAgQIEJhToEzAiogtwhXBIOKcQYVf4X3ft+wre+6Ic/4Rj5/L7vGol+L4aR8Rj2eIeP+7Fj0es49+RbxvFfH8mdFnPvprse8WNY9eXdcFygSs66OqQIAAAQIECBDoIyBg9XFe9RRzEyBAgACBJQUErCXXbmgCBAgQILCyQPvZBaz2xk4gQIAAAQIEFhMQsBZbuHEJECCQIaAGAQLPBQSs5z6+JUCAAAECBAi8LSBgvU3mAQIZAmoQIECAwMwCAtbM2zUbAQIECBAgcItA2YB1i5ZDCRAgQIAAAQIvCAhYLyC5hQABAgQIvCjgNgK/BASsXwz+IECAAAECBAjkCQhYeZYqESCQIaAGAQIEJhAQsCZYohEIECBAgACBsQQErLH2kdGNGgQIECBAgMDNAgLWzQtwPAECBAgQWENgrSkFrLX2bVoCBAgQIECgg4CA1QHZEQQIEMgQUIMAgToCAladXemUAAECBAgQKCIgYBVZlDYzBNQgQIAAAQJ9BASsPs5OIUCAAAECBBYSeCtgzeay7/vmGtOgwrvW4t1pMXdEbBF5V4seq1hmzx6Rt5eI37Wye2xRz75/7yri+n+r7Cd75y3mzq65dMDKxlSPAAECBG4RcCiB4QQErOFWoiECBAgQIECguoCAVX2D+ieQIaAGAQIECKQKCFipnIoRIECAAAECBLZNwMp5C1QhQIAAAQIECPwRELD+UPiBAAECBAjMJmCeuwQErLvknUuAAAECBAhMKyBgTbtagxEgkCGgBgECBM4ICFhn1DxDgAABAgQIEHgiIGA9wfFVhoAaBAgQIEBgPQEBa72dm5gAAQIECBBoLCBgNQZWngABAgQIEFhPQMBab+cmJkCAQIaAGgQIPBEQsJ7g+IoAAQIECBAgcEZAwDqj5hkCGQJqECBAgMC0AgLWtKs1GAECBAgQIHCXQOWAdZeZcwkQIECAAAECTwUErKc8viRAgAABAu8KuJ/AtglY3gICBAgQIECAQLKAgJUMqhwBAtcFVCBAgEB1AQErcYMRsUWsdyUSlioVkSg90JwAAAmzSURBVL/rUgCJzUbUsNz3fRv9SlzLn1IR+fuJGL/mH4CkH1q8O0mt/VUmInc3fxVf6C8C1pTLNhQBAgQIECBwp4CAdae+swkQIECAwEoCC80qYC20bKMSIECAAAECfQQErD7OTiFAgECGgBoECBQRELCKLEqbBAgQIECAQB0BAavOrnSaIaAGAQIECBDoICBgdUB2BAECBAgQILCWwLsBay0d0xIgQIAAAQIETggIWCfQPEKAAAECownoh8BYAgLWWPvQDQECBAgQIDCBgIA1wRKNQCBDQA0CBAgQyBMQsPIsVSJAgAABAgQI/BIQsH4xZPyhBgECBAgQIEDgt4CA9dvBnwQIECBAYE4BU90iIGDdwu5QAgQIECBAYGYBAWvm7ZqNAIEMATUIECDwtoCA9TaZBwgQIECAAAECzwUErOc+vs0QUIMAAQIECCwmIGAttnDjEiBAgAABAr8FWv4pYLXUVXtqgX3ft+wrIraI3Cu7xypLjch1jMiv18Iye98r12uxn+yaETXey+y5K9QTsCpsSY8ECBAYUkBTBAg8EhCwHsn4nAABAgQIECBwUkDAOgnnMQIZAmoQIECAwJwCAtacezUVAQIECBAgcKNA8YB1o5yjCRAgQIAAAQIPBASsBzA+JkCAAAECpwU8uLyAgLX8KwCAAAECBAgQyBYQsLJF1SNAIENADQIECJQWELBKr0/zBAgQIECAwIgCAtaIW8noSQ0CBAgQIEDgNgEB6zZ6BxMgQIAAgfUEVplYwFpl0+YkQIAAAQIEugkIWN2oHUSAAIEMATUIEKggIGBV2JIeCRAgQIAAgVICAlapdWk2Q0ANAgQIECDQWkDAai2sPgECBAgQILCcwImAtZyRgQkQIECAAAECbwkIWG9xuZkAAQIEhhXQGIGBBASsgZahFQIECBAgQGAOAQFrjj2agkCGgBoECBAgkCQgYCVBKrOeQERsEbnXvu9b9hUxfo/rvT2/J47I3U1E/C684J8Rkf77mM0Ykd9j9r8XLepF5M+dvZsW9QSsTFW1CBAgQIAAAQL/CAhY/yD4HwECBAgQmFnAbP0FBKz+5k4kQIAAAQIEJhcQsCZfsPEIEMgQUIMAAQLvCQhY73m5mwABAgQIECDwo4CA9SORGzIE1CBAgAABAisJCFgrbdusBAgQIECAwEeBZj8LWM1oFSZAgAABAgRWFRCwVt28uQkQIJAhoAYBAt8KCFjfsviQAAECBAgQIHBeQMA6b+dJAhkCahAgQIDAhAIC1oRLNRIBAgQIECBwr0D9gHWvn9MJECBAgAABAl8EBKwvJD4gQIAAAQLXBVRYW0DAWnv/pidAgAABAgQaCAhYDVCVJEAgQ0ANAgQI1BUQsOruTucECBAgQIDAoAIC1qCLyWhLDQIECBAgQOAeAQHrHnenEiBAgACBVQWWmFvAWmLNhiRAgAABAgR6CghYidr7vm8rXomEShUQiIgtIvcqMPZYLT7pJiJ3NxHx5LRzX0VE+jvU4t/ec9PVfyoidz+r7kbAqv+7YAICBAgQIEBgMAEBa7CFaKeLgEMIECBAgEBTAQGrKa/iBAgQIECAwIoC5wLWilJmJkCAAAECBAi8KCBgvQjlNgIECBAYX0CHBEYRELBG2YQ+CBAgQIAAgWkEBKxpVmkQAhkCahAgQIBAhoCAlaGoBgECBAgQIEDgg4CA9QEj40c1CBAgQIAAAQIClneAAAECBAjML2DCzgICVmdwxxEgQIAAAQLzCwhY8+/YhAQIZAioQYAAgTcEBKw3sNxKgAABAgQIEHhFQMB6Rck9GQJqECBAgACBZQQErGVWbVACBAgQIEDgq0CbTwSsNq6qEiBAgAABAgsLCFgLL9/oBAgQyBBQgwCBrwIC1lcTnxAgQIAAAQIELgkIWJf4PEwgQ0ANAgQIEJhNYOmAFRFbhCtiPIMKv2j7vm/ZV4u5K/RYYe7DsUWfFWpG5P4bcVhmXxG5PUZE+u939sxHvRXfn4ioMPY2RcAqIa1JAgQIECBAYBkBAWuZVRuUAAECBDoLOG5hAQFr4eUbnQABAgQIEGgjIGC1cVWVAIEMATUIECBQVEDAKro4bRMgQIAAAQLjCghY4+4mozM1CBAgQIAAgRsEBKwb0B1JgAABAgTWFph/egFr/h2bkAABAgQIEOgsIGB1BnccAQIEMgTUIEBgbAEBa+z96I4AAQIECBAoKCBgFVyaljME1CBAgAABAu0EBKx2tioTIECAAAECiwqcDliLehmbAAECBAgQIPCjgID1I5EbCBAgQKCQgFYJDCEgYA2xBk0QIECAAAECMwkIWDNt0ywEMgTUIECAAIHLAgLWZUIFCBAgQIAAAQJ/CwhYf3tk/E0NAgQIECBAYHEBAWvxF8D4BAgQILCKgDl7CghYPbWdRYAAAQIECCwhUCZg7fu+uRhceQeW+I3uMOSVHfR8tgVFz/5nPqvKblr0WaFmhXevgmOZgFUBU48ECBAgQIAAgUNAwDoUXJ0EHEOAAAECBNYQELDW2LMpCRAgQIAAgUcCDT4XsBqgKkmAAAECBAisLSBgrb1/0xMgQCBDQA0CBD4JCFifQPyVAAECBAgQIHBVQMC6Kuh5AhkCahAgQIDAVAIC1lTrNAwBAgQIECAwgsAsAWsESz0QIECAAAECBH4JCFi/GPxBgAABAgRaCKi5qoCAtermzU2AAAECBAg0ExCwmtEqTIBAhoAaBAgQqCggYFXcmp4JECBAgACBoQUErKHXk9GcGgQIECBAgEBvAQGrt7jzCBAgQIAAgW2b3EDAmnzBxiNAgAABAgT6CwhY/c2dSIAAgQwBNQgQGFhAwBp4OVojQIAAAQIEagoIWDX3pusMATUIECBAgEAjAQGrEayyBAgQIECAwLoCVwLWumomJ0CAAAECBAg8ERCwnuD4igABAgQqCuiZwP0CAtb9O9ABAQIECBAgMJmAgDXZQo1DIENADQIECBC4JiBgXfPzNAECBAgQIEDgi4CA9YUk4wM1CBAgQIAAgZUFBKyVt292AgQIEFhLwLTdBASsbtQOIkCAAAECBFYRELBW2bQ5CRDIEFCDAAECLwkIWC8xuYkAAQIECBAg8LqAgPW6lTszBNQgQIAAAQILCAhYCyzZiAQIECBAgMBzgexvBaxsUfUIECBAgACB5QUErOVfAQAECBDIEFCDAIGPAgLWRw0/EyBAgAABAgQSBASsBEQlCGQIqEGAAAEC8wgIWPPs0iQECBAgQIDAIAITBaxBRLVBgAABAgQILC8gYC3/CgAgQIAAgaYCii8pIGAtuXZDEyBAgAABAi0F/g8AAP//u2PQFAAAAAZJREFUAwC+ZDEhjiUm1wAAAABJRU5ErkJggg=="
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» file|body|string| 是 ||支持http(s)://, file://, base64://|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": [
        {
            "text": "http://qq.com"
        }
    ],
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|[object]|true|none||none|
|»» text|string|false|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

# OneBot 11/接口列表/其他

## POST 图片 OCR

POST /ocr_image

> Body 请求参数

```json
{
    // http 图片
    "image": "http://i0.hdslb.com/bfs/archive/c8fd97a40bf79f03e7b76cbc87236f612caef7b2.png"

    // 本地图片
    // "image": "file://d:\\1.jpg"

    // base64图片
    // "image": "base64://xxxxxx"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» image|body|string| 是 | 图片路径或链接|支持http://, file://, base64://|

> 返回示例

> 200 Response

```json
{"status":"ok","retcode":0,"data":{"texts":[{"text":"Sssr","confidence":1,"coordinates":[{"x":32,"y":20},{"x":185,"y":18},{"x":187,"y":89},{"x":34,"y":92}]}],"language":""},"message":"","wording":""}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» texts|[object]|true|none||none|
|»»» text|string|false|none||none|
|»»» confidence|integer|false|none||none|
|»»» coordinates|[object]|false|none||none|
|»»»» x|integer|true|none||none|
|»»»» y|integer|true|none||none|
|»» language|string|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## GET 获取图片rkey

GET /get_rkey

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "private_key": "&rkey=CAMSMBpHmxmalRynJ6OVvBU7LBRRSSKHTdiluhEB2Cnz9uuQ-RPsf0sPGLRJv1CgMVKrMg",
        "group_key": "&rkey=CAMSMBpHmxmalRynJ6OVvBU7LBRRSSKHTdilujmnQcVbrunT0aSihL9lJD0ywLfiRyJC-Q",
        "expired_time": 1751717813,
        "updated_time": "2025-07-05 19:26:53"
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» private_key|string|true|none||none|
|»» group_key|string|true|none||none|
|»» expired_time|integer|true|none||none|
|»» updated_time|string|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 获取推荐表情

POST /get_recommend_face

需 5.5.0 版本及以上

> Body 请求参数

```json
{
  "word": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» word|body|string| 是 ||关键词|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "url": [
            "https://wa.qq.com/qgif-web/0b90edbfe798e72c8d1022de9d9bb037.gif?sign=f322a18673973627c748ad903659bb2a&t=1753005249",
            "https://wa.qq.com/qgif-web/0b862da6938a8233a8cd2df6130e6152.gif?sign=871f5bbe96536d94f08465a728fe8101&t=1753005249",
            "https://wa.qq.com/qgif-web/03e91faf53a475a1319ed7b58f1da687.gif?sign=3ee66a495d5d7326c6a812a4d30bf6cc&t=1752920264",
            "https://wa.qq.com/qgif-web/039865ef68d849e9f5b52a39507c4cf3.jpg?sign=3e64ec45562392e863a97a0c225ea03d&t=1753001962",
            "https://wa.qq.com/qgif-web/0649c141c0400f22c44b664496751c57.jpg?sign=a281d8279be27d19020999cda27d9b90&t=1753002934",
            "https://wa.qq.com/qgif-web/74f636e46d751b56dc6614b26db18d99.jpg?sign=be550e708ffed1f906e28361b621deb4&t=1752976980",
            "https://wa.qq.com/qgif-web/bd1a69793dffdad2792238607eea4cf8.png?sign=f94683a1876d5c04711b6b0902b0e573&t=1752976896",
            "https://wa.qq.com/qgif-web/058ceed24a73968e9f1b4d7edb6d1a94.jpg?sign=f8b0bcb80e389303f4cf52ef84e4d4aa&t=1752976918",
            "https://wa.qq.com/qgif-web/0f1018d508e1aa1139c5efe6218fede4.gif?sign=0cc9f3692e7a41fb2c663ca047dc46e9&t=1752976832",
            "https://wa.qq.com/qgif-web/d2d55ab7d7d32806f40b0f6f89431cb0.jpg?sign=9222ad58c569e385f9c2d2259648e8ec&t=1753002953",
            "https://wa.qq.com/qgif-web/86767516255a9e814a576847a2cf9dc0.png?sign=3b2ad8027c7f948b91853823dd44c1ec&t=1752976935",
            "https://wa.qq.com/qgif-web/78d915f7962d9f97c2ecad65a6fc6751.gif?sign=2581d87607bb8ac0b6e4d872c6b61cc6&t=1752918380",
            "https://wa.qq.com/qgif-web/750d9a45d36469c41e8adba5f3fb6e11.gif?sign=f3c225d9855cba4d7765b98d3b33b2c3&t=1753002111",
            "https://wa.qq.com/qgif-web/f0d706516124030aea8f3fdb60310afe.png?sign=c61a5cd46ed72ccce2959d25f54ce745&t=1752976896",
            "https://wa.qq.com/qgif-web/afc0fef5af8c7ed2744f38a80386c744.gif?sign=4ee371e4555944fcdc4438165901c793&t=1752977030",
            "https://wa.qq.com/qgif-web/f8a7c81c29bc1eb864f9a18ae14cfb37.gif?sign=84fb43a97aada1ae648635f9bd9a0e87&t=1752976837",
            "https://wa.qq.com/qgif-web/df8cd3b2aa3a00e65efe14ab6072c3aa.gif?sign=315b491a0cce50fe83459055db0b8ef7&t=1752977030",
            "https://wa.qq.com/qgif-web/d4e6c50316dc0ee3597912416d019a76.jpg?sign=d58ffd8c6253aede1d8aeef632c9e4e5&t=1752916891",
            "https://wa.qq.com/qgif-web/f68a17d33b8ee84d77eb16c58e65232a.png?sign=8d29d6e99d9961a0f0862c332f3f683c&t=1752976896",
            "https://wa.qq.com/qgif-web/a30f0cbf4ed811940afab19acbf03dca.jpg?sign=05531b833dbde188e66fc871e32cbc6f&t=1752918180",
            "https://wa.qq.com/qgif-web/c19fa7bb0d5b46b044912b8fac262335.jpg?sign=5f723e3586597f67d5ab12e9710930ec&t=1752977012",
            "https://wa.qq.com/qgif-web/619c4c598524fd7ec9028cd6aef106db.jpg?sign=9f01ee3473a8e00e1c3f88d57e266e26&t=1752977083",
            "https://wa.qq.com/qgif-web/95d6543dce0f031e85602838dd33270a.jpg?sign=b8ccd4dc0968c584c09e75b711dacd7e&t=1752976843",
            "https://wa.qq.com/qgif-web/29cd3cb19ad512a4a7d0d992dac84537.jpg?sign=dc2bc22b3de4273cea496d29eb329385&t=1752976843",
            "https://wa.qq.com/qgif-web/6bc6e5eb2e20ab4d93ca971c877ed137.jpg?sign=4a19bc1943903ddde796ff112551ceae&t=1752977034",
            "https://wa.qq.com/qgif-web/ac47d12522af0eb32ee4d2024337b404.jpg?sign=3757a97557567f93e52c641c89b638b5&t=1753002260",
            "https://wa.qq.com/qgif-web/05feee88cda9e3b14619c7ca8cc5a994.gif?sign=826ac6a285ef2b0ab0ba603c25059c00&t=1752976832",
            "https://wa.qq.com/qgif-web/6947f77749de969dbbc7e0822f68ef87.jpg?sign=5ac53dfcc8523f7b6cb55273abd051b1&t=1752977085",
            "https://wa.qq.com/qgif-web/6e62673b07662778ca2b19c55ecd027b.png?sign=8386000f8e3272cd128dbab570571f25&t=1752977082",
            "https://wa.qq.com/qgif-web/378cbb4c8c3c0476536834735de60146.gif?sign=ee6fb43518da8ee43cb86cae74ded126&t=1752976846",
            "https://wa.qq.com/qgif-web/63a672df093498a478d5344d94b5437b.gif?sign=9e952c4a446b3ab3acc874619b222d84&t=1752918597",
            "https://wa.qq.com/qgif-web/b724b706a690a51515a3399816c9dc6c.gif?sign=8ae7e9f90e630df449052a98e5e7d692&t=1752916576",
            "https://wa.qq.com/qgif-web/6c9918d1f9e70f736d1d79fabd12a932.gif?sign=c61052c8149868c272fcd438f12d5593&t=1752976935",
            "https://wa.qq.com/qgif-web/935bfa9dd90e1cbf65a859c7bad1e1f5.jpg?sign=6d7e4bfc487907af60753aafa983288a&t=1752977034",
            "https://wa.qq.com/qgif-web/0547c5c7d05a5a645760c6698befd308.gif?sign=62747e7e97bab9493f636adeb36e1c0e&t=1753005433",
            "https://wa.qq.com/qgif-web/03504bdbc943f6955195e62647f7ad6c.jpg?sign=53826f4e47858fbde55f962201e40b8a&t=1753003914",
            "https://wa.qq.com/qgif-web/6958bd95f2ea108afb80284864c79a93.jpg?sign=b3ed80ca4d02a1ceb68b24e66a67663e&t=1752977030",
            "https://wa.qq.com/qgif-web/00ed39be750c98fe3ee3a0238bc31734.gif?sign=00671eceae0359607e57f9f12e10a716&t=1752915595",
            "https://wa.qq.com/qgif-web/8a9535e6de1cfe83391f74c297a681d6.gif?sign=5ec9211a420885d5f3e74795bfb15467&t=1752918654",
            "https://wa.qq.com/qgif-web/f30091e878faa981ff4f138f058d7c8f.jpg?sign=85797fdc5f912d2f1207bd65031c0ac0&t=1752917982",
            "https://wa.qq.com/qgif-web/e89fcf4905ae53a836bd1d72db3004c8.jpg?sign=e3973e3316f03cf462c85cfad32e58f2&t=1753002733",
            "https://wa.qq.com/qgif-web/06a95a47ffbf843985689eb3deba60e1.jpg?sign=5af44f930dd152c3032855ea22c18665&t=1752915706",
            "https://wa.qq.com/qgif-web/014e697a3dd8271a5ca8e85cc646a75c.gif?sign=295f31c72399d2d8a40b18b6198bd9a3&t=1753001651",
            "https://wa.qq.com/qgif-web/7cccaf09d88d8ff1840d91f022d4d146.gif?sign=0dca5fcd93e14f120c144f8af7d9aa36&t=1753004749",
            "https://wa.qq.com/qgif-web/2fcaa7e54180f5cb14e929c3ed2ecf1c.gif?sign=9bab20a4c050c43ad3c6526fe1dd9e50&t=1752977002",
            "https://wa.qq.com/qgif-web/f1f72f9a48c3e653347ddd8a28d5f3e2.jpg?sign=cd996198f41cbcda00dd7622472cedb8&t=1752918248",
            "https://wa.qq.com/qgif-web/9482a9dcdd349c92c612c2c519e0d08f.jpg?sign=9a4379456c655a202f328de2936858b4&t=1752976835",
            "https://wa.qq.com/qgif-web/e2399abc4873f80e3433550a9f4b224a.gif?sign=98de6983b62b49a4adb285bb22357e39&t=1752976962",
            "https://wa.qq.com/qgif-web/55e090abbf6cf19ab4db439c545c0b85.jpg?sign=09d1c404a1e7432128fadcee3c4c9df8&t=1752976836",
            "https://wa.qq.com/qgif-web/cde0087b40a47e957717c54846114a13.gif?sign=de980bb6ab46c7f0e56d0f856c06b500&t=1752920022"
        ]
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» url|[string]|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## GET 获取收藏表情

GET /fetch_custom_face

> 返回示例

> 200 Response

```json
{"status":"ok","retcode":0,"data":["https://p.qpic.cn/qq_expression/721011692/721011692_0_0_0_3BAE279225436E12D4E347B6CBDFF085_0_0/0"],"message":"","wording":""}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|[string]|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

## POST 发送Protobuf数据包

POST /send_pb

> Body 请求参数

```json
{
    "cmd": "OidbSvcTrpcTcp.0xed3_1",
    "hex": "08e7a00210ca01221c0a130a05080110ca011206a80602b006011a02080122050a030a1400"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» cmd|body|string| 是 ||none|
|» hex|body|string| 是 ||Protobuf的16进制字符串|

> 返回示例

> 200 Response

```json
{
    "status": "ok",
    "retcode": 0,
    "data": {
        "cmd": "OidbSvcTrpcTcp.0xed3_1",
        "hex": "08e7a00210ca01180022cf010a100a05080110ca011a077375636365737322ba010a5b0a4c26726b65793d43414d534d496254433057646d58424255394650753149464d58456472633873626a45316a7151675858626e4d575a56",
        "echo": "84fb3a5a-3bc5-4a58-b56f-73174f17d05c"
    },
    "message": "",
    "wording": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» status|string|true|none||none|
|» retcode|integer|true|none||none|
|» data|object|true|none||none|
|»» cmd|string|true|none||none|
|»» hex|string|true|none||none|
|»» echo|string|true|none||none|
|» message|string|true|none||none|
|» wording|string|true|none||none|

# Milky/系统 API

<a id="opIdget_login_info"></a>

## POST 获取登录信息

POST /api/get_login_info

> Body 请求参数

```json
{}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_login_info_input](#schemaapi_get_login_info_input)| 否 | get_login_info 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "uin": -9007199254740991,
    "nickname": "string"
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_impl_info_input](#schemaapi_get_impl_info_input)| 否 | get_impl_info 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "user_id": -9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_user_profile_input](#schemaapi_get_user_profile_input)| 否 | get_user_profile 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "nickname": "string",
    "qid": "string",
    "age": -2147483648,
    "sex": "male",
    "remark": "string",
    "bio": "string",
    "level": -2147483648,
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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
|body|body|[Api_get_group_list_input](#schemaapi_get_group_list_input)| 否 | get_group_list 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "user_id": -9007199254740991,
  "no_cache": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_friend_info_input](#schemaapi_get_friend_info_input)| 否 | get_friend_info 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
|body|body|[Api_get_group_list_input](#schemaapi_get_group_list_input)| 否 | get_group_list 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "no_cache": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_group_info_input](#schemaapi_get_group_info_input)| 否 | get_group_info 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "no_cache": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_group_member_list_input](#schemaapi_get_group_member_list_input)| 否 | get_group_member_list 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "user_id": -9007199254740991,
  "no_cache": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_group_member_info_input](#schemaapi_get_group_member_info_input)| 否 | get_group_member_info 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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

## POST 获取置顶的好友和群列表

POST /api/get_peer_pins

> Body 请求参数

```json
{}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_peer_pins_inputget_peer_pins](#schemaapi_get_peer_pins_inputget_peer_pins)| 是 | get_peer_pins 请求参数|none|

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

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|
|sex|male|
|sex|female|
|sex|unknown|

## POST 设置好友或群的置顶状态

POST /

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
|body|body|[Api_set_peer_pin_input](#schemaapi_set_peer_pin_input)| 是 | set_peer_pin 请求参数|none|

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

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

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
|body|body|[Api_set_avatar_input](#schemaapi_set_avatar_input)| 是 | set_avatar 请求参数|none|

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

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

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
|body|body|[Api_set_nickname_input](#schemaapi_set_nickname_input)| 是 | set_nickname 请求参数|none|

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

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

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
|body|body|[Api_set_bio_input](#schemaapi_set_bio_input)| 是 | set_bio 请求参数|none|

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

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

## POST 获取自定义表情 URL 列表

POST /api/get_custom_face_url_list

> Body 请求参数

```json
{}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_custom_face_url_list_input](#schemaapi_get_custom_face_url_list_input)| 是 | get_custom_face_url_list 请求参数|none|

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
|body|body|[Api_get_cookies_input](#schemaapi_get_cookies_input)| 否 | get_cookies 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
|body|body|[Api_get_csrf_token_input](#schemaapi_get_csrf_token_input)| 否 | get_csrf_token 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

# Milky/消息 API

<a id="opIdsend_private_message"></a>

## POST 发送私聊消息

POST /api/send_private_message

> Body 请求参数

```json
{
  "user_id": -9007199254740991,
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
|body|body|[Api_send_private_message_input](#schemaapi_send_private_message_input)| 否 | send_private_message 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "message_seq": -9007199254740991,
    "time": -9007199254740991
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
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
|body|body|[Api_send_group_message_input](#schemaapi_send_group_message_input)| 否 | send_group_message 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "message_seq": -9007199254740991,
    "time": -9007199254740991
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "user_id": -9007199254740991,
  "message_seq": -9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_recall_private_message_input](#schemaapi_recall_private_message_input)| 否 | recall_private_message 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "message_seq": -9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_recall_group_message_input](#schemaapi_recall_group_message_input)| 否 | recall_group_message 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "peer_id": -9007199254740991,
  "message_seq": -9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_message_input](#schemaapi_get_message_input)| 否 | get_message 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "peer_id": -9007199254740991,
  "start_message_seq": -9007199254740991,
  "limit": 20
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_history_messages_input](#schemaapi_get_history_messages_input)| 否 | get_history_messages 请求参数|none|

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
    "next_message_seq": -9007199254740991
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
|body|body|[Api_get_resource_temp_url_input](#schemaapi_get_resource_temp_url_input)| 否 | get_resource_temp_url 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
|body|body|[Api_get_forwarded_messages_input](#schemaapi_get_forwarded_messages_input)| 否 | get_forwarded_messages 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "peer_id": -9007199254740991,
  "message_seq": -9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_mark_message_as_read_input](#schemaapi_mark_message_as_read_input)| 否 | mark_message_as_read 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

# Milky/好友 API

<a id="opIdsend_friend_nudge"></a>

## POST 发送好友戳一戳

POST /api/send_friend_nudge

> Body 请求参数

```json
{
  "user_id": -9007199254740991,
  "is_self": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_send_friend_nudge_input](#schemaapi_send_friend_nudge_input)| 否 | send_friend_nudge 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "user_id": -9007199254740991,
  "count": 1
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_send_profile_like_input](#schemaapi_send_profile_like_input)| 否 | send_profile_like 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

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
|body|body|[Api_delete_friend_input](#schemaapi_delete_friend_input)| 是 | delete_friend 请求参数|none|

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
|body|body|[Api_get_friend_requests_input](#schemaapi_get_friend_requests_input)| 否 | get_friend_requests 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
|body|body|[Api_accept_friend_request_input](#schemaapi_accept_friend_request_input)| 否 | accept_friend_request 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
|body|body|[Api_reject_friend_request_input](#schemaapi_reject_friend_request_input)| 否 | reject_friend_request 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

# Milky/群聊 API

<a id="opIdset_group_name"></a>

## POST 设置群名称

POST /api/set_group_name

> Body 请求参数

```json
{
  "group_id": -9007199254740991,
  "new_group_name": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_set_group_name_input](#schemaapi_set_group_name_input)| 否 | set_group_name 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "image_uri": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_set_group_avatar_input](#schemaapi_set_group_avatar_input)| 否 | set_group_avatar 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "user_id": -9007199254740991,
  "card": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_set_group_member_card_input](#schemaapi_set_group_member_card_input)| 否 | set_group_member_card 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "user_id": -9007199254740991,
  "special_title": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_set_group_member_special_title_input](#schemaapi_set_group_member_special_title_input)| 否 | set_group_member_special_title 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "user_id": -9007199254740991,
  "is_set": true
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_set_group_member_admin_input](#schemaapi_set_group_member_admin_input)| 否 | set_group_member_admin 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "user_id": -9007199254740991,
  "duration": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_set_group_member_mute_input](#schemaapi_set_group_member_mute_input)| 否 | set_group_member_mute 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "is_mute": true
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_set_group_whole_mute_input](#schemaapi_set_group_whole_mute_input)| 否 | set_group_whole_mute 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "user_id": -9007199254740991,
  "reject_add_request": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_kick_group_member_input](#schemaapi_kick_group_member_input)| 否 | kick_group_member 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_group_announcements_input](#schemaapi_get_group_announcements_input)| 否 | get_group_announcements 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "content": "string",
  "image_uri": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_send_group_announcement_input](#schemaapi_send_group_announcement_input)| 否 | send_group_announcement 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "announcement_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_delete_group_announcement_input](#schemaapi_delete_group_announcement_input)| 否 | delete_group_announcement 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "page_index": -2147483648,
  "page_size": -2147483648
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_group_essence_messages_input](#schemaapi_get_group_essence_messages_input)| 否 | get_group_essence_messages 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "message_seq": -9007199254740991,
  "is_set": true
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_set_group_essence_message_input](#schemaapi_set_group_essence_message_input)| 否 | set_group_essence_message 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_quit_group_input](#schemaapi_quit_group_input)| 否 | quit_group 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
|body|body|[Api_send_group_message_reaction_input](#schemaapi_send_group_message_reaction_input)| 否 | send_group_message_reaction 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "user_id": -9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_send_group_nudge_input](#schemaapi_send_group_nudge_input)| 否 | send_group_nudge 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "start_notification_seq": -9007199254740991,
  "is_filtered": false,
  "limit": 20
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_group_notifications_input](#schemaapi_get_group_notifications_input)| 否 | get_group_notifications 请求参数|none|

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "notifications": [
      {}
    ],
    "next_notification_seq": -9007199254740991
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "notification_seq": -9007199254740991,
  "notification_type": "join_request",
  "group_id": -9007199254740991,
  "is_filtered": false
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_accept_group_request_input](#schemaapi_accept_group_request_input)| 否 | accept_group_request 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "notification_seq": -9007199254740991,
  "notification_type": "join_request",
  "group_id": -9007199254740991,
  "is_filtered": false,
  "reason": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_reject_group_request_input](#schemaapi_reject_group_request_input)| 否 | reject_group_request 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "invitation_seq": -9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_accept_group_invitation_input](#schemaapi_accept_group_invitation_input)| 否 | accept_group_invitation 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "invitation_seq": -9007199254740991
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_reject_group_invitation_input](#schemaapi_reject_group_invitation_input)| 否 | reject_group_invitation 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

# Milky/文件 API

<a id="opIdupload_private_file"></a>

## POST 上传私聊文件

POST /api/upload_private_file

> Body 请求参数

```json
{
  "user_id": -9007199254740991,
  "file_uri": "string",
  "file_name": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_upload_private_file_input](#schemaapi_upload_private_file_input)| 否 | upload_private_file 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "parent_folder_id": "/",
  "file_uri": "string",
  "file_name": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_upload_group_file_input](#schemaapi_upload_group_file_input)| 否 | upload_group_file 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "user_id": -9007199254740991,
  "file_id": "string",
  "file_hash": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_private_file_download_url_input](#schemaapi_get_private_file_download_url_input)| 否 | get_private_file_download_url 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "file_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_group_file_download_url_input](#schemaapi_get_group_file_download_url_input)| 否 | get_group_file_download_url 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "parent_folder_id": "/"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_get_group_files_input](#schemaapi_get_group_files_input)| 否 | get_group_files 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "file_id": "string",
  "parent_folder_id": "/",
  "target_folder_id": "/"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_move_group_file_input](#schemaapi_move_group_file_input)| 否 | move_group_file 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "file_id": "string",
  "parent_folder_id": "/",
  "new_file_name": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_rename_group_file_input](#schemaapi_rename_group_file_input)| 否 | rename_group_file 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "file_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_delete_group_file_input](#schemaapi_delete_group_file_input)| 否 | delete_group_file 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "folder_name": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_create_group_folder_input](#schemaapi_create_group_folder_input)| 否 | create_group_folder 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "folder_id": "string",
  "new_folder_name": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_rename_group_folder_input](#schemaapi_rename_group_folder_input)| 否 | rename_group_folder 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

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
  "group_id": -9007199254740991,
  "folder_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|[Api_delete_group_folder_input](#schemaapi_delete_group_folder_input)| 否 | delete_group_folder 请求参数|none|

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
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|鉴权失败，未携带或提供了错误的 access_token|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|请求的 API 不存在|Inline|
|415|[Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13)|Content-Type 非 application/json|Inline|

### 返回数据结构

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

# 数据模型

<h2 id="tocS_GroupUploadFile">GroupUploadFile</h2>

<a id="schemagroupuploadfile"></a>
<a id="schema_GroupUploadFile"></a>
<a id="tocSgroupuploadfile"></a>
<a id="tocsgroupuploadfile"></a>

```json
{
  "id": "string",
  "name": "string",
  "size": 0,
  "busid": 0
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|id|string|true|none||文件 ID|
|name|string|true|none||文件名|
|size|integer|true|none||文件大小（字节）|
|busid|integer|true|none||业务 ID|

<h2 id="tocS_FlashFile">FlashFile</h2>

<a id="schemaflashfile"></a>
<a id="schema_FlashFile"></a>
<a id="tocSflashfile"></a>
<a id="tocsflashfile"></a>

```json
{
  "name": "string",
  "size": 0,
  "path": "string"
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|name|string|true|none||文件名|
|size|integer|true|none||文件大小（字节）|
|path|string|false|none||本地文件路径（可选）|

<h2 id="tocS_MsgEmojiLike">MsgEmojiLike</h2>

<a id="schemamsgemojilike"></a>
<a id="schema_MsgEmojiLike"></a>
<a id="tocSmsgemojilike"></a>
<a id="tocsmsgemojilike"></a>

```json
{
  "emoji_id": "string",
  "count": 0
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|emoji_id|string|true|none||表情 ID|
|count|integer|true|none||该表情的点赞数量|

<h2 id="tocS_MessageSender">MessageSender</h2>

<a id="schemamessagesender"></a>
<a id="schema_MessageSender"></a>
<a id="tocSmessagesender"></a>
<a id="tocsmessagesender"></a>

```json
{
  "user_id": 0,
  "nickname": "string",
  "card": "string",
  "sex": "male",
  "age": 0,
  "level": "string",
  "role": "owner",
  "title": "string",
  "group_id": 0
}

```

消息发送者

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||发送者的 QQ 号|
|nickname|string|true|none||发送者的昵称|
|card|string|false|none||群名片/昵称（群消息）|
|sex|string|false|none||发送者的性别|
|age|integer|false|none||发送者的年龄|
|level|string|false|none||群等级（群消息）|
|role|string|false|none||群角色（群消息）|
|title|string|false|none||专属头衔（群消息）|
|group_id|integer|false|none||群号（来自群的临时聊天）|

#### 枚举值

|属性|值|
|---|---|
|sex|male|
|sex|female|
|sex|unknown|
|role|owner|
|role|admin|
|role|member|

<h2 id="tocS_MessageSegment">MessageSegment</h2>

<a id="schemamessagesegment"></a>
<a id="schema_MessageSegment"></a>
<a id="tocSmessagesegment"></a>
<a id="tocsmessagesegment"></a>

```json
{
  "type": "text",
  "data": {}
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|

#### 枚举值

|属性|值|
|---|---|
|type|text|
|type|image|
|type|music|
|type|video|
|type|record|
|type|file|
|type|flash_file|
|type|at|
|type|reply|
|type|json|
|type|face|
|type|mface|
|type|markdown|
|type|node|
|type|forward|
|type|xml|
|type|poke|
|type|dice|
|type|rps|
|type|contact|
|type|shake|
|type|keyboard|

<h2 id="tocS_TextSegment">TextSegment</h2>

<a id="schematextsegment"></a>
<a id="schema_TextSegment"></a>
<a id="tocStextsegment"></a>
<a id="tocstextsegment"></a>

```json
{
  "type": "text",
  "data": {
    "text": "string"
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» text|string|true|none||文本内容|

#### 枚举值

|属性|值|
|---|---|
|type|text|

<h2 id="tocS_ImageSegment">ImageSegment</h2>

<a id="schemaimagesegment"></a>
<a id="schema_ImageSegment"></a>
<a id="tocSimagesegment"></a>
<a id="tocsimagesegment"></a>

```json
{
  "type": "image",
  "data": {
    "file": "string",
    "url": "string",
    "file_size": "string",
    "summary": "string",
    "subType": 0,
    "type": "flash",
    "thumb": "string",
    "name": "string"
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» file|string|true|none||图片文件名或路径|
|» url|string|false|none||图片 URL|
|» file_size|string|false|none||文件大小（字节）|
|» summary|string|false|none||图片摘要|
|» subType|integer|false|none||图片子类型|
|» type|string|false|none||图片显示类型|
|» thumb|string|false|none||缩略图 URL|
|» name|string|false|none||图片名称|

#### 枚举值

|属性|值|
|---|---|
|type|image|
|type|flash|
|type|show|

<h2 id="tocS_VideoSegment">VideoSegment</h2>

<a id="schemavideosegment"></a>
<a id="schema_VideoSegment"></a>
<a id="tocSvideosegment"></a>
<a id="tocsvideosegment"></a>

```json
{
  "type": "video",
  "data": {
    "file": "string",
    "url": "string",
    "path": "string",
    "file_size": "string",
    "thumb": "string",
    "name": "string"
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» file|string|true|none||视频文件名|
|» url|string|false|none||视频 URL|
|» path|string|false|none||本地文件路径|
|» file_size|string|false|none||文件大小（字节）|
|» thumb|string|false|none||缩略图 URL|
|» name|string|false|none||视频名称|

#### 枚举值

|属性|值|
|---|---|
|type|video|

<h2 id="tocS_RecordSegment">RecordSegment</h2>

<a id="schemarecordsegment"></a>
<a id="schema_RecordSegment"></a>
<a id="tocSrecordsegment"></a>
<a id="tocsrecordsegment"></a>

```json
{
  "type": "record",
  "data": {
    "file": "string",
    "url": "string",
    "path": "string",
    "file_size": "string",
    "thumb": "string",
    "name": "string"
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» file|string|true|none||音频文件名|
|» url|string|false|none||音频 URL|
|» path|string|false|none||本地文件路径|
|» file_size|string|false|none||文件大小（字节）|
|» thumb|string|false|none||缩略图 URL|
|» name|string|false|none||音频名称|

#### 枚举值

|属性|值|
|---|---|
|type|record|

<h2 id="tocS_FileSegment">FileSegment</h2>

<a id="schemafilesegment"></a>
<a id="schema_FileSegment"></a>
<a id="tocSfilesegment"></a>
<a id="tocsfilesegment"></a>

```json
{
  "type": "file",
  "data": {
    "file": "string",
    "url": "string",
    "path": "string",
    "file_size": "string",
    "file_id": "string",
    "thumb": "string",
    "name": "string"
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» file|string|true|none||文件名|
|» url|string|false|none||文件 URL|
|» path|string|false|none||本地文件路径|
|» file_size|string|false|none||文件大小（字节）|
|» file_id|string|false|none||文件 UUID|
|» thumb|string|false|none||缩略图 URL|
|» name|string|false|none||文件名|

#### 枚举值

|属性|值|
|---|---|
|type|file|

<h2 id="tocS_FlashFileSegment">FlashFileSegment</h2>

<a id="schemaflashfilesegment"></a>
<a id="schema_FlashFileSegment"></a>
<a id="tocSflashfilesegment"></a>
<a id="tocsflashfilesegment"></a>

```json
{
  "type": "flash_file",
  "data": {
    "title": "string",
    "file_set_id": "string",
    "scene_type": 0
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» title|string|true|none||闪传文件标题|
|» file_set_id|string|true|none||文件集 ID|
|» scene_type|integer|true|none||场景类型|

#### 枚举值

|属性|值|
|---|---|
|type|flash_file|

<h2 id="tocS_AtSegment">AtSegment</h2>

<a id="schemaatsegment"></a>
<a id="schema_AtSegment"></a>
<a id="tocSatsegment"></a>
<a id="tocsatsegment"></a>

```json
{
  "type": "at",
  "data": {
    "qq": "all",
    "name": "string"
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» qq|any|true|none||QQ 号或 'all' 表示 @全体成员|

oneOf

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|»» *anonymous*|string|false|none||none|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|»» *anonymous*|string|false|none||none|

continued

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» name|string|false|none||显示名称|

#### 枚举值

|属性|值|
|---|---|
|type|at|
|*anonymous*|all|

<h2 id="tocS_ReplySegment">ReplySegment</h2>

<a id="schemareplysegment"></a>
<a id="schema_ReplySegment"></a>
<a id="tocSreplysegment"></a>
<a id="tocsreplysegment"></a>

```json
{
  "type": "reply",
  "data": {
    "id": "string"
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» id|string|true|none||要回复的消息 ID|

#### 枚举值

|属性|值|
|---|---|
|type|reply|

<h2 id="tocS_JsonSegment">JsonSegment</h2>

<a id="schemajsonsegment"></a>
<a id="schema_JsonSegment"></a>
<a id="tocSjsonsegment"></a>
<a id="tocsjsonsegment"></a>

```json
{
  "type": "json",
  "data": {
    "data": "string"
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» data|string|true|none||JSON 数据（字符串格式）|

#### 枚举值

|属性|值|
|---|---|
|type|json|

<h2 id="tocS_XmlSegment">XmlSegment</h2>

<a id="schemaxmlsegment"></a>
<a id="schema_XmlSegment"></a>
<a id="tocSxmlsegment"></a>
<a id="tocsxmlsegment"></a>

```json
{
  "type": "xml",
  "data": {
    "data": "string"
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» data|string|true|none||XML 数据（字符串格式）|

#### 枚举值

|属性|值|
|---|---|
|type|xml|

<h2 id="tocS_FaceSegment">FaceSegment</h2>

<a id="schemafacesegment"></a>
<a id="schema_FaceSegment"></a>
<a id="tocSfacesegment"></a>
<a id="tocsfacesegment"></a>

```json
{
  "type": "face",
  "data": {
    "id": "string"
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» id|string|true|none||表情 ID|

#### 枚举值

|属性|值|
|---|---|
|type|face|

<h2 id="tocS_MfaceSegment">MfaceSegment</h2>

<a id="schemamfacesegment"></a>
<a id="schema_MfaceSegment"></a>
<a id="tocSmfacesegment"></a>
<a id="tocsmfacesegment"></a>

```json
{
  "type": "mface",
  "data": {
    "emoji_package_id": 0,
    "emoji_id": "string",
    "key": "string",
    "summary": "string",
    "url": "string"
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» emoji_package_id|integer|true|none||表情包 ID|
|» emoji_id|string|true|none||表情 ID|
|» key|string|true|none||表情密钥|
|» summary|string|false|none||表情摘要/名称|
|» url|string|false|none||表情 URL|

#### 枚举值

|属性|值|
|---|---|
|type|mface|

<h2 id="tocS_MarkdownSegment">MarkdownSegment</h2>

<a id="schemamarkdownsegment"></a>
<a id="schema_MarkdownSegment"></a>
<a id="tocSmarkdownsegment"></a>
<a id="tocsmarkdownsegment"></a>

```json
{
  "type": "markdown",
  "data": {
    "content": "string"
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» content|string|true|none||Markdown 内容|

#### 枚举值

|属性|值|
|---|---|
|type|markdown|

<h2 id="tocS_NodeSegment">NodeSegment</h2>

<a id="schemanodesegment"></a>
<a id="schema_NodeSegment"></a>
<a id="tocSnodesegment"></a>
<a id="tocsnodesegment"></a>

```json
{
  "type": "node",
  "data": {
    "id": 0,
    "content": "string",
    "user_id": 0,
    "nickname": "string",
    "name": "string",
    "uin": 0
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» id|any|false|none||转发的消息 ID|

oneOf

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|»» *anonymous*|integer|false|none||none|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|»» *anonymous*|string|false|none||none|

continued

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» content|any|false|none||消息内容|

oneOf

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|»» *anonymous*|string|false|none||消息内容（字符串格式）|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|»» *anonymous*|[object]|false|none||none|

continued

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» user_id|integer|false|none||用户 ID（OneBot11 格式）|
|» nickname|string|false|none||昵称（OneBot11 格式）|
|» name|string|false|none||名称（go-cqhttp 格式）|
|» uin|any|false|none||UIN（go-cqhttp 格式）|

oneOf

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|»» *anonymous*|integer|false|none||none|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|»» *anonymous*|string|false|none||none|

#### 枚举值

|属性|值|
|---|---|
|type|node|

<h2 id="tocS_ForwardSegment">ForwardSegment</h2>

<a id="schemaforwardsegment"></a>
<a id="schema_ForwardSegment"></a>
<a id="tocSforwardsegment"></a>
<a id="tocsforwardsegment"></a>

```json
{
  "type": "forward",
  "data": {
    "id": "string"
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» id|string|true|none||转发消息 ID|

#### 枚举值

|属性|值|
|---|---|
|type|forward|

<h2 id="tocS_MusicSegment">MusicSegment</h2>

<a id="schemamusicsegment"></a>
<a id="schema_MusicSegment"></a>
<a id="tocSmusicsegment"></a>
<a id="tocsmusicsegment"></a>

```json
{
  "type": "music",
  "data": {
    "type": "qq",
    "id": "string",
    "url": "string",
    "audio": "string",
    "title": "string",
    "content": "string",
    "image": "string"
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» type|string|false|none||音乐平台类型|
|» id|string|false|none||音乐 ID（平台音乐）|
|» url|string|false|none||音乐 URL（自定义音乐）|
|» audio|string|false|none||音频 URL（自定义音乐）|
|» title|string|false|none||音乐标题（自定义音乐）|
|» content|string|false|none||音乐描述（自定义音乐）|
|» image|string|false|none||封面图片 URL（自定义音乐）|

#### 枚举值

|属性|值|
|---|---|
|type|music|
|type|qq|
|type|163|
|type|xm|
|type|custom|

<h2 id="tocS_PokeSegment">PokeSegment</h2>

<a id="schemapokesegment"></a>
<a id="schema_PokeSegment"></a>
<a id="tocSpokesegment"></a>
<a id="tocspokesegment"></a>

```json
{
  "type": "poke",
  "data": {
    "qq": 0,
    "id": 0
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» qq|integer|false|none||目标 QQ 号|
|» id|integer|false|none||戳一戳类型 ID|

#### 枚举值

|属性|值|
|---|---|
|type|poke|

<h2 id="tocS_DiceSegment">DiceSegment</h2>

<a id="schemadicesegment"></a>
<a id="schema_DiceSegment"></a>
<a id="tocSdicesegment"></a>
<a id="tocsdicesegment"></a>

```json
{
  "type": "dice",
  "data": {
    "result": 0
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» result|any|true|none||骰子结果（1-6）|

oneOf

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|»» *anonymous*|integer|false|none||none|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|»» *anonymous*|string|false|none||none|

#### 枚举值

|属性|值|
|---|---|
|type|dice|

<h2 id="tocS_RpsSegment">RpsSegment</h2>

<a id="schemarpssegment"></a>
<a id="schema_RpsSegment"></a>
<a id="tocSrpssegment"></a>
<a id="tocsrpssegment"></a>

```json
{
  "type": "rps",
  "data": {
    "result": 0
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» result|any|true|none||猜拳结果（1=石头，2=剪刀，3=布）|

oneOf

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|»» *anonymous*|integer|false|none||none|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|»» *anonymous*|string|false|none||none|

#### 枚举值

|属性|值|
|---|---|
|type|rps|

<h2 id="tocS_ContactSegment">ContactSegment</h2>

<a id="schemacontactsegment"></a>
<a id="schema_ContactSegment"></a>
<a id="tocScontactsegment"></a>
<a id="tocscontactsegment"></a>

```json
{
  "type": "contact",
  "data": {
    "type": "qq",
    "id": "string"
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» type|string|true|none||联系人类型|
|» id|string|true|none||联系人 ID|

#### 枚举值

|属性|值|
|---|---|
|type|contact|
|type|qq|
|type|group|

<h2 id="tocS_ShakeSegment">ShakeSegment</h2>

<a id="schemashakesegment"></a>
<a id="schema_ShakeSegment"></a>
<a id="tocSshakesegment"></a>
<a id="tocsshakesegment"></a>

```json
{
  "type": "shake",
  "data": {}
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||窗口抖动（空对象）|

#### 枚举值

|属性|值|
|---|---|
|type|shake|

<h2 id="tocS_KeyboardSegment">KeyboardSegment</h2>

<a id="schemakeyboardsegment"></a>
<a id="schema_KeyboardSegment"></a>
<a id="tocSkeyboardsegment"></a>
<a id="tocskeyboardsegment"></a>

```json
{
  "type": "keyboard",
  "data": {
    "rows": [
      {
        "buttons": [
          {
            "id": null,
            "render_data": null,
            "action": null
          }
        ]
      }
    ]
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|type|string|true|none||none|
|data|object|true|none||none|
|» rows|[object]|true|none||none|
|»» buttons|[[KeyboardButton](#schemakeyboardbutton)]|true|none||none|

#### 枚举值

|属性|值|
|---|---|
|type|keyboard|

<h2 id="tocS_KeyboardButton">KeyboardButton</h2>

<a id="schemakeyboardbutton"></a>
<a id="schema_KeyboardButton"></a>
<a id="tocSkeyboardbutton"></a>
<a id="tocskeyboardbutton"></a>

```json
{
  "id": "string",
  "render_data": {
    "label": "string",
    "visited_label": "string",
    "style": 0
  },
  "action": {
    "type": 0,
    "permission": {
      "type": 0,
      "specify_role_ids": [
        "string"
      ],
      "specify_user_ids": [
        "string"
      ]
    },
    "unsupport_tips": "string",
    "data": "string",
    "reply": true,
    "enter": true
  }
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|id|string|true|none||按钮 ID|
|render_data|object|true|none||none|
|» label|string|true|none||按钮标签|
|» visited_label|string|true|none||点击后的标签|
|» style|integer|true|none||按钮样式|
|action|object|true|none||none|
|» type|integer|true|none||动作类型|
|» permission|object|true|none||none|
|»» type|integer|true|none||权限类型|
|»» specify_role_ids|[string]|true|none||指定角色 ID|
|»» specify_user_ids|[string]|true|none||指定用户 ID|
|» unsupport_tips|string|true|none||不支持时的提示|
|» data|string|true|none||动作数据|
|» reply|boolean|true|none||是否回复|
|» enter|boolean|true|none||是否进入|

<h2 id="tocS_MessageEvent">MessageEvent</h2>

<a id="schemamessageevent"></a>
<a id="schema_MessageEvent"></a>
<a id="tocSmessageevent"></a>
<a id="tocsmessageevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "message",
  "message_id": 0,
  "message_seq": 0,
  "real_id": 0,
  "user_id": 0,
  "group_id": 0,
  "message_type": "private",
  "sub_type": "friend",
  "sender": {
    "user_id": 0,
    "nickname": "string",
    "card": "string",
    "sex": "male",
    "age": 0,
    "level": "string",
    "role": "owner",
    "title": "string",
    "group_id": 0
  },
  "message": [
    {
      "type": "text",
      "data": {
        "text": "string"
      }
    }
  ],
  "message_format": "array",
  "raw_message": "string",
  "font": 14,
  "target_id": 0,
  "temp_source": 0
}

```

消息

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|message_id|integer|true|none||消息 ID（短 ID）|
|message_seq|integer|true|none||消息序列号|
|real_id|integer|false|none||真实消息 ID（仅在 get_msg 接口存在）|
|user_id|integer|true|none||发送者的 QQ 号|
|group_id|integer|false|none||群号（仅群消息）|
|message_type|string|true|none||消息类型|
|sub_type|string|false|none||消息子类型|
|sender|[MessageSender](#schemamessagesender)|true|none||none|
|message|[anyOf]|true|none||消息内容（消息段数组格式）|

anyOf

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» *anonymous*|[TextSegment](#schematextsegment)|false|none||文本|

or

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» *anonymous*|[VideoSegment](#schemavideosegment)|false|none||视频|

or

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» *anonymous*|[RecordSegment](#schemarecordsegment)|false|none||语音|

or

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» *anonymous*|[FileSegment](#schemafilesegment)|false|none||文件|

or

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» *anonymous*|[AtSegment](#schemaatsegment)|false|none||@|

or

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» *anonymous*|[ReplySegment](#schemareplysegment)|false|none||回复|

or

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» *anonymous*|[JsonSegment](#schemajsonsegment)|false|none||Json|

or

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» *anonymous*|[FaceSegment](#schemafacesegment)|false|none||表情|

or

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» *anonymous*|[MfaceSegment](#schemamfacesegment)|false|none||商城表情|

or

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» *anonymous*|[MarkdownSegment](#schemamarkdownsegment)|false|none||Markdown|

or

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» *anonymous*|[ForwardSegment](#schemaforwardsegment)|false|none||转发|

or

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» *anonymous*|[DiceSegment](#schemadicesegment)|false|none||骰子|

or

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» *anonymous*|[RpsSegment](#schemarpssegment)|false|none||石头剪刀布|

or

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» *anonymous*|[KeyboardSegment](#schemakeyboardsegment)|false|none||按钮|

continued

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|message_format|string|true|none||消息格式类型|
|raw_message|string|true|none||原始消息内容（CQ 码格式）|
|font|integer|true|none||字体 ID|
|target_id|integer|false|none||目标 ID（仅发送的消息）|
|temp_source|integer|false|none||临时聊天来源（0 = 群聊）|

#### 枚举值

|属性|值|
|---|---|
|post_type|message|
|post_type|message_sent|
|message_type|private|
|message_type|group|
|sub_type|friend|
|sub_type|group|
|sub_type|normal|
|message_format|array|
|message_format|string|
|temp_source|0|
|temp_source|1|
|temp_source|2|
|temp_source|3|
|temp_source|4|
|temp_source|6|
|temp_source|7|
|temp_source|8|
|temp_source|9|

<h2 id="tocS_PokeEvent">PokeEvent</h2>

<a id="schemapokeevent"></a>
<a id="schema_PokeEvent"></a>
<a id="tocSpokeevent"></a>
<a id="tocspokeevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "notify",
  "sub_type": "poke",
  "user_id": 0,
  "target_id": 0,
  "group_id": 0,
  "raw_info": "<gtip align=\"center\"> <qq uin=\"u_l029ehNpnNjaQrZUhwv5uQ\" col=\"1\" nm=\"\" /> <img src=\"http://tianquan.gtimg.cn/nudgeaction/item/8/expression.jpg\" jp=\"https://zb.vip.qq.com/v2/pages/nudgeMall?_wv=2&amp;actionId=8\" /> <nor txt=\"揉了揉\"/> <qq uin=\"u_snYxnEfja-Po_cdFcyccRQ\" col=\"1\" nm=\"\" tp=\"0\"/> <nor txt=\"的干脆面，居然全碎啦！\"/> </gtip>"
}

```

戳一戳

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|sub_type|string|true|none||none|
|user_id|integer|true|none||发送戳一戳的用户|
|target_id|integer|true|none||被戳的目标用户|
|group_id|integer|false|none||群号（仅群聊戳一戳存在）|
|raw_info|string|false|none||原始戳一戳信息|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|notify|
|sub_type|poke|

<h2 id="tocS_PokeRecallEvent">PokeRecallEvent</h2>

<a id="schemapokerecallevent"></a>
<a id="schema_PokeRecallEvent"></a>
<a id="tocSpokerecallevent"></a>
<a id="tocspokerecallevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "notify",
  "sub_type": "poke_recall",
  "user_id": 0,
  "target_id": 0,
  "group_id": 0,
  "raw_info": "<gtip align=\"center\"> <qq uin=\"u_l029ehNpnNjaQrZUhwv5uQ\" col=\"1\" nm=\"\" /> <img src=\"http://tianquan.gtimg.cn/nudgeaction/item/8/expression.jpg\" jp=\"https://zb.vip.qq.com/v2/pages/nudgeMall?_wv=2&amp;actionId=8\" /> <nor txt=\"揉了揉\"/> <qq uin=\"u_snYxnEfja-Po_cdFcyccRQ\" col=\"1\" nm=\"\" tp=\"0\"/> <nor txt=\"的干脆面，居然全碎啦！\"/> </gtip>"
}

```

撤回戳一戳

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|sub_type|string|true|none||none|
|user_id|integer|true|none||发送戳一戳的用户|
|target_id|integer|true|none||被戳的目标用户|
|group_id|integer|false|none||群号（仅群聊戳一戳存在）|
|raw_info|string|false|none||原始戳一戳信息|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|notify|
|sub_type|poke_recall|

<h2 id="tocS_FriendRecallNoticeEvent">FriendRecallNoticeEvent</h2>

<a id="schemafriendrecallnoticeevent"></a>
<a id="schema_FriendRecallNoticeEvent"></a>
<a id="tocSfriendrecallnoticeevent"></a>
<a id="tocsfriendrecallnoticeevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "friend_recall",
  "user_id": 0,
  "message_id": 0
}

```

好友消息撤回

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|user_id|integer|true|none||撤回消息的好友 QQ 号|
|message_id|integer|true|none||被撤回的消息 ID|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|friend_recall|

<h2 id="tocS_FriendRequestEvent">FriendRequestEvent</h2>

<a id="schemafriendrequestevent"></a>
<a id="schema_FriendRequestEvent"></a>
<a id="tocSfriendrequestevent"></a>
<a id="tocsfriendrequestevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "request",
  "request_type": "friend",
  "user_id": 0,
  "comment": "string",
  "flag": "string",
  "via": "string"
}

```

好友申请

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|request_type|string|true|none||none|
|user_id|integer|true|none||请求者的 QQ 号|
|comment|string|true|none||请求消息|
|flag|string|true|none||请求标识，用于处理请求|
|via|string|true|none||请求来源|

#### 枚举值

|属性|值|
|---|---|
|post_type|request|
|request_type|friend|

<h2 id="tocS_FriendAddNoticeEvent">FriendAddNoticeEvent</h2>

<a id="schemafriendaddnoticeevent"></a>
<a id="schema_FriendAddNoticeEvent"></a>
<a id="tocSfriendaddnoticeevent"></a>
<a id="tocsfriendaddnoticeevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "friend_add",
  "user_id": 0
}

```

好友添加

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|user_id|integer|true|none||新好友的 QQ 号|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|friend_add|

<h2 id="tocS_ProfileLikeEvent">ProfileLikeEvent</h2>

<a id="schemaprofilelikeevent"></a>
<a id="schema_ProfileLikeEvent"></a>
<a id="tocSprofilelikeevent"></a>
<a id="tocsprofilelikeevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "notify",
  "sub_type": "profile_like",
  "operator_id": 0,
  "operator_nick": "string",
  "times": 0
}

```

名片点赞

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|sub_type|string|true|none||none|
|operator_id|integer|true|none||点赞的用户|
|operator_nick|string|true|none||点赞用户的昵称|
|times|integer|true|none||点赞次数|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|notify|
|sub_type|profile_like|

<h2 id="tocS_GroupUploadNoticeEvent">GroupUploadNoticeEvent</h2>

<a id="schemagroupuploadnoticeevent"></a>
<a id="schema_GroupUploadNoticeEvent"></a>
<a id="tocSgroupuploadnoticeevent"></a>
<a id="tocsgroupuploadnoticeevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "group_upload",
  "group_id": 0,
  "user_id": 0,
  "file": {
    "id": "string",
    "name": "string",
    "size": 0,
    "busid": 0
  }
}

```

群文件上传

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||上传者的 QQ 号|
|file|[GroupUploadFile](#schemagroupuploadfile)|true|none||none|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|group_upload|

<h2 id="tocS_GroupRequestEvent">GroupRequestEvent</h2>

<a id="schemagrouprequestevent"></a>
<a id="schema_GroupRequestEvent"></a>
<a id="tocSgrouprequestevent"></a>
<a id="tocsgrouprequestevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "request",
  "request_type": "group",
  "sub_type": "add",
  "comment": "string",
  "flag": "string",
  "group_id": 0,
  "user_id": 0,
  "invitor_id": 0,
  "source_group_id": 0
}

```

申请加群

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|request_type|string|true|none||none|
|sub_type|string|true|none||add = 加群请求，invite = 邀请机器人入群|
|comment|string|true|none||请求消息|
|flag|string|true|none||请求标识，用于处理请求|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||用户 ID（add 类型为请求者，invite 类型为邀请者）|
|invitor_id|integer|false|none||邀请者 ID（invite 类型）|
|source_group_id|integer|false|none||来源群号，如果是通过 QQ 群邀请|

#### 枚举值

|属性|值|
|---|---|
|post_type|request|
|request_type|group|
|sub_type|add|
|sub_type|invite|

<h2 id="tocS_GroupDismissEvent">GroupDismissEvent</h2>

<a id="schemagroupdismissevent"></a>
<a id="schema_GroupDismissEvent"></a>
<a id="tocSgroupdismissevent"></a>
<a id="tocsgroupdismissevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "group_dismiss",
  "group_id": 0,
  "user_id": 0
}

```

群解散

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||群主 QQ 号|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|group_dismiss|

<h2 id="tocS_GroupIncreaseEvent">GroupIncreaseEvent</h2>

<a id="schemagroupincreaseevent"></a>
<a id="schema_GroupIncreaseEvent"></a>
<a id="tocSgroupincreaseevent"></a>
<a id="tocsgroupincreaseevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "group_increase",
  "sub_type": "approve",
  "group_id": 0,
  "user_id": 0,
  "operator_id": 0
}

```

群成员新增

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|sub_type|string|true|none||approve = 同意入群，invite = 邀请入群|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||新成员的 QQ 号|
|operator_id|integer|true|none||操作者 ID（同意/邀请的人）|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|group_increase|
|sub_type|approve|
|sub_type|invite|

<h2 id="tocS_GroupDecreaseEvent">GroupDecreaseEvent</h2>

<a id="schemagroupdecreaseevent"></a>
<a id="schema_GroupDecreaseEvent"></a>
<a id="tocSgroupdecreaseevent"></a>
<a id="tocsgroupdecreaseevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "group_decrease",
  "sub_type": "leave",
  "group_id": 0,
  "user_id": 0,
  "operator_id": 0
}

```

群成员减少

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|sub_type|string|true|none||leave = 主动退群，kick = 被管理员踢出，kick_me = 机器人被踢|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||离开/被踢的用户|
|operator_id|integer|true|none||操作者 ID（执行操作的人）|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|group_decrease|
|sub_type|leave|
|sub_type|kick|
|sub_type|kick_me|

<h2 id="tocS_GroupTitleEvent">GroupTitleEvent</h2>

<a id="schemagrouptitleevent"></a>
<a id="schema_GroupTitleEvent"></a>
<a id="tocSgrouptitleevent"></a>
<a id="tocsgrouptitleevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "notify",
  "sub_type": "title",
  "group_id": 0,
  "user_id": 0,
  "title": "string"
}

```

群头衔

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|sub_type|string|true|none||none|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||获得头衔的用户|
|title|string|true|none||专属头衔|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|notify|
|sub_type|title|

<h2 id="tocS_GroupCardEvent">GroupCardEvent</h2>

<a id="schemagroupcardevent"></a>
<a id="schema_GroupCardEvent"></a>
<a id="tocSgroupcardevent"></a>
<a id="tocsgroupcardevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "group_card",
  "group_id": 0,
  "user_id": 0,
  "card_new": "string",
  "card_old": "string"
}

```

群名片

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||名片被修改的用户|
|card_new|string|true|none||新群名片/昵称|
|card_old|string|true|none||旧群名片/昵称|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|group_card|

<h2 id="tocS_GroupMsgEmojiLikeEvent">GroupMsgEmojiLikeEvent</h2>

<a id="schemagroupmsgemojilikeevent"></a>
<a id="schema_GroupMsgEmojiLikeEvent"></a>
<a id="tocSgroupmsgemojilikeevent"></a>
<a id="tocsgroupmsgemojilikeevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "group_msg_emoji_like",
  "group_id": 0,
  "user_id": 0,
  "message_id": 0,
  "likes": [
    {
      "emoji_id": "string",
      "count": 0
    }
  ],
  "is_add": true
}

```

群消息贴表情

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||点赞消息的用户|
|message_id|integer|true|none||被点赞的消息 ID|
|likes|[[MsgEmojiLike](#schemamsgemojilike)]|true|none||none|
|is_add|boolean|true|none||是否为添加，`false` 表示取消回应|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|group_msg_emoji_like|

<h2 id="tocS_GroupRecallNoticeEvent">GroupRecallNoticeEvent</h2>

<a id="schemagrouprecallnoticeevent"></a>
<a id="schema_GroupRecallNoticeEvent"></a>
<a id="tocSgrouprecallnoticeevent"></a>
<a id="tocsgrouprecallnoticeevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "group_recall",
  "group_id": 0,
  "user_id": 0,
  "operator_id": 0,
  "message_id": 0
}

```

群消息撤回

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||原消息发送者|
|operator_id|integer|true|none||撤回消息的人|
|message_id|integer|true|none||被撤回的消息 ID|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|group_recall|

<h2 id="tocS_GroupAdminNoticeEvent">GroupAdminNoticeEvent</h2>

<a id="schemagroupadminnoticeevent"></a>
<a id="schema_GroupAdminNoticeEvent"></a>
<a id="tocSgroupadminnoticeevent"></a>
<a id="tocsgroupadminnoticeevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "group_admin",
  "sub_type": "set",
  "group_id": 0,
  "user_id": 0
}

```

群管理员

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|sub_type|string|true|none||set = 设置管理员，unset = 取消管理员|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||被设置/取消管理员的用户 ID|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|group_admin|
|sub_type|set|
|sub_type|unset|

<h2 id="tocS_GroupBanEvent">GroupBanEvent</h2>

<a id="schemagroupbanevent"></a>
<a id="schema_GroupBanEvent"></a>
<a id="tocSgroupbanevent"></a>
<a id="tocsgroupbanevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "group_ban",
  "sub_type": "ban",
  "group_id": 0,
  "user_id": 0,
  "operator_id": 0,
  "duration": 0
}

```

群禁言

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|sub_type|string|true|none||ban = 禁言，lift_ban = 解除禁言|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||被禁言/解禁的用户（0 表示全员）|
|operator_id|integer|true|none||执行操作的管理员|
|duration|integer|true|none||禁言时长（秒）（-1 为永久，0 为解禁）|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|group_ban|
|sub_type|ban|
|sub_type|lift_ban|

<h2 id="tocS_EssenceEvent">EssenceEvent</h2>

<a id="schemaessenceevent"></a>
<a id="schema_EssenceEvent"></a>
<a id="tocSessenceevent"></a>
<a id="tocsessenceevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "essence",
  "sub_type": "add",
  "group_id": 0,
  "user_id": 0,
  "sender_id": 0,
  "operator_id": 0,
  "message_id": 0
}

```

群精华

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|sub_type|string|false|none||none|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||消息发送者 ID|
|sender_id|integer|true|none||消息发送者 ID（与 user_id 重复）|
|operator_id|integer|true|none||设置/取消精华的管理员|
|message_id|integer|true|none||被设为精华的消息 ID|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|essence|
|sub_type|add|
|sub_type|delete|

<h2 id="tocS_FlashFileEvent">FlashFileEvent</h2>

<a id="schemaflashfileevent"></a>
<a id="schema_FlashFileEvent"></a>
<a id="tocSflashfileevent"></a>
<a id="tocsflashfileevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "notice",
  "notice_type": "flash_file",
  "sub_type": "downloaded",
  "title": "string",
  "share_link": "string",
  "file_set_id": "string",
  "files": [
    {
      "name": "string",
      "size": 0,
      "path": "string"
    }
  ],
  "downloaded_size": 0,
  "uploaded_size": 0,
  "total_size": 0,
  "speed": 0,
  "remain_seconds": 0
}

```

闪传文件

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|notice_type|string|true|none||none|
|sub_type|string|true|none||none|
|title|string|true|none||闪传文件标题|
|share_link|string|true|none||分享链接|
|file_set_id|string|true|none||文件集 ID|
|files|[[FlashFile](#schemaflashfile)]|true|none||none|
|downloaded_size|integer|false|none||已下载大小（字节）（下载时）|
|uploaded_size|integer|false|none||已上传大小（字节）（上传时）|
|total_size|integer|false|none||总大小（字节）（下载/上传时）|
|speed|integer|false|none||传输速度（字节/秒）（下载/上传时）|
|remain_seconds|integer|false|none||剩余时间（秒）（下载/上传时）|

#### 枚举值

|属性|值|
|---|---|
|post_type|notice|
|notice_type|flash_file|
|sub_type|downloaded|
|sub_type|downloading|
|sub_type|uploaded|
|sub_type|uploading|

<h2 id="tocS_HeartbeatEvent">HeartbeatEvent</h2>

<a id="schemaheartbeatevent"></a>
<a id="schema_HeartbeatEvent"></a>
<a id="tocSheartbeatevent"></a>
<a id="tocsheartbeatevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "meta_event",
  "meta_event_type": "heartbeat",
  "status": {
    "online": true,
    "good": true
  },
  "interval": 5000
}

```

心跳

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|meta_event_type|string|true|none||none|
|status|object|true|none||none|
|» online|boolean¦null|true|none||机器人是否在线|
|» good|boolean|true|none||机器人状态是否良好|
|interval|integer|true|none||心跳间隔（毫秒）|

#### 枚举值

|属性|值|
|---|---|
|post_type|meta_event|
|meta_event_type|heartbeat|

<h2 id="tocS_LifeCycleEvent">LifeCycleEvent</h2>

<a id="schemalifecycleevent"></a>
<a id="schema_LifeCycleEvent"></a>
<a id="tocSlifecycleevent"></a>
<a id="tocslifecycleevent"></a>

```json
{
  "time": 1640995200,
  "self_id": 123456789,
  "post_type": "meta_event",
  "meta_event_type": "lifecycle",
  "sub_type": "enable"
}

```

生命周期

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|time|integer|true|none||事件时间戳（Unix 时间戳，秒）|
|self_id|integer|true|none||机器人的 QQ 号|
|post_type|string|true|none||事件类型|
|meta_event_type|string|true|none||none|
|sub_type|string|true|none||生命周期事件子类型|

#### 枚举值

|属性|值|
|---|---|
|post_type|meta_event|
|meta_event_type|lifecycle|
|sub_type|enable|
|sub_type|disable|
|sub_type|connect|

<h2 id="tocS_FileEntity">FileEntity</h2>

<a id="schemafileentity"></a>
<a id="schema_FileEntity"></a>
<a id="tocSfileentity"></a>
<a id="tocsfileentity"></a>

```json
{
  "group_id": 0,
  "file_id": "string",
  "file_name": "string",
  "busid": 0,
  "file_size": 0,
  "upload_time": 0,
  "dead_time": 0,
  "modify_time": 0,
  "download_times": 0,
  "uploader": 0,
  "uploader_name": "string"
}

```

群文件

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|file_id|string|true|none||文件 ID|
|file_name|string|true|none||文件名|
|busid|integer|true|none||文件类型|
|file_size|integer|true|none||文件大小|
|upload_time|integer|true|none||上传时间|
|dead_time|integer|true|none||过期时间，永久文件恒为0|
|modify_time|integer|true|none||最后修改时间|
|download_times|integer|true|none||下载次数|
|uploader|integer|true|none||上传者 ID|
|uploader_name|string|true|none||上传者名字|

<h2 id="tocS_FolderEntity">FolderEntity</h2>

<a id="schemafolderentity"></a>
<a id="schema_FolderEntity"></a>
<a id="tocSfolderentity"></a>
<a id="tocsfolderentity"></a>

```json
{
  "group_id": 0,
  "folder_id": "string",
  "folder_name": "string",
  "create_time": 0,
  "creator": 0,
  "creator_name": "string",
  "total_file_count": 0
}

```

群文件夹

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|folder_id|string|true|none||文件夹 ID|
|folder_name|string|true|none||文件名|
|create_time|integer|true|none||创建时间|
|creator|integer|true|none||创建者|
|creator_name|string|true|none||创建者名字|
|total_file_count|integer|true|none||子文件数量|

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
  "user_id": -9007199254740991,
  "nickname": "string",
  "sex": "male",
  "group_id": -9007199254740991,
  "card": "string",
  "title": "string",
  "level": -2147483648,
  "role": "owner",
  "join_time": -9007199254740991,
  "last_sent_time": -9007199254740991,
  "shut_up_end_time": -9007199254740991
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
|shut_up_end_time|integer¦null|false|none||禁言结束时间，Unix 时间戳（秒）|

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
  "group_id": -9007199254740991,
  "announcement_id": "string",
  "user_id": -9007199254740991,
  "time": -9007199254740991,
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
|image_url|string¦null|false|none||公告图片 URL|

<h2 id="tocS_GroupFileEntity">GroupFileEntity</h2>

<a id="schemagroupfileentity"></a>
<a id="schema_GroupFileEntity"></a>
<a id="tocSgroupfileentity"></a>
<a id="tocsgroupfileentity"></a>

```json
{
  "group_id": -9007199254740991,
  "file_id": "string",
  "file_name": "string",
  "parent_folder_id": "string",
  "file_size": -9007199254740991,
  "uploaded_time": -9007199254740991,
  "expire_time": -9007199254740991,
  "uploader_id": -9007199254740991,
  "downloaded_times": -2147483648
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
|expire_time|integer¦null|false|none||过期时的 Unix 时间戳（秒）|
|uploader_id|integer|true|none||上传者 QQ 号|
|downloaded_times|integer|true|none||下载次数|

<h2 id="tocS_GroupFolderEntity">GroupFolderEntity</h2>

<a id="schemagroupfolderentity"></a>
<a id="schema_GroupFolderEntity"></a>
<a id="tocSgroupfolderentity"></a>
<a id="tocsgroupfolderentity"></a>

```json
{
  "group_id": -9007199254740991,
  "folder_id": "string",
  "parent_folder_id": "string",
  "folder_name": "string",
  "created_time": -9007199254740991,
  "last_modified_time": -9007199254740991,
  "creator_id": -9007199254740991,
  "file_count": -2147483648
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
  "time": -9007199254740991,
  "initiator_id": -9007199254740991,
  "initiator_uid": "string",
  "target_user_id": -9007199254740991,
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
  "group_id": -9007199254740991,
  "notification_seq": -9007199254740991,
  "is_filtered": true,
  "initiator_id": -9007199254740991,
  "state": "pending",
  "operator_id": -9007199254740991,
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
|» operator_id|integer¦null|false|none||处理请求的管理员 QQ 号|
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
|» operator_id|integer¦null|false|none||处理请求的管理员 QQ 号|

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

<h2 id="tocS_Event">Event</h2>

<a id="schemaevent"></a>
<a id="schema_Event"></a>
<a id="tocSevent"></a>
<a id="tocsevent"></a>

```json
{
  "event_type": "bot_offline",
  "time": -9007199254740991,
  "self_id": -9007199254740991,
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
|» data|[IncomingMessage](#schemaincomingmessage)|true|none||接收消息|

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
|» data|object|true|none||入群申请事件|
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
|» data|object|true|none||群成员邀请他人入群事件|
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
|»» source_group_id|integer¦null|false|none||来源群号，如果是通过 QQ 群邀请|

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
|»» operator_id|integer¦null|false|none||管理员 QQ 号，如果是管理员同意入群|
|»» invitor_id|integer¦null|false|none||邀请者 QQ 号，如果是邀请入群|

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
|»» operator_id|integer¦null|false|none||管理员 QQ 号，如果是管理员踢出|

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
|» data|object|true|none||群消息回应事件|
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

<h2 id="tocS_IncomingMessage">IncomingMessage</h2>

<a id="schemaincomingmessage"></a>
<a id="schema_IncomingMessage"></a>
<a id="tocSincomingmessage"></a>
<a id="tocsincomingmessage"></a>

```json
{
  "message_scene": "friend",
  "peer_id": -9007199254740991,
  "message_seq": -9007199254740991,
  "sender_id": -9007199254740991,
  "time": -9007199254740991,
  "segments": [
    {}
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
      "type": "[",
      "data": {}
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
  "group_id": -9007199254740991,
  "message_seq": -9007199254740991,
  "message_time": -9007199254740991,
  "sender_id": -9007199254740991,
  "sender_name": "string",
  "operator_id": -9007199254740991,
  "operator_name": "string",
  "operation_time": -9007199254740991,
  "segments": [
    {
      "type": "[",
      "data": {}
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
    "text": "string"
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
|»» sender_name|string¦null|false|none||被引用的消息发送者名称，仅在合并转发中能够获取|
|»» time|integer|true|none||被引用的消息的 Unix 时间戳（秒）|
|»» segments|[allOf]|true|none||被引用的消息内容|

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
|»» file_hash|string¦null|false|none||文件的 TriSHA1 哈希值，仅在私聊文件中存在|

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
  "user_id": -9007199254740991,
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
|»» is_large|boolean¦null|false|none||是否为超级表情|

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
|»» sub_type|string¦null|false|none||图片类型|
|»» summary|string¦null|false|none||图片预览文本|

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
|»» thumb_uri|string¦null|false|none||封面图片 URI|

xor

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|*anonymous*|object|false|none|合并转发消息段|合并转发消息段|
|» type|string|true|none||none|
|» data|object|true|none||合并转发消息段|
|»» messages|[allOf]|true|none||合并转发消息内容|
|»» title|string¦null|false|none||合并转发标题|
|»» preview|[allOf]¦null|false|none||合并转发预览文本，若提供，至少 1 条，至多 4 条|
|»» summary|string¦null|false|none||合并转发摘要|
|»» prompt|string¦null|false|none||合并转发的预览外显文本，仅对移动端 QQ 有效|

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

<h2 id="tocS_Api_get_login_info_input">Api_get_login_info_input</h2>

<a id="schemaapi_get_login_info_input"></a>
<a id="schema_Api_get_login_info_input"></a>
<a id="tocSapi_get_login_info_input"></a>
<a id="tocsapi_get_login_info_input"></a>

```json
{}

```

get_login_info 请求参数

### 属性

*None*

<h2 id="tocS_Api_get_impl_info_input">Api_get_impl_info_input</h2>

<a id="schemaapi_get_impl_info_input"></a>
<a id="schema_Api_get_impl_info_input"></a>
<a id="tocSapi_get_impl_info_input"></a>
<a id="tocsapi_get_impl_info_input"></a>

```json
{}

```

get_impl_info 请求参数

### 属性

*None*

<h2 id="tocS_Api_get_user_profile_input">Api_get_user_profile_input</h2>

<a id="schemaapi_get_user_profile_input"></a>
<a id="schema_Api_get_user_profile_input"></a>
<a id="tocSapi_get_user_profile_input"></a>
<a id="tocsapi_get_user_profile_input"></a>

```json
{
  "user_id": -9007199254740991
}

```

get_user_profile 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||用户 QQ 号|

<h2 id="tocS_Api_get_login_info_output">Api_get_login_info_output</h2>

<a id="schemaapi_get_login_info_output"></a>
<a id="schema_Api_get_login_info_output"></a>
<a id="tocSapi_get_login_info_output"></a>
<a id="tocsapi_get_login_info_output"></a>

```json
{
  "uin": -9007199254740991,
  "nickname": "string"
}

```

get_login_info 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|uin|integer|true|none||登录 QQ 号|
|nickname|string|true|none||登录昵称|

<h2 id="tocS_Api_get_impl_info_output">Api_get_impl_info_output</h2>

<a id="schemaapi_get_impl_info_output"></a>
<a id="schema_Api_get_impl_info_output"></a>
<a id="tocSapi_get_impl_info_output"></a>
<a id="tocsapi_get_impl_info_output"></a>

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
|milky_version|string|true|none||协议端实现的 Milky 协议版本，目前为 "1.0"|

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

<h2 id="tocS_Api_get_user_profile_output">Api_get_user_profile_output</h2>

<a id="schemaapi_get_user_profile_output"></a>
<a id="schema_Api_get_user_profile_output"></a>
<a id="tocSapi_get_user_profile_output"></a>
<a id="tocsapi_get_user_profile_output"></a>

```json
{
  "nickname": "string",
  "qid": "string",
  "age": -2147483648,
  "sex": "male",
  "remark": "string",
  "bio": "string",
  "level": -2147483648,
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

<h2 id="tocS_Api_get_friend_list_input">Api_get_friend_list_input</h2>

<a id="schemaapi_get_friend_list_input"></a>
<a id="schema_Api_get_friend_list_input"></a>
<a id="tocSapi_get_friend_list_input"></a>
<a id="tocsapi_get_friend_list_input"></a>

```json
{
  "no_cache": false
}

```

get_group_list 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|no_cache|boolean¦null|false|none||是否强制不使用缓存|

<h2 id="tocS_Api_get_friend_list_output">Api_get_friend_list_output</h2>

<a id="schemaapi_get_friend_list_output"></a>
<a id="schema_Api_get_friend_list_output"></a>
<a id="tocSapi_get_friend_list_output"></a>
<a id="tocsapi_get_friend_list_output"></a>

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

<h2 id="tocS_Api_get_friend_info_input">Api_get_friend_info_input</h2>

<a id="schemaapi_get_friend_info_input"></a>
<a id="schema_Api_get_friend_info_input"></a>
<a id="tocSapi_get_friend_info_input"></a>
<a id="tocsapi_get_friend_info_input"></a>

```json
{
  "user_id": -9007199254740991,
  "no_cache": false
}

```

get_friend_info 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||好友 QQ 号|
|no_cache|boolean¦null|false|none||是否强制不使用缓存|

<h2 id="tocS_Api_get_friend_info_output">Api_get_friend_info_output</h2>

<a id="schemaapi_get_friend_info_output"></a>
<a id="schema_Api_get_friend_info_output"></a>
<a id="tocSapi_get_friend_info_output"></a>
<a id="tocsapi_get_friend_info_output"></a>

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

<h2 id="tocS_Api_get_group_list_input">Api_get_group_list_input</h2>

<a id="schemaapi_get_group_list_input"></a>
<a id="schema_Api_get_group_list_input"></a>
<a id="tocSapi_get_group_list_input"></a>
<a id="tocsapi_get_group_list_input"></a>

```json
{
  "no_cache": false
}

```

get_group_list 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|no_cache|boolean¦null|false|none||是否强制不使用缓存|

<h2 id="tocS_Api_get_group_list_output">Api_get_group_list_output</h2>

<a id="schemaapi_get_group_list_output"></a>
<a id="schema_Api_get_group_list_output"></a>
<a id="tocSapi_get_group_list_output"></a>
<a id="tocsapi_get_group_list_output"></a>

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

<h2 id="tocS_Api_get_group_info_input">Api_get_group_info_input</h2>

<a id="schemaapi_get_group_info_input"></a>
<a id="schema_Api_get_group_info_input"></a>
<a id="tocSapi_get_group_info_input"></a>
<a id="tocsapi_get_group_info_input"></a>

```json
{
  "group_id": -9007199254740991,
  "no_cache": false
}

```

get_group_info 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|no_cache|boolean¦null|false|none||是否强制不使用缓存|

<h2 id="tocS_Api_get_group_info_output">Api_get_group_info_output</h2>

<a id="schemaapi_get_group_info_output"></a>
<a id="schema_Api_get_group_info_output"></a>
<a id="tocSapi_get_group_info_output"></a>
<a id="tocsapi_get_group_info_output"></a>

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

<h2 id="tocS_Api_get_group_member_list_input">Api_get_group_member_list_input</h2>

<a id="schemaapi_get_group_member_list_input"></a>
<a id="schema_Api_get_group_member_list_input"></a>
<a id="tocSapi_get_group_member_list_input"></a>
<a id="tocsapi_get_group_member_list_input"></a>

```json
{
  "group_id": -9007199254740991,
  "no_cache": false
}

```

get_group_member_list 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|no_cache|boolean¦null|false|none||是否强制不使用缓存|

<h2 id="tocS_Api_get_group_member_list_output">Api_get_group_member_list_output</h2>

<a id="schemaapi_get_group_member_list_output"></a>
<a id="schema_Api_get_group_member_list_output"></a>
<a id="tocSapi_get_group_member_list_output"></a>
<a id="tocsapi_get_group_member_list_output"></a>

```json
{
  "members": [
    {
      "user_id": -9007199254740991,
      "nickname": "string",
      "sex": "male",
      "group_id": -9007199254740991,
      "card": "string",
      "title": "string",
      "level": -2147483648,
      "role": "owner",
      "join_time": -9007199254740991,
      "last_sent_time": -9007199254740991,
      "shut_up_end_time": -9007199254740991
    }
  ]
}

```

get_group_member_list 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|members|[allOf]|true|none||群成员列表|

<h2 id="tocS_Api_get_group_member_info_input">Api_get_group_member_info_input</h2>

<a id="schemaapi_get_group_member_info_input"></a>
<a id="schema_Api_get_group_member_info_input"></a>
<a id="tocSapi_get_group_member_info_input"></a>
<a id="tocsapi_get_group_member_info_input"></a>

```json
{
  "group_id": -9007199254740991,
  "user_id": -9007199254740991,
  "no_cache": false
}

```

get_group_member_info 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||群成员 QQ 号|
|no_cache|boolean¦null|false|none||是否强制不使用缓存|

<h2 id="tocS_Api_get_group_member_info_output">Api_get_group_member_info_output</h2>

<a id="schemaapi_get_group_member_info_output"></a>
<a id="schema_Api_get_group_member_info_output"></a>
<a id="tocSapi_get_group_member_info_output"></a>
<a id="tocsapi_get_group_member_info_output"></a>

```json
{
  "member": {
    "user_id": -9007199254740991,
    "nickname": "string",
    "sex": "male",
    "group_id": -9007199254740991,
    "card": "string",
    "title": "string",
    "level": -2147483648,
    "role": "owner",
    "join_time": -9007199254740991,
    "last_sent_time": -9007199254740991,
    "shut_up_end_time": -9007199254740991
  }
}

```

get_group_member_info 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|member|[GroupMemberEntity](#schemagroupmemberentity)|true|none||群成员信息|

<h2 id="tocS_Api_get_peer_pins_inputget_peer_pins">Api_get_peer_pins_inputget_peer_pins</h2>

<a id="schemaapi_get_peer_pins_inputget_peer_pins"></a>
<a id="schema_Api_get_peer_pins_inputget_peer_pins"></a>
<a id="tocSapi_get_peer_pins_inputget_peer_pins"></a>
<a id="tocsapi_get_peer_pins_inputget_peer_pins"></a>

```json
{}

```

get_peer_pins 请求参数

### 属性

*None*

<h2 id="tocS_Api_get_peer_pins_output">Api_get_peer_pins_output</h2>

<a id="schemaapi_get_peer_pins_output"></a>
<a id="schema_Api_get_peer_pins_output"></a>
<a id="tocSapi_get_peer_pins_output"></a>
<a id="tocsapi_get_peer_pins_output"></a>

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

<h2 id="tocS_Api_set_peer_pin_input">Api_set_peer_pin_input</h2>

<a id="schemaapi_set_peer_pin_input"></a>
<a id="schema_Api_set_peer_pin_input"></a>
<a id="tocSapi_set_peer_pin_input"></a>
<a id="tocsapi_set_peer_pin_input"></a>

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
|is_pinned|boolean¦null|false|none||是否置顶, `false` 表示取消置顶|

#### 枚举值

|属性|值|
|---|---|
|message_scene|friend|
|message_scene|group|
|message_scene|temp|

<h2 id="tocS_Api_get_cookies_input">Api_get_cookies_input</h2>

<a id="schemaapi_get_cookies_input"></a>
<a id="schema_Api_get_cookies_input"></a>
<a id="tocSapi_get_cookies_input"></a>
<a id="tocsapi_get_cookies_input"></a>

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

<h2 id="tocS_Api_get_cookies_output">Api_get_cookies_output</h2>

<a id="schemaapi_get_cookies_output"></a>
<a id="schema_Api_get_cookies_output"></a>
<a id="tocSapi_get_cookies_output"></a>
<a id="tocsapi_get_cookies_output"></a>

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

<h2 id="tocS_Api_get_csrf_token_input">Api_get_csrf_token_input</h2>

<a id="schemaapi_get_csrf_token_input"></a>
<a id="schema_Api_get_csrf_token_input"></a>
<a id="tocSapi_get_csrf_token_input"></a>
<a id="tocsapi_get_csrf_token_input"></a>

```json
{}

```

get_csrf_token 请求参数

### 属性

*None*

<h2 id="tocS_Api_get_csrf_token_output">Api_get_csrf_token_output</h2>

<a id="schemaapi_get_csrf_token_output"></a>
<a id="schema_Api_get_csrf_token_output"></a>
<a id="tocSapi_get_csrf_token_output"></a>
<a id="tocsapi_get_csrf_token_output"></a>

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

<h2 id="tocS_Api_send_private_message_input">Api_send_private_message_input</h2>

<a id="schemaapi_send_private_message_input"></a>
<a id="schema_Api_send_private_message_input"></a>
<a id="tocSapi_send_private_message_input"></a>
<a id="tocsapi_send_private_message_input"></a>

```json
{
  "user_id": -9007199254740991,
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

<h2 id="tocS_Api_send_private_message_output">Api_send_private_message_output</h2>

<a id="schemaapi_send_private_message_output"></a>
<a id="schema_Api_send_private_message_output"></a>
<a id="tocSapi_send_private_message_output"></a>
<a id="tocsapi_send_private_message_output"></a>

```json
{
  "message_seq": -9007199254740991,
  "time": -9007199254740991
}

```

send_group_message 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|message_seq|integer|true|none||消息序列号|
|time|integer|true|none||消息发送时间|

<h2 id="tocS_Api_send_group_message_input">Api_send_group_message_input</h2>

<a id="schemaapi_send_group_message_input"></a>
<a id="schema_Api_send_group_message_input"></a>
<a id="tocSapi_send_group_message_input"></a>
<a id="tocsapi_send_group_message_input"></a>

```json
{
  "group_id": -9007199254740991,
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

<h2 id="tocS_Api_send_group_message_output">Api_send_group_message_output</h2>

<a id="schemaapi_send_group_message_output"></a>
<a id="schema_Api_send_group_message_output"></a>
<a id="tocSapi_send_group_message_output"></a>
<a id="tocsapi_send_group_message_output"></a>

```json
{
  "message_seq": -9007199254740991,
  "time": -9007199254740991
}

```

send_group_message 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|message_seq|integer|true|none||消息序列号|
|time|integer|true|none||消息发送时间|

<h2 id="tocS_Api_recall_private_message_input">Api_recall_private_message_input</h2>

<a id="schemaapi_recall_private_message_input"></a>
<a id="schema_Api_recall_private_message_input"></a>
<a id="tocSapi_recall_private_message_input"></a>
<a id="tocsapi_recall_private_message_input"></a>

```json
{
  "user_id": -9007199254740991,
  "message_seq": -9007199254740991
}

```

recall_private_message 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||好友 QQ 号|
|message_seq|integer|true|none||消息序列号|

<h2 id="tocS_Api_recall_group_message_input">Api_recall_group_message_input</h2>

<a id="schemaapi_recall_group_message_input"></a>
<a id="schema_Api_recall_group_message_input"></a>
<a id="tocSapi_recall_group_message_input"></a>
<a id="tocsapi_recall_group_message_input"></a>

```json
{
  "group_id": -9007199254740991,
  "message_seq": -9007199254740991
}

```

recall_group_message 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|message_seq|integer|true|none||消息序列号|

<h2 id="tocS_Api_get_message_input">Api_get_message_input</h2>

<a id="schemaapi_get_message_input"></a>
<a id="schema_Api_get_message_input"></a>
<a id="tocSapi_get_message_input"></a>
<a id="tocsapi_get_message_input"></a>

```json
{
  "message_scene": "friend",
  "peer_id": -9007199254740991,
  "message_seq": -9007199254740991
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

<h2 id="tocS_Api_get_message_output">Api_get_message_output</h2>

<a id="schemaapi_get_message_output"></a>
<a id="schema_Api_get_message_output"></a>
<a id="tocSapi_get_message_output"></a>
<a id="tocsapi_get_message_output"></a>

```json
{
  "message": {
    "message_scene": "friend",
    "peer_id": -9007199254740991,
    "message_seq": -9007199254740991,
    "sender_id": -9007199254740991,
    "time": -9007199254740991,
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

<h2 id="tocS_Api_get_history_messages_input">Api_get_history_messages_input</h2>

<a id="schemaapi_get_history_messages_input"></a>
<a id="schema_Api_get_history_messages_input"></a>
<a id="tocSapi_get_history_messages_input"></a>
<a id="tocsapi_get_history_messages_input"></a>

```json
{
  "message_scene": "friend",
  "peer_id": -9007199254740991,
  "start_message_seq": -9007199254740991,
  "limit": 20
}

```

get_history_messages 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|message_scene|string|true|none||消息场景|
|peer_id|integer|true|none||好友 QQ 号或群号|
|start_message_seq|integer¦null|false|none||起始消息序列号，由此开始从新到旧查询，不提供则从最新消息开始|
|limit|integer¦null|false|none||期望获取到的消息数量，最多 30 条|

#### 枚举值

|属性|值|
|---|---|
|message_scene|friend|
|message_scene|group|
|message_scene|temp|

<h2 id="tocS_Api_get_history_messages_output">Api_get_history_messages_output</h2>

<a id="schemaapi_get_history_messages_output"></a>
<a id="schema_Api_get_history_messages_output"></a>
<a id="tocSapi_get_history_messages_output"></a>
<a id="tocsapi_get_history_messages_output"></a>

```json
{
  "messages": [
    {
      "message_scene": "[",
      "peer_id": -9007199254740991,
      "message_seq": -9007199254740991,
      "sender_id": -9007199254740991,
      "time": -9007199254740991,
      "segments": [
        null
      ],
      "friend": null
    }
  ],
  "next_message_seq": -9007199254740991
}

```

get_history_messages 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|messages|[allOf]|true|none||获取到的消息（message_seq 升序排列），部分消息可能不存在，如撤回的消息|
|next_message_seq|integer¦null|false|none||下一页起始消息序列号|

<h2 id="tocS_Api_get_resource_temp_url_input">Api_get_resource_temp_url_input</h2>

<a id="schemaapi_get_resource_temp_url_input"></a>
<a id="schema_Api_get_resource_temp_url_input"></a>
<a id="tocSapi_get_resource_temp_url_input"></a>
<a id="tocsapi_get_resource_temp_url_input"></a>

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

<h2 id="tocS_Api_get_resource_temp_url_output">Api_get_resource_temp_url_output</h2>

<a id="schemaapi_get_resource_temp_url_output"></a>
<a id="schema_Api_get_resource_temp_url_output"></a>
<a id="tocSapi_get_resource_temp_url_output"></a>
<a id="tocsapi_get_resource_temp_url_output"></a>

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

<h2 id="tocS_Api_get_forwarded_messages_input">Api_get_forwarded_messages_input</h2>

<a id="schemaapi_get_forwarded_messages_input"></a>
<a id="schema_Api_get_forwarded_messages_input"></a>
<a id="tocSapi_get_forwarded_messages_input"></a>
<a id="tocsapi_get_forwarded_messages_input"></a>

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

<h2 id="tocS_Api_get_forwarded_messages_output">Api_get_forwarded_messages_output</h2>

<a id="schemaapi_get_forwarded_messages_output"></a>
<a id="schema_Api_get_forwarded_messages_output"></a>
<a id="tocSapi_get_forwarded_messages_output"></a>
<a id="tocsapi_get_forwarded_messages_output"></a>

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

<h2 id="tocS_Api_mark_message_as_read_input">Api_mark_message_as_read_input</h2>

<a id="schemaapi_mark_message_as_read_input"></a>
<a id="schema_Api_mark_message_as_read_input"></a>
<a id="tocSapi_mark_message_as_read_input"></a>
<a id="tocsapi_mark_message_as_read_input"></a>

```json
{
  "message_scene": "friend",
  "peer_id": -9007199254740991,
  "message_seq": -9007199254740991
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

<h2 id="tocS_Api_send_friend_nudge_input">Api_send_friend_nudge_input</h2>

<a id="schemaapi_send_friend_nudge_input"></a>
<a id="schema_Api_send_friend_nudge_input"></a>
<a id="tocSapi_send_friend_nudge_input"></a>
<a id="tocsapi_send_friend_nudge_input"></a>

```json
{
  "user_id": -9007199254740991,
  "is_self": false
}

```

send_friend_nudge 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||好友 QQ 号|
|is_self|boolean¦null|false|none||是否戳自己|

<h2 id="tocS_Api_send_profile_like_input">Api_send_profile_like_input</h2>

<a id="schemaapi_send_profile_like_input"></a>
<a id="schema_Api_send_profile_like_input"></a>
<a id="tocSapi_send_profile_like_input"></a>
<a id="tocsapi_send_profile_like_input"></a>

```json
{
  "user_id": -9007199254740991,
  "count": 1
}

```

send_profile_like 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|user_id|integer|true|none||好友 QQ 号|
|count|integer¦null|false|none||点赞数量|

<h2 id="tocS_Api_get_friend_requests_input">Api_get_friend_requests_input</h2>

<a id="schemaapi_get_friend_requests_input"></a>
<a id="schema_Api_get_friend_requests_input"></a>
<a id="tocSapi_get_friend_requests_input"></a>
<a id="tocsapi_get_friend_requests_input"></a>

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
|limit|integer¦null|false|none||获取的最大请求数量|
|is_filtered|boolean¦null|false|none||`true` 表示只获取被过滤（由风险账号发起）的通知，`false` 表示只获取未被过滤的通知|

<h2 id="tocS_Api_get_friend_requests_output">Api_get_friend_requests_output</h2>

<a id="schemaapi_get_friend_requests_output"></a>
<a id="schema_Api_get_friend_requests_output"></a>
<a id="tocSapi_get_friend_requests_output"></a>
<a id="tocsapi_get_friend_requests_output"></a>

```json
{
  "requests": [
    {
      "time": -9007199254740991,
      "initiator_id": -9007199254740991,
      "initiator_uid": "string",
      "target_user_id": -9007199254740991,
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

<h2 id="tocS_Api_accept_friend_request_input">Api_accept_friend_request_input</h2>

<a id="schemaapi_accept_friend_request_input"></a>
<a id="schema_Api_accept_friend_request_input"></a>
<a id="tocSapi_accept_friend_request_input"></a>
<a id="tocsapi_accept_friend_request_input"></a>

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
|is_filtered|boolean¦null|false|none||是否是被过滤的请求|

<h2 id="tocS_Api_reject_friend_request_input">Api_reject_friend_request_input</h2>

<a id="schemaapi_reject_friend_request_input"></a>
<a id="schema_Api_reject_friend_request_input"></a>
<a id="tocSapi_reject_friend_request_input"></a>
<a id="tocsapi_reject_friend_request_input"></a>

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
|is_filtered|boolean¦null|false|none||是否是被过滤的请求|
|reason|string¦null|false|none||拒绝理由|

<h2 id="tocS_Api_set_group_name_input">Api_set_group_name_input</h2>

<a id="schemaapi_set_group_name_input"></a>
<a id="schema_Api_set_group_name_input"></a>
<a id="tocSapi_set_group_name_input"></a>
<a id="tocsapi_set_group_name_input"></a>

```json
{
  "group_id": -9007199254740991,
  "new_group_name": "string"
}

```

set_group_name 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|new_group_name|string|true|none||新群名称|

<h2 id="tocS_Api_set_group_avatar_input">Api_set_group_avatar_input</h2>

<a id="schemaapi_set_group_avatar_input"></a>
<a id="schema_Api_set_group_avatar_input"></a>
<a id="tocSapi_set_group_avatar_input"></a>
<a id="tocsapi_set_group_avatar_input"></a>

```json
{
  "group_id": -9007199254740991,
  "image_uri": "string"
}

```

set_group_avatar 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|image_uri|string|true|none||头像文件 URI，支持 `file://` `http(s)://` `base64://` 三种格式|

<h2 id="tocS_Api_set_group_member_card_input">Api_set_group_member_card_input</h2>

<a id="schemaapi_set_group_member_card_input"></a>
<a id="schema_Api_set_group_member_card_input"></a>
<a id="tocSapi_set_group_member_card_input"></a>
<a id="tocsapi_set_group_member_card_input"></a>

```json
{
  "group_id": -9007199254740991,
  "user_id": -9007199254740991,
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

<h2 id="tocS_Api_set_group_member_special_title_input">Api_set_group_member_special_title_input</h2>

<a id="schemaapi_set_group_member_special_title_input"></a>
<a id="schema_Api_set_group_member_special_title_input"></a>
<a id="tocSapi_set_group_member_special_title_input"></a>
<a id="tocsapi_set_group_member_special_title_input"></a>

```json
{
  "group_id": -9007199254740991,
  "user_id": -9007199254740991,
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

<h2 id="tocS_Api_set_group_member_admin_input">Api_set_group_member_admin_input</h2>

<a id="schemaapi_set_group_member_admin_input"></a>
<a id="schema_Api_set_group_member_admin_input"></a>
<a id="tocSapi_set_group_member_admin_input"></a>
<a id="tocsapi_set_group_member_admin_input"></a>

```json
{
  "group_id": -9007199254740991,
  "user_id": -9007199254740991,
  "is_set": true
}

```

set_group_member_admin 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||被设置的 QQ 号|
|is_set|boolean¦null|false|none||是否设置为管理员，`false` 表示取消管理员|

<h2 id="tocS_Api_set_group_member_mute_input">Api_set_group_member_mute_input</h2>

<a id="schemaapi_set_group_member_mute_input"></a>
<a id="schema_Api_set_group_member_mute_input"></a>
<a id="tocSapi_set_group_member_mute_input"></a>
<a id="tocsapi_set_group_member_mute_input"></a>

```json
{
  "group_id": -9007199254740991,
  "user_id": -9007199254740991,
  "duration": 0
}

```

set_group_member_mute 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||被设置的 QQ 号|
|duration|integer¦null|false|none||禁言持续时间（秒），设为 `0` 为取消禁言|

<h2 id="tocS_Api_set_group_whole_mute_input">Api_set_group_whole_mute_input</h2>

<a id="schemaapi_set_group_whole_mute_input"></a>
<a id="schema_Api_set_group_whole_mute_input"></a>
<a id="tocSapi_set_group_whole_mute_input"></a>
<a id="tocsapi_set_group_whole_mute_input"></a>

```json
{
  "group_id": -9007199254740991,
  "is_mute": true
}

```

set_group_whole_mute 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|is_mute|boolean¦null|false|none||是否开启全员禁言，`false` 表示取消全员禁言|

<h2 id="tocS_Api_kick_group_member_input">Api_kick_group_member_input</h2>

<a id="schemaapi_kick_group_member_input"></a>
<a id="schema_Api_kick_group_member_input"></a>
<a id="tocSapi_kick_group_member_input"></a>
<a id="tocsapi_kick_group_member_input"></a>

```json
{
  "group_id": -9007199254740991,
  "user_id": -9007199254740991,
  "reject_add_request": false
}

```

kick_group_member 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||被踢的 QQ 号|
|reject_add_request|boolean¦null|false|none||是否拒绝加群申请，`false` 表示不拒绝|

<h2 id="tocS_Api_get_group_announcements_input">Api_get_group_announcements_input</h2>

<a id="schemaapi_get_group_announcements_input"></a>
<a id="schema_Api_get_group_announcements_input"></a>
<a id="tocSapi_get_group_announcements_input"></a>
<a id="tocsapi_get_group_announcements_input"></a>

```json
{
  "group_id": -9007199254740991
}

```

get_group_announcements 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|

<h2 id="tocS_Api_get_group_announcements_output">Api_get_group_announcements_output</h2>

<a id="schemaapi_get_group_announcements_output"></a>
<a id="schema_Api_get_group_announcements_output"></a>
<a id="tocSapi_get_group_announcements_output"></a>
<a id="tocsapi_get_group_announcements_output"></a>

```json
{
  "announcements": [
    {
      "group_id": -9007199254740991,
      "announcement_id": "string",
      "user_id": -9007199254740991,
      "time": -9007199254740991,
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

<h2 id="tocS_Api_send_group_announcement_input">Api_send_group_announcement_input</h2>

<a id="schemaapi_send_group_announcement_input"></a>
<a id="schema_Api_send_group_announcement_input"></a>
<a id="tocSapi_send_group_announcement_input"></a>
<a id="tocsapi_send_group_announcement_input"></a>

```json
{
  "group_id": -9007199254740991,
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
|image_uri|string¦null|false|none||公告附带图像文件 URI，支持 `file://` `http(s)://` `base64://` 三种格式|

<h2 id="tocS_Api_delete_group_announcement_input">Api_delete_group_announcement_input</h2>

<a id="schemaapi_delete_group_announcement_input"></a>
<a id="schema_Api_delete_group_announcement_input"></a>
<a id="tocSapi_delete_group_announcement_input"></a>
<a id="tocsapi_delete_group_announcement_input"></a>

```json
{
  "group_id": -9007199254740991,
  "announcement_id": "string"
}

```

delete_group_announcement 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|announcement_id|string|true|none||公告 ID|

<h2 id="tocS_Api_get_group_essence_messages_input">Api_get_group_essence_messages_input</h2>

<a id="schemaapi_get_group_essence_messages_input"></a>
<a id="schema_Api_get_group_essence_messages_input"></a>
<a id="tocSapi_get_group_essence_messages_input"></a>
<a id="tocsapi_get_group_essence_messages_input"></a>

```json
{
  "group_id": -9007199254740991,
  "page_index": -2147483648,
  "page_size": -2147483648
}

```

get_group_essence_messages 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|page_index|integer|true|none||页码索引，从 0 开始|
|page_size|integer|true|none||每页包含的精华消息数量|

<h2 id="tocS_Api_get_group_essence_messages_output">Api_get_group_essence_messages_output</h2>

<a id="schemaapi_get_group_essence_messages_output"></a>
<a id="schema_Api_get_group_essence_messages_output"></a>
<a id="tocSapi_get_group_essence_messages_output"></a>
<a id="tocsapi_get_group_essence_messages_output"></a>

```json
{
  "messages": [
    {
      "group_id": -9007199254740991,
      "message_seq": -9007199254740991,
      "message_time": -9007199254740991,
      "sender_id": -9007199254740991,
      "sender_name": "string",
      "operator_id": -9007199254740991,
      "operator_name": "string",
      "operation_time": -9007199254740991,
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

<h2 id="tocS_Api_set_group_essence_message_input">Api_set_group_essence_message_input</h2>

<a id="schemaapi_set_group_essence_message_input"></a>
<a id="schema_Api_set_group_essence_message_input"></a>
<a id="tocSapi_set_group_essence_message_input"></a>
<a id="tocsapi_set_group_essence_message_input"></a>

```json
{
  "group_id": -9007199254740991,
  "message_seq": -9007199254740991,
  "is_set": true
}

```

set_group_essence_message 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|message_seq|integer|true|none||消息序列号|
|is_set|boolean¦null|false|none||是否设置为精华消息，`false` 表示取消精华|

<h2 id="tocS_Api_quit_group_input">Api_quit_group_input</h2>

<a id="schemaapi_quit_group_input"></a>
<a id="schema_Api_quit_group_input"></a>
<a id="tocSapi_quit_group_input"></a>
<a id="tocsapi_quit_group_input"></a>

```json
{
  "group_id": -9007199254740991
}

```

quit_group 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|

<h2 id="tocS_Api_send_group_message_reaction_input">Api_send_group_message_reaction_input</h2>

<a id="schemaapi_send_group_message_reaction_input"></a>
<a id="schema_Api_send_group_message_reaction_input"></a>
<a id="tocSapi_send_group_message_reaction_input"></a>
<a id="tocsapi_send_group_message_reaction_input"></a>

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
|reaction|string|true|none||表情 ID|
|reaction_type|string¦null|false|none||发送的回应类型|
|is_add|boolean¦null|false|none||是否添加表情，`false` 表示取消|

#### 枚举值

|属性|值|
|---|---|
|reaction_type|face|
|reaction_type|emoji|

<h2 id="tocS_Api_send_group_nudge_input">Api_send_group_nudge_input</h2>

<a id="schemaapi_send_group_nudge_input"></a>
<a id="schema_Api_send_group_nudge_input"></a>
<a id="tocSapi_send_group_nudge_input"></a>
<a id="tocsapi_send_group_nudge_input"></a>

```json
{
  "group_id": -9007199254740991,
  "user_id": -9007199254740991
}

```

send_group_nudge 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|user_id|integer|true|none||被戳的群成员 QQ 号|

<h2 id="tocS_Api_get_group_notifications_input">Api_get_group_notifications_input</h2>

<a id="schemaapi_get_group_notifications_input"></a>
<a id="schema_Api_get_group_notifications_input"></a>
<a id="tocSapi_get_group_notifications_input"></a>
<a id="tocsapi_get_group_notifications_input"></a>

```json
{
  "start_notification_seq": -9007199254740991,
  "is_filtered": false,
  "limit": 20
}

```

get_group_notifications 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|start_notification_seq|integer¦null|false|none||起始通知序列号|
|is_filtered|boolean¦null|false|none||`true` 表示只获取被过滤（由风险账号发起）的通知，`false` 表示只获取未被过滤的通知|
|limit|integer¦null|false|none||获取的最大通知数量|

<h2 id="tocS_Api_get_group_notifications_output">Api_get_group_notifications_output</h2>

<a id="schemaapi_get_group_notifications_output"></a>
<a id="schema_Api_get_group_notifications_output"></a>
<a id="tocSapi_get_group_notifications_output"></a>
<a id="tocsapi_get_group_notifications_output"></a>

```json
{
  "notifications": [
    {
      "type": "[",
      "group_id": -9007199254740991,
      "notification_seq": -9007199254740991,
      "is_filtered": true,
      "initiator_id": -9007199254740991,
      "state": "[",
      "operator_id": -9007199254740991,
      "comment": "string"
    }
  ],
  "next_notification_seq": -9007199254740991
}

```

get_group_notifications 响应数据

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|notifications|[allOf]|true|none||获取到的群通知（notification_seq 降序排列），序列号不一定连续|
|next_notification_seq|integer¦null|false|none||下一页起始通知序列号|

<h2 id="tocS_Api_accept_group_request_input">Api_accept_group_request_input</h2>

<a id="schemaapi_accept_group_request_input"></a>
<a id="schema_Api_accept_group_request_input"></a>
<a id="tocSapi_accept_group_request_input"></a>
<a id="tocsapi_accept_group_request_input"></a>

```json
{
  "notification_seq": -9007199254740991,
  "notification_type": "join_request",
  "group_id": -9007199254740991,
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
|is_filtered|boolean¦null|false|none||是否是被过滤的请求|

#### 枚举值

|属性|值|
|---|---|
|notification_type|join_request|
|notification_type|invited_join_request|

<h2 id="tocS_Api_reject_group_request_input">Api_reject_group_request_input</h2>

<a id="schemaapi_reject_group_request_input"></a>
<a id="schema_Api_reject_group_request_input"></a>
<a id="tocSapi_reject_group_request_input"></a>
<a id="tocsapi_reject_group_request_input"></a>

```json
{
  "notification_seq": -9007199254740991,
  "notification_type": "join_request",
  "group_id": -9007199254740991,
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
|is_filtered|boolean¦null|false|none||是否是被过滤的请求|
|reason|string¦null|false|none||拒绝理由|

#### 枚举值

|属性|值|
|---|---|
|notification_type|join_request|
|notification_type|invited_join_request|

<h2 id="tocS_Api_accept_group_invitation_input">Api_accept_group_invitation_input</h2>

<a id="schemaapi_accept_group_invitation_input"></a>
<a id="schema_Api_accept_group_invitation_input"></a>
<a id="tocSapi_accept_group_invitation_input"></a>
<a id="tocsapi_accept_group_invitation_input"></a>

```json
{
  "group_id": -9007199254740991,
  "invitation_seq": -9007199254740991
}

```

accept_group_invitation 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|invitation_seq|integer|true|none||邀请序列号|

<h2 id="tocS_Api_reject_group_invitation_input">Api_reject_group_invitation_input</h2>

<a id="schemaapi_reject_group_invitation_input"></a>
<a id="schema_Api_reject_group_invitation_input"></a>
<a id="tocSapi_reject_group_invitation_input"></a>
<a id="tocsapi_reject_group_invitation_input"></a>

```json
{
  "group_id": -9007199254740991,
  "invitation_seq": -9007199254740991
}

```

reject_group_invitation 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|invitation_seq|integer|true|none||邀请序列号|

<h2 id="tocS_Api_upload_private_file_input">Api_upload_private_file_input</h2>

<a id="schemaapi_upload_private_file_input"></a>
<a id="schema_Api_upload_private_file_input"></a>
<a id="tocSapi_upload_private_file_input"></a>
<a id="tocsapi_upload_private_file_input"></a>

```json
{
  "user_id": -9007199254740991,
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

<h2 id="tocS_Api_upload_private_file_output">Api_upload_private_file_output</h2>

<a id="schemaapi_upload_private_file_output"></a>
<a id="schema_Api_upload_private_file_output"></a>
<a id="tocSapi_upload_private_file_output"></a>
<a id="tocsapi_upload_private_file_output"></a>

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

<h2 id="tocS_Api_upload_group_file_input">Api_upload_group_file_input</h2>

<a id="schemaapi_upload_group_file_input"></a>
<a id="schema_Api_upload_group_file_input"></a>
<a id="tocSapi_upload_group_file_input"></a>
<a id="tocsapi_upload_group_file_input"></a>

```json
{
  "group_id": -9007199254740991,
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
|parent_folder_id|string¦null|false|none||目标文件夹 ID|
|file_uri|string|true|none||文件 URI，支持 `file://` `http(s)://` `base64://` 三种格式|
|file_name|string|true|none||文件名称|

<h2 id="tocS_Api_upload_group_file_output">Api_upload_group_file_output</h2>

<a id="schemaapi_upload_group_file_output"></a>
<a id="schema_Api_upload_group_file_output"></a>
<a id="tocSapi_upload_group_file_output"></a>
<a id="tocsapi_upload_group_file_output"></a>

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

<h2 id="tocS_Api_get_private_file_download_url_input">Api_get_private_file_download_url_input</h2>

<a id="schemaapi_get_private_file_download_url_input"></a>
<a id="schema_Api_get_private_file_download_url_input"></a>
<a id="tocSapi_get_private_file_download_url_input"></a>
<a id="tocsapi_get_private_file_download_url_input"></a>

```json
{
  "user_id": -9007199254740991,
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

<h2 id="tocS_Api_get_private_file_download_url_output">Api_get_private_file_download_url_output</h2>

<a id="schemaapi_get_private_file_download_url_output"></a>
<a id="schema_Api_get_private_file_download_url_output"></a>
<a id="tocSapi_get_private_file_download_url_output"></a>
<a id="tocsapi_get_private_file_download_url_output"></a>

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

<h2 id="tocS_Api_get_group_file_download_url_input">Api_get_group_file_download_url_input</h2>

<a id="schemaapi_get_group_file_download_url_input"></a>
<a id="schema_Api_get_group_file_download_url_input"></a>
<a id="tocSapi_get_group_file_download_url_input"></a>
<a id="tocsapi_get_group_file_download_url_input"></a>

```json
{
  "group_id": -9007199254740991,
  "file_id": "string"
}

```

get_group_file_download_url 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|file_id|string|true|none||文件 ID|

<h2 id="tocS_Api_get_group_file_download_url_output">Api_get_group_file_download_url_output</h2>

<a id="schemaapi_get_group_file_download_url_output"></a>
<a id="schema_Api_get_group_file_download_url_output"></a>
<a id="tocSapi_get_group_file_download_url_output"></a>
<a id="tocsapi_get_group_file_download_url_output"></a>

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

<h2 id="tocS_Api_get_group_files_input">Api_get_group_files_input</h2>

<a id="schemaapi_get_group_files_input"></a>
<a id="schema_Api_get_group_files_input"></a>
<a id="tocSapi_get_group_files_input"></a>
<a id="tocsapi_get_group_files_input"></a>

```json
{
  "group_id": -9007199254740991,
  "parent_folder_id": "/"
}

```

get_group_files 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|parent_folder_id|string¦null|false|none||父文件夹 ID|

<h2 id="tocS_Api_get_group_files_output">Api_get_group_files_output</h2>

<a id="schemaapi_get_group_files_output"></a>
<a id="schema_Api_get_group_files_output"></a>
<a id="tocSapi_get_group_files_output"></a>
<a id="tocsapi_get_group_files_output"></a>

```json
{
  "files": [
    {
      "group_id": -9007199254740991,
      "file_id": "string",
      "file_name": "string",
      "parent_folder_id": "string",
      "file_size": -9007199254740991,
      "uploaded_time": -9007199254740991,
      "expire_time": -9007199254740991,
      "uploader_id": -9007199254740991,
      "downloaded_times": -2147483648
    }
  ],
  "folders": [
    {
      "group_id": -9007199254740991,
      "folder_id": "string",
      "parent_folder_id": "string",
      "folder_name": "string",
      "created_time": -9007199254740991,
      "last_modified_time": -9007199254740991,
      "creator_id": -9007199254740991,
      "file_count": -2147483648
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

<h2 id="tocS_Api_move_group_file_input">Api_move_group_file_input</h2>

<a id="schemaapi_move_group_file_input"></a>
<a id="schema_Api_move_group_file_input"></a>
<a id="tocSapi_move_group_file_input"></a>
<a id="tocsapi_move_group_file_input"></a>

```json
{
  "group_id": -9007199254740991,
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
|parent_folder_id|string¦null|false|none||文件所在的文件夹 ID|
|target_folder_id|string¦null|false|none||目标文件夹 ID|

<h2 id="tocS_Api_rename_group_file_input">Api_rename_group_file_input</h2>

<a id="schemaapi_rename_group_file_input"></a>
<a id="schema_Api_rename_group_file_input"></a>
<a id="tocSapi_rename_group_file_input"></a>
<a id="tocsapi_rename_group_file_input"></a>

```json
{
  "group_id": -9007199254740991,
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
|parent_folder_id|string¦null|false|none||文件所在的文件夹 ID|
|new_file_name|string|true|none||新文件名称|

<h2 id="tocS_Api_delete_group_file_input">Api_delete_group_file_input</h2>

<a id="schemaapi_delete_group_file_input"></a>
<a id="schema_Api_delete_group_file_input"></a>
<a id="tocSapi_delete_group_file_input"></a>
<a id="tocsapi_delete_group_file_input"></a>

```json
{
  "group_id": -9007199254740991,
  "file_id": "string"
}

```

delete_group_file 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|file_id|string|true|none||文件 ID|

<h2 id="tocS_Api_create_group_folder_input">Api_create_group_folder_input</h2>

<a id="schemaapi_create_group_folder_input"></a>
<a id="schema_Api_create_group_folder_input"></a>
<a id="tocSapi_create_group_folder_input"></a>
<a id="tocsapi_create_group_folder_input"></a>

```json
{
  "group_id": -9007199254740991,
  "folder_name": "string"
}

```

create_group_folder 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|folder_name|string|true|none||文件夹名称|

<h2 id="tocS_Api_create_group_folder_output">Api_create_group_folder_output</h2>

<a id="schemaapi_create_group_folder_output"></a>
<a id="schema_Api_create_group_folder_output"></a>
<a id="tocSapi_create_group_folder_output"></a>
<a id="tocsapi_create_group_folder_output"></a>

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

<h2 id="tocS_Api_rename_group_folder_input">Api_rename_group_folder_input</h2>

<a id="schemaapi_rename_group_folder_input"></a>
<a id="schema_Api_rename_group_folder_input"></a>
<a id="tocSapi_rename_group_folder_input"></a>
<a id="tocsapi_rename_group_folder_input"></a>

```json
{
  "group_id": -9007199254740991,
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

<h2 id="tocS_Api_delete_group_folder_input">Api_delete_group_folder_input</h2>

<a id="schemaapi_delete_group_folder_input"></a>
<a id="schema_Api_delete_group_folder_input"></a>
<a id="tocSapi_delete_group_folder_input"></a>
<a id="tocsapi_delete_group_folder_input"></a>

```json
{
  "group_id": -9007199254740991,
  "folder_id": "string"
}

```

delete_group_folder 请求参数

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|group_id|integer|true|none||群号|
|folder_id|string|true|none||文件夹 ID|

<h2 id="tocS_Api_set_avatar_input">Api_set_avatar_input</h2>

<a id="schemaapi_set_avatar_input"></a>
<a id="schema_Api_set_avatar_input"></a>
<a id="tocSapi_set_avatar_input"></a>
<a id="tocsapi_set_avatar_input"></a>

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

<h2 id="tocS_Api_set_nickname_input">Api_set_nickname_input</h2>

<a id="schemaapi_set_nickname_input"></a>
<a id="schema_Api_set_nickname_input"></a>
<a id="tocSapi_set_nickname_input"></a>
<a id="tocsapi_set_nickname_input"></a>

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

<h2 id="tocS_Api_set_bio_input">Api_set_bio_input</h2>

<a id="schemaapi_set_bio_input"></a>
<a id="schema_Api_set_bio_input"></a>
<a id="tocSapi_set_bio_input"></a>
<a id="tocsapi_set_bio_input"></a>

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

<h2 id="tocS_Api_get_custom_face_url_list_input">Api_get_custom_face_url_list_input</h2>

<a id="schemaapi_get_custom_face_url_list_input"></a>
<a id="schema_Api_get_custom_face_url_list_input"></a>
<a id="tocSapi_get_custom_face_url_list_input"></a>
<a id="tocsapi_get_custom_face_url_list_input"></a>

```json
{}

```

get_custom_face_url_list 请求参数

### 属性

*None*

<h2 id="tocS_Api_get_custom_face_url_list_output">Api_get_custom_face_url_list_output</h2>

<a id="schemaapi_get_custom_face_url_list_output"></a>
<a id="schema_Api_get_custom_face_url_list_output"></a>
<a id="tocSapi_get_custom_face_url_list_output"></a>
<a id="tocsapi_get_custom_face_url_list_output"></a>

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

<h2 id="tocS_Api_delete_friend_input">Api_delete_friend_input</h2>

<a id="schemaapi_delete_friend_input"></a>
<a id="schema_Api_delete_friend_input"></a>
<a id="tocSapi_delete_friend_input"></a>
<a id="tocsapi_delete_friend_input"></a>

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
|message|string¦null|false|none||错误消息，仅失败时返回|

#### 枚举值

|属性|值|
|---|---|
|status|ok|
|status|failed|

