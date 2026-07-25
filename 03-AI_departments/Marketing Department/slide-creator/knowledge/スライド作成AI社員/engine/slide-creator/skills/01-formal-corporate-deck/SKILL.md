---
name: formal-corporate-deck
description: 会社説明資料・営業資料・コンサル提案書など、特定企業や意思決定者へ見せる正式な法人向け資料をHTML/CSS/JSスライドで構築する。ブランド Web Deckとは違い、公開URLで広く読ませる資料ではなく、信頼感・情報密度・根拠を重視する。
argument-hint: "[資料タイプ / 提出先 / 目的 / 提出相手]"
---

# formal-corporate-deck スキル（正式法人資料専用）

## 位置づけ

**会社説明資料・営業資料・コンサル提案書・対企業提案書**など、ビジネスの場で使う正式な法人向け資料を HTML/CSS/JS スライドで構築する。

`05-brand-web-deck` とは違い、**読み手が1人〜数人の意思決定者**であることを前提に、情報密度・信頼感・根拠・ブランド一貫性を最優先する。

### 既存スキルとの使い分け

| 作りたいもの | 読むスキル |
|---|---|
| セミナー・ウェビナー・ワークショップ用スライド | `../03-presentation-mode/SKILL.md` |
| 登壇・LT・プレゼン用（1スライド1メッセージ） | `../03-presentation-mode/SKILL.md` |
| **会社説明資料・営業提案書・コンサル提案** | **`../01-formal-corporate-deck/SKILL.md`（このファイル）** |
| ブランドサイトと同じ世界観の公開Webデッキ・読み物資料 | `../05-brand-web-deck/SKILL.md` |
| CMO訴求設計・マーケティングストーリー | `../../knowledge/references/html-cmo-marketing-story.md` |

### 01 と 05 の違い

| 観点 | 01-formal-corporate-deck | 05-brand-web-deck |
|---|---|---|
| 一言でいうと | 正式な法人資料 | ブランドサイト流の公開Webデッキ |
| 主な読者 | 特定企業の担当者・経営者・意思決定者 | Web上で読む見込み客・受講者・広い読者 |
| 優先するもの | 信頼感、根拠、情報密度、提出先への最適化 | サイト世界観、読みやすさ、画像活用、公開運用 |
| 出口 | 商談・提案・提出・社内稟議 | 公開URL・資料ページ・リード獲得・読み物 |

迷ったら、相手の会社名や提出先が明確なら01、ブランドサイト上で広く読ませるなら06を使う。

## 親スキル・共通ルール

技術実装の基盤は `../02-slide-builder-main/SKILL.md` と共通。以下を継承する:

- multi-file 構成（`index.html` / `css/style.css` / `js/slides.js` / `js/app.js`）
- slides.js の関数ファクトリ方式（1スライド = 1関数）
- サイドバーはデフォルト非表示・オーバーレイ式
- コンテンツ縦センター配置（`justify-content: center`）
- 脱AIデザインゲート（全項目適用）
- 品質チェック（テキストはみ出し・改行位置・コントラスト比）

**このスキル固有の上書き・追加ルールは以下に記載。**

---

## コーポレート資料の設計原則

### 1. 信頼ファースト

- テイストは **「信頼感」または「スタイリッシュ」** を既定とする
- ホワイトベース + ダークアクセント。派手な演出・アニメーションは控える
- 数字・実績・事例を多用し、主張には必ず根拠を添える

### 2. 情報密度を高く

- セミナー用の「1スライド60文字」制限は適用しない
- 1スライドあたり **最大200文字**。ただし視認性を損なわない範囲
- 箇条書きは最大 **5項目**
- 図解・表・チャートを積極的に使い、テキスト壁を避ける

### 3. ブランド一貫性

- ブランド ブランドカラー・フォント・ロゴ配置を厳守
- 全スライドに統一感のある背景処理を適用

### 4. ブランド素材の最大活用

ブランド HPサイトには 100点以上の高品質素材がある。**プレースホルダ画像（picsum等）は原則禁止**。以下の素材ライブラリから適切な画像を選んで使う。

---

## ブランド素材ライブラリ（必須参照）

### 素材ベースパス

```
<社内ナレッジ>/株式会社アイウエオ/assets/img/
```

