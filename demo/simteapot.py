# -*- coding: utf-8 -*-

"""
一个简单的opengl茶壶
"""

from OpenGL.GL import *
from OpenGL.GLUT import *

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(0.1, 0, 5, 0)
    glutWireTeapot(0.5)
    glFlush()


#使用glut初始化OpenGL
glutInit()
#显示模式:GLUT_SINGLE无缓冲直接显示|GLUT_RGBA采用RGB(A非alpha)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
# 窗口默认位置
glutInitWindowPosition(0, 0)
# 窗口大小
glutInitWindowSize(400, 400)
glutCreateWindow(b"first")
#调用函数绘制图像
glutDisplayFunc(drawFunc)
glutIdleFunc(drawFunc)
#主循环
glutMainLoop()