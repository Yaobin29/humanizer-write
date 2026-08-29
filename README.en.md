# humanizer-write

[中文说明](README.md) | English

`humanizer-write` is a writing and editing skill for identifying formulaic AI-writing patterns and revising them into clearer, more natural prose while preserving meaning, tone, and evidence boundaries.

It has a dedicated scientific-writing mode for abstracts, figure legends, Results, Introductions, Discussions, cover letters, and Nature/Science-like writing aimed at interdisciplinary readers.

## What makes this version different

This is not only a translation of a general humanizer. The skill includes an English-aware scientific editing mode that focuses on:

| Context | Editing focus |
| --- | --- |
| General English prose | Remove filler, promotional language, vague attribution, excessive transitions, and mechanical repetition |
| Scientific manuscripts | Make the scientific object, action, variable, and evidence relationship explicit |
| Nature/Science-like paragraphs | Organize the logic as known result → present system → variable relationship → bounded consequence |
| Contrastive templates | Evaluate `not X, but Y`, `not only X, but also Y`, and the Chinese equivalent rather than banning them mechanically |
| Academic author narration | Do not treat `Here, we show`, `We found`, or `here/we` as AI markers by themselves |

The scientific mode checks for:

- self-justifying novelty language such as `the novelty lies in...`;
- abstract noun stacks and missing subjects;
- blurred boundaries between observations, inferences, design goals, and mechanistic explanations;
- evidence-strength drift, such as changing `suggests` or `supports` into `demonstrates`;
- rhetorical inflation that removes necessary conditions such as field strength, geometry, or cell state.

The goal is not to game an AI detector. It is to make the writing more precise, readable, and faithful to the author's actual claim.

## Supported text

- English and Chinese articles, reports, blogs, and explanatory prose;
- AI-generated or heavily templated English paragraphs;
- scientific abstracts, figure legends, Results, Introductions, Discussions, and cover letters;
- biomedical, engineering, and interdisciplinary writing where scope, condition, modality, and novelty must remain controlled.

## Installation

### Codex

```bash
git clone https://github.com/Yaobin29/humanizer-write.git ~/.codex/skills/humanizer-write
```

### Claude Code

```bash
git clone https://github.com/Yaobin29/humanizer-write.git ~/.claude/skills/humanizer-write
```

If the destination already exists, back it up or remove the old copy before cloning. Reload the skill or reopen the relevant agent session after installation.

## Usage

Invoke the skill directly:

```text
/humanizer-write
Rewrite the paragraph below for a Nature-style Results section. Preserve the original scope, conditions, modality, and data meaning.
```

For scientific text, providing the paragraph function helps the skill choose the correct editing mode:

```text
Text type: scientific manuscript
Section: Introduction
Task: reduce AI-like phrasing without strengthening the novelty claim
```

The scientific mode normally returns:

1. a one-sentence diagnosis of the reader cost;
2. revised prose;
3. a scientific-boundary check covering scope, condition, modality, and novelty.

## English scientific-writing example

The original sentence explains novelty before showing the physical relationship:

```text
The distinction pursued here is not the first combination of the two inputs. Rather, it is the low-field assignment of magnetic short microfibre orientation and axial layer pitch to distinct dominant field inputs.
```

A more direct version is:

```text
At low field, the magnetic input orients the short microfibres, whereas the acoustic input sets the axial layer pitch within the same cell-laden hydrogel.
```

If the prior-literature boundary is genuinely needed, it can be retained in a bounded form:

```text
Magnetic and acoustic inputs have been combined previously. In this cell-laden fibre hydrogel, however, the magnetic field orients the short microfibres, whereas the acoustic field sets the axial layer pitch at low field.
```

The principle is to state the object, action, and variable relationship directly. Do not infer `first` or `novel` from wording alone, and do not mechanically delete legitimate academic phrases such as `Here, we show...`.

## Patterns covered

`SKILL.md` covers 24 common patterns, including:

- inflated claims about significance, legacy, or industry-wide impact;
- promotional language and vague attribution;
- superficial sentence-final `-ing` analysis;
- high-frequency AI vocabulary, filler phrases, and excessive hedging;
- `not X, but Y`, `not only X, but also Y`, and the Chinese equivalent;
- forced lists of three, false ranges, and thesaurus-driven repetition;
- overuse of em dashes, bold text, emojis, and inline headings;
- conversational residue, knowledge-cutoff disclaimers, and generic positive conclusions;
- abstract subjects, novelty self-justification, and evidence-strength drift in scientific prose.

## Files

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

- `SKILL.md`: skill definition and complete editing rules;
- `README.md`: Chinese documentation;
- `README.en.md`: this English documentation;
- `references/nature-science-writing.md`: scientific-writing mode and claim-preservation rules;
- `references/negative-parallelism.md`: decision boundaries for contrastive templates in Chinese and English.

## Sources

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [Wikipedia: Negative parallelisms](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#Negative_parallelisms)
- [blader/humanizer](https://github.com/blader/humanizer)
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)
- [Do LLMs write like humans?](https://arxiv.org/html/2410.16107v1)
- [Nature Portfolio: How to write your paper](https://www.nature.com/nature-portfolio/for-authors/write)
- [Nature formatting guide](https://www.nature.com/nature/for-authors/formatting-guide)
- [Science-family Research: Guidelines for Authors](https://spj.science.org/page/research/for-authors/)

## License

See [`LICENSE`](LICENSE). When reusing or redistributing this package, also follow the licenses and attribution requirements of the original sources and referenced materials.