### 用途別素材マップ

| 用途 | 推奨素材 |
|---|---|
| **表紙ロゴ** | `brand-logo.png` |
| **代表写真** | `speaker-ceo.jpg`、`ceo-message.png` |
| **ミッション** | `mission-play.png` |
| **ビジョン** | `vision-place.png` |
| **バリュー** | `value-good.png`、`value-thanks.png`、`value-bet.png` |
| **サービス概要（6事業）** | `service_01_agent.png` 〜 `service_06_education.png` |
| **AI社員構築** | `agent_multimodel_arch.png`、`agent_department_roles.png`、`agent_automation_pipeline.png`、`agent_service_01〜03.png`、`agent_step_01〜03.png` |
| **ナレッジ構築** | `knowledge_graph_viz.png`、`knowledge_context_flow.png`、`illust_knowledge_flow.png`、`knowledge_service_01〜03.png`、`knowledge_case_01〜03.png` |
| **SNS自動化** | `xops_buzz_pipeline.png`、`xops_persona_management.png`、`xops_daily_01〜03.png`、`xops_service_01〜03.png` |
| **プロダクト** | `studio_slidebox_demo.png`、`studio_videopocket_demo.png`、`slidebox_logo.png`、`studio_product_slidebox.png`、`studio_product_videopocket.png`、`studio_service_01〜03.png` |
| **サンプルコミュニティ（イベント）** | `community_logo.png`、`community_ecosystem.png`、`community_event_01〜03.png`、`community_event_atmosphere.png`、`community_partner_01〜03.png` |
| **サンプルプロダクト（教育）** | `product_before_after.png`、`product_journey.png`、`product_why_01〜03.png` |
| **事業イラスト（汎用）** | `biz01_v1〜v5.png` 〜 `biz05_v1〜v5.png`（各事業5バリエーション） |
| **マスコット** | `mascot_main.png`、`mascot_trio.png`、`mascot_org.png`、`mascot_journey.png`、`mascot_graduation.png`、`mascot_icons.png`、`mascot_pointing.png`、`mascot_marketing.png`、`mascot_slideclaw.png` |
| **図解** | `diagram_brain_vs_ai.png`、`diagram_daily_workflow.png`、`diagram_knowledge_workflow.png`、`diagram_two_step.png` |
| **イベント写真** | `event_seminar.png`、`event_meetup_new.png` |
| **キャラクター** | `chars/claude_code_1〜5.png`、`chars/codex_1〜2.png`、`chars/sample_agent_1〜4.png`、`chars/obsidian_1〜3.png`、`chars/sample_product_1,3,5.png` |
| **Xアカウントサムネ** | `tweets/acct1_top.jpg` 〜 `tweets/acct9_top.jpg`（9アカウント） |

### 素材選択ルール

1. **スライドの内容に最も合う素材を1〜2点選ぶ**（多すぎると散漫になる）
2. サービス紹介 → 該当サービスの `service_0X_*.png` + 詳細図を組み合わせ
3. 実績・数字 → `biz0X_v*.png` のイラスト系を背景装飾に
4. 代表紹介 → `speaker-ceo.jpg`（写真）、理念系 → `ceo-message.png`
5. 図解が必要だが適切な素材がない → `gpt-image-2` で生成（3:4比率）
6. **ブランド素材がある場面で Unsplash / picsum を使わない**

---

## 表紙デザイン（HP風・コーポレート専用）

コーポレート資料の表紙は、**ブランド HPサイトのヒーローセクションを踏襲した高級感のあるデザイン**を既定とする。

### 表紙パターン

| パターン | クラス | 向き |
|---|---|---|
| **HP風グラデーション表紙**（既定） | `.corp-cover-hero` | 会社説明資料・コーポレート全般 |
| ロゴ中央 + 宛名 | `.tpl-cover-logo` | 個別提案資料（○○株式会社様 宛） |
| 全面ダーク + 大タイトル | `.tpl-cover-full` | キーノート・経営方針発表 |

### HP風表紙の仕様

```
背景: ブランドグラデーション（左下から右上）
  linear-gradient(145deg, #7b6ce0 0%, #9b8cff 24%, #c87941 49%, #e8b88a 74%, #f7f0f6 100%)
ロゴ: 中央上部に白反転ロゴ（filter: brightness(0) invert(1)）
タイトル: 白文字・中央配置・大サイズ
サブタイトル: 白文字・70%透過
下端: 細い白ライン（装飾）
```

