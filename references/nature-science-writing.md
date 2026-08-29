Use this reference when editing a scientific manuscript, abstract, figure legend, cover letter, or research paragraph toward a clear, concise, high-impact-journal reader experience. It is a mode inside `humanizer-write`, not a separate style imitation skill.

# 科研论文模式：Nature–Science reader experience

## 编辑边界

“Nature/Science 风格”只表示公开的高层次编辑目标：清晰、简洁、可跨学科理解、主语和动作直接、背景服务于结果、结论不超过证据。不要复制已发表论文的句式，不要凭措辞创造 novelty，也不要把谨慎结果改成宣传语。

Nature 的公开作者指导强调主动而直接的表达、拆解技术概念、减少不必要的术语，并让正文保持聚焦。[Nature Portfolio: How to write your paper](https://www.nature.com/nature-portfolio/for-authors/write) 还建议作者熟悉目标期刊的实际读者和文章结构。[Nature formatting guide](https://www.nature.com/nature/for-authors/formatting-guide) 强调背景、主要结论和更广泛语境之间的清晰组织。Science-family 的公开作者指导也强调信息性小标题和简洁呈现，但不同 Science 期刊仍有各自的格式规则。[Research: Guidelines for Authors](https://spj.science.org/page/research/for-authors/)

## 与通用 humanizer 的冲突处理

科研模式覆盖通用 skill 中与学术写作冲突的建议：

| 通用建议 | 科研模式的处理 |
|---|---|
| 注入真实个性 | 不额外注入意见、幽默或第一人称；优先恢复证据和作者真实判断 |
| 允许一些混乱 | 不制造结构混乱；用自然节奏，但维持论证顺序 |
| 变化句长 | 只在不损害变量关系和可读性时调整节奏 |
| 删除中性报道 | 科研结果本来就需要中性报道；删除的是空泛、中性但无信息的句子 |
| 让文字有“灵魂” | 让科学关系可见，不用情绪、夸张或金句替代结果 |

## 不要泛化删除 here / we

`here` 和 `we` 是正常的学术话语资源，不是 AI 标记。以下表达可以根据段落功能保留：

```text
Here, we show that...
Here, we used...
We found...
We observed...
```

尤其在摘要、Results 开头、Methods 和研究问题的总结句中，第一人称或 “here” 可以帮助读者定位当前研究。只有在它们反复替代科学对象，或把本应直接陈述的结果改写成“本文如何贡献”的自我叙述时，才考虑改写。例如：

```text
保留：Here, we show that the magnetic field orients the short microfibres.
改写：The distinction pursued here is the assignment of fibre orientation to the magnetic input.
```

判断重点是句子的功能和信息结构，不是代词本身。

## 最小科学模型

每个段落先建立四个槽位：

| 槽位 | 要回答的问题 |
|---|---|
| 已知/先例 | 之前已经证明了什么？ |
| 当前系统 | 本文具体使用或观察了什么？ |
| 变量关系 | 哪个输入控制、改变或测量哪个变量？ |
| 后果 | 这个关系让什么成为可能，或解释了什么？ |

默认顺序：

```text
已知结果或限制
        ↓
当前材料、场、细胞或实验系统
        ↓
受控变量或观测关系
        ↓
有边界的科学后果
```

推荐句法：

```text
[具体科学对象] + [具体动词] + [变量或对象] + [有边界的后果]
```

优先使用“磁场、声场、细胞、纤维层、水凝胶、测量到的取向”等主语，而不是“本文的区分、该工作的贡献、该方法的创新、角色的分配”等抽象主语。

## 工作流程

### 1. 识别段落功能

标记它是在做什么：背景、先例、gap、系统介绍、结果、机制、限制或意义。Results 句子优先从观察开始；Introduction 可以铺垫问题和 gap；Discussion 可以解释，但不能把解释写成 novelty 证明。

### 2. 建立 claim map

| 角色 | 检查问题 |
|---|---|
| Prior work | 文献实际支持了什么？ |
| Present work | 当前系统做了什么？ |
| Distinguishing variable | 哪个变量真正不同或被独立控制？ |
| Consequence | 读者应该记住什么后果？ |
| Evidence status | 这是 observed、designed、inferred 还是 hypothesized？ |

空缺的槽位不能用更漂亮的语言填补。应删掉这部分修辞负担，或向用户指出缺少科学信息。

### 3. 识别科研版 AI 腔

| 反模式 | 常见信号 | 编辑动作 |
|---|---|---|
| 自我证明式 novelty | “the distinction pursued here is…”, “the novelty lies in…” | 直接写对象、动作和变量关系；不要把正常的 “Here, we show…” 一并删除 |
| 防御式优先级声明 | “not the first combination… rather…” | 非必要时删除；必要时压缩成背景句 |
| 抽象名词堆叠 | “the low-field assignment of…” | 拆成并列主动句 |
| 先例编舞 | “these precedents show…”, “taken together…” 连续出现 | 只保留先例承担的功能 |
| 证据强度漂移 | “suggests” 被改成 “demonstrates” | 恢复原 modality |
| 宣传式意义 | “powerful platform”, “new paradigm”, “unprecedented control” | 改为已展示的具体能力 |

不要机械禁用 “however”, “rather” 或 “not X, but Y”，也不要机械删除 “here/we”。先问它是否纠正了真实误解、区分了两个容易混淆的变量，或改变了读者的解释。

### 4. 从科学关系重写

1. 让材料、场、细胞、结构或测量结果成为主语。
2. 使用 aligns、orients、sets、couples、confines、biases、reveals、limits 等具体动词的准确对应词。
3. 直接说受控变量或观测结果。
4. 只在对比会改变解释时保留 prior-work 对比。
5. 把最重要的后果放在句末或段落末。
6. 逐项检查 scope、condition、modality 和 novelty 是否保持不变。

## “不是……而是……”的科研边界

这个结构不是禁用句式。前半句对应真实误解或概念混淆时可以保留；如果只是为了抬高后半句，就直接说后半句。

| 情况 | 处理 |
|---|---|
| 纠正读者很可能有的误解 | 可以保留，但让两边平行、具体 |
| 区分分类与因果、相关与机制等真实概念 | 可以保留 |
| 把普通优化抬高成“范式变化” | 删除并写具体变量 |
| 科研段落中连续使用 | 优先拆成事实句、方法句或结果句 |

## 用户示例

原句：

> These precedents show that magnetic and acoustic actuation can each contribute to tissue organization, but the distinction pursued here is not the first combination of the two inputs. Rather, it is the low-field assignment of magnetic short microfibre orientation and axial layer pitch to distinct dominant field inputs within the same cell-laden fibre hydrogel.

诊断：读者先被要求理解作者如何定义 novelty，之后才看到磁场和声场分别控制什么。 “the distinction pursued here” 和 “the assignment of” 把一个清楚的物理关系压成抽象名词。

如果优先级声明不是必要信息：

> Magnetic and acoustic actuation perform different structural roles at low field. The magnetic field orients the short microfibres, whereas the acoustic field sets the axial pitch of the layers within the same cell-laden hydrogel.

如果文献边界必须保留：

> Magnetic and acoustic inputs have been combined previously. In this cell-laden fibre hydrogel, however, the magnetic field orients the short microfibres, whereas the acoustic field sets the axial layer pitch at low field.

只有在用户提供的文献证据支持时，才保留 “have been combined previously”。不要从原句本身推断 “first” 或 “novel”。

## 输出契约

科研模式默认输出：

```markdown
问题类型：WHY / HOW / MIX

读者成本：<the sentence delays, hides, or inflates what>

改写：
<revised prose>

科学边界：<scope, condition, modality, novelty preserved or flagged>
```

如果用户要学习而不是只要改写，再给一个对照练习：要求用户指出主语、动词、变量和后果，不要只评价“更优雅”。

## 最终检查

- 第一分句是否从科学对象或清楚的研究动作开始？不要把合法的 “Here, we show…” 误删。
- 每个句子是否有可见主语和具体动词？
- 读者是否能直接看到哪个输入作用于哪个变量？
- “not X, but Y”是否只保留在真实纠偏场景中？
- 是否删除了不必要的 novelty 自我解释？
- 是否保留了 field strength、geometry、cell state 等必要条件？
- 是否把观察、推断、设计目标和机制解释混在了一种语气里？
- 是否有任何地方把 claim 写得更强、更广或更确定？
