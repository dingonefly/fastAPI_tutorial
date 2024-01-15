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