### HP風表紙 HTML テンプレート

```html
<div class="corp-cover-hero">
  <div class="corp-cover-hero__overlay"></div>
  <div class="corp-cover-hero__content">
    <img src="assets/brand-logo.png" alt="ブランド" class="corp-cover-hero__logo">
    <h1 class="corp-cover-hero__title">会社説明資料</h1>
    <p class="corp-cover-hero__subtitle">株式会社アイウエオ</p>
    <p class="corp-cover-hero__date">2026年5月</p>
  </div>
  <div class="corp-cover-hero__line"></div>
</div>
```

### HP風表紙 CSS

```css
.corp-cover-hero {
  width: 100%; height: 100%;
  background: linear-gradient(145deg, #7b6ce0 0%, #9b8cff 24%, #c87941 49%, #e8b88a 74%, #f7f0f6 100%);
  display: flex; align-items: center; justify-content: center;
  position: relative; overflow: hidden;
}
.corp-cover-hero__overlay {
  position: absolute; inset: 0;
  background: radial-gradient(ellipse at 30% 50%, rgba(0,0,0,0.15) 0%, transparent 70%);
}
.corp-cover-hero__content {
  position: relative; z-index: 1;
  text-align: center; color: #fff;
}
.corp-cover-hero__logo {
  height: 6cqw; margin-bottom: 3cqw;
  filter: brightness(0) invert(1);
}
.corp-cover-hero__title {
  font-size: 5cqw; font-weight: 800;
  letter-spacing: 0.15em; margin-bottom: 1.5cqw;
}
.corp-cover-hero__subtitle {
  font-size: 2cqw; opacity: 0.85; font-weight: 400;
}
.corp-cover-hero__date {
  font-size: 1.4cqw; opacity: 0.6; margin-top: 2cqw;
}
.corp-cover-hero__line {
  position: absolute; bottom: 3cqw; left: 10%; right: 10%;
  height: 2px; background: rgba(255,255,255,0.3);
}
```

---

## 2枚目以降の背景処理

コーポレート資料では、2枚目以降のスライドに**統一された背景装飾**を適用し、素のホワイトバックにしない。

### 背景パターン（既定）

```css
/* 通常スライド背景（2枚目以降） */
.corp-slide-bg {
  background: #fafafa;
  position: relative;
}
.corp-slide-bg::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0;
  height: 4px;
  background: var(--c-gradient);
}
.corp-slide-bg::after {
  content: '';
  position: absolute; bottom: 0; right: 0;
  width: 30%; height: 30%;
  background: radial-gradient(ellipse at bottom right, rgba(155,140,255,0.05) 0%, transparent 70%);
  pointer-events: none;
}
```

### セクション扉の背景

セクション扉は通常の白背景ではなく、**薄いグラデーション面**を使って区切りを明確にする:

```css
.corp-section-door {
  background: linear-gradient(135deg, #f4f2fb 0%, #fff 60%, #fff8f2 100%);
}
```

---

## コーポレート資料の標準構成

### 会社説明資料（15〜25枚）

```
1.  表紙（HP風グラデーション + ロゴ + タイトル）
2.  AGENDA（目次）
3.  セクション扉: 01 会社概要
4.  会社概要（社名・設立・所在地・代表・事業内容）
5.  ミッション・ビジョン
6.  バリュー（THE AIUEO WAY）
7.  セクション扉: 02 事業紹介
8.  事業全体像（6事業の概観図）
9.  事業詳細 x 2〜6枚（主力事業を重点的に）
10. セクション扉: 03 実績
11. 数字で見るブランド（売上・フォロワー・AI活用率等）
12. 導入事例 / お客様の声
13. セクション扉: 04 代表紹介
14. 代表プロフィール（写真左 + 経歴右）
15. セクション扉: 05 お問い合わせ
16. CTA / 連絡先 / クロージング
```

### コンサル提案資料（20〜30枚）

