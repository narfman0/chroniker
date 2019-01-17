import unittest
from chroniker import main

START_PATH = "tests/fixtures/smb3_warpless_start1.png"
END_PATH = "tests/fixtures/smb3_warpless_end1.png"
VIDEO_PATH = "tests/fixtures/smb3_warpless_clip1.mp4"


class TestMain(unittest.TestCase):
    def test_match_image(self):
        image = main.read_image(START_PATH)
        kp2, des2 = main.train_model(image)
        for frame in main.generate_frames_from_video(VIDEO_PATH):
            kp1, des1 = main.train_model(frame)
            main.match_image(frame, image, des1, des2, kp1, kp2)
