import time
import unittest
from unittest.mock import patch

from chroniker import main, util

START_PATH = "tests/fixtures/smb3_warpless_start1.png"
END_PATH = "tests/fixtures/smb3_warpless_end1.png"
VIDEO_PATH = "tests/fixtures/smb3_clip_begin.mp4"

logger = util.create_logger(__name__)


class TestMain(unittest.TestCase):
    def test_match_image(self):
        start_time = time.time()
        img2 = main.read_image(START_PATH)
        kp2, des2 = main.train_model(img2)
        for frame in main.generate_frames_from_video(VIDEO_PATH):
            kp1, des1 = main.train_model(frame)
            matches, matches_mask = main.match_image(frame, img2, des1, des2, kp1, kp2)
            logger.info(f"Found {len(matches)} matches")
        end_time = time.time()
        logger.info(f"Total time to process video: {end_time - start_time}")

    @patch("chroniker.main.cv2")
    @patch("chroniker.main.plt")
    def test_draw_matches(self, plt, cv2):
        main.draw_matches(None, [], None, [], [], [])