```
1.  表紙（ロゴ中央 + 宛名）
2.  AGENDA
3.  セクション扉: 01 課題認識
4.  お客様の現状と課題（ヒアリング内容を反映）
5.  セクション扉: 02 ご提案内容
6.  提案の全体像
7.  提案詳細 x 3〜5枚
8.  セクション扉: 03 なぜブランドか
9.  ブランドの強み / 実績
10. 導入事例
11. セクション扉: 04 進め方
12. スケジュール / マイルストーン
13. 料金体系
14. セクション扉: 05 次のステップ
15. CTA / 連絡先
```

---

## インテーク（コーポレート資料用）

```text
コーポレート資料の作成を開始します。未定は「おまかせ」でOKです。

1. **資料タイプ**: 会社説明資料 / コンサル提案書 / 営業資料 / パートナー資料 / おまかせ
2. **提出先**: （例: ○○株式会社様 / 投資家向け / 一般公開用）
3. **目的**: （例: 初回商談用 / 協業提案 / 採用広報）
4. **強調したいポイント**: （例: AI社員構築の実績 / SNS運用力 / 教育事業）
5. **素材**: 追加素材あり / ブランド既存素材のみ / おまかせ
6. **ページ数**: ショート（10〜15枚）/ 標準（15〜25枚）/ 詳細（25枚〜）/ おまかせ
7. **保存場所**: （既定: このスキルと同階層に `<デッキ名>/` を作成）
8. **進め方**: 構成を確認してから生成（標準） / すぐ生成
```

---

## アセット準備（毎回最初にやる）

1. `<出力先>/assets/` フォルダを作成
2. `../brand-assets/brand-logo.png` → `assets/brand-logo.png` にコピー
3. `../brand-assets/speaker-photo.png` → `assets/speaker-photo.png` にコピー
4. **ブランド新サイト素材**（上記「素材ライブラリ」参照）から、各スライドで使う画像を `assets/` にコピー
5. コピーした画像は HTML 内で `assets/ファイル名` で参照
6. **ブランド素材で足りない場合のみ** Unsplash または gpt-image-2 を使用

---

## 出力先（既定ルール）

- **既定**: このスキルと同じディレクトリ（`01-formal-corporate-deck/output/archive/`）配下に `<日付>-<デッキ名>/` を作成して格納する
  - 例: `01-formal-corporate-deck/output/archive/2026-06-09-brand-company-deck/`
  - 例: `01-formal-corporate-deck/output/archive/2026-06-09-partner-proposal-acme/`
- ユーザー指定があればそちらを優先
- multi-file 構成: `index.html` / `css/style.css` / `js/slides.js` / `js/app.js` / `assets/`

---

## 品質チェック（コーポレート資料固有）

親スキルの品質チェックに加え、以下を確認:

- [ ] 表紙がHP風グラデーションまたはロゴ中央テンプレになっている
- [ ] ブランドロゴが表紙とクロージングに配置されている
- [ ] 2枚目以降の背景に統一装飾（上端グラデーションライン等）がある
- [ ] ブランド素材がある場面でプレースホルダ画像を使っていない
- [ ] 数字・実績には出典または時点を明記している
- [ ] 提出先がある場合、宛名が正しく入っている
- [ ] 全スライドでブランドカラーが統一されている
- [ ] 情報密度が十分（テキストが薄すぎるスライドがない）
- [ ] 代表写真（`speaker-ceo.jpg`）を使う場合、品位が保たれている
- [ ] サービス紹介で使った素材が内容と一致している

---

## 必読（コーポレート資料作成時）

| パス | いつ読むか |
|---|---|
| `../SKILL.md` | 毎回。HTMLスライドの正本・ブランドカラー定義 |
| `../../knowledge/templates/deck-shell.md` | 毎回。表紙→AGENDA→セクション扉の組み立て順 |
| `../../knowledge/references/html-slide-cover-agenda-templates.md` | 毎回。AGENDA・セクション扉のレイアウト |
| `../../knowledge/references/html-slide-body-patterns-catalog.md` | 本文レイアウト選定時。§A〜§Z + ブランドアセットマップ |
| `../../knowledge/references/html-slide-plain-japanese.md` | 毎回。日本語の平易化 |
| `../../knowledge/references/slide-output-rules.md` | 実装時。Unicode・絵文字・出力ルール |
| `../02-slide-builder-main/SKILL.md` | 技術実装の詳細が必要な時 |
