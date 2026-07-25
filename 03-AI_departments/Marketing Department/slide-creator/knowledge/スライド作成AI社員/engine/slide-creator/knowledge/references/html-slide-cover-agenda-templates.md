# HTMLスライド：表紙・AGENDA・セクション扉・本文（既定シェル）

**ブランド / CMO の HTML スライド**では、新規デッキを multi-file（`index.html` + `css/style.css` + `js/slides.js` + `js/app.js`）で作るとき、次を**毎回**デフォルトとする（ユーザー指定で別デザインがない限り）。

1. **1枚目** — 表紙テンプレ  
2. **2枚目** — AGENDA（目次の行数はデッキで可変）  
3. **目次の各ブロック（01〜0N）の本文に入る直前** — **セクション扉**（巨大淡番号 + バー + タイトル + 一行説明）

**スキル入口**: `../templates/deck-shell.md`
**日本語**: `html-slide-plain-japanese.md` · **本文パターン（フロー・カード等）**: `html-slide-body-patterns-catalog.md` + 案件 `css/body-patterns.css`

## 配色・フォント（このテンプレの既定 — ブランド ブランド）

| トークン | CSS 変数 | 値 | 用途 |
|----------|---------|-----|------|
| ダーク | `--c-dark` | `#1a1a2e` | AGENDA 左カラム背景・表紙タイトル色・ステートメント背景 |
| アクセント | `--c-accent` | `#9b8cff` | キッカー・番号・アクセントバー・ブリッジ背景 |
| アクセント（濃） | `--c-accent-dark` | `#7b6ce0` | ホバー・グラデーション起点 |
| オレンジ | `--c-orange` | `#c87941` | ワークバッジ・第2アクセント・ブリッジ橙 |
| オレンジ（淡） | `--c-orange-light` | `#e8b88a` | グラデーション中間 |
| サーフェス | `--c-surface` | `#f4f2fb` | 表紙テキスト側背景・タイル背景 |
| ミュート | `--c-muted` | `#6c6c8a` | サブテキスト |
| ボーダー | `--c-border` | `#e0ddf0` | カード・タイル枠線 |
| グラデーション | `--c-gradient` | `linear-gradient(145deg, #7b6ce0 0%, #9b8cff 24%, #c87941 49%, #e8b88a 74%, #f7f0f6 100%)` | アクセントバー・装飾ライン |

フォントスタック（欧文＋日本語）:

`"Noto Sans JP", "Helvetica Neue", "Hiragino Kaku Gothic ProN", system-ui, sans-serif`

番号（AGENDA の `01` 等）:

`"Helvetica Neue", Helvetica, sans-serif`（PPTX テンプレートの Helvetica 番号を踏襲）

## 1枚目：表紙（左右分割・右にビジュアル）

**構造**: 左 `flex:1` テキスト / 右 `flex:1` 背景画像（`background-size: cover`）。

- 左上ラベル例: `PRESENTATION`（用途に応じて `WORKSHOP` / `WEBINAR` 等に差し替え可）
- `h1`: メインタイトル（`<br>` で行分け可）
- 下段: スピーカー名・日付など一行（例: `Speaker Name — 2026.04.02`）
- 右列: **既定**はプレースホルダー画像 `https://picsum.photos/seed/office/1280/720`。**納品時**は `assets/cover-photo.jpg` 等に差し替え（オフライン配布ではローカル画像推奨）

### HTML（インライン版・そのまま流用可）

```html
<div style="width:100%;height:100%;display:flex;font-family:'Helvetica Neue','Hiragino Kaku Gothic ProN',sans-serif;">
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;padding:5vw 4vw;background:#f8f8fc;">
    <div style="font-size:1.5vw;color:#9b8cff;font-weight:700;letter-spacing:.2vw;margin-bottom:1.5vw;">PRESENTATION</div>
    <h1 style="font-size:4.5vw;font-weight:800;color:#1a1a2e;line-height:1.25;margin-bottom:2vw;">メインタイトルを<br>ここに配置</h1>
    <p style="font-size:1.8vw;color:#6c6c8a;">Speaker Name — 2026.04.02</p>
  </div>
  <div style="flex:1;background-image:url(https://picsum.photos/seed/office/1280/720);background-size:cover;background-position:center;"></div>
</div>
```

### CSS クラス版（デッキ内で推奨）

`hp-upstream-pillars-html` 等の実装では `.html-tpl-cover-root` および子要素を使う。詳細は各デッキの `css/style.css`。

