# Install sol-luna-local-parallel

## 给使用者

推荐把下面这句话交给你的 Agent：

```text
安装 sol-luna-local-parallel：https://raw.githubusercontent.com/Fable-Forge/sol-luna-local-parallel/main/docs/install.md
```

## 给执行安装的 Agent

### 目标

从 `https://github.com/Fable-Forge/sol-luna-local-parallel` 安装 `sol-luna-local-parallel`，验证目标目录和 `SKILL.md`，并诚实报告哪些 Agent 已可发现。

### 边界

- 安装前确定目标运行时。当前 Skill 的桌面任务复用流程仅支持 Codex Desktop；放入其他 Agent Skills 目录不代表具备所需桌面任务工具。
- 不覆盖内容不同的现有目录；发现冲突时先报告哈希或差异。
- 不写入当前项目工作区之外的无关位置。
- 不声称正在运行的会话会热加载；需要时请用户开启新会话验证。

### 推荐安装

```bash
npx skills add Fable-Forge/sol-luna-local-parallel
```

### 手动目标目录

| 运行时 | 目标目录 |
|---|---|
| Codex | `~/.codex/skills/sol-luna-local-parallel/` |
| Claude Code | `~/.claude/skills/sol-luna-local-parallel/` |
| Agent Skills | `~/.agents/skills/sol-luna-local-parallel/` |

手动安装时，只复制本仓库的 skill payload：`SKILL.md`、`agents/`、`references/` 和功能性 `scripts/`；不要把 README、许可证或 GitHub workflow 放进运行时目录。

### 验证

1. 确认目标目录中的 `SKILL.md` 存在。
2. 对比源与目标 payload 的 SHA-256 或逐文件清单。
3. 若本机有 Agent Skills/Codex validator，运行结构校验。
4. 在新会话中用 README 所述自然语言场景测试是否真实触发。
5. 分别报告 `结构有效`、`安装可见` 和 `真实触发`，未执行的项目标为 `pending_external`。
