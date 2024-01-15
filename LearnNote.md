# fastAPI_tutorial
My first FastAPI project

tutorial docs: https://fastapi.tiangolo.com/zh/deployment/versions/

### Lesson 1
https://fastapi.tiangolo.com/zh/tutorial/first-steps/
导入 FastAPI。
创建一个 app 实例。
编写一个路径操作装饰器（如 @app.get("/")）。
编写一个路径操作函数（如上面的 def root(): ...）。
运行开发服务器（如 uvicorn main:app --reload）。

### Lesson 2
https://fastapi.tiangolo.com/zh/tutorial/path-params/
使用 FastAPI，通过简短、直观和标准的 Python 类型声明，你将获得：

编辑器支持：错误检查，代码补全等
数据 "解析"
数据校验
API 标注和自动生成的文档
而且你只需要声明一次即可。

### Lesson 3
https://fastapi.tiangolo.com/zh/tutorial/query-params/
在这个例子中，有3个查询参数：

needy，一个必需的 str 类型参数。
skip，一个默认值为 0 的 int 类型参数。
limit，一个可选的 int 类型参数。