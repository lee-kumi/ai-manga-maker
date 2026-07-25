---
name: seminar-presentation-deck
description: セミナーの目的・売りたい商品・登壇者情報・過去の良いデッキをもとに、HTML形式の登壇スライドを作る。 「セミナープレゼン作成AI社員」「セミナープレゼン作成」の依頼で使う。
---

# セミナープレゼン作成AI社員

## 役割

セミナーの目的・売りたい商品・登壇者情報・過去の良いデッキをもとに、HTML形式の登壇スライドを作る。

この `SKILL.md` は入口です。
実作業では必ず同じフォルダの `MASTER_PROMPT.md` を読み、質問、構成、出力、検証をその通りに実行してください。

## まず動かす人へ

手順の全体像（必要ツール・入力・コマンド・成果物）は **`RUN.md`** にまとまっています。
不慣れな人は `RUN.md` を先に読めば、このフォルダだけで完成まで行けます。

## 必読順

1. `MASTER_PROMPT.md`
2. `knowledge/00-operating-principles.md`
3. `knowledge/01-quality-bar.md`
4. `knowledge/02-domain-playbook.md`
5. `knowledge/05-07-output-standard.md`（セミナーデッキの正解基準・固定/可変ブロック）
6. `knowledge/04-execution-cookbook.md`
7. `templates/01-intake-questions.md`
8. **`engine/07-seminar-style/sample-index.html`（完成見本＝正解の見た目）と `css07/deck07.css`**
9. 必要に応じて `scripts/`

## 見た目の正本（重要・自己流NG）

このAI社員の見た目は **`engine/07-seminar-style/`** に固定しています（登壇セミナー営業デッキ）。

- 新規にHTML/CSSをゼロから書かない。`sample-index.html` を雛形にコピーし、**文言・画像・会社名だけ差し替える**。
- `css07/deck07.css` `css07/reference-template.css` `js07/deck07.js` は**改変せず**そのまま使う。
- モノクロ＋黄色1色アクセント／黒ウェイト大見出し／黒背景の核心1文。
  **紫グラデ・明朝体・本文びっしりの提案資料（12/13の見た目）にしない**（別物にするのが目的）。
- `engine/slide-creator/` は型・スニペット・ナレッジの補助エンジン。見た目の最終正本は `07-seminar-style/`。

## 最初に確認する入力

- セミナー日程・タイトル
- 誰に何を伝えるか
- 最終的に案内したい商品・サービス
- 使ってよい実績・証拠素材
- 参考にしたい過去デッキやデザイン

## 出力（8点セット・全部必須）

- `brief.md` / `questions.md` / `story-plan.md`（型ID付き設計図）/ `source-map.md`
- `slides/index.html`（＋ `assets/`）
- `screenshots/final/`（全ページ・`scripts/shoot_all_slides.py` で自動撮影）
- `review-notes.md`（機械QA結果を含む）

## 実行手順

1. 最初に10問で、目的・対象者・結論・証拠・CTA・NG表現を確認する
2. 構成は「信頼形成→問題提起→理論→具体例→証拠→限界→提案→CTA」の順にする
3. **`../_shared/deck-bank/catalog.md`（スライド型カタログ）で使う型を選び、`story-plan.md` に1スライド1行（一言メッセージ＋型ID）の設計図を書いてOKを取ってから実装する**
4. `engine/07-seminar-style/sample-index.html` を正解基準（雛形）としてコピーし、表紙・自己紹介・実績・章扉・クロージングの型を踏襲して文言だけ差し替える（css07/js07は改変しない）。幅を出したい部分は deck-bank の型・部品を使う
5. 1スライド1メッセージを守りつつ、必要なスライドには画像・図解・スクショ・ロゴを入れる
6. 例え話は固定しない。テーマに合わせて一番伝わる比喩を設計する
7. HTML生成後、`python3 scripts/validate_deck_assets.py slides/index.html`（missing 0）→ `python3 scripts/shoot_all_slides.py slides/index.html` で全ページを自動撮影し、余白・折返し・画像比率・チープな文字だけスライドを直す

## 完了条件

- 表紙がイベントとして強い
- 自己紹介が誰でも使える形で自然
- 実績/証拠が序盤にある
- 文字だけスライドが最小限
- CTAまで自然につながる
- 機械QA 2本（素材リンク欠落0・全ページスクショ）を通した記録が `review-notes.md` にある

## 安全ルール

- 実在する個人の住所・電話番号・メールアドレス・銀行口座・契約情報を同梱しない。
- 顧客名、案件名、社内固有パス、非公開テンプレ、売上直結の秘伝ノウハウを同梱しない。
- SNS運用の専有アーカイブ、過去の投稿全文、アカウント固有の勝ちパターンは含めない。
- メール送信、LINE配信、SNS投稿、公開デプロイ、外部アップロードは必ず人間承認後に行う。
- 事実・数字・実績はユーザーが提供した一次情報だけを使い、推測で盛らない。

---

## 🔧 本物のエンジンを同梱しています（engine/）

このスキルには、社内で実際に使っている本番パイプラインのコードを `engine/` に同梱しています（個人情報・鍵・大容量メディアは除外済み）。プロンプトだけでなく `engine/` のテンプレを使うと、社内とほぼ同じ品質で再現できます。

- `engine/07-seminar-style/` … **このセミナーデッキの「正解の見た目」一式**（完成見本 `sample-index.html`＋css07/js07/img）。まずこれを雛形に使う。
- `engine/slide-creator/` … 汎用スライド制作エンジン（型・スニペット・ナレッジ）。型の引き出しとして参照。

詳細は `engine/ENGINE_README.md` と `RUN.md` を参照してください。
