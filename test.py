from logic_functions import find_board
import cv2

test_image_through_find_board = find_board("test_image.jpg")

cv2.imread(test_image_through_find_board)