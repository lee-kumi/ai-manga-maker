# engine/ — 社内と同じ「本物のパイプライン」

このフォルダには、登壇セミナーデッキの本物の素材を、社内で実際に動いているコードのまま同梱しています。
プロンプトだけでなくテンプレ/CSS/完成見本が入っているので、社内とほぼ同じ品質で再現できます。

## 2つのエンジン（役割が違う）

- **`07-seminar-style/`（このセミナーデッキの正解の見た目・まずこれを使う）**
  - `sample-index.html` … 完成見本（26枚・架空会社「株式会社アイウエオ」）。**この見た目を正解にする**。
  - `css07/deck07.css` `css07/reference-template.css` … 07セミナーの視覚DNA（モノクロ＋黄色1色／黒ウェイト大見出し／semantic-layer 1920×1080スケール）。**改変せず使う**。
  - `js07/deck07.js` … スライド送り＋拡大縮小（ハッシュ `#1` `#2` … でページ指定）。
  - `img/` … 表紙・証拠スクショ・AIツールロゴ（見本用。自社素材に差し替える）。
  - 使い方: `sample-index.html` を `slides/index.html` にコピー → 文言・画像・会社名だけ差し替え。新規HTMLを自己流で書かない。

- **`slide-creator/`（汎用スライド制作エンジン・型の引き出し）**
  - 03-presentation-mode のスニペット/deck-shell/body-patterns/slide-builder。レイアウト型を選ぶときの参照用。
  - ⚠️ `slide-creator/` 配下のナレッジには社内の内部パス（`<社内ナレッジ>/...` 等）への言及が残っています。**それらの内部素材は配布ZIPには含まれません**。見た目の正本は上の `07-seminar-style/` を使ってください。

## 配布安全のために加工した点
- 実在する個人名・協業者名は一般名（講師 / ゲストA など）に置換しています。
- 絶対パスは `<WORKSPACE>` / `<HOME>/`、メール/電話はダミーに置換しています。
- 鍵・トークン・送信用認証・実データ CSV・大容量メディア・node_modules は同梱していません。
- メール送信 / LINE 配信 / 公開デプロイなど外部に出る操作は、必ず人間の承認後に実行してください。

## 使い方の基本
1. このフォルダを自分の環境にコピーする。
2. `SKILL.md` / `MASTER.prompt.md`（あれば）と各 `scripts/` の冒頭 docstring を読む。
3. 依存（ffmpeg / Remotion の npm install / Python パッケージ等）は各スクリプトの説明に従って入れる。
4. 自分の素材（動画・原稿・画像）を入力に渡して実行する。

