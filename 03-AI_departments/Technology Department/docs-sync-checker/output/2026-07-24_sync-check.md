# docs同期チェック結果 2026-07-24

- 点検者：docs-sync-checker
- 点検対象：Cover Compass新版の大型更新（旧main `73a316c` → 新main `bcd59a2`）
- 正本：GitHub main版＝公開サイト＝この作業環境（一致確認済み）

## ① 今回変わったファイル一覧（9件）
- .claude/skills/cover-concept/SKILL.md
- .claude/skills/cover-design/SKILL.md
- Agent.md
- CLAUDE.md
- cover-maker.html
- docs/cover-maker-rules.md
- docs/kindle-cover-design-rules.md
- docs/manga-maker-rules.md
- index.html

## ② ペアごとの判定（全5ペア）
| # | ペア | 判定 |
|---|---|---|
| 1 | cover-maker.html ⇄ docs/cover-maker-rules.md | ✅ OK（両方更新） |
| 2 | v2.html ⇄ docs/manga-maker-rules.md | ⚠️ 要確認 → 調査の結果 実質OK（下記） |
| 3 | docs/kindle-cover-design-rules.md ⇄ cover-maker.html / cover-design SKILL / Agent.md | ✅ OK（すべて同時更新） |
| 4 | ツール/スキル/docs追加 ⇄ CLAUDE.md ファイル一覧 | ✅ OK（Agent.md・kindle-cover-design-rules.md・cover-designスキルを一覧に記載済み） |
| 5 | 「作りの約束事」方針変更 ⇄ CLAUDE.md | ✅ OK（今回、約束事の方針変更なし） |

## ③ 要確認の詳細（ペア#2）
- **機械的な検知**：`docs/manga-maker-rules.md` は更新されたが、`v2.html` は今回の更新範囲では未変更。
  → ルール上は「片方だけ変わった」ズレ疑い。
- **調査結果 → 実質OK**：
  - `v2.html` には該当ルールが既に存在（縦書き3件・キャラクターシート/四面図6件・オノマトペ5件をコード内に確認）。
  - `v2.html` の最終更新は 2026-07-12（`dd65f23`）で、これらルールはそれ以前から実装済み。
  - つまり今回の doc 更新は、**先に入っていたコードの内容に docs を追いつかせた**もの。内容の食い違いはなし。
- **おまけの発見（軽微）**：
  - `docs/manga-maker-rules.md` 冒頭の「抽出元：`v2.html`（**2026-07-14時点**）」に対し、`v2.html` の実際の最終更新は **2026-07-12**。
  - 内容ではなく**日付ラベルのズレ**。実害は小さいが、正確にするなら 07-12 に直すとよい。

## ④ 次にやること
- 内容の同期ズレは**なし**。緊急対応は不要。
- 気になるなら `docs/manga-maker-rules.md` の抽出元日付を `2026-07-12` に修正（人間の判断。修正はこの社員では行わない）。

---
合格条件チェック：全5ペア判定済み ✅ ／ 要確認に具体ファイル名あり ✅ ／ 成果物を output に保存 ✅
