# fastAPI_tutorial
My first FastAPI project

tutorial docs: https://fastapi.tiangolo.com/zh/deployment/versions/

### Lesson 1 Start APP
https://fastapi.tiangolo.com/zh/tutorial/first-steps/
导入 FastAPI。
创建一个 app 实例。
编写一个路径操作装饰器（如 @app.get("/")）。
编写一个路径操作函数（如上面的 def root(): ...）。
运行开发服务器（如 uvicorn main:app --reload）。

### Lesson 2 路径参数
https://fastapi.tiangolo.com/zh/tutorial/path-params/
使用 FastAPI，通过简短、直观和标准的 Python 类型声明，你将获得：

编辑器支持：错误检查，代码补全等
数据 "解析"
数据校验
API 标注和自动生成的文档
而且你只需要声明一次即可。

### Lesson 3 查询参数
https://fastapi.tiangolo.com/zh/tutorial/query-params/
在这个例子中，有3个查询参数：

needy，一个必需的 str 类型参数。
skip，一个默认值为 0 的 int 类型参数。
limit，一个可选的 int 类型参数。

### Lesson4 请求体
https://fastapi.tiangolo.com/zh/tutorial/body/#__tabbed_1_1
仅仅使用了 Python 类型声明，FastAPI 将会：

将请求体作为 JSON 读取。
转换为相应的类型（在需要时）。
校验数据。
如果数据无效，将返回一条清晰易读的错误信息，指出不正确数据的确切位置和内容。
将接收的数据赋值到参数 item 中。
由于你已经在函数中将它声明为 Item 类型，你还将获得对于所有属性及其类型的一切编辑器支持（代码补全等）。
为你的模型生成 JSON 模式 定义，你还可以在其他任何对你的项目有意义的地方使用它们。
这些模式将成为生成的 OpenAPI 模式的一部分，并且被自动化文档 UI 所使用。

### lesson5  查询参数和字符串校验
https://fastapi.tiangolo.com/zh/tutorial/query-params-str-validations/
你可以为查询参数声明额外的校验和元数据。
from fastapi import  Query

通用的校验和元数据：

alias
title
description
deprecated
特定于字符串的校验：

min_length
max_length
regex
在这些示例中，你了解了如何声明对 str 值的校验。

请参阅下一章节，以了解如何声明对其他类型例如数值的校验。

### lesson 6 路径参数和数值校验
https://fastapi.tiangolo.com/zh/tutorial/path-params-numeric-validations/
from typing import Annotated    
from fastapi import FastAPI, Path, Query
你能够以与 查询参数和字符串校验 相同的方式使用 Query、Path（以及其他你还没见过的类）声明元数据和字符串校验。

而且你还可以声明数值校验：

gt：大于（greater than）
ge：大于等于（greater than or equal）
lt：小于（less than）
le：小于等于（less than or equal）

### lesson 7 请求体-多个参数
https://fastapi.tiangolo.com/zh/tutorial/body-multiple-params/
from fastapi import Body
你可以添加多个请求体参数到路径操作函数中，即使一个请求只能有一个请求体。

但是 FastAPI 会处理它，在函数中为你提供正确的数据，并在路径操作中校验并记录正确的模式。

你还可以声明将作为请求体的一部分所接收的单一值。

你还可以指示 FastAPI 在仅声明了一个请求体参数的情况下，将原本的请求体嵌入到一个键中

### lesson 8 请求体-字段
from pydantic import BaseModel, Field
你可以使用 Pydantic 的 Field 为模型属性声明额外的校验和元数据。

你还可以使用额外的关键字参数来传递额外的 JSON Schema 元数据。

### lesson 9 请求体-嵌套模型
使用 FastAPI 你可以拥有 Pydantic 模型提供的极高灵活性，同时保持代码的简单、简短和优雅。

而且还具有下列好处：

编辑器支持（处处皆可自动补全！）
数据转换（也被称为解析/序列化）
数据校验
模式文档
自动生成的文档

### lesson 10 模式的额外信息-例子
所以，虽然 example 不是JSON Schema的一部分，但它是OpenAPI的一部分，这将被文档UI使用。

### lesson 11 额外的数据类型
UUID datetime.datetime

### lesson 12 cookie & header
from fastapi import FastAPI, Header

### lesson 13 reponse & form & file
response_model
status_code

OAuth2 规范的 "密码流" 模式规定要通过表单字段发送 username 和 password
from fastapi import FastAPI, File, UploadFile

### lesson 14 错误处理
HTTPException

### lesson 15 路径操作配置
status_code tags summary description docstring
通过传递参数给路径操作装饰器 ，即可轻松地配置路径操作、添加元数据

### lesson 16 Json 兼容器
from fastapi.encoders import jsonable_encoder

### lesson 17 PUT & PATCH

### lesson 18 依赖项
依赖注入常用于以下场景：

共享业务逻辑（复用相同的代码逻辑）
共享数据库连接
实现安全、验证、角色权限
等……
上述场景均可以使用依赖注入，将代码重复最小化。

依赖注入系统如此简洁的特性，让 FastAPI 可以与下列系统兼容：

关系型数据库
NoSQL 数据库
外部支持库
外部 API
认证和鉴权系统
API 使用监控系统
响应数据注入系统
等等……

- 类作为依赖项
- 子依赖项
- 路径操作装饰器依赖项
- 全局依赖项
- yield 依赖项

FastAPI supports dependencies that do some extra steps after finishing.
To do this, use yield instead of return, and write the extra steps (code) after.

### lesson 19 安全性
- Oauth2
- OpenID Connect
- OpenAPI 
 - apiKey
 - http
 - oauth2
 - openIdConnect
FastAPI 在 fastapi.security 模块中为每个安全方案提供了几种工具，这些工具简化了这些安全机制的使用方法。
 -  JWT 令牌（Token）和安全密码哈希（Hash）实现真正的安全机制。

### lesssn 20 中间件 & CORS

### lesson 21 SQL数据库
大部分代码是SQLAlchemy的标准代码，您可以用于任何框架。FastAPI特定的代码和往常一样少。

### lesson 22 更大的应用，多个文件
项目组织方式 

### lesson 23 后台任务、元数据、静态文件
- 导入并使用 BackgroundTasks 通过 路径操作函数 中的参数和依赖项来添加后台任务。
- 标签tags
- 使用 StaticFiles从目录中自动提供静态文件

### lesson 24 测试和调试
- TestClient

