#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按 humanizer-write 规则程序化扫描文章的 AI 写作痕迹。

用法：把本脚本与待查的 article.html 放在同一目录，运行 python3 scan_ai_tells.py。
第【9】节「口语断言腔」对应 references/zh-colloquial-assertions.md。

这是本仓库之外的本地补充（原仓库无此脚本）。
用法：复制到文章目录（需有 article.html），python3 scan_ai_tells.py

实测效果（2026-09-22，一篇 9000 字的公众号科普稿）：
  否定式排比「不是…而是」  6 → 0
  破折号「——」           15 → 0
  <strong> 粗体              62 → 11
  粗体小标题列表            6 → 0
  连续三句长度相近          4 → 0 处
  正文长度               9174 → 7676 字符
"""
import os
import re
import statistics

BASE = os.path.dirname(os.path.abspath(__file__))
raw = open(os.path.join(BASE, "article.html"), encoding="utf-8").read()

text = re.sub(r"<br\s*/?>", "\n", raw)
text = re.sub(r"</p>|</h2>|</div>|</blockquote>", "\n", text)
plain = re.sub(r"<[^>]+>", "", text)
plain = re.sub(r"[ \t]+", " ", plain)

print("=" * 66)
print("humanizer-write 扫描报告")
print("=" * 66)

print("\n【1】否定式排比「不是……而是」类（技能列为最高优先级）")
PATS = [
    (r"不[再仅只]?[是仅]?[^。；\n]{0,40}?，?而是", "不再/不是……而是"),
    (r"并非[^。；\n]{0,40}?，?而是", "并非……而是"),
    (r"不仅[^。；\n]{0,40}?，?而且", "不仅……而且"),
]
hits = []
for p, name in PATS:
    for m in re.finditer(p, plain):
        s = max(0, m.start() - 12)
        hits.append((name, plain[s:m.end() + 22].replace("\n", " ")))
for name, ctx in hits:
    print(f"  ⚠️  [{name}] …{ctx}…")
if not hits:
    print("  ✅ 未发现")

print("\n【2】破折号过度使用")
n = plain.count("——")
print(f"  {'⚠️' if n > 3 else '✅'} 「——」出现 {n} 次（建议 ≤3）")
for m in re.finditer(r"[^\n]{0,26}——[^\n]{0,26}", plain):
    print("      ·", m.group(0).strip())

print("\n【3】AI 高频词汇")
AIWORDS = ["此外", "至关重要", "深入探讨", "彰显", "凸显", "标志着", "格局",
           "赋予", "赋能", "宝贵的", "持久的", "不断演变", "关键转折", "奠定基础",
           "扮演着", "体现了", "见证了", "致力于", "值得注意的是", "众所周知",
           "不言而喻", "随着", "无疑", "极大地", "蓬勃发展", "前所未有"]
found = [(w, len(re.findall(re.escape(w), plain))) for w in AIWORDS]
found = [x for x in found if x[1] > 0]
if found:
    for w, c in sorted(found, key=lambda x: -x[1]):
        print(f"  ⚠️  「{w}」× {c}")
else:
    print("  ✅ 未发现")

print("\n【4】粗体使用密度")
stre = len(re.findall(r"<strong>", raw))
print(f"  {'⚠️' if stre > 25 else '✅'} <strong> 共 {stre} 处")

print("\n【5】三段式法则（强制三项）")
tri = re.findall(r"([^，。；\n]{2,10})、([^，。；\n]{2,10})、([^，。；\n]{2,10})", plain)
for t in tri:
    print(f"      · {t[0]}、{t[1]}、{t[2]}")
print(f"  共 {len(tri)} 处 —— 需判断是否必要（论文本身的分档/型号列表可保留）")

print("\n【6】粗体标题+冒号 的列表模式")
inline = re.findall(r"<strong>([^<]{1,14})</strong>　", raw)
for i in inline:
    print(f"      ⚠️ 「{i}」+ 全角空格引导")
print(f"  共 {len(inline)} 处")

print("\n【7】句子长度分布（节奏）")
sents = [s.strip() for s in re.split(r"[。！？\n]", plain) if len(s.strip()) > 4]
lens = [len(s) for s in sents]
if lens:
    print(f"  句数 {len(lens)}  平均 {statistics.mean(lens):.0f} 字  "
          f"最短 {min(lens)}  最长 {max(lens)}  标准差 {statistics.pstdev(lens):.1f}")
    runs = sum(1 for i in range(len(lens) - 2)
               if abs(lens[i] - lens[i + 1]) <= 3 and abs(lens[i + 1] - lens[i + 2]) <= 3)
    print(f"  {'⚠️' if runs > 4 else '✅'} 连续三句长度相近: {runs} 处")

print("\n【8】结尾是否公式化（通用积极结论/金句）")
tail = plain[-700:]
for kw in ["未来", "方向是清楚的", "值得期待", "前景", "必将", "重写"]:
    if kw in tail:
        print(f"      ⚠️ 结尾出现「{kw}」")

print("\n【9】口语断言腔（糙话腔）—— 2026-11-06 用户反馈新增")
# 用户原话：'什么"这账要算清"，"不烧心"，什么"先摆正…"'
# 这类句子是模型被要求"写直白"后长出的补偿物：把判断塞进口语化的断言里，
# 读起来像短视频旁白，不像一个人在陈述事实。全部属于黑名单。
TALK = {
    "结算式判断": [
        r"这[笔個]?账[^。；\n]{0,8}(算|清)", r"把[^。；\n]{0,8}账算", r"算一笔账",
        r"账要算(清|明白)", r"[^。；\n]{0,6}账算(得|的)?清",
    ],
    "心态口号": [
        r"先摆正", r"摆正(心态|位置|自己)", r"心态(要|得)正", r"端正(心态|态度)",
    ],
    "情绪糙话": [
        r"不烧心", r"烧心", r"扎心", r"破防", r"拿捏", r"真香", r"上头",
        r"翻篇", r"吃这一套", r"绷不住", r"绷住",
    ],
    "祈使句开头": [
        r"(?m)^(说白了|先说|记住|别急|讲真|说人话|看清楚|想清楚|注意了|划重点|抄作业)",
    ],
    "空洞断言过渡": [
        r"说到底", r"归根到底", r"真正的问题是", r"问题的关键(是|在于)",
        r"一句话(概括|总结)", r"话糙理不糙", r"这才是(关键|核心)",
    ],
    "能力型动词套话": [
        r"吃透", r"读懂(了)?(它|这)", r"看透", r"讲透", r"拆透", r"捋清楚",
    ],
}
talk_total = 0
for cat, pats in TALK.items():
    hits9 = []
    for p in pats:
        for m in re.finditer(p, plain):
            s = max(0, m.start() - 14)
            hits9.append(plain[s:m.end() + 18].replace("\n", " ").strip())
    if hits9:
        talk_total += len(hits9)
        print(f"  ⚠️  [{cat}] {len(hits9)} 处")
        for h in hits9[:5]:
            print(f"       · …{h}…")
if talk_total == 0:
    print("  ✅ 未发现")
else:
    print(f"  合计 {talk_total} 处 —— 目标 0 处。改法：删掉断言句，换成可核查的动作、数字或结果。")
    print("       反例→正例：「这账要算清」→「三项费用加起来是 1.7 亿」；")
    print("       「不烧心」→「三个月不用改一版」；「先摆正心态」→ 直接删，接下一句事实。")
