import numpy as JS
import matplotlib.pyplot as plt

'''

theta = JS.arange(0, 2 * JS.pi, 0.02)
plt.subplot(121, polar=True)
plt.plot(theta, 1.6 * JS.ones_like(theta), linewidth=2)
plt.plot(3 * theta, theta / 3, "--", linewidth=2)
plt.subplot(122, polar=True)
plt.plot(theta, 1.4 * JS.cos(5 * theta), "--", linewidth=2)
plt.plot(theta, 1.8 * JS.cos(4 * theta), linewidth=2)
plt.rgrids(JS.arange(0.5, 2, 0.5), angle=45)
plt.thetagrids([0, 45])
plt.savefig("D:/ring.png")
plt.show()
'''


'''
plt.figure(figsize=(8, 4))
x = JS.random.random(100)
y = JS.random.random(100)
plt.plot(x, y, "o")
plt.scatter(x, y, s=x * 1000, c=y, marker=(5, 1), alpha=0.8, lw=2, facecolors="none")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.savefig("D:/draw.png")
plt.show()

'''
