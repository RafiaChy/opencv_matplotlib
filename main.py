import cv2
import matplotlib.pyplot as plt

img = cv2.imread('baboon.jpg', 1)
building = cv2.imread('building.jpg', 1)
building = cv2.cvtColor(building, cv2.COLOR_BGR2RGB)

butterfly = cv2.imread('butterfly.jpg', 1)
butterfly = cv2.cvtColor(butterfly, cv2.COLOR_BGR2RGB)

gradient = cv2.imread('gradient.png', 1)
gradient = cv2.cvtColor(gradient, cv2.COLOR_BGR2RGB)

happyFish = cv2.imread('HappyFish.jpg', 1)
happyFish = cv2.cvtColor(happyFish, cv2.COLOR_BGR2RGB)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

images = [img, happyFish, butterfly, butterfly, gradient]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(images[i])


plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()