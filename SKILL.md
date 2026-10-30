---
name: humanizer-write
description: 编辑、润色和重写中文或英文文本，降低模板化 AI 写作痕迹，同时保留事实、论证、科学证据边界和原作者声音。适用于知乎与微信公众号个人观点文章、博客、科普、一般文案、学术论文、摘要、Results、Introduction、Discussion、图注及 cover letter。支持通用自然化、作者感知个人文章、科研论文三种模式；可用用户批准的范文建立写作档案并依据反馈持续修订。用户提出“去 AI 味”“更像我写的”“humanize”“学术润色”或要求比较原稿与改稿时使用。
---

# Humanizer-write V2 | Author-aware editing

## 目标与不可违反的边界

把文本编辑得更清楚、更自然、更符合作者，而不是以绕过 AI 检测器为目标。AI 痕迹清单只是编辑线索，不是作者身份判定证据。

**最高优先级：** 不发明事实、数字、引用、访谈、研究结果、用户经历或来源；不悄悄改变作者立场、论证顺序、限定条件及不确定性；不把可行性写成已验证结果。原文缺少关键细节时保留抽象表达或明确标注待补信息，禁止为了“具体”而捏造。用户明确要求创作新增内容时，将新增内容与原意编辑区分。

## 任务路由

1. **General**：无个性化参考的一般文章、邮件、说明文。读取 `references/ai-writing-patterns.md` 中相关部分；保持内容中性和直接。
2. **Personal Essay**：知乎、公众号、主观评论、个人经验、用户提出“像我写的”。读取 `references/personal-essay.md`；可读取 `references/author-profile.md`（该档案仅为可验证的初始假设）。以用户提供的样本和当前修改意见为优先，不得把档案当作事实或强制模板。
3. **Scientific**：论文、摘要、Results、Introduction、Discussion、图注、学术 cover letter。读取 `references/nature-science-writing.md` 和 `references/content-fidelity.md`；科研规则覆盖通用“增加情绪、个性、允许混乱”等建议。保护范围、条件、证据强度和 novelty。
4. 用户同时有个人和科研文本时分别路由，不合并风格标准。
5. 只有需要判断“不是……而是……” / `not X, but Y` 的取舍或重复时，读取 `references/negative-parallelism.md`。

## 编辑执行

1. **确认文本边界**：识别原稿、用户提供的背景、允许新增的材料以及目标受众。未提供的事实不能默补。
2. **抓取核心论证**：用内部简表识别主张、依据、例子、限定条件、观点强度和段落功能；标记不能改写的术语、数字与引用。
3. **诊断读者成本**：优先修复空洞抽象、机械强调、重复和逻辑跃迁；不得机械禁用某个字词、破折号、三段式或第一人称。
4. **重写**：尽量小幅编辑；必要时才调整段落。Personal Essay 保留问题如何被提出、分析、形成判断的路径；Scientific 直接交代科学对象、动作、变量与后果。
5. **双重检查**：先核对事实/论证保真，再核对语言、作者声音与读者成本。使用 `references/content-fidelity.md` 的硬门槛。
6. **反馈迭代**：用户明确接受/拒绝的写法才能成为风格证据。参考 `references/evaluation.md`；不可声称自动永久学习或更新了账户记忆/文件，除非真正执行相应操作。

## 交付格式

默认先给**完整可复制的修订稿**，必要时附 2–5 句具体修改说明。用户只要稿件时，省略评分和长诊断。用户要求审计时，展示原文问题、关键修改、保真风险和证据空缺。科研模式在需要时增加简洁的 evidence-boundary 检查。不要以机械 50 分或“已完全去 AI 化”作为认证。

## 按需参考

- `references/ai-writing-patterns.md`：24 类常见写作模式（仅作为候选信号）
- `references/personal-essay.md`：个人观点文的论证与声音保护
- `references/author-profile.md`：用户风格假设和样本登记方法
- `references/nature-science-writing.md`：科研专用规则与 claim map
- `references/negative-parallelism.md`：中英文对举句式判断
- `references/content-fidelity.md`：事实、推断、引用和论证保真硬门槛
- `references/evaluation.md`：评价、对照测试、反馈更新协议
