from email.generator import Generator
import cv2
from typing import Iterator, Tuple


def SlidingWindow(image: cv2.Mat, slideSize: Tuple[int, int]) -> Iterator[Tuple[cv2.Mat, int, int]]:
    for y in range(0, image.shape[0], slideSize[1]):
        if y + slideSize[1] > image.shape[0]: break   
        for x in range(0, image.shape[1], slideSize[0]):
            if x + slideSize[0] > image.shape[1]: break      
            yield (image[y: y + slideSize[1], x: x + slideSize[0]], x, y + slideSize[1])

if __name__ == "__main__":
    image = cv2.imread("SNAP-165320-0073.jpg")
    for i, slide in enumerate(SlidingWindow(image, (256, 256))):
        boundingBox = (slide[1], slide[2])
        cv2.imwrite(f"test/slide_{i}_{boundingBox[0]}_{boundingBox[1]}.png", slide[0])
