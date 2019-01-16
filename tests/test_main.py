import unittest
from chroniker import main

END_PATH = "tests/fixtures/smb3_warpless_end1.png"
VIDEO_PATH = "tests/fixtures/smb3_warpless_clip1.mp4"


class TestMain(unittest.TestCase):
    def test_match_image(self):
        detector = main.create_detector()
        image = main.read_image(END_PATH)
        kp2, des2 = main.train_model(image, detector)
        for frame in main.generate_frames_from_video(VIDEO_PATH):
            kp1, des1 = main.train_model(frame, detector)
            main.match_image(frame, image, des1, des2, kp1, kp2)
