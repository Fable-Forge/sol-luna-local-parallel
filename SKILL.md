---
name: sol-luna-local-parallel
description: Reuse a small pool of local Luna desktop tasks for Sol-led parallel work with non-overlapping write scopes; create a new task only when no suitable verified Luna task is available.
---

# Sol to Luna Local Parallel

## Overview

Maintain a small pool of user-visible Luna desktop tasks in the same saved local project. A Luna conversation is a reusable workstream, not a disposable conversation for each work item. Sol owns decomposition, conflict prevention, tracking, and final acceptance.

Never substitute internal `spawn_agent` workers when the user asks for Luna. Never create a branch or worktree for this workflow.

## Dispatch Gate

Dispatch only when all conditions hold:

- The user has authorized independent Luna tasks. A standing user preference in global instructions counts.
- At least two units can run concurrently with disjoint write sets and no dependency between those concurrent units. Later related units may be sent to a worker after its current assignment completes.
- The current saved project can be matched unambiguously by path through the project list.
- Each task has a precise goal, allowed write paths, validation command, and completion report.

Keep shared interfaces, entry points, project configuration, lock files, generated indexes, and cross-task integration with Sol. If only one safe task remains, do not create parallel Luna tasks.

## Task Ownership Boundary

- Maintain a delegation registry for the saved project: ownership row, `threadId`, `hostId`, verified model/reasoning/environment, exact title, current assignment, and completion state. Preserve it across compaction and later rounds. A worker created under this skill in an earlier round may be reused when its recorded ID and creation evidence identify it; the user does not need to reauthorize that same workflow worker.
- A conversation found by `list_threads` is not a worker merely because it shares the project, is idle, discusses the same feature, or has "Luna" in its title. For a pre-existing task without verified workflow provenance, enroll it only when the user explicitly identifies and authorizes it; verify its actual model before treating it as Luna. A title is never model or ownership evidence.
- Before every `send_message_to_thread`, confirm that the destination is registered, belongs to the exact saved project and host, has completed its previous assignment, has no pending user input or approval, and is not already running. Sending a message may start a new turn; a request to "only report paths" or "coordinate" is still an assignment.
- A worker's old write allowlist expires when Sol accepts that assignment. A new message must state the new exact allowlist and make every other path read-only. Reusing a conversation never carries file ownership or permission forward implicitly.
- Inspect non-delegated tasks with `list_threads` / `read_thread` only when needed. Never wake, interrupt, retitle, switch models, or send coordination instructions to them under this skill. A user-authorized development plan does not transfer control of unrelated testing or development conversations.
- If another task owns conflicting files, keep those files read-only and continue disjoint work. Defer the shared edit or ask the user when it is essential; do not recruit that task to obtain a handoff. If an out-of-scope message was already sent, disclose the error and stop further sends; do not send a correction, cancellation, or apology to that task without user authorization.

## Build the Ownership Table

Before dispatch, make a private table with `task`, `allowed_write_paths`, `shared_read_only_paths`, `validation`, `depends_on`, and `candidate_threadId`. Group related sequential work into a Luna workstream. One conversation may receive several assignments over time, but only one active assignment at once.

Reject parallel dispatch if any two allowed write sets overlap, one task produces input required by another, or both can write the same generated, cache, or configuration file. Existing dirty files are read-only unless explicitly assigned.

Use 2-3 concurrent Luna workstreams when parallelism is safe. Do not exceed 3 concurrent assignments. The number of work items is not the number of conversations to create.

## Reuse Before Creation

1. Match the current saved project path exactly through `list_projects`. Consult the delegation registry and use `list_threads` / `read_thread` to confirm candidate state. Reconstruct a prior worker only from a recorded `threadId` and creation evidence (or explicit user enrollment), not from its title alone.
2. Prefer a completed, verified `gpt-6-luna` / `xhigh` / `local` worker from the same project whose workstream is related to the new unit. Check its previous result and changed paths before assigning more work. If the prior assignment is blocked, pending user action, or still running, do not reuse it yet.
3. Use `send_message_to_thread` to give that worker the next bounded unit. State the new goal, current workspace baseline, exact write allowlist, read-only context, scoped validation, and completion report. Explicitly say the previous allowlist has expired. Wait for this new turn with `wait_threads`; keep its cursor and completion evidence separate from the previous assignment.
4. Create only the missing concurrent workstream slots. Reuse can happen in waves: when one Luna finishes, Sol may review its changes and send the next related unit to that same conversation while other Luna tasks continue. Do not create a fresh conversation just because a new ownership row is ready.
5. If no suitable worker is available, record why (for example, different project, unverified model, active turn, pending approval, or unrelated scope). Never take over another task merely to avoid creating a conversation.

