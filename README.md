<div align="center">

# ⚒️ Sol-Luna Local Parallel

English · [简体中文](README.zh-CN.md)

### Reuse Luna workstreams. Keep Sol in control.

<p>Run independent Codex Desktop work in the same local project with a small pool of verified Luna tasks. Sol assigns exclusive write paths, checks each result, and reuses a completed task for the next related unit.</p>

<p>
  <a href="https://github.com/Fable-Forge/sol-luna-local-parallel/blob/main/LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-0969da"></a>
  <img alt="Maturity: experimental" src="https://img.shields.io/badge/maturity-experimental-8250df">
  <img alt="Platform: Codex Desktop" src="https://img.shields.io/badge/platform-Codex_Desktop-1f883d">
  <img alt="Worker: GPT-6 Luna" src="https://img.shields.io/badge/worker-GPT--6_Luna-8250df">
  <a href="https://github.com/Fable-Forge/sol-luna-local-parallel/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/Fable-Forge/sol-luna-local-parallel?style=social"></a>
</p>

<p><strong>🔁 <a href="#reuse-example">See the reuse workflow</a></strong></p>

</div>

**[How it works](#reuse-example) · [When to use it](#use-cases) · [Quick install](#quick-install) · [Compatibility](#compatibility) · [Validation](#validation) · [Contact](#contact)**

---

<a id="reuse-example"></a>
## How task reuse works

Suppose Luna A handles supplier content while Luna B handles a separate UI unit. When A finishes, Sol checks its changes and gives A the next related content unit with a **new** write allowlist. B can continue its own work. The next unit does not require a third conversation.

- **Reuse verified workers first:** match the exact saved project and confirm the task's origin, model, reasoning effort, local environment, and completed state. A matching title alone is not proof.
- **Keep ownership explicit:** each assignment gets its own exclusive write paths and validation. The previous allowlist expires after Sol accepts the result.
- **Accept the integrated result in Sol:** wait for every assigned task, review changed paths, then run combined verification. Luna's completion report is a handoff.

The [Skill instructions](SKILL.md) define the full dispatch gate, boundaries, and prompt contract.

<a id="use-cases"></a>
## When to use it

Use it when a Sol-led Codex Desktop task has at least two independent units with non-overlapping write paths in the same saved local project. The skill may also be invoked explicitly when you ask to delegate parallel work to Luna; its dispatch gate still applies. Keep coupled or shared-file work with Sol.

<a id="quick-install"></a>
## Quick install

Give this instruction to an Agent with command-line access:

```text
Install sol-luna-local-parallel: https://raw.githubusercontent.com/Fable-Forge/sol-luna-local-parallel/main/docs/install.md
```

Or use the Agent Skills CLI:

```bash
npx skills add Fable-Forge/sol-luna-local-parallel
```

Read the [installation guide](docs/install.md) first. See [update](docs/update.md) and [uninstall](docs/uninstall.md) for lifecycle instructions.

<a id="compatibility"></a>
## Compatibility

- Supported: Codex Desktop with local project tasks and `gpt-6-luna` / `xhigh`
- Maturity: `experimental`
- GitHub Topics: `codex`, `multi-agent`, `parallel`, `workflow`

Installation does not guarantee that an already-running session will hot-load the skill. Verify a natural-language trigger in a fresh session after installation. An exact saved-project match and two safe concurrent work units are required before dispatch.

## Repository layout

- `SKILL.md`: triggers, boundaries, and primary workflow
- `agents/openai.yaml`: Codex display metadata
- `references/`: detailed material loaded on demand, when present
- `scripts/`: reusable tools and repository validator, when present
- `docs/`: install, update, and uninstall guides

<a id="validation"></a>
## Validation boundary

Structural validation, installation visibility, real triggering, and final output quality are separate claims. Passing CI proves only the repository structure and static rules; a real Agent trigger still requires its own acceptance test.

If this skill helps your workflow, [star the repository](https://github.com/Fable-Forge/sol-luna-local-parallel/stargazers) so other Codex Desktop users can find it.

<a id="contact"></a>
## Contact and collaboration

- 📚 All skills: [FableForge Agent Skills](https://github.com/Fable-Forge/fableforge-agent-skills)
- 📧 Email: [53815263@qq.com](mailto:53815263@qq.com)
- 🐛 Bugs and feature requests: [sol-luna-local-parallel Issues](https://github.com/Fable-Forge/sol-luna-local-parallel/issues)
- 💬 Usage questions and business collaboration: [FableForge Discussions](https://github.com/Fable-Forge/fableforge-agent-skills/discussions) or email

## License

[MIT](LICENSE) © 2026 FableForge
