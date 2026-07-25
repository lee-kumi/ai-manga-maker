# Unsplash 画像活用ガイド（HTMLスライド用）

**用途**: HTMLスライド制作時に Unsplash からスタイリッシュな写真を取得し、スライドに配置するためのルール。

**更新履歴**
- 2026-05-11 — 初版

---

## 基本方針

- ブランド 自社アセット（`<社内ナレッジ>/株式会社アイウエオ/assets/img/`、`brand-assets/`）が内容に合う場合は**自社アセットを優先**
- 自社アセットにない「雰囲気写真」「背景テクスチャ」「感情喚起用のイメージ」に Unsplash を使う
- Unsplash は**装飾・演出・空気感の補強**であり、情報の中核（製品写真・実績データ等）には使わない

## 取得方法

### Unsplash Source URL（直リンク）

```
https://images.unsplash.com/photo-{PHOTO_ID}?w={幅}&h={高さ}&fit=crop&q=80
```

### 検索して選ぶ場合

1. `https://unsplash.com/s/photos/{キーワード}` で検索
2. スライドのテーマに合う写真を選ぶ
3. 写真の URL（`https://images.unsplash.com/photo-...`）をコピー
4. クエリパラメータで最適化: `?w=1920&h=1080&fit=crop&q=80`

### サイズ指定

| 用途 | 推奨サイズ | パラメータ |
|------|-----------|-----------|
| フルスクリーン背景 | 1920×1080 | `?w=1920&h=1080&fit=crop&q=80` |
| 左右分割（50%パネル） | 960×1080 | `?w=960&h=1080&fit=crop&q=80` |
| カード内画像 | 640×400 | `?w=640&h=400&fit=crop&q=80` |
| ステップカード上部 | 480×320 | `?w=480&h=320&fit=crop&q=80` |

## テーマ別キーワード辞書

スライドの内容に合わせて以下のキーワードから選ぶ。**複数キーワードをスペース区切りで組み合わせる**と精度が上がる。

### ビジネス・テック系

| シーン | キーワード例 |
|--------|-------------|
| 表紙・オープニング | `technology workspace minimal`, `modern office light`, `laptop desk clean` |
| AI・テクノロジー | `artificial intelligence abstract`, `neural network`, `digital transformation`, `data visualization` |
| チームワーク | `team collaboration`, `business meeting`, `startup team`, `brainstorming` |
| 成長・成果 | `growth chart`, `success business`, `achievement`, `mountain summit` |
| 問題提起 | `frustrated business`, `complexity`, `maze`, `overwhelmed` |

### 抽象・テクスチャ系（背景向き）

| シーン | キーワード例 |
|--------|-------------|
| ダーク背景 | `abstract dark texture`, `black marble`, `dark gradient`, `night city aerial` |
| ライト背景 | `white minimal abstract`, `light texture paper`, `soft gradient`, `white architecture` |
| アクセント背景 | `abstract red`, `geometric pattern`, `line art minimal` |
| 自然・安心感 | `nature light`, `morning fog`, `calm water`, `green leaves minimal` |
| 未来感 | `futuristic architecture`, `glass building`, `neon minimal`, `space` |

### 感情・ストーリー系

| シーン | キーワード例 |
|--------|-------------|
| 希望・始まり | `sunrise`, `open road`, `new beginning`, `first step` |
| 変化・転換 | `butterfly`, `transformation`, `before after`, `crossroads` |
| 信頼・安定 | `handshake`, `foundation`, `bridge`, `anchor` |
| スピード・加速 | `speed motion`, `fast train`, `running`, `rocket launch` |

## HTML での配置パターン

### パターン1: フルスクリーン背景（§G ステートメント、ブリッジ）

```html
<div class="html-tpl-pat-statement" style="
  background-image: linear-gradient(rgba(26,26,46,0.75), rgba(26,26,46,0.75)),
                    url('https://images.unsplash.com/photo-XXXXX?w=1920&h=1080&fit=crop&q=80');
  background-size: cover;
  background-position: center;
">
  <div class="html-tpl-pat-statement__inner">
    <div class="html-tpl-pat-statement__text">メッセージをここに</div>
  </div>
</div>
```

**ポイント**: `linear-gradient` のオーバーレイで文字の可読性を確保する。`rgba(26,26,46,0.75)` が標準。写真が明るい場合は `0.8` に上げる。

### パターン2: 左右分割の画像パネル（§4 画像左 / §P 画像右）

```html
<div class="html-tpl-pat-txtimg__visual" style="
  background-image: url('https://images.unsplash.com/photo-XXXXX?w=960&h=1080&fit=crop&q=80');
  background-size: cover;
  background-position: center;
"></div>
```

