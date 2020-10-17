# -*- coding: utf-8 -*-

"""
简单窗口程序
可以创建一个窗口，此窗口可以关闭
窗口中存在一个可以根据按键进行旋转的方块
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import OpenGL.GL as OGLGL

from utils import color

class Window(object):
    """
    绘图窗口
    """
    DIMENSION_ROTATE = 5
    DIMENSION_TRANSLATE = 1
    DIMENSION_EYE = 10
    window = None # 全局窗口对象
    W_H = (1000, 800)

    def __init__(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)
        glutInitWindowSize(*Window.W_H)
        glutInitWindowPosition(400, 400)
        Window.window = glutCreateWindow("simple")
        glutDisplayFunc(self.drawGLScene)
        glutIdleFunc(self.drawGLScene)
        glutReshapeFunc(self.reSizeGLScene, 800, 600)

        glutKeyboardFunc(self.key_listener)
        glutSpecialFunc(self.key_listener)

        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)

        #启用0号光源
        glEnable(GL_LIGHT0)

        x, y, z = color.COLOR_BLACK
        # 设置背景颜色
        glClearColor(x, y, z, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearDepth(1.0)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(Window.W_H[0])/float(Window.W_H[1]), 0.1, 200.0)

        glutMainLoop()

    def reSizeGLScene(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def drawGLScene(self):
        """
        逻辑
        :return:
        """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)

        glFlush()

    def key_listener(self, key, x, y):
        """
        键盘事件监听
        :param key:
        :param x:
        :param y:
        :return:
        """
        pass

def main():
    w = Window()

if __name__ == "__main__":
    main()