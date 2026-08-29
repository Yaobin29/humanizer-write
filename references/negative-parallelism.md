Use this reference as the first-pass check when Chinese or English text repeatedly uses contrastive templates such as `不是……而是……`, `not X, but Y`, `not only X, but also Y`, or `这不是……而是……`, and you need to decide whether to keep or rewrite them. Do not treat `here`, `we`, `Here, we show`, or `We found` as AI patterns by themselves.

# 否定式排比参考

## 核心判断

`不是……而是……` / `not X, but Y` 不是禁用句式。问题出在它被当成默认强调模板时，会让文本显得像在"摆姿态"，而不是在传递信息。相比单独检查 `here/we`，这类跨语言的否定式对举更值得优先检查。

| 场景 | 建议 | 判断依据 |
|---|---|---|
| 纠正真实误解 | 可保留 | 前半句对应读者很可能真的会有的误解 |
| 划清概念边界 | 可保留 | `X` 和 `Y` 是两个容易混淆、且需要区分的概念 |
| 单纯拔高语气 | 建议改写 | 前半句只是垫高情绪，没有新增信息 |
| 科研或说明文陈述 | 通常改写 | 直接说方法、变量、结果通常更清楚 |
| 连续多次出现 | 优先改写 | 节奏机械，容易暴露 AI 模板痕迹 |

## English equivalents

| Pattern | Keep when | Rewrite when |
|---|---|---|
| `not X, but Y` | X and Y are real competing interpretations or concepts | X is only a rhetorical foil for elevating Y |
| `not only X, but also Y` | Both contributions are independently useful and the parallelism helps | The second clause is a generic upgrade of the first |
| `Here, we show...` / `We found...` | The sentence reports the current study or locates the result | It repeatedly replaces the scientific subject with paper narration |

## 快速规则

1. 如果 `X` 不是一个真实存在的误解，删掉前半句。
2. 如果 `Y` 可以直接成立，直接说 `Y`。
3. 如果这是科研、技术、汇报文本，优先改成事实句、方法句或结果句。
4. 只有在"纠偏"本身有信息价值时，才保留这种对照结构。
5. 不要把 `here/we` 当作否定式对举的替代性 AI 指标；它们必须结合句子功能判断。

## 常见坏味道

| 模式 | 为什么别扭 | 更自然的处理 |
|---|---|---|
| 不是小修小补，而是革命性变化 | 语气过满，信息不足 | 直接写具体改了什么、提升了什么 |
| 不是一种工具，而是一种全新范式 | 抽象拔高，没有证据 | 具体说明适用场景和边界 |
| 这不是 A，而是 B | 如果 A 从未被提出，前半句就是虚设靶子 | 直接陈述 B |

## 例子

**原句：**
> 这项研究不是简单优化打印参数，而是在重新定义生物制造的未来。

**建议改写：**
> 这项研究比较了不同曝光时间、材料配比和喷头速度对成形质量的影响。

原因：前半句没有在纠正一个真实误解，后半句又过度拔高，信息密度反而下降。

**原句：**
> 这不是一个分类问题，而是一个因果识别问题。

**可保留：**
> 这不是一个分类问题，而是一个因果识别问题。

原因：这里前半句有实际辨误作用，保留能帮助读者快速建立正确问题框架。

## 外部参考

| 来源 | 相关性 | 备注 |
|---|---|---|
| [Wikipedia: Signs of AI writing - Negative parallelisms](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Negative_parallelisms) | 直接 | 明确把 `Not just X, but also Y`、`Not X, but Y` 列为常见 LLM 模式 |
| [blader/humanizer](https://github.com/blader/humanizer) | 直接 | 上游人性化规则来源，已将该类结构作为修订对象 |
| [Do LLMs write like humans? Variation in grammatical and rhetorical styles](https://arxiv.org/html/2410.16107v1) | 间接 | 支持"LLM 偏好固定语法与修辞结构、风格变化不足"这一更广泛判断 |

## 使用边界

- 不要把单次出现的 `不是……而是……` 直接判成 AI 痕迹。
- 不要把 `here`、`we`、`Here, we show` 或 `We found` 单独判成 AI 痕迹。
- 真正要看的是：是否过度重复，是否在不需要对照时硬做对照，是否让句子比直接陈述更虚。
- 目标不是"消灭这个句式"，而是防止它替代真实表达。
