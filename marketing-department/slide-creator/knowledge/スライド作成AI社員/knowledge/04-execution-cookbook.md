# 04-execution-cookbook.md — セミナープレゼン作成AI社員

## このAI社員の完成フォルダ例

```text
output/archive/YYYY-MM-DD_task-name/
├── brief.md            ← 前提整理（templates/02-brief.md の型で）
├── questions.md        ← 聞いたこと・回答・残った仮定
├── story-plan.md       ← 話の流れ（章 → 1スライド1行の設計図）
├── source-map.md       ← 使った素材・数字の出どころ
├── slides/index.html   ← 完成デッキ本体
├── assets/             ← 使用画像（比率を壊さない）
├── screenshots/final/  ← 全ページスクショ（俯瞰QA用）
└── review-notes.md     ← 判断理由・QA結果・次回への改善
```

## 入力から出力へ変換する順番

1. 入力情報を全部読む。
2. `事実`、`素材`、`ユーザー希望`、`制約`、`未確認` に分ける。
3. 受け手の立場で「最初に知りたいこと」「疑問に思うこと」「不安に思うこと」を書き出す。
4. その不安を潰すために、構成、説明、証拠、FAQ、次アクションを並べる。
5. 初稿を作る。
6. 目的に合わない要素を削る。
7. 足りない証拠、例、比較、手順を足す。
8. 最後に安全チェックと再現メモを残す。

## 作業メモの型

```md
# 作業メモ

## 今回の目的
-

## 受け手
-

## 最終行動
-

## 使った一次情報
-

## 仮定したこと
-

## 判断したこと
-

## 次回から固定できること
-
```

## 補助スクリプト（それぞれ何をするか・いつ使うか）

- `scripts/create_deck_project.py deck-plan.json`: **案件フォルダの一発生成**。スライド計画JSON（slug/title/slides配列: layout/kicker/title/body/caption）から `output/archive/日付_slug/` に slides/index.html＋brief/questions/story-plan/source-map/review-notes＋assets/＋screenshots/final/ の骨格を全部作る。**新規案件はまずこれ**。
- `scripts/build_basic_html_deck.py slides.json -o slides/index.html`: **JSON→ダークテーマHTMLデッキ変換**。layout: cover / proof / four / quote / split / steps / evidence を書き分けられる。ラフを一気に形にしたい時用（見た目の主役は engine/07-seminar-style か deck-bank のテンプレ。これは下書き機）。
- `scripts/build_template_library.py <スクショフォルダ> -o template-library.json`: **参考デッキのスクショ群を「型索引」化**。ファイル名から cover/profile/proof/question/comparison/section_bridge に自動分類し、`文言はコピーせず構図を抽象化して使う` ルール付きのJSON索引を作る。参考資料をもらった時の最初の一手。
- `scripts/extract_video_frames.py 動画.mp4 --fps 1/5`: **過去登壇の録画からスライド候補画像を抽出**（5秒に1枚）。ffmpeg必須。参考デッキがHTMLでなく動画しか無い時に、上の索引化とセットで使う。
- `scripts/validate_deck_assets.py slides/index.html`: **納品前の素材リンク検査**。HTML内のsrc/hrefが指すローカルファイルの欠落を検出（missing 0 が合格）。
- `scripts/shoot_all_slides.py slides/index.html`: **全ページスクショの自動撮影**（headless Chrome）。`screenshots/final/` に slide_001.png〜 を並べ、俯瞰QA（同型連続・余白崩れ・文字はみ出し）に使う。手動で#1,#2…と撮る作業を置き換える。

## レビュー質問

- これは誰のどんな悩みに答えているか。
- 受け手は最初の30秒/300字で読む理由が分かるか。
- 数字、価格、日付、URLに根拠があるか。
- 出力されたファイルを人間がそのまま編集できるか。
- 外部に出してはいけない情報が混ざっていないか。
- 今回うまくいった判断基準を次回も使える形で残したか。

## 引き継ぎ文テンプレ

```md
完成しました。
主な成果物は以下です。

- [成果物1]
- [成果物2]
- [成果物3]

今回の判断ポイント:
-

未確認:
-

次にやるなら:
-
```

## 失敗時の立て直し

- 出力が薄い: 入力情報が少ないか、受け手の悩みが定義できていない。10問に戻る。
- 構成が弱い: 結論、理由、具体例、証拠、次アクションに分け直す。
- 見た目が弱い: 表、比較、ステップ、スクショ、図解、余白設計のどれが足りないか見る。
- 事実が怪しい: 断定をやめ、未確認事項に移す。
- 再現性が低い: 完成物ではなく判断基準を `knowledge/` に残す。
