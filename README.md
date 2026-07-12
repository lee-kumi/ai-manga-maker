# 🎨 AI漫画ツール集（ai-manga-maker）

Kindle出版のための **AI漫画づくり・表紙づくりを支援するツール集** です。
すべてブラウザだけで動きます。インストール不要・無料。

👉 **使う：https://lee-kumi.github.io/ai-manga-maker/**

## なにができる？

各ツールは「本の情報」や「物語の設計」を入力すると、
**画像生成AI（ナノバナナ・ChatGPT）やテキストAI（Claude・ChatGPT）に貼り付けるプロンプト**を作ってくれます。

| ツール | できること |
|---|---|
| [AI漫画メーカー v2](https://lee-kumi.github.io/ai-manga-maker/v2.html) | 企画 → キャラ・画風 → コマ割り → 画像生成 の4STEPで漫画を設計 |
| [Kindle表紙メーカー](https://lee-kumi.github.io/ai-manga-maker/cover-maker.html) | クリックされやすい表紙案＋画像生成プロンプト（漫画表紙／テキスト本表紙の2種対応） |
| [キャラクターシート生成](https://lee-kumi.github.io/ai-manga-maker/charsheet.html) | 顔ブレ防止用のキャラ設定資料を作る |
| [ストーリー設計アプリ](https://lee-kumi.github.io/ai-manga-maker/story-design.html) | 悩み・本音・壁・カギ・結末で物語を組み立てる |

## 大事な考え方

- **漫画は「絵」ではなく「物語」**。企画を固めてから画像生成へ（詳しくは [docs/manga-maker-rules.md](docs/manga-maker-rules.md)）
- **表紙はアートではなく「広告」**。クリックされることが最優先（詳しくは [docs/cover-maker-rules.md](docs/cover-maker-rules.md)）
- 生成画像に日本語の文字は入れない。**文字は後からCanvaで載せる**（日本語崩れ防止）

## データの保存について

- 入力したデータは**お使いのブラウザの中（localStorage）**にだけ保存されます
- 別の端末には引き継がれません。**「バックアップを保存」で定期的にファイルに書き出してください**

## 開発メモ

- 1ツール＝1つのHTMLファイル（ビルド不要）。作りの約束事は [CLAUDE.md](CLAUDE.md) を参照
- アプリのルールを変えたら `docs/` の対応する文書も同時に更新すること
