# youtube-slide-image-prompt — YouTube用スライド画像プロンプト設計スキル

YouTube動画用スライドに入れる図解画像、比較図、フロー図、マトリクス等の**画像生成AIプロンプトを作成する** Claude Code カスタムスキルです。画像そのものやSlidev本体は生成しません。

## 何をするスキルか

- YouTube台本やスライド案をもとに、1枚ごとの図解画像プロンプトを設計
- 型カタログ（フロー・比較・ピラミッド・マトリクス・リスト・放射・タイムライン・因果関係）から最適な型を選択
- 生成したプロンプトは画像生成AI（gpt-image-2・Skywork等）にそのまま渡せる
- 脱AIデザイン原則に基づき「AIっぽい均一なビジュアル」を回避
- YouTubeスライド本体は `youtube-script-writer/skills/03-presentation-slides/SKILL.md` が担当し、このスキルはその画像生成部分を補助

## セットアップ

### 1. スキルファイルを配置

```bash
git clone https://github.com/kawai-developer/skills_diagram.git
mv skills_diagram ~/.claude/skills/youtube-slide-image-prompt
```

### 2. Claude Code のスキルとして登録

`~/.claude/settings.json` に以下を追加:

```json
{
  "skills": [
    {
      "name": "youtube-slide-image-prompt",
      "path": "~/.claude/skills/youtube-slide-image-prompt/SKILL.md"
    }
  ]
}
```

### 3. 呼び出し

```
/youtube-slide-image-prompt [YouTube台本 or スライド内容 or 画像化したいテーマ]
```

## 使用例

```
/youtube-slide-image-prompt YouTube台本のslide_08を1枚の比較図解にするプロンプトを作って
/youtube-slide-image-prompt Claude CodeとCodexの違いを動画用スライド画像にする
/youtube-slide-image-prompt ~/projects/youtube/slides.md
```

## ファイル構成

```
youtube-slide-image-prompt/
├── SKILL.md              # スキル本体（Claude Codeが読む）
└── knowledge/references/
    ├── diagram-types.md  # 図解型カタログ（D1〜D8）
    ├── anti-ai-design.md # 脱AIデザイン原則
    ├── フロー図_ステップ型.txt
    ├── 比較表_2択.txt
    ├── マトリクス_2x2.txt
    ├── ピラミッド.txt
    ├── ランキング.txt
    ├── タイムライン_横型.txt
    ├── 関係図_ネットワーク.txt
    ├── マインドマップ.txt
    ├── チェックリスト.txt
    ├── ツール比較_分岐型.txt
    ├── 数値比較_棒グラフ.txt
    ├── 用語解説_カード型.txt
    ├── 漫画_4コマ.txt
    ├── 表.txt
    ├── before_after.txt
    └── claude_code_install_guide.md  # 使用例サンプル
```

## 出力ルール

- 出力ファイルには**画像生成AIにそのままペーストできるプロンプトのみ**を記載
- 複数図解は `---` で区切る
- YouTubeスライド案件の場合: `youtube-script-writer/skills/03-presentation-slides/output/<slug>/slide_NN_prompt.txt` または計画ファイル側へ反映
- 記事・SNSなど補助用途の場合: 案件フォルダ側の `図解.md` に保存

## 動作要件

- Claude Code（CLI）
- カスタムスキル機能が有効な環境