### パターン3: 表紙の右ビジュアル

```html
<div style="flex:1;
  background-image: url('https://images.unsplash.com/photo-XXXXX?w=960&h=1080&fit=crop&q=80');
  background-size: cover;
  background-position: center;
"></div>
```

### パターン4: カード内の装飾画像（§B 3カード、§S ステップカード）

```html
<img src="https://images.unsplash.com/photo-XXXXX?w=640&h=400&fit=crop&q=80"
     alt="説明テキスト"
     style="width:100%; height:200px; object-fit:cover; border-radius:16px 16px 0 0;">
```

### パターン5: ギャラリーの一部（§M）

ブランド 実素材と Unsplash を混ぜて使う場合:

```html
<div class="html-tpl-pat-gallery__grid html-tpl-pat-gallery__grid--2x2">
  <div class="html-tpl-pat-gallery__item">
    <img src="assets/mv_ai_working01.png" alt="" class="html-tpl-pat-gallery__img">
    <div class="html-tpl-pat-gallery__caption">AI が働く現場</div>
  </div>
  <div class="html-tpl-pat-gallery__item">
    <img src="https://images.unsplash.com/photo-XXXXX?w=640&h=400&fit=crop&q=80"
         alt="" class="html-tpl-pat-gallery__img">
    <div class="html-tpl-pat-gallery__caption">最新のワークスペース</div>
  </div>
</div>
```

## 構成案での記述方法

構成承認ドラフトでは、各スライドの `ビジュアル:` 行に Unsplash キーワードを明記する:

```text
4. 問題提起 | F5（§4 画像左）
メッセージ: 手作業が限界を迎えている
ビジュアル: Unsplash「frustrated business person desk」左50% + ダーク気味
トークスクリプト概要: よくある属人化の失敗パターンを語る
```

承認後の HTML 実装で、キーワードに合う具体的な写真を選定する。

## 品質ルール

### 必須

- [ ] **Unsplash URL がスライドの表示テキストに出ていない**（CSS/HTML の属性値としてのみ使用）
- [ ] **オーバーレイなしで文字を重ねていない**（背景写真 + テキストの場合は必ず `linear-gradient` オーバーレイ）
- [ ] **文字とのコントラスト比が 4.5:1 以上**（WCAG 2.1 準拠）
- [ ] **写真の選定がスライドの内容と一致している**（「AI」の話に食べ物の写真を使わない等）
- [ ] **1デッキ内で同じ写真を2回以上使っていない**
- [ ] **人物写真の品位を守っている**（大袈裟な表情・安っぽい演出・ストックフォト臭の強いポーズを避ける）

### 推奨

- [ ] 1デッキで Unsplash 画像は全体の30〜50%程度に留める（残りは ブランド アセット + 図解）
- [ ] テイストを統一する（同一デッキ内で暖色系と寒色系を混ぜすぎない）
- [ ] 写真のトーンをデッキのカラーパレットに合わせる（`#1a1a2e` ダーク系なら寒色・モノトーン寄りの写真）
- [ ] フルブリード背景には解像度 1920px 以上の写真を使う（`?w=1920` 指定）
- [ ] `?q=80` で画質を確保しつつファイルサイズを抑える

## ブランド アセットとの使い分け早見表

| 内容 | ブランド アセット | Unsplash |
|------|-------------|----------|
| ブランド のロゴ・代表写真 | **必ず ブランド** | 使わない |
| ブランド のサービス画像・アイコン | **ブランド 優先** | なければ Unsplash |
| 導入ステップ・プロセス図 | **ブランド 優先**（`step_img`） | なければ Unsplash |
| AI ワーキング風景 | **ブランド 優先**（`mv_ai_working`） | 混ぜて使ってもよい |
| 表紙・ブリッジの雰囲気写真 | なければ | **Unsplash 推奨** |
| ステートメント背景テクスチャ | `bg-1.png` / `feature_bg.png` | **Unsplash 推奨** |
| 感情喚起（希望・問題提起等） | 該当なし | **Unsplash 推奨** |
| イベント・登壇写真 | **ブランド 優先**（`event_photo`） | 使わない |

## Unsplash 利用時の注意

- Unsplash のライセンスは商用利用可・クレジット不要だが、スライド末尾やノートに `Photos by Unsplash` と入れておくと丁寧
- 写真の URL はオンライン前提。オフライン配布の場合は画像をダウンロードして `assets/unsplash/` に配置する
- Unsplash API（`api.unsplash.com`）を使う場合は API キーが必要。URL 直リンクなら不要
