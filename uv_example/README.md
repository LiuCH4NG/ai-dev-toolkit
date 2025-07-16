# UV (Python 项目管理) 核心示例

本目录旨在展示 `uv` 作为现代化Python项目管理工具的核心功能，重点突出其如何使用 `uv init`、`uv pip sync`、`pyproject.toml` 和 `uv.lock` 来保证开发环境的一致性和可复现性。

## 目录结构

```
.
├── main.py           # 示例Python脚本
├── pyproject.toml    # 项目定义与依赖声明文件 (PEP 621)
├── uv.lock           # uv生成的锁文件，确保依赖版本精确一致
└── README.md         # 说明文档
```

## 核心工作流

这种基于 `pyproject.toml` 的工作流是现代Python开发的最佳实践。

1.  **初始化新项目 (uv init)**

    对于一个全新的项目，你可以使用 `uv init` 来交互式地生成 `pyproject.toml` 文件，并自动创建虚拟环境。

    ```bash
    # 在一个空目录中运行
    uv init
    ```

2.  **同步环境 (uv pip sync / uv sync)**

    在已经存在 `pyproject.toml` 的项目中，`uv pip sync` 是最核心的命令之一。它会读取 `pyproject.toml` (或 `uv.lock`)，并确保你的虚拟环境与文件中声明的依赖 **完全一致**。这意味着它会：
    -   安装所有必需的包。
    -   **移除** 虚拟环境中任何未在 `pyproject.toml` 中声明的包。

    ```bash
    # 确保你已经创建并激活了虚拟环境
    uv venv
    source .venv/bin/activate

    # 同步环境
    uv pip sync
    ```

    **`uv pip sync` vs `uv sync`**

    *   **`uv pip sync`**: 专注于将 **当前激活的虚拟环境** 与 `pyproject.toml` 或 `uv.lock` 中声明的依赖 **精确同步**。它会安装缺失的包，并 **移除** 虚拟环境中任何未在声明文件中列出的包。适用于虚拟环境已存在的情况。
    *   **`uv sync`**: 这是一个更高级、更便捷的命令。如果当前目录没有虚拟环境，它会 **自动创建一个**（等同于 `uv venv`），然后执行 `uv pip sync` 的功能。适用于新项目快速启动或不确定虚拟环境状态时。简而言之，`uv sync` = `uv venv` (如果需要) + `uv pip sync`。

    对于新项目或不确定环境状态时，可以直接使用 `uv sync`：
    ```bash
    uv sync
    ```

3.  **运行代码**

    ```bash
    python main.py
    ```

4.  **管理依赖**

    *   **添加新依赖**:
        首先，在 `pyproject.toml` 文件的 `[project.dependencies]` 列表中手动添加新的包，例如 `pandas`。
        ```toml
        dependencies = [
            "requests==2.31.0",
            "pandas"
        ]
        ```
        然后，再次运行 `uv pip sync` 来更新你的环境。

    *   **生成/更新锁文件 (uv pip compile)**:
        为了让其他开发者或CI/CD环境能够安装与你完全一致的依赖版本（包括子依赖），你需要生成或更新 `uv.lock` 文件。

        ```bash
        # --update-all 会查找所有依赖的最新兼容版本
        uv pip compile pyproject.toml --output-file uv.lock --update-all
        ```

        **你应该将 `pyproject.toml` 和 `uv.lock` 都提交到版本控制中。**

    *   **从锁文件精确同步**:
        当其他协作者拿到你的项目后，他们只需要运行以下命令，即可完美复现你的开发环境：
        ```bash
        uv pip sync --locked
        ```

这个示例展示了 `uv` 如何通过声明式的项目文件和锁文件机制，解决了传统Python项目依赖管理的痛点，带来了更可靠、更高效的协作体验。