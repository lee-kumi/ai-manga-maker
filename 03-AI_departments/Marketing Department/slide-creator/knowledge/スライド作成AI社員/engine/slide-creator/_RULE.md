# Slide creator（スライド作成者）


> **新規ファイル作成時の必須手順** (絶対遵守)
> 1. `MEMORY.md` 全件を読む
> 2. 該当する `feedback_*.md` / `reference_*.md` のルールを新ファイルに反映
> 3. 参照した memory ファイルと新ファイルを `[[双方向リンク]]` で結ぶ
> 4. このファイルから参照する `00-rules/` / `SKILL.md` も `[[link]]` で結ぶ
> 守らない場合: コンテキストが散逸し AI が暴走する
>
> 詳細手順: [[memory-inheritance]]

## スコープ

構成・HTMLスライド作成手順。現在の正本は番号付きスキル配下にある。

- **入口ハブ**: `skills/SKILL.md`
- **HTML実装基盤**: `skills/02-slide-builder-main/SKILL.md`
- **登壇・セミナー・ピッチ**: `skills/03-presentation-mode/SKILL.md`
- **会社説明・正式な法人資料**: `skills/01-formal-corporate-deck/SKILL.md`
- **YouTube用スライド画像プロンプト**: `skills/04-youtube-slide-image-prompt/SKILL.md`
- **ブランドサイト流のWebデッキ・公開資料**: `skills/05-brand-web-deck/SKILL.md`
- **PDF/既存スライド参照クローンHTML**: `skills/06-pdf-style-clone-html-deck/SKILL.md`
- **セミナー動画参照クローンHTML**: `skills/07-seminar-video-style-clone-deck/SKILL.md`
- **退避済み旧スキル**: `99-trash/2026-06-09_slide-creator-skill-retirement/`
- **共通ナレッジ**: `knowledge/templates/`、`knowledge/references/`、`knowledge/assets/`

HTMLスライドは Marp テンプレ・Marp ディレクティブを使わない。Marp系の旧入口は現在の主導線から外す。
削除候補・退避対象は、スキル配下に `99-retired` を作らず、必ずワークスペース直下の `99-trash/` へ移動する。

## 読む順

1. まず `skills/SKILL.md` で用途を判定する。
2. HTML実装に進むなら `skills/02-slide-builder-main/SKILL.md` を読む。
3. 登壇・ウェビナー・セミナーなら `skills/03-presentation-mode/SKILL.md` を読む。
4. 会社説明資料・正式な法人向け資料なら `skills/01-formal-corporate-deck/SKILL.md` を読む。
5. YouTube動画用スライドに入れる図解画像プロンプトが必要なら `skills/04-youtube-slide-image-prompt/SKILL.md` を読む。
6. ブランドサイトと同じ世界観の公開デッキ・読み物資料なら `skills/05-brand-web-deck/SKILL.md` を読む。
7. 参考PDF・既存スライドを強く模倣してHTML化するなら `skills/06-pdf-style-clone-html-deck/SKILL.md` を読む。
8. 長尺セミナー動画からスライド切替を抽出し、販売デッキを作るなら `skills/07-seminar-video-style-clone-deck/SKILL.md` を読む。
9. 図解HTMLの依頼は slide-creator 04 ではなく、CEO配下 `<部門>/ceo（代表取締役）/skills/07-html-diagram-explainer/SKILL.md` を読む。

## スキルマップ

| 番号 | スキル | 用途 |
|---:|---|---|
| 01 | `skills/01-formal-corporate-deck/SKILL.md` | 正式な会社説明資料・営業資料・対企業提案書 |
| 02 | `skills/02-slide-builder-main/SKILL.md` | HTML/CSS/JSスライド実装基盤 |
| 03 | `skills/03-presentation-mode/SKILL.md` | 登壇・プレゼン用HTMLスライド |
| 04 | `skills/04-youtube-slide-image-prompt/SKILL.md` | YouTube動画用スライド画像の生成プロンプト設計 |
| 05 | `skills/05-brand-web-deck/SKILL.md` | example.com流Webデッキ |
| 06 | `skills/06-pdf-style-clone-html-deck/SKILL.md` | PDF/既存スライドの全ページ画像化、レイアウト抽出、HTMLクローン実装、全枚数スクショQA |
| 07 | `skills/07-seminar-video-style-clone-deck/SKILL.md` | 長尺セミナー動画のスライド切替スクショ化、販売導線レイアウト抽出、バックエンド商品を売る登壇HTMLデッキ化 |

## 退避済み旧スキル

| 旧番号 | 退避先 | 理由 |
|---:|---|---|
| 04 | `99-trash/2026-06-09_slide-creator-skill-retirement/moved/<部門>/Marketing Department/slide-creator/skills/04-cmo-marketing/SKILL.md` | CMO観点は共通ナレッジ/03/05へ吸収する方が使いやすいため |
| 07 | `99-trash/2026-06-09_slide-creator-skill-retirement/moved/<部門>/Marketing Department/slide-creator/skills/07-slide-creation/SKILL.md` | 旧Marp継承で、現在のHTMLデッキ主導線と合わないため |

## 現在の整理メモ

- `01-formal-corporate-deck` は残す。正式な会社説明・法人資料の入口として使う。
- `05-brand-web-deck` も残す。ブランドサイトと同じ世界観、公開用Webデッキ、読み物型資料の入口として使う。
- `04-youtube-slide-image-prompt` は残す。YouTube動画用スライドに入れる画像生成プロンプトの設計役として使う。
- 旧 `04-cmo-marketing` と旧 `07-slide-creation` はワークスペース直下 `99-trash/2026-06-09_slide-creator-skill-retirement/` へ退避済み。
- 汎用の画像図解はCEO 06、HTML図解はCEO 07。slide-creator 04は「YouTubeスライド画像プロンプト」に限定する。

## エスカレーション

講義全体のストーリー・セミナー告知との整合 → CMO。
