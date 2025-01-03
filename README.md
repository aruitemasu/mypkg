# 日本の税金の歴史コマンドhttps://github.com/aruitemasu/ros2
[![test](https://github.com/aruitemasu/ros2/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/aruitemasu/ros2/actions/workflows/test.yml)

このリポジトリは、ros2を使って日本の税金の歴史についてのプログラムになります。

# 機能

- ```zeikinn.py```を実行したら次に違う端末で```rekishi.py```を実行します。
- 両方実行したら、日本の税金の歴史についてパブリッシャがトピックに情報を出します。
- ```./test.bash```で実行したら勝手にcolcon biuld され一緒にパブリッシャがトピックに情報を出します。

# 必要なソフトウェア

- Python3.8以上
- ROS 2

# テスト環境
- Ubuntu 20.04 LST

# ファイルの構成
- ```zeikinn.py```:実行したらパブリッシャのトピック情報が動き出すスクリプト
- ```rekishi.py```:```zeikinn.py```を実行したらパブリッシャのトピック情報が動き出すスクリプト
- ```test.bash```:```zeikinn.py```と```rekishi.py```のパブリッシャを一緒にトピックに出し、動作確認をするテスト用のスクリプト

# 導入方法
- 1.このリポジトリをクローンします。

```
git clone https://github.com/aruitemasu/ros2
```

- 2.この```ros2_ws```のデイレクトリに移動してから```rekishi.py```を実行して違う端末で```zeikinn.py```を実行してください。

```
cd ros_ws
ros2 run mypkg rekishi
```
違う端末
```
cd ros_ws
ros2 run mypkg zeikinn
```

- 3.別のやり方 ```ros2_ws/src/mypkg/test```のデイレクトリに移動してから```./test.bash```を実行してください。

```
cd ros_ws/src/mypkg/test
./test.bash
```
# 使用方法
プログラムの動作
- 入力方法1

```ros2 run mypkg <スクリプト名>```からの実行をして次に違う端末でまた```ros2 run mypkg <スクリプト名>```で日本の税金の歴史についてのノードが出てきます。

```
cd ros2_ws
ros2 run mypkg <スクリプト名>
```

例

```
cd ros2_ws
ros2 run mypkg rekishi.py
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
ros2 run mypkg zeikinn.py
###実行結果###
[INFO] [1735887670.543555798] [tax_talker]: Published tax info: 1989:3:消費税導入
[INFO] [1735887671.011828304] [tax_talker]: Published tax info: 1990:3:そのままです。
.
.
.
```

- 入力方法2

```cd ros2_ws/src/mypkg/test```のデイレクトリに移動してから```./test.bash```を使って直接実行し```rekishi.py```と```zeikinn.py```の両方のパブリッシャのトピック情報のノードが出てきます。

例

```
cd ros2_ws/src/mypkg/test
./test.bash
###実行結果###
[rekishi-2] [INFO] [1735886587.475792804] [tax_listener]: 1989に消費税が3%になりました(消費税導入)。
[zeikinn-1] [INFO] [1735886587.476250580] [tax_talker]: Published tax info: 1989:3:消費税導入
.
.
.
[zeikinn-1] [INFO] [1735886605.444142636] [tax_talker]: Published tax info: 2025:10:そのままです。
[zeikinn-1] [INFO] [1735886605.943853745] [tax_talker]: Published tax info: 2026:10:そのままです。
```

# ライセンスと著作権

このソフトウェアパッケージは3条項BSDライセンスの下、最頒布および使用が許可されています。

© 2024 Katsumi Sunahara

