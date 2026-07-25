# 06-template-library-schema.md

参考スライドをテンプレート化する時は、完成HTMLをコピーするのではなく、用途別の抽象情報にする。

```json
{
  "template_id": "T-001",
  "family": "proof_wall",
  "source_image": "references/slide-001.png",
  "best_for": "実績・成果物・スクショを大量に見せる",
  "slots": ["kicker", "main_message", "proof_images", "caption", "logo"],
  "visual_rules": [
"証拠画像の比率を壊さない",
"見出しは1メッセージに絞る",
"画像枚数が多い場合は余白を均等にする"
  ],
  "avoid": [
"文言の丸コピー",
"実案件の固有名詞の流用",
"画像を無理にトリミングする"
  ]
}
```

## family一覧

- `cover`: 表紙
- `profile`: 自己紹介
- `proof`: 実績
- `question`: 問いかけ
- `theory`: 理論図解（方程式・3層など）
- `metaphor`: 例え話
- `comparison`: 比較（2カード・Before/After）
- `comparison_table`: 比較表（自力 vs 伴走 などの行列テーブル）
- `timeline`: ロードマップ／タイムライン（◯週間の進み方を横並びフェーズで）
- `pain`: 受講者の現状課題（痛みグリッド）
- `formula`: 方程式・フレームワーク（A = X × Y × Z）
- `faq`: よくある不安／反論処理
- `pricing`: 価格・条件（大数字1主張）
- `proof_wall`: 大量証拠
- `section_bridge`: 章扉
- `closing`: 商品説明/CTA

## 選び方

1. そのスライドの役割を決める。
2. 役割に合う family を選ぶ。
3. 参考スライドの文言ではなく構図を抽象化する。
4. 今回の素材に合わせて比率を守って配置する。
5. スクショQAで破綻を直す。
