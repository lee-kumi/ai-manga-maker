# 05-slide-project-structure.md

セミナースライドを作る時は、次の構造で出力する。

```text
YYYY-MM-DD_event-slug/
├── brief.md
├── questions.md
├── story-plan.md
├── source-map.md
├── review-notes.md
├── assets/
│   ├── cover/
│   ├── proof/
│   ├── screenshots/
│   ├── logos/
│   └── video/
├── slides/
│   └── index.html
└── screenshots/
└── final/
    ├── slide-001.png
    ├── slide-002.png
    └── ...
```

## `source-map.md` に必ず書くこと

| slide | message | template_family | source_asset | reason | check |
|---:|---|---|---|---|---|
| 1 | 表紙 | cover | assets/cover/... | イベント期待値を作るため | 比率/文字/CTA |

## `review-notes.md` に必ず書くこと

- 全ページを見て直した箇所
- まだ弱い可能性がある箇所
- 次回固定化するテンプレート
- 次回変えるべき比喩
- ユーザー確認が必要な数字・素材
