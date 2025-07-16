# Claude Code (终端AI代码助手) 示例

本目录提供一个使用 `Claude Code` 与 `Git` 和 `Node.js` 项目交互的示例。

## 目录结构

```
.
├── index.js      # 示例脚本
├── package.json  # 项目配置文件
├── CLAUDE.md     # Claude Code的配置文件
└── README.md     # 说明文档
```

## 如何使用

**前提**: 你已经安装了 `claude-code` 并完成了认证。同时，此目录已经是一个 `git` 仓库。

1.  **初始化项目**

    ```bash
    # 安装依赖
    npm install
    ```

2.  **启动 `Claude Code`**

    在终端中，进入此目录，然后启动 `Claude Code` 的交互式会话：

    ```bash
    claude
    ```

3.  **与 `Claude Code` 交互**

    现在你可以用自然语言与 `Claude Code` 对话了。由于 `CLAUDE.md` 文件的存在，`Claude Code` 会知道这个项目的特定规范。

    **示例指令:**

    *   **理解项目**: `Claude Code` 会读取 `CLAUDE.md` 和其他文件来理解项目。
        > "你好，请问这个项目是做什么的？"

    *   **代码修改**: 让 `Claude Code` 遵循 `CLAUDE.md` 中的规范来修改代码。
        > "请修改 index.js，在'successful'前面加上'request'。

        `Claude Code` 会进行修改，并且其代码风格会遵循你在 `CLAUDE.md` 中定义的规则（例如，使用单引号）。

    *   **Git操作**: `Claude Code` 可以帮你处理Git工作流。
        > "请查看当前的git状态。"
        > "请帮我暂存所有修改，并创建一个commit。commit消息应该是 'feat: update response message'。"

        `Claude Code` 会执行 `git add .` 和 `git commit -m "..."`。

    *   **代码审查**:
        > "/review index.js"

        使用斜杠命令 `/review`，`Claude Code` 会对指定文件进行代码审查，并给出建议。

这个示例展示了 `Claude Code` 如何通过 `CLAUDE.md` 文件深度集成到你的项目中，理解并遵循你的编码规范，同时还能作为你的Git助手，简化版本控制操作。