Example: Luna A finishes a supplier-content unit while Luna B is still working on a separate UI unit. After checking A's result and paths, Sol sends the next supplier-content unit to Luna A with a fresh allowlist; Sol does not create Luna C for that item.

## Create Missing Desktop Tasks

1. Use the exact project match established above.
2. Create only the number of tasks needed to fill safe concurrent slots, with:
   - explicit `title: "Luna <slot> · <stable workstream>"`, for example `Luna A · 问答内容`; every worker title must begin with `Luna`. Keep the workstream title across sequential assignments instead of renaming for every item.
   - `model: gpt-6-luna`
   - `thinking: xhigh`
   - `target.type: project`
   - the matched `projectId`
   - `target.environment.type: local`
3. Record each returned `threadId` and `hostId` in the delegation registry. Never pass a `clientThreadId` to thread tools; resolve the ready thread through the task list if creation is still pending.
4. Verify the created task's stored title. If normalization removed the prefix, use `set_thread_title` on that registered task only and verify again. Keep the `Luna` prefix during follow-ups and later title changes. A title is a visual label, not evidence of the actual model; model verification remains separate.
5. Emit the created-task directive required by the desktop app when reporting created tasks.

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

For a reused thread, begin the new message with: "上一项任务已由 Sol 核对完成；本条是新的独立授权。旧允许写入清单失效，以本条清单为准。" Then include the full contract above. Do not rely on the thread remembering an earlier allowlist or validation command.

## Track and Accept

- Wait on every assigned thread, newly created or reused, with `wait_threads`. Carry forward the cursor for its current assignment; do not mistake an earlier completion, commentary, or timeout for this assignment's completion.
- Read a registered task when it completes or needs attention. Send follow-up to that same registered thread for in-scope corrections; recheck the registry before sending.
- Never use the CLI Stop Hook or `.codex-worker.json` to determine desktop-task completion.
- If a Luna needs another task's path, stop that task. Reassign only after the conflicting owner completes, or keep the shared change with Sol.
- After all assignments report completion, compare the current workspace against the pre-dispatch baseline. Changed paths must be a subset of the union of current assigned paths plus explicit Sol-owned integration paths. Check each completed assignment's changed paths before reusing that conversation.
- Review actual changes and run the combined project verification. Luna reports and scoped tests are evidence, not final acceptance.
- Report partial completion honestly if any thread is blocked, pending approval, or fails combined verification.
- Report which conversations were reused and which were newly created, with their task IDs, actual model/reasoning, completion states, changed-path checks, and combined verification. Do not count sequential assignments as new conversations.

## Quick Reference

| Decision | Required action |
|---|---|
| Two disjoint write sets | Reuse two verified idle Luna workstreams first; create only missing slots |
| Next related unit after a Luna finishes | Review its result, then send the new contract to the same task |
| Existing "Luna" title without provenance | Do not enroll from the title alone |
| Overlapping or shared file | Keep with Sol or run serially |
| Git project | Still use `environment: local` |
| Need a true Luna | Set `model: gpt-6-luna`; do not use internal subagent tools |
| Luna stops talking | Check thread state; do not infer completion from Stop Hook |
| Scoped tests pass | Sol still runs combined verification |

## Common Mistakes

| Mistake | Correction |
|---|---|
| Creating one conversation for every work item | Treat 2-3 Luna conversations as reusable workstreams and send later related units to a completed worker. |
| Assuming an old allowlist remains active | Give every follow-up its own exact paths and validation; expire the old scope. |
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
- `create_thread` is about to run while a completed, verified, related Luna worker is available for the same project.
- A follow-up is being sent before the previous assignment completes or while it needs user input.
- `spawn_agent` is being used as a substitute for an explicitly requested Luna.
- A send/coordination target is absent from the delegation registry, or was selected merely because it shares the project.
- A newly created Luna worker has no explicit `Luna` title prefix, or a pre-existing task is being relabeled to make it appear delegated.
- Sol is about to finish before all thread states and combined verification are checked.
