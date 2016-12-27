#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   Graphium
# URL:      http://tehutehu.com
# License:  MIT License
# Created:  2016-12-27
#
import sys
import tkinter as tk
from PIL import Image, ImageTk



class Frame(tk.Frame):
    def imprep(self,fname):
        img = Image.open(fname)
        return [img, ImageTk.PhotoImage(img)]
    def callback(self,event):
        print('x:%d,y:%d' % (event.x, event.y))
        clip_size = self.clip_size
        img = self.rawimg
        w = img.size[0]
        h = img.size[1]
        x = event.x
        y = event.y
        a1x = x - clip_size/2
        a1y = y - clip_size/2
        a2x = x + clip_size/2
        a2y = y + clip_size/2
       
        if x < (clip_size / 2):
            a1x=0
            a2x=clip_size
        if y < (clip_size / 2):
            a1y = 0
            a2y=clip_size
        if x + (clip_size/2) > w:
            a2x = w
            a1x = w - clip_size
        if y + (clip_size/2) > h:
            a2y = h
            a1y = h - clip_size
        try:
            im2 = img.crop((a1x,a1y,a2x,a2y))
            im2.save(self.out_dir + '/' + str(self.ptr)+'.jpg','JPEG')
        except Exception as e:
            print(e)

        self.ptr += 1
        img = self.imprep(self.datalist[self.ptr])
        self.il.configure(image=img[1])
        self.il.image=img[1]
        self.rawimg=img[0]
        
    
    def __init__(self, datalist, clip_size, out_dir, master=None):
        self.datalist = [x.strip() for x in open(datalist).readlines()]
        self.clip_size = clip_size
        self.out_dir = out_dir
        self.ptr = 0

        tk.Frame.__init__(self,master)
        img = Image.open(self.datalist[self.ptr])
        self.rawimg = img
        self.img = ImageTk.PhotoImage(img)
    
        self.il = tk.Label(self,image=self.img)
        self.il.bind('<Button-1>',self.callback)
        self.il.pack()

if __name__ == '__main__':
    import argparse
    ps = argparse.ArgumentParser()
    ps.add_argument('datalist',type=str)
    ps.add_argument('clip_size',type=int)
    ps.add_argument('out_dir',type=str)
    args = ps.parse_args()
    f = Frame(args.datalist, args.clip_size, args.out_dir)
    f.pack()
    f.mainloop()

