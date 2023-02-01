#Importing Image
image = imread("./images/kittens.jpg",as_gray=True)

#Resizing Image
image = resize(image,(1000,1000))

#Showing Image
fig = plt.figure(figsize=(7,7))
plt.grid(True)
plt.imshow(image,cmap=plt.cm.gray)

#Making tiles shapes, shuffling the image and putting it all together
image_shape = (200,200)
image_blocks_original = view_as_blocks(image,block_shape=image_shape)

image_blocks = image_blocks_original
image_blocks = image_blocks.reshape((-1,) + image_shape)

np.random.shuffle(image_blocks)
image_montage = montage2d(image_blocks)

#Showing Shuffle Image
fig = plt.figure(figsize=(7,7))
plt.imshow(image_montage,cmap=plt.cm.gray)