### 表紙バリエーション（PPTX テンプレート由来）

PPTX テンプレートから 4 種類の表紙パターンを移植。用途に応じて使い分ける。

| バリエーション | クラス | 向き |
|-------------|-------|------|
| 左右分割（既定） | `.tpl-cover` | セミナー・ウェビナー・ワークショップ |
| 全面ダーク + 大タイトル | `.tpl-cover-full` | キーノート・発表会。下端にグラデーションライン |
| ロゴ中央 | `.tpl-cover-logo` | 提案・見積もり資料。ロゴ + サブタイトル + 宛先 + 日付 |
| 左右分割 + ロゴ中央（応用） | `.tpl-cover` + ロゴ配置 | 上記の組み合わせ |

```html
<!-- 全面ダーク表紙 -->
<div class="tpl-cover-full">
  <div class="tpl-cover-full__title">メインタイトル</div>
  <div class="tpl-cover-full__sub">サブタイトル</div>
</div>

<!-- ロゴ中央表紙 -->
<div class="tpl-cover-logo">
  <img src="assets/brand-logo.png" alt="ブランド" class="tpl-cover-logo__img">
  <p class="tpl-cover-logo__subtitle">ご提案資料</p>
  <p class="tpl-cover-logo__for">○○株式会社様</p>
  <p class="tpl-cover-logo__date">2026年○月○日</p>
</div>
```

---

## 2枚目：AGENDA（左ダーク + 右に目次リスト）

- 左 `width:38%` · 背景 `#1a1a2e` · 見出し `AGENDA` · サブ `本日の内容` 等
- 上端に細いアクセントバー（`#9b8cff`）
- 右列: 番号 `01` `02` … + 見出し + 一行説明の繰り返し（**行数はデッキに合わせて増減**）

### HTML（インライン版）

```html
<div style="width:100%;height:100%;display:flex;font-family:'Helvetica Neue','Hiragino Kaku Gothic ProN',sans-serif;background:#fff;">
  <div style="width:38%;background:#1a1a2e;display:flex;flex-direction:column;justify-content:center;padding:5vw;">
    <div style="width:4vw;height:.3vw;background:#9b8cff;margin-bottom:2.5vw;"></div>
    <h1 style="font-size:5vw;font-weight:800;color:#fff;letter-spacing:.1vw;">AGENDA</h1>
    <p style="font-size:1.6vw;color:rgba(255,255,255,.4);margin-top:1.5vw;">本日の内容</p>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;padding:5vw 5vw 5vw 4vw;">
    <div style="display:flex;flex-direction:column;gap:2.5vw;">
      <!-- 行を必要数だけ複製して編集 -->
      <div style="display:flex;align-items:flex-start;gap:2vw;">
        <div style="font-size:2.4vw;font-weight:800;color:#9b8cff;flex-shrink:0;width:3.5vw;">01</div>
        <div><h3 style="font-size:2vw;font-weight:700;color:#1a1a2e;">はじめに</h3><p style="font-size:1.4vw;color:#6c6c8a;margin-top:.3vw;">背景と目的の共有</p></div>
      </div>
    </div>
  </div>
</div>
```

## 3. セクション扉（章開き）— 目次の **各ブロック** の直前

**いつ使うか**: AGENDA の **01 の本文スライドの直前**、**02 の本文の直前** … と、**目次に出したブロック数と同じ枚数**だけ差し込む。

**見た目**: 左に大きい淡色の番号（`14vw` 相当・色 `#f0f0f6`）、右に細いアクセントバー（`#9b8cff`）+ セクションタイトル + 一行説明。背景 `#fff`、パディング `5vw`。

### HTML（インライン版）

```html
<div style="width:100%;height:100%;display:flex;align-items:center;font-family:'Helvetica Neue','Hiragino Kaku Gothic ProN',sans-serif;background:#fff;padding:5vw;">
  <div style="font-size:14vw;font-weight:900;color:#f0f0f6;line-height:1;margin-right:3vw;">01</div>
  <div>
    <div style="width:3vw;height:.25vw;background:#9b8cff;margin-bottom:1.5vw;"></div>
    <h1 style="font-size:4.2vw;font-weight:800;color:#1a1a2e;line-height:1.3;">セクションタイトル</h1>
    <p style="font-size:1.7vw;color:#6c6c8a;margin-top:1vw;">Section Description</p>
  </div>
</div>
```