## 中身
└── slide-creator/
    ├── _RULE.md
    ├── knowledge/
    │   ├── README.md
    │   ├── assets/
    │   │   ├── ai-tool-logos/
    │   │   │   ├── AI_TOOL_LOGO_LIBRARY_PROPOSAL.md
    │   │   │   ├── anthropic/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── bolt/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── canva/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── chatgpt/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── claude/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── claude_code/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── claude_code_clean/
    │   │   │   │   └── logo.png
    │   │   │   ├── codex/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── cursor/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── deepseek/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── devin/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── elevenlabs/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── figma/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── firebase/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── gemini/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── gemini_cli/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── github_copilot/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── gpt_5/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── gpt_55/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── grok/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── hermes_agent/
    │   │   │   │   ├── logo.png
    │   │   │   │   ├── logo_original_backup 2.png
    │   │   │   │   ├── logo_original_backup 3.png
    │   │   │   │   └── source.txt
    │   │   │   ├── kling/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── lovable/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── manifest.json
    │   │   │   ├── manus/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── mcp/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── midjourney/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── mistral/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── nano_banana/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── notebooklm/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── notion/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── obsidian/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── openai/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── openclaw/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── perplexity/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── qwen/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── replit/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── runway/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── sora/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── supabase/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── v0/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   ├── veo/
    │   │   │   │   ├── logo.png
    │   │   │   │   └── source.txt
    │   │   │   └── windsurf/
    │   │   │       ├── logo.png
    │   │   │       └── source.txt
    │   │   └── brand/
    │   │       ├── README.md
    │   │       └── brand-logo.png
    │   ├── references/
    │   │   ├── html-cmo-marketing-story.md
    │   │   ├── html-slide-body-patterns-catalog.md
    │   │   ├── html-slide-cover-agenda-templates.md
    │   │   ├── html-slide-plain-japanese.md
    │   │   ├── html-slide-unsplash-guide.md
    │   │   └── slide-output-rules.md
    │   └── templates/
    │       ├── deck-shell-quick.md
    │       └── deck-shell.md
    └── skills/
        ├── 01-formal-corporate-deck/
        │   └── SKILL.md
        ├── 02-slide-builder-main/
        │   ├── .gitignore
        │   ├── README.md
        │   ├── SKILL.md
        │   ├── knowledge/
        │   │   ├── references/
        │   │   │   ├── design-styles/
        │   │   │   │   ├── cute.css
        │   │   │   │   ├── dynamic.css
        │   │   │   │   ├── fresh.css
        │   │   │   │   ├── friendly.css
        │   │   │   │   ├── futuristic.css
        │   │   │   │   ├── luxury.css
        │   │   │   │   ├── minimal.css
        │   │   │   │   ├── pop.css
        │   │   │   │   ├── stylish.css
        │   │   │   │   └── trust.css
        │   │   │   ├── slide-copy-fitting.md
        │   │   │   ├── slide-design-principles.md
        │   │   │   ├── slide-diagram-catalog.html
        │   │   │   ├── slide-layout-catalog.html
        │   │   │   ├── slide-taste-catalog.html
        │   │   │   └── slide-web-standards.md
        │   │   └── scripts/
        │   │       └── validate-slide-deck.mjs
        │   └── package.json
        ├── 03-presentation-mode/
        │   ├── SKILL.md
        │   ├── knowledge/
        │   │   └── assets/
        │   │       ├── README.md
        │   │       └── gifts/
        │   │           └── line_qr.png
        │   └── templates/
        │       ├── _shared/
        │       │   ├── bg/
        │       │   │   ├── abstract1.jpg
        │       │   │   ├── blueprint1.jpg
        │       │   │   ├── code1.jpg
        │       │   │   ├── coffee1.jpg
        │       │   │   ├── notebook1.jpg
        │       │   │   ├── q_community.jpg
        │       │   │   ├── q_thinking.jpg
        │       │   │   ├── q_workspace2.jpg
        │       │   │   └── workspace1.jpg
        │       │   ├── event/
        │       │   │   └── cover_event.png
        │       │   ├── line_qr.png
        │       │   ├── logos/
        │       │   │   ├── canva.png
        │       │   │   ├── chatgpt.png
        │       │   │   ├── claude_code.png
        │       │   │   ├── codex.png
        │       │   │   ├── cursor.png
        │       │   │   ├── figma.png
        │       │   │   ├── gemini.png
        │       │   │   ├── chatgpt.png
        │       │   │   ├── manus.png
        │       │   │   ├── mcp.png
        │       │   │   ├── midjourney.png
        │       │   │   ├── notion.png
        │       │   │   ├── obsidian.png
        │       │   │   ├── claude_code.png
        │       │   │   ├── peatix.png
        │       │   │   ├── perplexity.png
        │       │   │   ├── replit.png
        │       │   │   ├── runway.png
        │       │   │   └── supabase.png
        │       │   └── style.css
        │       ├── eternal/
        │       │   ├── 01-speaker-self-intro.html
        │       │   ├── 02-team-intro.html
        │       │   └── README.md
        │       ├── index.html
        │       └── snippets/
        │           ├── 01-cover.html
        │           ├── 02-agenda.html
        │           ├── 03-section.html
        │           ├── 04-speakers.html
        │           ├── 05-thanks.html
        │           ├── AA-illust-side.html
        │           ├── AB-table.html
        │           ├── AC-flow-vbars.html
        │           ├── AD-xgrid.html
        │           ├── AE-stack.html
        │           ├── AF-stat-bang.html
        │           ├── AG-gifts-3.html
        │           ├── AH-qr.html
        │           ├── AI-bio-detail.html
        │           ├── AJ-bio-team.html
        │           ├── AK-question-dark.html
        │           ├── AL-question-light.html
        │           ├── AM-statement-grad.html
        │           ├── AN-chapter.html
        │           ├── AO-bigword-3d.html
        │           ├── AP-cardsvis.html
        │           ├── AQ-merge.html
        │           ├── AR-orgchart.html
        │           ├── AS-evolution.html
        │           ├── AT-vscards.html
        │           ├── AU-dataflow.html
        │           ├── U-photo-bg.html
        │           ├── V-photo-num.html
        │           ├── W-photo-label.html
        │           ├── X-eyebrow-big.html
        │           ├── Y-bigword.html
        │           ├── Z-color-tobira.html
        │           └── _frame.html
        ├── 04-youtube-slide-image-prompt/
        │   ├── README.md
        │   ├── SKILL.md
        │   └── knowledge/
        │       └── references/
        │           ├── anti-ai-design.md
        │           ├── before_after.txt
        │           ├── claude_code_install_guide.md
        │           ├── diagram-types.md
        │           ├── コンセプト図_ピラミッド.txt
        │           ├── タイムライン_横型.txt
        │           ├── チェックリスト.txt
        │           ├── ツール比較_分岐型.txt
        │           ├── フロー図_ステップ型.txt
        │           ├── マインドマップ.txt
        │           ├── マトリクス_2x2.txt
        │           ├── ランキング.txt
        │           ├── 数値比較_棒グラフ.txt
        │           ├── 比較表_2択.txt
        │           ├── 漫画_4コマ.txt
        │           ├── 用語解説_カード型.txt
        │           ├── 表.txt
        │           └── 関係図_ネットワーク.txt
        ├── 05-brand-web-deck/
        │   ├── SKILL.md
        │   └── knowledge/
        │       ├── image-catalog.md
        │       └── layout-catalog.md
        └── SKILL.md
