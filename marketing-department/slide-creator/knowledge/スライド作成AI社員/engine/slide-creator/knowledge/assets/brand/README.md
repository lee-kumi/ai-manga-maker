# ブランドアセット（HTMLスライド共通）

新規HTMLスライドデッキを作るとき、必ずここから `assets/` へコピーして使う。

## ファイル一覧

| ファイル | 説明 | 使いどころ |
|----------|------|-----------|
| `brand-logo.png` | ブランドロゴ（黒、透過背景） | 表紙左上、クロージング中央（暗背景では `filter: brightness(0) invert(1)` で白反転） |
| `speaker-photo.png` | 講師の登壇写真 | 表紙右ビジュアル、自己紹介スライド、画像左+テキスト右テンプレートの左画像 |

## 使い方

```bash
# デッキの assets/ にコピー
cp brand-assets/brand-logo.png  <出力先>/assets/brand-logo.png
cp brand-assets/speaker-photo.png <出力先>/assets/speaker-photo.png
```

HTML での参照例:
```html
<!-- 表紙ロゴ -->
<img src="assets/brand-logo.png" alt="ブランド" class="cover-logo">

<!-- 表紙右ビジュアル（人物写真） -->
<div class="html-tpl-cover-right" style="background-image: url('assets/speaker-photo.png'); background-size: cover; background-position: center top;"></div>

<!-- クロージングロゴ（白反転） -->
<img src="assets/brand-logo.png" alt="ブランド" class="closing-logo">
```

## CSS クラス

```css
.cover-logo {
  width: 12vw;
  height: auto;
  margin-bottom: 2.5vw;
  object-fit: contain;
}

.closing-logo {
  width: 10cqw;
  height: auto;
  margin: 0 auto 2cqw;
  filter: brightness(0) invert(1);
  object-fit: contain;
}
```

## 追加するとき

新しいアセットを追加したら、このファイルと `../SKILL.md` のブランドアセット表を両方更新する。
