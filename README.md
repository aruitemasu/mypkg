# 日本の税金の歴史
[![test](https://github.com/aruitemasu/ros2/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/aruitemasu/ros2/actions/workflows/test.yml)

ロボットシステム学の課題2で作成したROS2のパッケージです。

# 機能

- 日本の税金の歴史について0.5秒ごとに税金が始まってから1年ずつ経過していき、税金が上がったタイミングを教えてくれます。

# 必要なソフトウェア

- Python 3.8以上
- ROS 2 foxy

# テスト環境
- Ubuntu 22.04.5 LST

# ファイルの構成
## zeikinnノード
- ```zeikinn.py```:実行したらパブリッシュしたトピック情報が動き出すノード

### パブリッシュ トピックス
- tax_info(std_msgs.msg/String)
  - 税金が始まった年から税率のパーセントが増税したことや税率がそのままになっていることがわかるデータ

## rekishiノード(テスト用のノード)
- ```rekishi.py```:このノードは、テスト用であり実行したら```zeikinn.py```の日本の税金の歴史についての情報を受け取たことを確認するためのノード

# 導入方法
- 1 このリポジトリをクローンします。

```
git clone https://github.com/aruitemasu/ros2
```

- 2 この```ros2_ws```のデイレクトリに移動してから```rekishi.py```を実行して違う端末で```zeikinn.py```を実行してください。

```
cd ros_ws
ros2 run mypkg rekishi
```
違う端末
```
cd ros_ws
ros2 run mypkg zeikinn
```

# 使用方法

- 入力方法1

```ros2 run mypkg <スクリプト名>```からの実行をして次に違う端末でまた```ros2 run mypkg <スクリプト名>```で日本の税金の歴史についてのノードが出てきます。

```
cd ros2_ws
ros2 run mypkg <スクリプト名>
```

例

```
cd ros2_ws
ros2 run mypkg rekishi
###実行結果###

###実行結果(zeikinn.py)を実行した後###
[INFO] [1735887670.542955281] [tax_listener]: 1989年に消費税が3%になりました(消費税導入)。
[INFO] [1735887671.013672370] [tax_listener]: 1990年は消費税が3%のままです。
.
.
.
```

違う端末

```
cd ros2_ws
ros2 run mypkg zeikinn
###実行結果###
[INFO] [1735887670.543555798] [tax_talker]: Published tax info: 1989:3:消費税導入
[INFO] [1735887671.011828304] [tax_talker]: Published tax info: 1990:3:そのままです。
.
.
.
```

- 入力方法2

```ros2 run mypkg zeikinn```を実行してから次に違い端末で```ros2 topic list```をいれたら3つのリストが出てくるので自分で使ったものを選択し、```ros2 topic echo /tax_info```でデータの実行結果が出てきます。

例
```
cd ros_ws
ros2 run mypkg zeikinn
###実行結果###
[INFO] [1735887670.543555798] [tax_talker]: Published tax info: 1989:3:消費税導入
[INFO] [1735887671.011828304] [tax_talker]: Published tax info: 1990:3:そのままです。
.
.
.
```
違う端末
```
cd ros2_ws
ros2 topic echo /tax_info
###実行結果###
data: 1989:3:消費税導入
---
data: 1990:3:そのままです。
---
.
.
.
```

# ライセンスと著作権

このソフトウェアパッケージは3条項BSDライセンスの下、最頒布および使用が許可されています。

© 2024 Katsumi Sunahara

