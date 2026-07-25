# HTMLスライド出力ルール（ナレッジ）

このファイルは、HTMLスライドを生成するたびに必ず参照する **品質保証ルール集**。
`slide-creator/skills/html/` 配下にスライドを出力する際は、毎回このファイルを読む。

## 1. CSS Unicode エスケープ禁止（致命的バグ防止）

**絶対禁止**: `content: "\2713"` や `content: "\25CF"` など、CSSの `\XXXX` 形式のUnicodeエスケープ。
ブラウザ/フォントの組み合わせで `\27` のように文字化けし、スライド全体が壊れて見える。

**必ずこうする**: 実際のUTF-8文字を直接書く。

```css
/* NG — 文字化けリスク */
.checklist li::before { content: "\2713"; }
.bullet li::before { content: "\25CF"; }

/* OK — 実際の文字を直接使う */
.checklist li::before { content: "✓"; }
.bullet li::before { content: "●"; }
```

**HTMLテンプレートリテラル内も同様**: `&#9654;` のようなHTML実体参照は使ってよいが、
テンプレートリテラル内で `\u2713` のようなJS Unicodeエスケープは避け、直接文字を書く。

## 2. 絵文字禁止 — 実画像で置き換え

**絶対禁止**: スライド内に絵文字・HTML 実体参照の絵文字（`&#128640;` 🚀、`&#129302;` 🤖 等）を使うこと。
プレゼン資料としてチープに見えるため、全て **実画像** に差し替える。

**差し替え方法（優先順・鍵が無くても1〜2で完結できる）**:
1. **AI ツールロゴ** — ツール名（GitHub, Vercel, サンプルプロダクト 等）が出る文脈では `ai_tool_logos/` のロゴを使う
2. **CSS図解・プレースホルダ** — 概念・比喩は `../_shared/deck-bank/` の DGM 図解型（D01〜D30）か、CSSだけで描くカード/図形で表現する（外部画像に頼らない）
3. **（任意・要ネット）Unsplash 画像** — `https://images.unsplash.com/photo-XXXXX?w=400&q=80` を使う場合は必ず `assets/` へダウンロードしてローカル参照
4. **（任意・要APIキー/課金）画像検索・生成** — Serper API（`SERPER_API_KEY`）や gpt-image-2（`OPENAI_API_KEY`）。**キーが無ければこの手順は丸ごとスキップしてよい**（2のCSS図解で成立させる）

**CSS クラス**: `.s-icon-img` で統一サイズ（丸角 `border-radius: 16px`）、`.s-icon-img--round` で正円。

**フローステップの数字アイコン**: 絵文字の代わりに数字（1, 2, 3）を使う。ツールアイコンが必要な場合は `<img>` タグ。

**重要: アイコン画像は必ずローカル保存**:
- `<img>` タグで使う画像は **必ず `assets/` にダウンロードしてからローカルパスで参照** する
- 外部 URL（Unsplash 等）を `<img src="https://...">` で直接使うと、オフラインや CORS で表示されない
- 背景画像（`background-image: url('https://...')`）は大きなビジュアルのみ外部 URL 許可。ただし納品時はローカル推奨
- ダウンロードコマンド例: `curl -sL -o assets/icon-name.jpg "https://images.unsplash.com/photo-XXXXX?w=400&q=80"`

## 3. AI ツールロゴの活用（絵文字の代替に最適）

**ロゴライブラリ**: `slide-creator/ai_tool_logos/`（`manifest.json` にツール名・エイリアス・ファイルパス定義）

**使い方**:
1. スライド内でAIツール名（GitHub Copilot, Cursor, Claude, Vercel v0, Obsidian 等）が登場する場合、`ai_tool_logos/` から該当ロゴをデッキの `assets/` にコピー
2. `manifest.json` の `aliases` でツール名をマッチング
3. スライド内でツール紹介・比較・一覧を出すときにロゴ画像を使う
4. ロゴの加工（オーバーレイ・色変更等）は禁止。そのまま使う

**利用可能なロゴ一覧（抜粋）**:
- `claude_code/logo.png` — Claude Code
- `cursor/logo.png` — Cursor
- `github_copilot/logo.png` — GitHub Copilot
- `v0/logo.png` — v0 (Vercel)
- `obsidian/logo.png` — Obsidian
- `openclaw/logo.png` — サンプルプロダクト
- `lovable/logo.png` — Lovable
- `bolt/logo.png` — Bolt.new
- `replit/logo.png` — Replit
- その他40+ツール（manifest.json参照）

