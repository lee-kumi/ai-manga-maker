# HTMLスライド作成スキル（CMO × Webスライド）

このファイルは、Marp 形式と完全に分けた **HTML スライド専用の正本**。

## 位置づけ

CMO 観点で、提案・ウェビナー・セミナー・ローンチ・採用広報向けの HTML/CSS/JS スライド Web サイトを設計・制作する。

**Marp ではない。** `.marp.md`、Marp フロントマター、Marp ディレクティブ、Marp 公式背景テンプレート、Marp 用ロゴ相対パスは扱わない。

## 用途別の入口

| 作りたいもの | 読むファイル |
|---|---|
| HTML/CSS/JS スライド全般の実装基盤 | `02-slide-builder-main/SKILL.md` |
| 登壇・プレゼン・ウェビナー・セミナー | `03-presentation-mode/SKILL.md` |
| 会社説明資料・正式な法人資料・コーポレート資料 | `01-formal-corporate-deck/SKILL.md` |
| YouTube動画用スライドに入れる図解画像プロンプト | `04-youtube-slide-image-prompt/SKILL.md` |
| ブランドサイトと同じ世界観の公開Webデッキ・読み物資料 | ※この社員のパックには非同梱（`05-brand-web-deck` は同梱対象外） |
| PDF・既存スライドを強く模倣したHTMLデッキ | ※この社員のパックには非同梱（`06-pdf-style-clone-html-deck` は同梱対象外） |
| 長尺セミナー動画からスライドを抽出して販売デッキ化 | ※この社員のパックには非同梱（`07-seminar-video-style-clone-deck` は同梱対象外） |
| HTML図解・フォルダ構成図・スキル図 | パック内の図解担当 `../../../../28-diagram-maker/SKILL.md`（HTMLモード） |
| 画像図解 | パック内の図解担当 `../../../../28-diagram-maker/SKILL.md`（画像モード） |

## 01 と 05 の使い分け

| 観点 | 01-formal-corporate-deck | 05-brand-web-deck |
|---|---|---|
| 主な用途 | 会社説明、正式な法人資料、営業・コンサル提案 | ブランドサイト流のWebデッキ、公開資料、読み物型資料 |
| 読者 | 1人から数人の意思決定者 | Web上で読む見込み客、受講者、社内外の広い読者 |
| 優先するもの | 信頼感、情報密度、根拠、ブランド一貫性 | サイト世界観、画像活用、公開しやすさ、読みやすさ |
| デザイン | 余白大きめ、落ち着いた法人資料、グレイン調も可 | example.com の見た目、16:9 HTML、公開デッキ運用 |
| 判断 | 残す | 残す |

迷ったら、相手が「特定企業の意思決定者」なら01、公開URLで読ませるブランドブランド資料なら05を使う。

## ブランドアセット

共通素材は `../knowledge/assets/brand/` に置く。新規デッキは **必ず** 出力先の `assets/` フォルダにコピーして使う。

| ファイル | 用途 |
|---|---|
| `../knowledge/assets/brand/brand-logo.png` | ブランド ロゴ。表紙・クロージングに使用 |
| `../knowledge/assets/brand/speaker-photo.png` | 代表 講師の登壇写真。代表紹介スライドに使用 |

**デッキ作成時のアセット手順**:
1. `<出力先>/assets/` フォルダを作成
2. `../knowledge/assets/brand/` からロゴ・写真をコピー
3. **ブランド公開サイト素材**（`<自社サイト>/assets/img/`）から、デッキ内容に合う画像を選んで `assets/` にコピー（用途別の対応表は `../knowledge/references/html-slide-body-patterns-catalog.md` を参照）
4. HTML 内では `assets/brand-logo.png`、`assets/speaker-photo.png` 等で参照
5. クライアント固有の画像もすべて `assets/` に配置
6. `picsum` プレースホルダはドラフト段階のみ。ブランド 実素材があるものは実素材を優先

## 会社情報ソース（提案デッキ共通）

