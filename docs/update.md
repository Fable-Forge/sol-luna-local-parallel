# Update sol-luna-local-parallel

## 给使用者

```text
更新 sol-luna-local-parallel：https://raw.githubusercontent.com/Fable-Forge/sol-luna-local-parallel/main/docs/update.md
```

## 给执行更新的 Agent

1. 定位已安装目录并确认目标确实是 `sol-luna-local-parallel`。
2. 获取 `https://github.com/Fable-Forge/sol-luna-local-parallel` 的最新版本。
3. 在覆盖前比较本地 payload；若用户修改过，停止并展示差异。
4. 重新运行安装命令或按 `docs/install.md` 手动同步 payload。
5. 重新做结构校验、逐文件哈希和新会话触发测试。

本次更新把 Luna 对话改为可复用的工作流。更新后在新会话中测试：先核实旧任务的来源与状态，再为下一项工作指定新的写入清单；不要仅凭标题复用已有对话。

推荐命令：

```bash
npx skills add Fable-Forge/sol-luna-local-parallel
```

不要用“命令成功”替代安装内容和实际触发验证。