## 3. スライド出力先ルール

- **成果物は `slide-creator/skills/html/` 配下**にフォルダを作って格納
- フォルダ名: `week{NN}-{テーマ英語}` 形式（例: `week05-dev-basics`）
- multi-file構成: `index.html`, `css/style.css`, `css/body-patterns.css`, `js/slides.js`, `js/app.js`, `assets/`

## 4. 初回レンダリング品質チェック

HTMLスライド生成後、以下を **脳内チェック** してから出力完了とする:

- [ ] CSS `content:` プロパティにUnicodeエスケープがない（実文字のみ）
- [ ] `::before` / `::after` の疑似要素が正しく表示される想定か
- [ ] フォントスタックに日本語フォントが含まれている
- [ ] 全スライドに `data-notes`（トークスクリプト）がある
- [ ] テンプレートリテラル内のクォート（`'`, `"`）がエスケープ衝突しない
- [ ] `slide-content--flush` の子要素が `width: 100%; height: 100%` で親を埋める
- [ ] AGENDAの行数とセクション扉の数が一致
- [ ] Unsplash画像URLが `https://images.unsplash.com/` で始まっている
- [ ] ロゴ・写真が `assets/` にコピーされ相対パスで参照されている
- [ ] `picsum` プレースホルダが残っていない（納品時）
- [ ] プレースホルダテキスト（CATEGORY, SECTION 01 等）が残っていない
- [ ] ダークスライドの背景色が `#000` ではなく `var(--c-main)` 等テーマ色

## 5. ブランド ブランドカラー（全デッキ共通）

新規デッキは必ず以下の CSS 変数を `:root` に定義する。旧アクセント `#e94560` は使用禁止。

```css
:root {
  --c-base: #FAFAF8;
  --c-main: #1a1a2e;
  --c-accent: #9b8cff;
  --c-accent-dark: #7b6ce0;
  --c-orange: #c87941;
  --c-orange-light: #e8b88a;
  --c-sub: #b0a4f0;
  --c-border: #e0ddf0;
  --c-surface: #f4f2fb;
  --c-muted: #6c6c8a;
  --c-dark: #1a1a2e;
  --c-gradient: linear-gradient(145deg, #7b6ce0 0%, #9b8cff 24%, #c87941 49%, #e8b88a 74%, #f7f0f6 100%);
}
```

**グラデーションの用途**: アクセントバー（`.accent-line`）、セクション扉バー（`.tpl-section__bar`）、AGENDA バー、表紙下端ライン。単色アクセントは `--c-accent`（紫）、第2アクセントは `--c-orange`。

## 6. PPTX テンプレート由来のレイアウト型

以下のクラスが `css/style.css` に定義されている。新規デッキでも全て含める。

| クラス | PPTX 元パターン | 向き |
|--------|---------------|------|
| `.tpl-cover-full` | 全面ダーク表紙 | キーノート・発表会 |
| `.tpl-cover-logo` | ロゴ中央表紙 | 提案・見積もり資料 |
| `.tpl-section-center` | 中央タイトルセクション扉 | キーノート向き |
| `.tpl-contents` | 番号付き CONTENTS リスト | AGENDA の代替 |
| `.tpl-titleimg` | タイトルバー＋画像 | スクショ・デモ画面 |
| `.tpl-numhighlight` | 大きな数字＋メッセージ | KPI・成果指標 |
| `.tpl-table` | テーブル（ヘッダダーク） | 比較表・料金表 |
| `.tpl-bullside` | 箇条書き＋サイドメッセージ | 結論を右に大きく |
| `.tpl-graph` | パイチャート＋凡例 | 割合・構成比 |
| `.tpl-statement-grad` | グラデーション背景ステートメント | 強い印象のメッセージ |
| `.tpl-bridge-orange` | オレンジブリッジ | セクション切替（第2色） |

## 7. テンプレートリテラルの安全ルール

slides.js の各スライド関数はテンプレートリテラル（バッククォート）で書くため:

- `data-notes` 内のテキストにバッククォート `` ` `` を使わない
- `data-notes` 内のテキストに `${` を使わない（テンプレート展開される）
- HTMLの属性値はダブルクォート `"` 推奨。シングルクォート `'` はインラインstyleの `url('...')` のみ
- `style` 属性内のURLはシングルクォートで囲む: `style="background-image:url('https://...')"`
