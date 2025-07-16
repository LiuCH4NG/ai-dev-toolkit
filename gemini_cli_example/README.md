# Gemini CLI 示例

本目录提供一些使用 `Gemini CLI` 的基础和进阶示例。

## 如何使用

**前提**: 你已经通过 `npx` 或 `npm` 安装了 `gemini-cli` 并完成了认证。

打开终端，你可以直接通过 `gemini` 命令与AI进行交互。下面是一些实用的例子。

### 示例1: 生成代码

你可以让 `Gemini CLI` 为你编写一个完整的脚本文件。

**指令:**

```bash
gemini "创建一个Python脚本，名为 aio_requests.py。这个脚本需要使用 aiohttp 库并发地向3个不同的URL发送GET请求，并打印出每个请求的状态码。请包含完整的代码和错误处理。" > aio_requests.py
```

**说明:**

*   我们用自然语言清晰地描述了需求：脚本语言、文件名、功能、使用的库以及错误处理。
*   通过 `> aio_requests.py`，我们将 `Gemini CLI` 生成的内容直接输出到一个新文件中。

### 示例2: 解释代码

如果你有一个不熟悉的代码文件，可以让 `Gemini CLI` 为你解释。

**指令:**

```bash
cat aio_requests.py | gemini "请逐行解释这段Python代码的功能，特别是 aiohttp 和 asyncio 的用法。"
```

**说明:**

*   我们使用 `cat` 命令读取文件内容，并通过管道 `|` 将其作为输入传递给 `Gemini CLI`。
*   `Gemini CLI` 会接收管道内容作为上下文，然后根据你的问题进行回答。

### 示例3: 利用Web搜索获取实时信息

`Gemini CLI` 可以使用 `@search` 工具来回答需要最新信息的问题。

**指令:**

```bash
gemini "@search anaconda被uv收购的事件是真的吗？"
```

**说明:**

*   `@search` 工具会驱动 `Gemini CLI` 进行网络搜索，并基于搜索结果进行回答，确保信息的时效性和准确性。

### 示例4: 生成文档

你可以让 `Gemini CLI` 帮你为项目生成文档。

**指令:**

```bash
gemini "请为 aio_requests.py 脚本编写一个Markdown格式的说明文档，包含功能介绍、如何安装依赖 (aiohttp) 以及如何运行。" > aio_requests_readme.md
```

这些示例展示了 `Gemini CLI` 如何成为你强大的终端助手，无论是编码、学习还是文档撰写，都能极大地提升你的效率。
