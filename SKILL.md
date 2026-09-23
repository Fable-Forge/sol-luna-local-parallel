---
name: sol-luna-local-parallel
description: Use when a Sol-led Codex desktop task contains two or more independent implementation units with non-overlapping write scopes, or when the user asks to delegate or parallelize work to Luna.
---

# Sol to Luna Local Parallel

## Overview

Create user-visible Luna desktop tasks in the same saved local project. Sol owns decomposition, conflict prevention, tracking, and final acceptance.

Never substitute internal `spawn_agent` workers when the user asks for Luna. Never create a branch or worktree for this workflow.

## Dispatch Gate

Dispatch only when all conditions hold:

- The user has authorized independent Luna tasks. A standing user preference in global instructions counts.
- At least two tasks have disjoint write sets and no sequential dependency.
- The current saved project can be matched unambiguously by path through the project list.
- Each task has a precise goal, allowed write paths, validation command, and completion report.

Keep shared interfaces, entry points, project configuration, lock files, generated indexes, and cross-task integration with Sol. If only one safe task remains, do not create parallel Luna tasks.

## Build the Ownership Table

Before creation, make a private table with `task`, `allowed_write_paths`, `shared_read_only_paths`, `validation`, and `depends_on`.

Reject parallel dispatch if any two allowed write sets overlap, one task produces input required by another, or both can write the same generated, cache, or configuration file. Existing dirty files are read-only unless explicitly assigned.

Use 2-3 concurrent Luna tasks. Do not exceed 3.

## Create Desktop Tasks

1. List Codex projects and match the current saved project path exactly.
2. Create one task per ownership row with:
   - `model: gpt-6-luna`
   - `thinking: xhigh`
   - `target.type: project`
   - the matched `projectId`
   - `target.environment.type: local`
3. Record each returned `threadId` and `hostId`. Never pass a `clientThreadId` to thread tools; resolve the ready thread through the task list if creation is still pending.
4. Emit the created-task directive required by the desktop app when reporting created tasks.

Do not use `worktree`, `startingState`, branch creation, commits, stashes, or merges.

## Luna Prompt Contract

```text
你是独立 Luna 实现任务，直接工作在现有项目目录。
目标：<one goal>
允许写入：<exclusive path list>
只读上下文：<shared paths if needed>
禁止写入：允许清单之外的所有文件、其他 Luna 的范围、共享入口和配置。
禁止：创建分支、创建 worktree、stash、commit、merge、全仓格式化。
验证：<exact scoped command>
如果必须越界，停止修改并报告所需路径、原因和当前状态。
完成后报告：修改文件、验证命令及结果、遗留风险或阻塞。
```

## Track and Accept

- Wait on all created threads with `wait_threads`; carry forward each cursor and do not treat commentary or timeout as completion.
- Read a task when it completes or needs attention. Send follow-up to the same thread for in-scope corrections.
- Never use the CLI Stop Hook or `.codex-worker.json` to determine desktop-task completion.
- If a Luna needs another task's path, stop that task. Reassign only after the conflicting owner completes, or keep the shared change with Sol.
- After all tasks report completion, compare the current workspace against the pre-dispatch baseline. Changed paths must be a subset of the union of assigned paths plus explicit Sol-owned integration paths.
- Review actual changes and run the combined project verification. Luna reports and scoped tests are evidence, not final acceptance.
- Report partial completion honestly if any thread is blocked, pending approval, or fails combined verification.

## Quick Reference

| Decision | Required action |
|---|---|
| Two disjoint write sets | Create two local Luna desktop tasks |
| Overlapping or shared file | Keep with Sol or run serially |
| Git project | Still use `environment: local` |
| Need a true Luna | Set `model: gpt-6-luna`; do not use internal subagent tools |
| Luna stops talking | Check thread state; do not infer completion from Stop Hook |
| Scoped tests pass | Sol still runs combined verification |

## Common Mistakes

| Mistake | Correction |
|---|---|
| Assuming a Git repository requires a worktree | The user's standing preference requires the saved project's local environment. |
| Calling an internal subagent "Luna" | Internal tools cannot guarantee the requested model or create a sidebar task. |
| Giving every Luna the full repository | Give an exclusive write allowlist and make everything else read-only. |
| Running shared integration tests concurrently | Let Luna run scoped checks; Sol runs the combined suite after delivery. |
| Treating delivery as acceptance | Sol reviews the workspace and verifies the integrated result. |

## Red Flags

Stop and correct the dispatch if any of these appear:

- `environment.type` is `worktree`.
- A branch, commit, stash, or merge is proposed.
- Two Luna prompts contain an overlapping allowed path.
- A prompt lacks exact allowed paths or validation.
- More than three Luna tasks are active for one batch.
- `spawn_agent` is being used as a substitute for an explicitly requested Luna.
- Sol is about to finish before all thread states and combined verification are checked.
