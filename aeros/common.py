DISPLAY_DIMENSIONS = (800, 800)

def flipy(y):
    """Small hack to convert chipmunk physics to pygame coordinates"""
    return -y+DISPLAY_DIMENSIONS[1]
