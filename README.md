# 日本の税金の歴史
[![test](https://github.com/aruitemasu/ros2/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/aruitemasu/ros2/actions/workflows/test.yml)

ロボットシステム学の課題2で作成したROS2のパッケージです。

# 機能

- 日本の税金の歴史について0.5秒ごとに税金が始まってから1年ずつ経過していき、税金が上がったタイミングを教えてくれます。

# 必要なソフトウェア
- ROS 2 Humble

# テスト環境
- Ubuntu 22.04.5 LTS

# ファイルの構成
## zeikinnノード
- ```zeikinn```:西暦と税率と消費税の変化についてパブリッシュするノード

### Published Topics
- tax_info(std_msgs.msg/String)
  - 西暦と税率と消費税の変化

## rekishiノード(テスト用のノード)
- ```rekishi```:このノードは、テスト用であり実行したら```zeikinn```の日本の税金の歴史についての情報を受け取たことを確認するためのノード

# 使用方法

- 入力方法1

```
cd ros2_ws
ros2 run mypkg <スクリプト名>
```

例

```
ros2 run mypkg rekishi
###別のターミナルで```ros2 run mypkg zeikinn```を実行した後###
[INFO] [1735887670.542955281] [tax_listener]: 1989年に消費税が3%になりました(消費税導入)。
[INFO] [1735887671.013672370] [tax_listener]: 1990年は消費税が3%のままです。
.
.
.
```

- 入力方法2

例
```
ros2 run mypkg zeikinn
```
別のターミナル
```
ros2 topic echo /tax_info
###実行結果###
data: 1989:3:消費税導入
---
data: 1990:3:そのままです。
---
data: 1991:3:そのままです。
---
data: 1992:3:そのままです。
---
data: 1993:3:そのままです。
---
data: 1994:3:そのままです。
---
data: 1995:3:そのままです。
---
data: 1996:3:そのままです。
---
data: 1997:5:初の導入
---
data: 1998:5:そのままです。
---
.
.
.
```

# ライセンスと著作権

このソフトウェアパッケージは3条項BSDライセンスの下、再頒布および使用が許可されています。

© 2024 Katsumi Sunahara

