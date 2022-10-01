import cv2
import numpy as np
from typing import Iterator, Tuple


def SlidingWindow(image: cv2.Mat, slideSize: Tuple[int, int]) -> Iterator[Tuple[cv2.Mat, int, int]]:
    extraY = image.shape[0] % slideSize[1]
    extraX = image.shape[1] % slideSize[0]
    if extraY != 0:
        extraBlockBottom = np.zeros((slideSize[1] - extraY, image.shape[1], 3), np.uint8)
        image = np.concatenate((image, extraBlockBottom), axis=0)
    if extraX != 0:
        extraBlocRight = np.zeros((image.shape[0], slideSize[0] - extraX, 3), np.uint8)
        image = np.concatenate((image, extraBlocRight), axis=1)
    
    for y in range(0, image.shape[0], slideSize[1]):
        for x in range(0, image.shape[1], slideSize[0]):
            yield (image[y: y + slideSize[1], x: x + slideSize[0]], x, y + slideSize[1])

if __name__ == "__main__":
    image = cv2.imread("SNAP-165320-0073.jpg")
    for i, slide in enumerate(SlidingWindow(image, (256, 256))):
        boundingBox = (slide[1], slide[2])
        cv2.imwrite(f"test/slide_{i}_{boundingBox[0]}_{boundingBox[1]}.png", slide[0])