ブランド の提案資料を作るときは、以下のフォルダから会社情報・実績データ・画像を取得する。

| パス（`<自社サイト>/` 配下） | 内容 |
|---|---|
| `brand-assets/company-profile.md` | 会社概要・代表経歴・設立情報 |
| `assets/img/` | ブランド公開サイトの画像素材 |
| `assets/ai_tool_logos/` | AIツールロゴ |
| `assets/x-profiles/` | Xアカウントのプロフィール画像 |
| `decks/style.css` | 公開デッキ共通CSS |
| `decks/deck.js` | 公開デッキ共通JS |

**提案デッキでの活用パターン**:
- **表紙**: ロゴのみ中央配置（`cover-logo-only` レイアウト）
- **代表紹介**: §4 画像左（`speaker-ceo.jpg`）+ 右テキスト（経歴・実績リスト）
- **X運用実績**: 8 アカウントのプロフィール画像 + フォロワー数をグリッド表示（`x-accounts-grid`）
- **数字実績**: 売上・フォロワー総数・投稿自動生成数・コミュニティ規模を `results-grid` で表示
- **クロージング**: ロゴ白反転（`closing-logo`）+ メッセージ

## 必読

| パス | いつ読むか |
|---|---|
| `../knowledge/templates/deck-shell.md` | 毎回。表紙、AGENDA、章扉、本文の組み立て順 |
| `../knowledge/references/html-slide-cover-agenda-templates.md` | 毎回。表紙・AGENDA・セクション扉のレイアウト |
| `../knowledge/references/html-slide-plain-japanese.md` | 毎回。日本語を平易にする |
| `../knowledge/references/html-slide-body-patterns-catalog.md` | 本文のレイアウト型、図解型、ブランドカラー |
| `../knowledge/references/html-cmo-marketing-story.md` | CMO の訴求設計、ストーリー、CTA、証拠設計 |
| `../knowledge/references/html-slide-unsplash-guide.md` | 写真を使う場合の取得・配置ルール |
| `02-slide-builder-main/SKILL.md` | HTML/CSS/JS の実装まで進む時 |
| `02-slide-builder-main/knowledge/references/slide-copy-fitting.md` | 日本語コピーをHTMLスライドへ入れる前 |
| `02-slide-builder-main/knowledge/references/slide-layout-catalog.html` | HTMLレイアウトを選ぶ時 |
| `02-slide-builder-main/knowledge/references/slide-diagram-catalog.html` | 図解・グラフをHTML化する時 |
| `03-presentation-mode/SKILL.md` | 登壇・プレゼン用に特化する時 |
| `01-formal-corporate-deck/SKILL.md` | 会社説明資料・営業提案書・コンサル提案を作る時 |
| `04-youtube-slide-image-prompt/SKILL.md` | YouTube動画用スライドの図解画像プロンプトを作る時 |
| `05-brand-web-deck/SKILL.md` | ブランドサイト流の公開Webデッキを作る時 |
| `06-pdf-style-clone-html-deck/SKILL.md` | 参考PDF/既存スライドをHTMLへ移植する時 |
| `07-seminar-video-style-clone-deck/SKILL.md` | セミナー動画から販売用HTMLデッキへ移植する時 |

## インテーク

不足していれば、1メッセージでまとめて確認する。未定は `おまかせ` でよい。

```text
HTMLスライドのCMOブリーフを確認します。

1. 使う場面: 提案 / ウェビナー / セミナー / ローンチ / 採用広報 / 社内共有 / おまかせ
2. テーマ:
3. 対象者:
4. 目的:
5. 見終わった後に取ってほしい行動:
6. 信じてもらうための材料: 実績 / 数字 / 事例 / デモ / 比較 / 受講者の声 / おまかせ
7. 素材: 原稿あり / 箇条書きあり / URL・資料あり / おまかせ
8. ページ数・時間:
9. 出力: 構成案だけ / HTML実装まで / おまかせ
10. 保存場所:
```

