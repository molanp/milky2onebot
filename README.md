# milky2onebot

<div align="center">
  <img src="https://github.com/user-attachments/assets/5e9651eb-c23d-4e31-89cd-4e2ed709ef68" width="200" alt="Logo" />
  <p><strong>M2Onebot</strong></p>
  <p>一个将Milky协议转换到Onebot协议的程序</p>
</div>

本项目基于 Milky 1.2.2 和 Onebot.v11(Lucklilly) 开发

## 运行

复制示例配置：

```shell
copy config.example.toml config.toml
```

也可以用环境变量指定配置路径：

```shell
set M2OB_CONFIG=D:\path\to\config.toml
```

```shell
uv run uvicorn src.gateway:app
```

~~我以后会打包成二进制的~~

## 配置

配置文件使用 TOML，默认读取当前工作目录下的 `config.toml`。配置按用途分为：

- `[server]`: 本服务监听地址。
- `[logging]`: 项目日志级别和颜色。
- `[milky]`: Milky 连接方式、地址、token 和重连间隔。
- `[onebot]`: OneBot 连接方式、地址、token 和重连间隔。
- `[heartbeat.onebot]`: OneBot v11 心跳配置。
- `[heartbeat.milky]`: Milky 预留心跳配置，默认关闭。
- `[performance]`: HTTP 超时和 WebSocket 消息大小上限。

所有关键配置都可以用 `M2OB_` 前缀环境变量覆盖，例如 `M2OB_MILKY_HOST`、`M2OB_ONEBOT_PORT`。

## 兼容性

api太多了，我不知道有没有缺失api，有的话提 issue 我再补

## 已完成的测试

本项目使用 [zhongwen-4-fraq-plugins/Matcha-for-Milky](https://github.com/zhongwen-4-fraq-plugins/Matcha-for-Milky) 进行测试

- [x] 消息转发
- [x] 发送消息
  - [x] 文本
  - [x] 图片
  - [x] 图文
  - [x] at
  - [x] 回复
- 事件
  - [x] 撤回
  - [x] 好友添加
  - [x] 群聊添加
- [x] 获取群列表
