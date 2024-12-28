#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

rclpy.init()
node = Node("tax_talker")
pub = node.create_publisher(String, "tax_info", 10)

# 消費税が変わった年と税率
tax_changes = [
    {"year": 1989, "rate": 3, "note": "消費税導入"},
    {"year": 1997, "rate": 5, "note": "初の増税"},
    {"year": 2014, "rate": 8, "note": "二度目の増税"},
    {"year": 2019, "rate": 10, "note": "三度目の増税"}
]

#データ生成用
current_rate = 0
current_year = tax_changes[0]["year"] # 開始の年
index = 0

def get_tax_data(year):
    global current_rate
    # 税率変更のチェック
    for change in tax_changes:
        if change["year"] == year:
            current_rate = change["rate"]
            return {"year": year, "rate": current_rate, "note": change["note"]}
    # そのままの年
    return {"year": year, "rate": current_rate, "note": "そのままです。"}


def cb():
    global current_year, index
    msg = String()
    data = get_tax_data(current_year)
    msg.data = f'{data["year"]}:{data["rate"]}:{data["note"]}'
    pub.publish(msg)
    node.get_logger().info(f'Published tax info: {msg.data}')
    current_year += 1  # 次の年に進む


def main():
    node.create_timer(0.5, cb)  # 0.5秒ごとに次の年を送信
    rclpy.spin(node)
