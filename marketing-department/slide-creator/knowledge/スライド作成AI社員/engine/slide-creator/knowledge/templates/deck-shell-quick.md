---
name: html-deck-shell
description: HTMLスライドを作るとき、表紙・AGENDA・目次の各ブロック直前のセクション扉を毎回同じ型で置く（ブランド / CMO 既定）。
---

# HTML デッキの骨格（毎回これ）

新規の **HTML スライド Web**（`index.html` + `css/style.css` + `js/slides.js` + `js/app.js`）では、ユーザーが別デザインを指定しない限り、次の **3種を必ず**使う。

| 順番 | 役割 | 参照 |
|------|------|------|
| 1枚目 | **表紙**（左コピー + 右ビジュアル） | `references/html-slide-cover-agenda-templates.md` §1 |
| 2枚目 | **AGENDA**（左ダーク + 右に番号付き目次） | 同ファイル §2 |
| AGENDA の **各項目の直前** | **セクション扉**（巨大番号 01… + バー + タイトル + 一行説明） | 同ファイル §3 |

## セクション扉のルール

- 目次を **N 行**にしたら、セクション扉も **原則 N 枚**（`01`〜`0N`）。本文スライドの**最初の前**に置く。
- 番号は目次と**一致**させる（AGENDA の 01 とセクション扉の `01` が同じブロックを指す）。
- 実装は **CSS クラス**（`.html-tpl-section-root` 等）推奨。インライン版は `html-slide-cover-agenda-templates.md` に記載。

## 実装チェック

- [ ] `slideFactories` の先頭が表紙 → AGENDA
- [ ] 各目次ブロックの直前にセクション扉がある
- [ ] `css/style.css` に表紙・AGENDA・セクション扉のクラスがある（またはインラインで完全再現）

詳細・コピペ用 HTML は **`references/html-slide-cover-agenda-templates.md`** のみを正とする。