## 実行手順

1. ブリーフを読み、`../knowledge/references/html-cmo-marketing-story.md` の Strategy Gate を埋める
2. 目的別ストーリー型を選ぶ
3. セクションごとに「主張」「証拠」「ビジュアル」「CTA」を決める
4. 構成承認ドラフトを出す。ユーザー承認前に HTML/CSS/JS を書かない
5. 承認後、HTML 実装まで求められていれば `02-slide-builder-main/SKILL.md` を技術標準として読む
6. HTML スライドは `slides/index.html`, `css/style.css`, `js/app.js`, `js/slides.js` の multi-file を既定にする
7. 生成後、slide-builder の validator と `../knowledge/references/html-cmo-marketing-story.md` の Quality Checklist を通す

## 構成承認ドラフト形式

```text
CMO HTMLスライド構成案 v1
用途:
対象者:
狙う行動:
核となる約束:
信じてもらう材料:
全XX枚

1. 表紙
メッセージ:
役割: 興味喚起 / 期待値設定
証拠:
ビジュアル:
HTMLレイアウト候補:

2. 問題提起
メッセージ:
役割: 共感 / 放置コスト
証拠:
ビジュアル:
HTMLレイアウト候補:
```

## ブランド ブランドカラー（全デッキ共通）

| 変数 | 値 | 用途 |
|------|-----|------|
| `--c-dark` | `#1a1a2e` | 見出し・ダーク背景 |
| `--c-accent` | `#9b8cff` | 番号・キッカー・ブリッジ |
| `--c-accent-dark` | `#7b6ce0` | グラデーション起点 |
| `--c-orange` | `#c87941` | 第2アクセント・ワークバッジ |
| `--c-orange-light` | `#e8b88a` | グラデーション中間 |
| `--c-surface` | `#f4f2fb` | 表紙・タイル背景 |
| `--c-gradient` | `linear-gradient(145deg, #7b6ce0 0%, #9b8cff 24%, #c87941 49%, #e8b88a 74%, #f7f0f6 100%)` | アクセントバー・装飾 |

グラデーションは ブランド 公開サイトの世界観に合わせる。アクセントバー・セクション扉バー・表紙下端ラインなどに使う。

## HTML 実装時の原則

- **デッキのシェル** — 手順・チェックは `../knowledge/templates/deck-shell.md` を読む。
- **表紙・目次の既定** — **1枚目は表紙**（左テキスト / 右ビジュアル `tpl-cover`、全面ダーク `tpl-cover-full`、ロゴ中央 `tpl-cover-logo` の 3 パターンから選択）、**2枚目は AGENDA**（左ダーク `AGENDA` / 右に番号付き目次）。構造・配色は `../knowledge/references/html-slide-cover-agenda-templates.md` に従う。別デザインをユーザーが明示したときだけ例外。
- **セクション扉** — **目次に載せた各ブロック（01〜0N）の本文に入る直前**に、同ファイルの「セクション扉」テンプレを**必ず1枚**入れる（番号は目次と一致）。別運用をユーザーが明示したときだけ例外。
- **通常本文（ビジュアルあり）** — 事例・製品・人物など、左画像・右テキストが合うときは `../knowledge/references/html-slide-cover-agenda-templates.md` の **§4（画像左 50%）** を既定。画像は ブランド アセット優先、雰囲気写真は **Unsplash**（`../knowledge/references/html-slide-unsplash-guide.md`）を活用。`picsum` はドラフトのみ。
- **プレゼンモード** — 登壇・ウェビナー・LT 用途の場合は `03-presentation-mode/SKILL.md` を読む。1スライド60文字以内・ビジュアル60%以上・全スライドにトークスクリプトを付ける
- **日本語** — 堅い・不自然な表現は避け、`../knowledge/references/html-slide-plain-japanese.md` に沿って **誰にでも通じる語**に直す（略語・英語ラベルだらけにしない）。
- **本文レイアウトのバリエーション** — フロー・カード・Before/After・2択・5理由・引用・大見出しなどは `../knowledge/references/html-slide-body-patterns-catalog.md` と各デッキの **`css/body-patterns.css`**。新パターンを足したら **カタログと CSS を同じコミットで更新**する。
- **絵文字禁止** — スライド内に絵文字・HTML 実体参照の絵文字を使わない。代わりに **AI ツールロゴ**（`ai_tool_logos/`）、**Unsplash 画像**、**Serper API 画像検索**、**gpt-image-2 生成画像** を使う。フローステップの数字は `1, 2, 3` のテキスト。詳細は `../knowledge/references/slide-output-rules.md` を読む。
- 1スライド1メッセージ。見出しはカテゴリ名ではなく主張文にする
- CTA は最後だけに閉じ込めない。必要なら中盤で「今日やること」、終盤で「次にやること」を分ける
- 図解化できる箇条書きは、フロー、マトリクス、Before/After、タイムライン、ファネルに置き換える
- ローカルファイル名、リポジトリパス、参照ドキュメント一覧をスライド本文に出さない
- 難語や略語はその場で意味が取れる日本語へ直す。RACI / MVP / PdM / スコープ等は略語だけで置かない
- HTML 実装の細部は `02-slide-builder-main/` を参照するが、CMO 訴求の判断はこのファイルを優先する

