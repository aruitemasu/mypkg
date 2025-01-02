# 日本の税金の歴史コマンド
[![test](https://github.com/aruitemasu/ros2/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/aruitemasu/ros2/actions/workflows/test.yml)

このリポジトリは、ros2を使って日本の税金の歴史についてのプログラムになります。

# 機能

- ```zeikinn.py```を実行したら次に違うタブで```rekishi.py```を実行します。
- 両方実行したら、パブリッシャがトピックに情報を出します。
- test.bashで実行したら一緒にパブリッシャが出てくる。

# 必要なソフトウェア

- python3

# テスト環境
-Ubuntu 20.04 LST

# ファイルの構成
- ```zeikinn.py```:
- ```rekishi.py```:
- ```test.bash```:

# 導入方法
- 1.このリポジトリをクローンします。

```
git clone https://github.com/aruitemasu/ros2.git
```

- 2.ros2_wsのデイレクトリに移動してから./test.bashを実行してください。

```
cd ros_ws/src/mypkg/test
```

# 使用方法
プログラムの動作
- 入力方法

直接実行するros2スクリプトを使用して日本の税金の歴史についてのノードが出てきます。

```
./test.bash
```


例

```

```

# ライセンスと著作権

このソフトウェアパッケージは3条項BSDライセンスの下、最頒布および使用が許可されています。

© 2024 Katsumi Sunahara

