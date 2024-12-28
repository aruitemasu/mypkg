#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

rclpy.init()
node = Node("tax_listener")


def cb(msg):
    data = msg.data.split(":")
    year = int(data[0])
    rate = int(data[1])
    note = data[2]
    if "増税" in note:
        node.get_logger().info(f"{year}年に消費税が{rate}%に上がりました（{note}）。")
    elif "そのまま" in note:
        node.get_logger().info(f"{year}年は消費税が{rate}%のままです。")
    else:
        node.get_logger().info(f"{year}年に消費税が{rate}%になりました（{note}）。")


def main():
    node.create_subscription(String, "tax_info", cb, 10)
    rclpy.spin(node)

