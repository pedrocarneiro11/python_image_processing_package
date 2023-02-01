import matplotlib.pyplot as plot


def plot_image(image):
    plot.figure(figsize=(12, 4))
    plot.imshow(image, cmap='gray')
    plot.axis('off')
    plot.show()


def plot_result(*args):
    number_images = len(args)
    fig, axis = plot.subplot(nrows=1, ncols=number_images, figsize=(12, 4))
    names_list = ['image {}'.format(i) for i in range(1, number_images)]
    names_list.append('Result')
    for ax, name, image in zip(axis, names_list, args):
        ax.set_title(name)
        ax.imshow(image, cmap='gray')
        ax.axis('off')
    fig.light_layout()
    plot.show()


def histogram(image):
    fig, axis = plot.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    color_list = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_list)):
        ax.set_title('{} histogram'.format(color.title()))
        ax.hist(image[:, :, index].ravel(), bins=256, color=color, alpha=0.8)
    fig.light_layout()
    plot.show()
