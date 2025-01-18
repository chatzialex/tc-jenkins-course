#!/usr/bin/env python3
import unittest
import rospy

class TestDroneSim(unittest.TestCase):
    def setUp(self):
        rospy.init_node('test_drone_sim', anonymous=True)

    def test_topics_exist(self):
        topics_to_check = [
            "/drone/takeoff",
            "/drone/gt_pose",
            "/drone/land"
        ]

        master = rospy.get_master()
        _, _, state = master.getSystemState()

        published_topics = {sublist[0] for sublist in state[0]}
        subscribed_topics = {sublist[0] for sublist in state[1]}
        active_topics = published_topics.union(subscribed_topics)

        for topic in topics_to_check:
            with self.subTest(topic=topic):
                self.assertIn(topic, active_topics,
                              f"Topic '{topic}' is neither published nor subscribed!")

if __name__ == "__main__":
    unittest.main()
