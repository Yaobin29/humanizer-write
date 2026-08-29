# humanizer-write

中文说明｜[English README](README.en.md)

`humanizer-write` 是一个用于编辑和审阅文本的写作 skill：识别模板化的 AI 写作痕迹，并在保留原意、语气和证据边界的前提下，使表达更直接、自然、具体。

它尤其适合英文科研写作，包括 abstract、figure legend、Results、Introduction、Discussion、cover letter，以及面向 Nature/Science-like 跨学科读者的段落。

## 这个版本的重点

这个 skill 不只是把英文规则翻译成中文。它加入了面向英文科研文本的编辑模式：

| 场景 | 处理重点 |
| --- | --- |
| 通用英文文本 | 删除填充短语、宣传式语言、模糊归因、过度连接和机械重复 |
| 英文科研论文 | 让科学对象、动作、变量和证据关系直接可见 |
| Nature/Science-like 段落 | 组织为“已知结果 → 当前系统 → 变量关系 → 有边界的后果” |
| 中英文共同的对举句式 | 检查 `不是……而是……`、`not X, but Y`、`not only X, but also Y` 是否真的有辨误作用 |
| 学术作者叙述 | 不把 `Here, we show`、`We found` 或 `here/we` 本身误判为 AI 痕迹 |

科研模式会特别检查：

- 自我证明式 novelty，例如 `the novelty lies in...`；
- 抽象名词堆叠和主语缺失；
- 把观察、推断、设计目标和机制解释写成同一种确定语气；
- 把 `suggests`、`supports` 等谨慎表述不恰当地改成 `demonstrates`；
- 删除修辞性拔高，同时保留 field strength、geometry、cell state 等必要条件。

目标不是“欺骗” AI 检测器，而是让文本真正更清楚、更像作者在准确地表达自己的判断。

## 适用文本

- 英文和中文的文章、报告、博客及说明文；
- AI 生成或过度模板化的英文段落；
- 科研摘要、图注、Results、Introduction、Discussion 和 cover letter；
- 需要保持 scope、condition、modality 和 novelty 边界的生物医学、工程和跨学科写作。

## 安装

### Codex

```bash
git clone https://github.com/Yaobin29/humanizer-write.git ~/.codex/skills/humanizer-write
```

### Claude Code

```bash
git clone https://github.com/Yaobin29/humanizer-write.git ~/.claude/skills/humanizer-write
```

如果目标目录已经存在，请先备份或删除旧副本，再执行克隆。安装后重新加载 skill，或重新打开对应的 agent 会话。

## 使用

直接调用：

```text
/humanizer-write
请把下面这段话改成适合 Nature-style Results 的英文。保留原有的 scope、condition、modality 和数据含义。
```

处理科研文本时，最好同时说明段落功能：

```text
Text type: scientific manuscript
Section: Introduction
Task: reduce AI-like phrasing without strengthening the novelty claim
```

科研模式默认给出：

1. 一句读者成本诊断；
2. 改写后的句子或段落；
3. 科学边界检查，说明 scope、condition、modality 和 novelty 是否保持不变。

## 英文科研示例

原句把物理关系压缩成了抽象的 novelty 自我解释：

```text
The distinction pursued here is not the first combination of the two inputs. Rather, it is the low-field assignment of magnetic short microfibre orientation and axial layer pitch to distinct dominant field inputs.
```

更直接的写法是：

```text
At low field, the magnetic input orients the short microfibres, whereas the acoustic input sets the axial layer pitch within the same cell-laden hydrogel.
```

如果“此前已有组合”这一文献边界确实需要保留，可以写成：

```text
Magnetic and acoustic inputs have been combined previously. In this cell-laden fibre hydrogel, however, the magnetic field orients the short microfibres, whereas the acoustic field sets the axial layer pitch at low field.
```

这里的原则是直接写出对象、动作和变量关系；不从措辞本身推断 `first` 或 `novel`，也不机械删除正常的 `Here, we show...`。

## 检查的写作模式

`SKILL.md` 覆盖 24 类常见问题，包括：

- 夸大的意义、遗产或行业影响；
- 宣传式语言和模糊归因；
- 句末肤浅的 `-ing` 分析；
- 高频 AI 词汇、填充短语和过度限定；
- `not X, but Y`、`不是……而是……` 等否定式排比；
- 强行三段式、虚假范围和同义词循环；
- 破折号、粗体、表情符号和内联标题的过度使用；
- 协作交流痕迹、知识截止日期免责声明和通用积极结论；
- 科研文本中的抽象主语、novelty 自证和证据强度漂移。

## 文件

```text
humanizer-write/
├── SKILL.md
├── README.md
├── README.en.md
├── LICENSE
└── references/
    ├── nature-science-writing.md
    └── negative-parallelism.md
```

- `SKILL.md`：skill 定义和完整处理规则；
- `README.md`：中文说明；
- `README.en.md`：English documentation；
- `references/nature-science-writing.md`：英文科研论文模式和科学 claim-preservation 规则；
- `references/negative-parallelism.md`：中英文否定式排比的判断边界。

## 参考来源

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [Wikipedia: Negative parallelisms](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Negative_parallelisms)
- [blader/humanizer](https://github.com/blader/humanizer)
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)
- [Do LLMs write like humans?](https://arxiv.org/html/2410.16107v1)
- [Nature Portfolio: How to write your paper](https://www.nature.com/nature-portfolio/for-authors/write)
- [Nature formatting guide](https://www.nature.com/nature/for-authors/formatting-guide)
- [Science-family Research: Guidelines for Authors](https://spj.science.org/page/research/for-authors/)

## 许可

请参阅 [`LICENSE`](LICENSE)。使用或再发布时，请同时遵守原始来源和对应参考资料的许可要求。
