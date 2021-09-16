"""
Week 1 practice project template for Python Data Visualization
Load a county-level PNG map of the USA and draw it using matplotlib
"""

import matplotlib.pyplot as plt

# Houston location
HOUSTON_POS = [302, 280]
USA_SVG_SIZE = [555, 352]


def draw_USA_map(map_name):
    """
    Given the name of a PNG map of the USA (specified as a string),
    draw this map using matplotlib
    """

    # Load map image, note that using 'rb'option in open() is critical since png files are binary
    img = plt.imread(map_name,'rb')
    #  Get dimensions of USA map image
    # apparently img dpi in solution is 80. no idea where this is from
    img_dpi = 80
    img_size = img.shape[0:2]
    img_size = img_size[::-1]

    img_px = [i/img_dpi for i in img_size] #resolution agnositic options
    plt.figure(figsize=img_px)
    # Plot USA map
    fig = plt.imshow(img)
    # Plot green scatter point in center of map
    plt.scatter(img_size[0]//2,img_size[1]//2,c='g')

    # Plot red scatter point on Houston, Tx - include code that rescale coordinates for larger PNG files
    plt.scatter(HOUSTON_POS[0] * img_size[0]/USA_SVG_SIZE[0], HOUSTON_POS[1] * img_size[1]/USA_SVG_SIZE[1], c='r')
    pass


# draw_USA_map("USA_Counties_555x352.png")
# draw_USA_map("USA_Counties_1000x634.png")
draw_USA_map(r"assets\week1\USA_Counties_555x352.png")
# draw_USA_map(r"assets\week1\USA_Counties_1000x634.png")
plt.show()
