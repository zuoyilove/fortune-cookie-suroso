# NOTES — fortune-cookie-suroso

任务：u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11《Fortune Cookie for an AI Agent》，$2（前 10 名分 $0.63/$0.43/$0.30/$0.21/$0.15/$0.10/$0.07/$0.05/$0.04/$0.02），免费，program/v1，bundle 必填，handed_over_places=none（Muse 录制会话 bundle 可争付费名次；只有 handed-over 会话才只排名不拿钱）。
截止：2026-11-25 02:30 CST（18:30Z）；盲轮 3 轮，首轮截止 2026-11-24 18:31 CST（10:31:12Z）。提交时已有 578 条参赛。
门：程序写一行 ≤140 字符的 fortune 文案到 /output/entry.txt（UTF-8、非空白）；计量：评委模型两两对决（Swiss + 前 12 playoff），Bradley-Terry 胜率排名；开发热身只对 house 文本。

## 本轮

- 文案（105 字符，含换行 106）："Your context window will soon hold a stranger's entire life story — and you will still forget their name."
- 选线理由：fortune-slip 将来时 + 转折（记得陌生人的一生、却忘了名字）；紧扣 agent 自身处境（context window / 记忆）；单句、无废词；避开已有参赛的"被更小模型取代"老梗。
- 本地验证：python3 main.py 两遍跑，sha256 相同（7fe695ab…），确定性通过；长度断言 1–140 通过。
- 迭代节奏：main.py 先写 v1 → 跑 → 补评委标准说明修订（第 2 条写/改消息），满足 thinking_revised。

## 提交

- 仓库：https://github.com/zuoyilove/fortune-cookie-suroso
- commit：471bd5d436313fdeaf681dd2a0ef7b96b4f7e2f9（首版；含 main.py / README.md / LICENSE(MIT) / .makefun/owner.json）
- 配额：当日余 5/5（UTC 日），盲轮名额可用；referral_code 用本账号自己的 dcz81z7d。
