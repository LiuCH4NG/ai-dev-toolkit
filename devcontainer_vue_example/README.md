# Dev Containers Vue.js 示例

本目录展示了如何为一个简单的 Vue.js 前端项目配置开发容器。

## 目录结构

```
.
├── .devcontainer/      # Dev Container 配置目录
│   └── devcontainer.json # 核心配置文件
├── public/
│   └── index.html      # Vue 应用的HTML模板
├── src/
│   ├── App.vue         # Vue 根组件
│   └── main.js         # Vue 应用入口
├── package.json        # 项目依赖
└── README.md           # 说明文档
```

## 如何使用

**前提**:

1.  你的本地计算机上已经安装了 **Docker Desktop**。
2.  你的VSCode中已经安装了 **"Dev Containers"** 扩展。

**操作流程**:

1.  **打开项目**

    使用VSCode打开 `devcontainer_vue_example` 这个根目录。

2.  **在容器中重新打开**

    VSCode的右下角会弹出一个提示：“Folder contains a Dev Container configuration file. Reopen in Container.”

    点击 **"Reopen in Container"** 按钮。

3.  **等待构建**

    VSCode将根据 `.devcontainer/devcontainer.json` 的配置，自动拉取或构建Docker镜像。第一次可能会花费几分钟时间。构建完成后，VSCode窗口会重新加载。

4.  **开始开发**

    此时，你的VSCode已经完全运行在容器内部了。你可以看到左下角的状态栏显示 `Dev Container: ...`。

    *   **终端也是容器内的**: 打开VSCode的集成终端 (`Ctrl+`` `)，你会发现你正位于容器的Linux环境中，并且Node.js已经安装好了。
    *   **依赖已安装**: `devcontainer.json` 中的 `postCreateCommand` 已经自动为你执行了 `npm install`。
    *   **运行项目**: 在终端中运行 Vue 开发服务器：
        ```bash
        npm run serve
        ```
    *   **端口已转发**: `devcontainer.json` 中的 `forwardPorts` 配置会自动将容器内的8080端口映射到你的本地计算机。直接在本地浏览器中访问 `http://localhost:8080` 即可看到 Vue 应用。

这个示例展示了如何为前端项目配置Dev Containers，确保所有开发者都在一致的环境中进行开发和测试。
