# Humanizer-write: AI 写作去痕工具（中文版）

> **声明：**
> - 本项目的核心文件翻译自 [blader/humanizer](https://github.com/blader/humanizer/tree/main)
> - 实用工具部分（核心规则、快速检查清单、质量评分）参考了 [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)
> - 原项目基于维基百科的 [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) 指南

---

## 项目简介

Humanizer-write 是一个用于去除文本中 AI 生成痕迹的工具，帮助你将 AI 生成的内容改写得更自然、更像人类书写的文本。它还包含一个科研论文模式，用于处理摘要、Results、Introduction、Discussion 和 Nature/Science-like 高影响力科学写作。

本项目适用于：
- 编辑和审阅 AI 生成的内容
- 提升文章的人性化程度
- 学习识别 AI 写作的常见模式
- 将科研论文中的自我证明式 novelty、抽象名词堆叠和证据强度漂移改成直接、克制的科学表达
- 优先检查中英文共同的否定式对举（`不是……而是……`、`not X, but Y`）；不把正常的 `here/we` 学术表达单独判成 AI

## 安装

### 方法一：通过 npx 一键安装（推荐）

```bash
npx skills add https://github.com/op7418/Humanizer-zh.git
```

这是最简单的安装方式，会自动将技能安装到正确的目录。

### 方法二：通过 Git 克隆

```bash
# 克隆到 Claude Code 的 skills 目录
git clone https://github.com/op7418/Humanizer-zh.git ~/.claude/skills/humanizer-write
```

### 方法三：手动安装

1. 下载本项目的 ZIP 文件或克隆到本地
2. 将 `Humanizer-zh` 文件夹复制到 Claude Code 的 skills 目录：
   - **macOS/Linux**: `~/.claude/skills/`
   - **Windows**: `%USERPROFILE%\.claude\skills\`

3. 确保文件夹结构如下：
   ```
   ~/.claude/skills/humanizer-write/
   ├── SKILL.md       # 技能定义文件（中文版）
   └── README.md      # 说明文档
   ```

### 验证安装

重启 Claude Code 或重新加载 skills 后，在对话中输入：

```
/humanizer-write
```

如果安装成功，该技能将被激活。

## 使用

### 基础用法

在 Claude Code 中，你可以通过以下方式使用 Humanizer：

#### 1. 直接调用技能

```
/humanizer-write 请帮我人性化以下文本：

[粘贴你的 AI 生成文本]
```

#### 2. 在对话中使用

```
请用 humanizer 帮我改写这段话，让它更自然：

这个项目作为我们团队致力于创新的证明。此外，它展示了我们在不断演变的技术格局中的关键作用。
```

#### 3. 处理文件内容

```
/humanizer-write 请人性化 article.md 文件中的内容
```

### 使用场景示例

#### 场景 1：改写营销文案

**输入：**
```
/humanizer-write
坐落在风景如画的杭州市中心，这家咖啡馆拥有丰富的文化底蕴和令人叹为观止的装饰。它作为城市咖啡文化的焦点，为顾客提供无缝、直观和充满活力的体验。
```

**输出示例：**
> 这家咖啡馆在杭州市中心开了三年，以手冲咖啡和老建筑改造的空间出名。

#### 场景 2：改写学术摘要

**输入：**
```
/humanizer-write
本研究深入探讨了机器学习在医疗诊断中的关键作用，突出了其在不断演变的医疗格局中的重要性。此外，它为该领域的未来发展奠定了坚实的基础。
```

**输出示例：**
> 本研究分析了机器学习在医疗诊断中的应用，重点是肺癌早期筛查。研究使用了 2019-2023 年间 5000 例病历数据。

#### 场景 3：改写博客文章

**输入：**
```
/humanizer-write
人工智能不仅仅是一种技术，它是我们思考未来的方式的革命。行业专家认为这将对整个社会产生持久影响。
```

**输出示例：**
> 我一直在想 AI 会怎么改变我们的工作方式。上周和几个做产品的朋友聊，有人觉得很兴奋，有人担心失业，大概率真相在中间某个无聊的地方。

## 检测的 AI 写作模式

本工具能够识别并修复 **24 种** AI 写作痕迹，分为四大类：

### 📝 内容模式（6种）
1. 过度强调意义、遗产和更广泛的趋势
2. 过度强调知名度和媒体报道
3. 以 -ing 结尾的肤浅分析
4. 宣传和广告式语言
5. 模糊归因和含糊措辞
6. 提纲式的"挑战与未来展望"部分

### 🔤 语言和语法模式（6种）
7. 过度使用的"AI 词汇"
8. 避免使用"是"（系动词回避）
9. 否定式排比（含"不是……而是……"）
10. 三段式法则过度使用
11. 刻意换词（同义词循环）
12. 虚假范围

### 🎨 风格模式（6种）
13. 破折号过度使用
14. 粗体过度使用
15. 内联标题垂直列表
16. 标题中的标题大写
17. 表情符号
18. 弯引号

### 💬 交流模式和填充词（6种）
19. 协作交流痕迹
20. 知识截止日期免责声明
21. 谄媚/卑躬屈膝的语气
22. 填充短语
23. 过度限定
24. 通用积极结论

## 文件说明

- **`SKILL.md`** - 中文版技能定义文件
- **`README.md`** - 本说明文档
- **`references/negative-parallelism.md`** - `不是……而是……` 等否定式排比的判断边界与参考出处
- **`references/nature-science-writing.md`** - 科研论文模式、Nature/Science reader experience、科学反模式和 claim-preservation 检查

**注：** 英文原版请参考 [blader/humanizer](https://github.com/blader/humanizer)

## 手动使用方法

### 基本流程

1. **识别 AI 模式** - 对照 `SKILL.md` 中列出的 24 种模式扫描文本
2. **重写问题片段** - 用自然的表达替换 AI 痕迹
3. **保留核心含义** - 确保信息完整性
4. **维持适当语调** - 匹配文本应有的风格
5. **选择模式** - 通用文本可以恢复自然个性；科研文本切换到科学论文模式
6. **科研模式检查** - 保留变量关系、证据强度、范围、条件和 novelty 边界

### 关键原则

#### ✨ 不仅要"干净"，更要"鲜活"

避免 AI 模式只是基础，好的写作需要真实的人类声音：

- **有观点** - 不要只报告事实，要对它们做出反应
- **变化节奏** - 混合使用长短句
- **承认复杂性** - 真实的人有复杂感受
- **适当使用"我"** - 第一人称是诚实的表现
- **允许一些混乱** - 完美的结构反而显得机械
- **对感受要具体** - 用具体细节替代抽象概括

#### 示例对比

**改写前（AI 味道）：**
> 新的软件更新作为公司致力于创新的证明。此外，它提供了无缝、直观和强大的用户体验——确保用户能够高效地完成目标。这不仅仅是一次更新，而是我们思考生产力方式的革命。

**改写后（人性化）：**
> 软件更新添加了批处理、键盘快捷键和离线模式。来自测试用户的早期反馈是积极的，大多数报告任务完成速度更快。

**变化：**
- 删除了夸大的象征意义（"作为……的证明"）
- 删除了 AI 词汇（"此外"、"无缝"）
- 删除了三段式法则（"无缝、直观和强大"）
- 删除了否定式排比（"不仅仅是……而是……"、"不是……而是……"）
- 添加了具体功能和真实反馈

## 常见 AI 词汇警示列表

以下词汇在 AI 生成文本中出现频率异常高：

- 此外、至关重要、深入探讨、强调
- 持久的、增强、培养、获得
- 突出、相互作用、复杂/复杂性
- 格局（抽象名词）、关键性的、展示
- 织锦（抽象名词）、证明、强调
- 宝贵的、充满活力的

## 贡献

如果你发现翻译问题或想要改进文档，欢迎提交 Issue 或 Pull Request。

### 中文语境特殊性

在翻译和适配过程中，我们考虑了中文写作的特点：
- 某些英文模式在中文中表现不同（如标题大小写问题）
- 添加了适合中文语境的示例
- 调整了部分表达以符合中文习惯
- 将中文里高频但容易失衡的 `不是……而是……` 明确纳入"否定式排比"的判断范围
- 科研模式不追求额外的情绪、幽默或“允许混乱”，而是优先让科学对象、变量和证据边界可见

## 参考资源

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) - 原始指南来源
- [Wikipedia: Signs of AI writing - Negative parallelisms](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Negative_parallelisms) - `Not X, but Y` 类结构的直接参考
- [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) - 维基百科 AI 清理项目
- [blader/humanizer](https://github.com/blader/humanizer) - 原始英文版项目
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) - 实用工具部分的灵感来源
- [Do LLMs write like humans? Variation in grammatical and rhetorical styles](https://arxiv.org/html/2410.16107v1) - 关于 LLM 偏好固定修辞结构的研究背景
- [Nature Portfolio: How to write your paper](https://www.nature.com/nature-portfolio/for-authors/write) - 清晰、简洁、主动语态和拆解复杂概念
- [Nature: Formatting guide](https://www.nature.com/nature/for-authors/formatting-guide) - 面向跨学科读者组织背景、结论和上下文
- [Science-family Research: Guidelines for Authors](https://spj.science.org/page/research/for-authors/) - 信息性结构和简洁呈现

## 许可

本翻译项目遵循原项目的许可协议。核心内容基于维基百科社区的观察和总结。

---

**提示：** 这个工具不是为了"欺骗" AI 检测器，而是为了真正提升写作质量。最好的"去 AI 化"方法是让文字有真实的人类思考和声音。