### CSS クラス版（デッキ内で推奨）

`.html-tpl-section-root` / `.html-tpl-section-num` / `.html-tpl-section-body` / `.html-tpl-section-bar` / `.html-tpl-section-h1` / `.html-tpl-section-desc` — 各デッキの `css/style.css` に定義。

- **番号**は AGENDA の `01`…と **必ず一致**させる。
- 説明行は日本語のみでもよい（プレースホルダの `Section Description` は差し替え）。

---

### セクション扉バリエーション（PPTX テンプレート由来）

| バリエーション | クラス | 向き |
|-------------|-------|------|
| 左番号 + 右タイトル（既定） | `.tpl-section` | 標準。番号は `14cqw` の淡色 |
| 中央タイトル（ダーク背景） | `.tpl-section-center` | キーノート向き。上端にグラデーションライン |

```html
<!-- 中央型セクション扉 -->
<div class="tpl-section-center">
  <h1 class="tpl-section-center__h1">セクションタイトル</h1>
</div>
```

### CONTENTS パターン（PPTX: 番号付き縦リスト）

AGENDA の代替。シンプルに番号 + テキストの縦リスト。PPTX テンプレートの `01-06` パターン。

クラス: `.tpl-contents` / `__title` / `__list` / `__item` / `__item-num`（Helvetica 太字） / `__item-text`

```html
<div class="tpl-contents">
  <h2 class="tpl-contents__title">CONTENTS</h2>
  <div class="tpl-contents__list">
    <div class="tpl-contents__item">
      <div class="tpl-contents__item-num">01</div>
      <div class="tpl-contents__item-text">URLひとつで伝わる世界</div>
    </div>
    <!-- 繰り返し -->
  </div>
</div>
```

---

## 4. 本文スライド（画像左 50%・テキスト右）— 通常スライドの既定パターン

**いつ使うか**: セクション扉のあと、**事例・製品・人物・図版付き説明**など、ビジュアルとコピーを並べるとき。

**見た目**: 左に `width:50%` の画像（`background-size: cover`）、右にカテゴリラベル（`#9b8cff`）+ 見出し + 本文。背景 `#fff`。ラベルは `CATEGORY` のままではなく、**日本語の小見出し**（例: `ゴールツリー`）に差し替える。

### HTML（インライン版）

```html
<div style="width:100%;height:100%;display:flex;font-family:'Helvetica Neue','Hiragino Kaku Gothic ProN',sans-serif;background:#fff;">
  <div style="width:50%;background-image:url(https://picsum.photos/seed/tech/1280/720);background-size:cover;background-position:center;"></div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;padding:4vw 5vw;">
    <div style="font-size:1.4vw;color:#9b8cff;font-weight:700;letter-spacing:.15vw;margin-bottom:1vw;">CATEGORY</div>
    <h2 style="font-size:3.4vw;font-weight:800;color:#1a1a2e;line-height:1.3;margin-bottom:2vw;">画像＋テキスト<br>レイアウト</h2>
    <p style="font-size:1.6vw;color:#6c6c8a;line-height:1.9;">左半分に画像、右半分にテキスト。製品紹介、事例紹介、人物紹介など幅広く使えるパターンです。</p>
  </div>
</div>
```

### CSS クラス版（デッキ内で推奨）

`.html-tpl-imgtxt-root` / `__visual` / `__content` / `__kicker` / `__title` / `__text` — 各デッキの `css/style.css` に定義（`hp-upstream-pillars-html` に同梱例あり）。

- 画像は **プレースホルダ**可。納品時は `assets/` のローカル画像推奨。
- **右左**を入れ替える場合は同じ比率で `flex-direction: row-reverse` を検討（別パターンとして文書化してもよい）。

---

## 実装メモ

- 表紙・AGENDA・セクション扉でスライド全体を埋めるときは親 `<section class="slide">` 内の **パディングをゼロ**にする（`.slide-content--flush` 等）。**本文分割レイアウト**も同様にフルブリードで埋める。
- **箇条書き中心のスライド**は従来どおり `.slide-content` + タイポクラスでもよい。図版＋短い主張のときは **§4 の分割パターン**を優先。
- `slides.js` の `slideFactories` は **先頭が表紙 → 2枚目が AGENDA → 各セクション扉 → 本文…** の順を守る。
- Marp 用の `cover-reference.png` テンプレとは**別物**（HTML 専用）。
