import cv2
from matplotlib import pyplot as plt

from chroniker import util

logger = util.create_logger(__name__)


def read_image(path):
    return cv2.imread(path, 0)


def train_model(img):
    """ Train a model based on the image
    returns: keypoints, descriptors tuple
    """
    fast = cv2.FastFeatureDetector_create(threshold=60, nonmaxSuppression=False)
    kp = fast.detect(img, None)
    freak = cv2.xfeatures2d.FREAK_create()
    des = freak.compute(img, kp)[1]
    return kp, des


def generate_frames_from_video(video_path):
    """ Return a generator representing each frame in video """
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 1
    while success:
        success, image = vidcap.read()
        logger.debug(f"Read new frame #{count}: {success}")
        count += 1
        yield image


def match_image(img1, img2, des1, des2, kp1, kp2, flann=True):
    """ Given the descripters from model, does image match """
    if flann:
        matches = match_flann(des1, des2)
    else:
        matches = match_bruteforce(des1, des2)
    # Need to draw only good matches, so create a mask
    matches_mask = [[0, 0] for i in range(len(matches))]
    # ratio test as per Lowe's paper
    try:
        for i, (m, n) in enumerate(matches):
            if m.distance < 0.7 * n.distance:
                matches_mask[i] = [1, 0]
    except Exception as e:
        logger.error(f"Received exception in match enumeration: {e}")
        return
    return matches, matches_mask


def draw_matches(img1, kp1, img2, kp2, matches, matches_mask):
    draw_params = dict(
        matchColor=(0, 255, 0),
        singlePointColor=(255, 0, 0),
        matchesMask=matches_mask,
        flags=0,
    )
    img = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)
    plt.imshow(img), plt.show()


def match_bruteforce(des1, des2):
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    return bf.match(des1, des2)


def match_flann(des1, des2):
    FLANN_INDEX_LSH = 6
    index_params = dict(
        algorithm=FLANN_INDEX_LSH, table_number=6, key_size=12, multi_probe_level=2
    )
    search_params = dict(checks=50)  # or pass empty dictionary
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    return flann.knnMatch(des1, des2, k=2)
