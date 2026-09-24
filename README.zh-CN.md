<div align="center">

# ⚒️ Sol-Luna Local Parallel

[English](README.md) · 简体中文

### 复用 Luna 工作流，由 Sol 掌控验收

<p>在同一个本地项目中，以少量已核实的 Luna 任务并行处理独立工作。Sol 分配互斥写入范围、检查每次结果，再把相关的下一项工作交给已完成的任务。</p>

<p>
  <a href="https://github.com/Fable-Forge/sol-luna-local-parallel/blob/main/LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-0969da"></a>
  <img alt="Maturity: experimental" src="https://img.shields.io/badge/maturity-experimental-8250df">
  <img alt="Platform: Codex Desktop" src="https://img.shields.io/badge/platform-Codex_Desktop-1f883d">
  <img alt="Worker: GPT-6 Luna" src="https://img.shields.io/badge/worker-GPT--6_Luna-8250df">
  <a href="https://github.com/Fable-Forge/sol-luna-local-parallel/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/Fable-Forge/sol-luna-local-parallel?style=social"></a>
</p>

<p><strong>🔁 <a href="#reuse-example">查看任务复用示例</a></strong></p>

</div>

**[工作方式](#reuse-example) · [适用场景](#use-cases) · [快速安装](#quick-install) · [兼容性](#compatibility) · [验证边界](#validation) · [联系](#contact)**

---

<a id="reuse-example"></a>
## 任务如何复用

例如，Luna A 负责供应商内容，Luna B 负责互不冲突的 UI 工作。A 完成后，Sol 检查其改动，再给 A 分配下一项相关内容任务，并提供**新的**允许写入清单；B 可以继续工作。下一项任务无需再创建第三个对话。

- **先复用已核实的任务：**精确匹配已保存项目，核实任务来源、模型、思考强度、本地环境和完成状态。仅有相似标题不能证明归属。
- **每次明确文件归属：**每项任务都有独立的互斥写入路径和验证方式；Sol 验收后，旧写入清单即失效。
- **由 Sol 验收整合结果：**等待各项任务完成，核对实际修改路径，再运行组合验证。Luna 的完成报告只是交接证据。

完整的派发条件、边界和提示词契约见 [Skill 指令](SKILL.md)。

<a id="use-cases"></a>
## 适合什么时候用

适用于 Sol 主导的 Codex Desktop 任务：同一已保存的本地项目中，至少有两项写入路径互斥、可以同时执行的独立工作。你也可以明确要求把并行工作交给 Luna，但仍须满足 Skill 的派发条件。共享文件和紧密耦合的工作由 Sol 处理。

<a id="quick-install"></a>
## 快速安装

把下面这句话交给支持命令行的 Agent：

```text
帮我安装 sol-luna-local-parallel：https://raw.githubusercontent.com/Fable-Forge/sol-luna-local-parallel/main/docs/install.md
```

也可以使用 Agent Skills CLI：

```bash
npx skills add Fable-Forge/sol-luna-local-parallel
```

安装前请阅读 [安装说明](docs/install.md)。更新和卸载分别见 [更新说明](docs/update.md) 与 [卸载说明](docs/uninstall.md)。

<a id="compatibility"></a>
## 兼容性

- 支持：可创建本地项目任务、使用 `gpt-6-luna` / `xhigh` 的 Codex Desktop
- 成熟度：`experimental`
- GitHub Topics：`codex`, `multi-agent`, `parallel`, `workflow`

安装不代表正在运行的会话会热加载 Skill。安装后请在新会话中测试自然语言触发；派发前还需要精确匹配已保存项目，并确认有两项可安全并行的工作。

## 仓库结构

- `SKILL.md`：触发条件、边界与主工作流
- `agents/openai.yaml`：Codex 展示元数据
- `references/`：按需加载的详细资料（如有）
- `scripts/`：可复用工具与仓库验证器（如有）
- `docs/`：安装、更新与卸载说明

<a id="validation"></a>
## 验证边界

结构校验、安装可见、真实触发和最终产出质量是四件不同的事。CI 通过只能证明仓库结构和静态规则通过；真实 Agent 触发仍需单独验收。

如果这个 Skill 对你有帮助，欢迎给[仓库点星](https://github.com/Fable-Forge/sol-luna-local-parallel/stargazers)，方便其他 Codex Desktop 用户找到它。

<a id="contact"></a>
## 联系与合作

- 📚 全部 Skill：[FableForge Agent Skills](https://github.com/Fable-Forge/fableforge-agent-skills)
- 📧 Email：[53815263@qq.com](mailto:53815263@qq.com)
- 🐛 Bug 与功能建议：[sol-luna-local-parallel Issues](https://github.com/Fable-Forge/sol-luna-local-parallel/issues)
- 💬 使用交流与业务合作：[FableForge Discussions](https://github.com/Fable-Forge/fableforge-agent-skills/discussions) 或邮件

## License

[MIT](LICENSE) © 2026 FableForge
