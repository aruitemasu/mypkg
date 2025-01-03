# 日本の税金の歴史コマンド
[![test](https://github.com/aruitemasu/ros2/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/aruitemasu/ros2/actions/workflows/test.yml)

このリポジトリは、ros2を使って日本の税金の歴史についてのプログラムになります。

# 機能

- ```zeikinn.py```を実行したら次に違うタブで```rekishi.py```を実行します。
- 両方実行したら、パブリッシャがトピックに情報を出します。
- ./test.bashで実行したら勝手にcolcon biuld され一緒にパブリッシャのトピックが出てきます。

# 必要なソフトウェア

- python3

# テスト環境
- Ubuntu 20.04 LST

# ファイルの構成
- ```zeikinn.py```:実行したらパブリッシャのトピック情報が動き出すスクリプト
- ```rekishi.py```:```zeikinn.py```を実行したらパブリッシャのトピック情報が動き出すスクリプト
- ```test.bash```:```zeikinn.pyとrekishi.py```のパブリッシャを一緒にトピックに出し、動作確認をするテスト用のスクリプト

# 導入方法
- 1.このリポジトリをクローンします。

```
git clone https://github.com/aruitemasu/ros2
```

- 2.ros2_wsのデイレクトリに移動してからrekishi.pyを実行して違うタブでzeikinn.pyを実行してください。

```
cd ros_ws
ros2 run mypkg rekishi
違うタブ
cd ros_ws
ros2 run mypkg zeikinn
```

- 3.別のやり方 ros2_ws/src/mypkg/testのデイレクトリに移動してから./test.bashを実行してください。

```
cd ros_ws/src/mypkg/test
./test.bash
```
# 使用方法
プログラムの動作
- 入力方法1



- 入力方法2

./test.bashを使った直接実行するros2スクリプトを使用して日本の税金の歴史についてのノードが出てきます。

```
cd ros_ws/src/mypkg/test
./test.bash
```


例

```

```

# ライセンスと著作権

このソフトウェアパッケージは3条項BSDライセンスの下、最頒布および使用が許可されています。

© 2024 Katsumi Sunahara

