# SPDX-FileCopyrightText: 2023 RIku Okada
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0
node.create_timer(0.5, self.cb)
                                            
def cb():
    global n
    msg = Int16()
    msg.data = n
    pub.publish(msg)
    n += 1

node = Node("talker")
talker = Talker(node)
rclpy.spin(node)
