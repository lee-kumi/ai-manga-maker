# presentation-mode 共通アセット

このフォルダの中身は **全プレゼンで再利用できる共有資産**。新規デッキを作る時は `output/archive/<slug>/assets/` に必要なものをコピーして使う（出力先からは相対パス参照）。

## 構成

```
knowledge/assets/
├── x-profiles/   ← ブランド系8アカウントのX プロフィール画像(jpg)
├── people/       ← 主要人物の登壇用写真(講師・パートナー・他ゲスト)
├── style-refs/   ← レイアウト参考画像(講師から渡された参考スライド)
└── README.md     ← これ
```

## x-profiles/(8アカウント・実績スライドで使う)

自社サイトの公開アセット（`assets/x-profiles/`）のミラーを置く想定。ファイル名・表示名・数値はすべて自社の実値に差し替えて使う。

| ファイル | アカウント | 表示名 | フォロワー |
|---|---|---|---:|
| `acct1.jpg` | @your_main | サンプルスタジオ | （フォロワー数） |
| `acct2.jpg`   | @your_acct2   | サンプルコミュニティ             | （フォロワー数） |
| `acct3.jpg`  | @your_sub  | あなた＠サンプルプロダクトガチ勢 | （フォロワー数） |
| `acct4.jpg`  | @your_acct5  | サンプルスタジオ2       | （フォロワー数） |
| `acct5.jpg`     | @your_acct3     | メンバーA             | （フォロワー数） |
| `acct6.jpg` | @your_acct2b | サンプルノート    | （フォロワー数） |
| `acct7.jpg`  | @your_acct6  | サンプル研究所 | （フォロワー数） |
| `acct8.jpg`     | @your_acct4     | サンプルビジネス        | （フォロワー数） |

**合計: （フォロワー数）**。最新値は自社で管理する `x-followers.json` 等を参照する想定。

セミナーで「自分のチームのアカウントを紹介する」「合計フォロワー数で実績を見せる」時は、ここから直接コピーで OK。実装例はサンプルデッキの Slide 04a-04c (実績バーン → 8アカグリッド → メトリクス)。

## people/

セミナーで使う**正式な登壇者写真**を蓄積する。プロフィール画像（小・丸トリミング用）ではなく、スピーカーカード（160px×160px相当）で使える正面・スーツ・笑顔系。

| ファイル | 用途 |
|---|---|
| `speaker.png`  | 講師（@your_sub、株式会社アイウエオ 代表）正式登壇写真 |
| `guest.png` | パートナー氏（@guest_speaker）正式登壇写真 |

新しいゲストが出るたびに、このフォルダに追加していく。命名は `<handle>.png` 推奨。

## style-refs/(9種類)

講師が「このスタイルを表現の幅としてスキルに入れて」と渡してくれた参考画像。

| ref | スタイル | CSS クラス |
|---|---|---|
| `ref_02.png` | 全画面写真背景 + 中央ヌキ文字 | `.tpl-photo-bg` |
| `ref_03.png` | 写真背景 + 番号 + 大見出し + サブ説明 | `.tpl-photo-num` |
| `ref_04.png` | 写真背景 + 左下ラベル風タイトル | `.tpl-photo-label` |
| `ref_05.png` | 上小タイトル + 下バーン大見出し + サブ | `.tpl-eyebrow-big` |
| `ref_06.png` | テーブル（ヘッダ + 強調列） | `.tpl-table` |
| `ref_07.png` | 縦バー横並び5段ステップ（強調1個） | `.tpl-flow-vbars` |
| `ref_08.png` | 左テキスト + 右イラスト（unDraw 風） | `.tpl-illust-side` |
| `ref_09.png` | カラー扉 + イラスト + 透かしテキスト | `.tpl-color-tobira` |
| `ref_10.png` | 中央バーンの1メッセージ | `.tpl-bigword` |

CSS 実装はサンプルデッキの `css/style.css` 末尾のパターンパック §U〜§AC が**最新の実装サンプル**。新デッキで使う時はそこからコピペできる。

加えて **§AD〜§AF** を追加：
| クラス | 用途 |
|---|---|
| `.tpl-xgrid`     | Xアカウント8枚グリッド + フォロワー数 + 合計 |
| `.tpl-stack`     | 自動化スタック(AIロゴ + MCP + 内製機能タグ) |
| `.tpl-stat-bang` | 大数字バーン（（フォロワー数）など、1メトリック1枚） |

## 外部の共通アセット(参照だけ・コピーで使う)

このスキル配下の `knowledge/assets/` には**置いていない**が、ロゴ・ブランド画像は他フォルダで管理されている。新規デッキ作成時は必要分を **`<出力先>/assets/`** にコピーして使う。

### AI ツールロゴ(40+本)

**正本パス**: `slide-creator/knowledge/assets/ai-tool-logos/<tool>/logo.png`

| カテゴリ | 含まれるツール（一部） |
|---|---|
| **Claude 系** | claude / claude_code / anthropic |
| **OpenAI 系** | chatgpt / gpt_5 / gpt_55 / codex / openai / sora |
| **Google 系** | gemini / gemini_cli / nano_banana / notebooklm / firebase |
| **エディタ・コーディング** | cursor / windsurf / replit / lovable / bolt / github_copilot / devin / v0 |
| **画像・動画** | midjourney / runway / kling / veo |
| **AIエージェント基盤** | mcp / hermes_agent / openclaw / manus |
| **ノート・ナレッジ** | obsidian / notion |
| **検索・API** | perplexity / grok / deepseek / qwen / mistral / elevenlabs |
| **デザイン・コラボ** | canva / figma / supabase |

カタログは `slide-creator/knowledge/assets/ai-tool-logos/manifest.json`（aliasマッチング・fallback 定義込み）。

### ブランドブランド

**正本パス**: `slide-creator/knowledge/assets/brand/`

| ファイル | 用途 |
|---|---|
| `brand-logo.png` | ブランド ロゴ（表紙中央・クロージング・HUD） |
| `speaker-photo.png`| 講師 旧プロフィール写真（高解像度版・必要時のみ。**最新は `people/speaker.png` を使う**） |

## 使い方（新デッキ作成時）

1. 出力先 `output/archive/<slug>/assets/` を作成
2. このフォルダから必要分（people/, x-profiles/, style-refs/）を `cp`
3. AI ツールロゴが必要なら `slide-creator/knowledge/assets/ai-tool-logos/<tool>/logo.png` を `<出力先>/assets/logos/<tool>.png` にコピー
4. ブランドブランド画像が必要なら `slide-creator/knowledge/assets/brand/` から `<出力先>/assets/brand/` にコピー
5. 写真背景が必要なら **Unsplash 直リンク**（`rgba(26,26,46,.62-.75)` のオーバーレイ必須）か **gpt-image-2** で生成して `<出力先>/assets/` にローカル保存
6. スタイル参考は `style-refs/` を見て、CSS パターンパックから流用

## 画像生成（gpt-image-2 使用時）

- 抽象アクセント・背景・図解は `image-generator` skill 経由で生成
- 出力は必ず `<出力先>/assets/` にローカル保存（CORS/オフライン対応のため）
- 16:9 比率指定: `1920x1080` または `1536x864`(主要)
- AI ツールロゴと併用する時は `slide-creator/knowledge/assets/ai-tool-logos/<tool>/logo.png` を **生成参照画像** に渡す
