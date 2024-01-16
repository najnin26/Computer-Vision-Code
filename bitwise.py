import cv2 as cv
import numpy as np

blank=np.zeros((400,400), dtype='uint8')
rec=cv.rectangle(blank.copy(), (30,30), (370,370),255,-1)
cir=cv.circle(blank.copy(), (200,200), 200, 255,-1)

cv.imshow('Rectangle', rec)
cv.imshow('Circle', cir)

# bitwise AND --> intersecting regions
bit_AND=cv.bitwise_and(rec, cir)
cv.imshow('And', bit_AND)

# bitwise OR --> non-intersecting and intersecting regions
bit_OR=cv.bitwise_or(rec, cir)
cv.imshow('OR', bit_OR)

# bitwise XOR --> non-intersecting regions
bit_XOR=cv.bitwise_xor(rec, cir)
cv.imshow('XOR', bit_XOR)

# bitwise NOT
bit_NOT=cv.bitwise_not(cir)
cv.imshow('NOT', bit_NOT)

cv.waitKey(0)
cv.destroyAllWindows()