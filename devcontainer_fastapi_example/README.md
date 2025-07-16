# Dev Containers FastAPI 示例

本目录展示了如何为一个简单的 FastAPI 后端项目配置开发容器。

## 目录结构

```
.
├── .devcontainer/      # Dev Container 配置目录
│   └── devcontainer.json # 核心配置文件
├── main.py             # FastAPI 应用
├── requirements.txt    # Python 依赖
└── README.md           # 说明文档
```

## 如何使用

**前提**:

1.  你的本地计算机上已经安装了 **Docker Desktop**。
2.  你的VSCode中已经安装了 **"Dev Containers"** 扩展。

**操作流程**:

1.  **打开项目**

    使用VSCode打开 `devcontainer_fastapi_example` 这个根目录。

2.  **在容器中重新打开**

    VSCode的右下角会弹出一个提示：“Folder contains a Dev Container configuration file. Reopen in Container.”

    点击 **"Reopen in Container"** 按钮。

3.  **等待构建**

    VSCode将根据 `.devcontainer/devcontainer.json` 的配置，自动拉取或构建Docker镜像。第一次可能会花费几分钟时间。构建完成后，VSCode窗口会重新加载。

4.  **开始开发**

    此时，你的VSCode已经完全运行在容器内部了。你可以看到左下角的状态栏显示 `Dev Container: ...`。

    *   **终端也是容器内的**: 打开VSCode的集成终端 (`Ctrl+`` `)，你会发现你正位于容器的Linux环境中，并且Python和相关依赖已经安装好了。
    *   **依赖已安装**: `devcontainer.json` 中的 `postCreateCommand` 已经自动为你执行了 `pip install -r requirements.txt`。
    *   **运行项目**: 在终端中运行 FastAPI 应用：
        ```bash
        uvicorn main:app --host 0.0.0.0 --port 8000
        ```
    *   **端口已转发**: `devcontainer.json` 中的 `forwardPorts` 配置会自动将容器内的8000端口映射到你的本地计算机。直接在本地浏览器中访问 `http://localhost:8000` 即可看到 FastAPI 响应。
    *   **API 文档**: 访问 `http://localhost:8000/docs` 可以查看 FastAPI 自动生成的 Swagger UI 文档。

这个示例展示了如何为后端项目配置Dev Containers，确保所有开发者都在一致的环境中进行开发和测试，并且可以方便地访问API文档。