## 出力先

- ユーザー指定があれば指定先を優先
- 未指定なら、使用したスキルの `output/` フォルダに保存する（例: `01-formal-corporate-deck/output/`、`05-brand-web-deck/output/`）
- スキルに紐づかない汎用スライドは `slide-creator/output/` に保存する

## 品質基準

- [ ] **1枚目が表紙テンプレ・2枚目が AGENDA テンプレ**（`../knowledge/references/html-slide-cover-agenda-templates.md`）になっている
- [ ] **目次の各ブロック直前にセクション扉**があり、番号が目次と一致している（`../knowledge/templates/deck-shell.md`）
- [ ] 図版＋主張の本文は **§4 画像左・テキスト右** を検討済み（合わない枚だけ箇条書き型でよい）
- [ ] Marp Markdown として作っていない
- [ ] Marp 用テンプレート・ディレクティブ・ロゴ相対パスを混ぜていない
- [ ] Audience / Desired Action / Core Promise / Proof が構成に反映されている
- [ ] 各セクションに主張、証拠、ビジュアル方針、CTA のいずれかがある
- [ ] テキスト主体スライドが続く箇所を図解・数字・対比へ変換した
- [ ] HTML 実装時は slide-builder の validator または同等チェックを実行した
- [ ] コピーが `../knowledge/references/html-slide-plain-japanese.md` の方針に沿っている（平易な日本語）
- [ ] 追加した本文パターンは `../knowledge/references/html-slide-body-patterns-catalog.md` / `body-patterns.css` に反映済み

## 退避済み旧スキル

- `99-trash/2026-06-09_slide-creator-skill-retirement/moved/<部門>/Marketing Department/slide-creator/skills/04-cmo-marketing/SKILL.md`: 旧CMO観点。新規作業の入口にはしない。
- `99-trash/2026-06-09_slide-creator-skill-retirement/moved/<部門>/Marketing Department/slide-creator/skills/07-slide-creation/SKILL.md`: 旧Marp継承。新規作業の入口にはしない。

## 現役スキルの番号

- `01-formal-corporate-deck/SKILL.md`: 正式法人資料
- `02-slide-builder-main/SKILL.md`: HTML実装基盤
- `03-presentation-mode/SKILL.md`: 登壇・プレゼン
- `04-youtube-slide-image-prompt/SKILL.md`: YouTube用スライド画像プロンプト
- `05-brand-web-deck/SKILL.md`: ブランド公開Webデッキ
- `06-pdf-style-clone-html-deck/SKILL.md`: PDF/既存スライドクローン
- `07-seminar-video-style-clone-deck/SKILL.md`: セミナー動画クローン
