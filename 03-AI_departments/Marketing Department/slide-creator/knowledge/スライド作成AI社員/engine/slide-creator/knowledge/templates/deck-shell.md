---
name: html-deck-shell
description: HTMLスライドの表紙・AGENDA・セクション扉・本文（画像左+テキスト右・フロー・カード等）の既定シェル。新規デッキは毎回この順で組み立てる。
---

# HTML デッキのシェル（毎回これ）

**親スキル**: 同階層の `../SKILL.md`（HTML スライド正本）

## 必ず読む（コピペの元）

| ファイル | 内容 |
|----------|------|
| `../references/html-slide-cover-agenda-templates.md` | **表紙・AGENDA・セクション扉・本文（画像左+テキスト右）** の HTML/CSS 仕様とインライン例 |
| `../references/html-slide-plain-japanese.md` | **日本語を平易に**（読みやすさ優先） |
| `../references/html-slide-body-patterns-catalog.md` | **本文パターン**（§A〜§T 基本20型 + §U〜§Z PPTX由来6型 = 全26パターン）+ ブランド アセット一覧 + ブランドカラー早見表 |
| `../references/html-slide-unsplash-guide.md` | **Unsplash 画像の取得・配置ルール**（表紙・ブリッジ・背景写真・ブランド アセットとの使い分け） |

## アセット準備（毎回最初にやる）

1. `<出力先>/assets/` を作成
2. `../brand-assets/brand-logo.png` → `assets/brand-logo.png` にコピー
3. `../brand-assets/speaker-photo.png` → `assets/speaker-photo.png` にコピー
4. **ブランド新サイト素材**（`assets/img/`）から、デッキ内容に合う画像を `assets/` にコピー（用途別の対応表は `../references/html-slide-body-patterns-catalog.md` 末尾の「ブランド新サイトアセット一覧」を参照）
5. 表紙の右ビジュアルで代表写真を使う場合 → `background-image: url('assets/speaker-photo.png')` または `assets/ceo-stage.png`
6. ロゴは表紙の左上 or クロージングスライド（§T CTA）に配置

## スライド順（既定）

1. **表紙** — 3パターンから選ぶ:
   - **左右分割型**（`.tpl-cover`）: 左テキスト + 右ビジュアル。セミナー・ウェビナー・ワークショップ向き
   - **全面ダーク型**（`.tpl-cover-full`）: 大タイトル中央 + 下端グラデーションライン。キーノート・発表会向き
   - **ロゴ中央型**（`.tpl-cover-logo`）: ロゴ・サブタイトル・宛先・日付を中央配置。提案資料におすすめ
2. **AGENDA** — 左ダーク + 右に `01`〜`0N` の目次（**N はデッキで可変**）
3. 以降、**目次の 01 の本文に入る直前**に **セクション扉**（巨大淡番号 + バー + タイトル + 一行説明）
4. そのセクションの**本文スライド群** — 図版＋主張が合う枚は **§4 画像左・テキスト右**。フロー・対比・カードなどは **`html-slide-body-patterns-catalog.md` + `body-patterns.css`** から選ぶ。箇条書きのみの枚は `.slide-content` + 既存タイポでも可。
5. **目次の 02 の本文に入る直前**にまた **セクション扉**（番号 `02`）
6. … **目次と同じ数だけセクション扉を繰り返す**

**禁止**: 目次に載せたブロックに、扉なしでいきなり箇条書き本文から入る（ユーザーが「扉なし」で明示したときだけ例外）。

## 実装メモ

- `js/slides.js` では `slideFactories` の先頭を **表紙 → AGENDA** に固定し、セクション扉は **`slide-content--flush` + `.html-tpl-section-root`**（各デッキの `css/style.css` にクラス定義）。
- セクション扉の **番号** は AGENDA の `01`…と **一致**させる。
- 説明文（英語サブタイトル）は任意。日本語のみでもよい。

## 品質チェック

- [ ] 1枚目が表紙テンプレ、2枚目が AGENDA テンプレ
- [ ] 目次の各セクション直前にセクション扉がある（目次の行数と一致）
- [ ] セクション扉の番号が目次と一致している
- [ ] 図版付き本文は **§4 画像左・テキスト右** を使うか判断済み（ラベルは日本語に）
- [ ] 日本語は `html-slide-plain-japanese.md` の方針に沿っている
- [ ] 新しいパターンを足したら **カタログ + `body-patterns.css`** を更新した
