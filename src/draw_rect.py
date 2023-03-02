import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image


im = Image.open('C:\\ADAI\\Face-Recognition-with-InsightFace\\src\\frame3.jpg')

# Display the image
plt.imshow(im)

# Get the current reference
ax = plt.gca()

rect = patches.Rectangle((556, 203), 620-556, 289-203, linewidth=1, edgecolor='r', facecolor='none')
#442.903	169.676	295.196	544.884
rect_1 = patches.Rectangle((443, 169), 295, 545, linewidth=1, edgecolor='b', facecolor='none')

# Add the patch to the Axes
ax.add_patch(rect)
ax.add_patch(rect_1)

plt.show()