#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().run_line_magic('cd', '"C:\\Users\\My Laptop\\Desktop\\KULIAH SEMESTER 5\\SISMUL\\UAS"')


# In[59]:


from IPython.display import Image
from PIL import Image, ImageDraw
from datetime import datetime
import time
from __future__ import print_function
import os
from PIL import ImageFilter
import cv2


# In[15]:


#NOMOR SATU


#KONFIGURASI WAKTU
ts = time.time()
#PENYESUAIAN FORMAT WAKTU
waktu = datetime.fromtimestamp(ts).strftime("%d/%m/%Y %H:%M:%S")

#KONFIGURASI ISI TEKS YANG BERISIKAN NIM, NAMA, TANGGAL DAN WAKTU, DAN INOVASI PENAMBAHAN TULISAN
teks = ("18218024 - Yonatan Jori Saputro \n"+ str(waktu) + "\n" + "UAS II3150 18218024" )

#KONFIGURASI GAMBAR TAMBAHAN BERISI TEKS
addedimage = Image.new('RGB', (200, 60), color = (73, 109, 137))

#KONFIGURASI ISI DARI GAMBAR YANG BERISI GAMBAR
fill = ImageDraw.Draw(addedimage)
fill.text((10,10), teks, fill=(255,255,0))

#PENYIMPANAN GAMBAR TAMBAHAN KE DIRECTORY
addedimage.save('addedimage.png')

#LISTING GAMBAR YANG AKAN DIGUNAKAN DALAM GIF
images = ["18218024_Yonatan Jori Saputro.png", "addedimage.png"]

#MENAMBAHKAN FRAME
frames = []
for i in images:
    new_frame = Image.open(i)
    frames.append(new_frame)

#MENYIMPAN GIF YANG ADA DENGAN KONFIGURASI TERTENTU
frames[0].save('nomor_1_18218024.gif', format='GIF',
    append_images=frames[1:],
    save_all=True,
    duration=300, loop=0)


# In[51]:


#NOMOR DUA


#KONFIGURASI GAMBAR YANG AKAN DIGUNAKAN (DARI NOMOR SATU)
img1 = Image.open("18218024_Yonatan Jori Saputro.png")
img2 = Image.open("addedimage.png")

#KONFIGURASI UKURAN GAMBAR YANG AKAN DIGUNAKAN 
x1 = 0
y1 = 0
w1, h1 = img1.size

x2 = 300
y2 = 350
w2, h2 = img2.size

#MEMBUAT GAMBAR BARU YANG BERISIKAN TEMPELAN DARI DUA GAMBAR
result = Image.new("RGB", (w1, h1))
result.paste(img1, (x1, y1, x1 + w1, y1 + h1))
result.paste(img2, (x2, y2, x2 + w2, y2 + h2))

result.save(os.path.expanduser('nomor_2_1_18218024.png'))

#KONFIGURASI FILTER EMBOSSING PADA GAMBAR BARU
imageObject = Image.open("nomor_2_1_18218024.png")

imageEmboss = imageObject.filter(ImageFilter.EMBOSS)

imageEmboss.save(os.path.expanduser('nomor_2_18218024.png'))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[49]:


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os

#KONFIGURASI FUNGSI PENGUBAH GAMBAR MENJADI NILAI HEXA RGB-NYA
def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

#MEMBUKA GAMBAR SEBELUM FILTER UNTUK DIANALISIS
image = cv2.imread('nomor_2_1_18218024.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#JUMLAH GAMBAR DALAM PIE CHART
number_of_colors = 8

#KONFIGURASI GAMBAR
modified_image = image.reshape(image.shape[0]*image.shape[1], 3)

clf = KMeans(n_clusters = number_of_colors)
labels = clf.fit_predict(modified_image)

counts = Counter(labels)

center_colors = clf.cluster_centers_

#MENDAPATKAN URUTAN GAMBAR DENGAN ITERASI WARNA PADA GAMBAR 
ordered_colors = [center_colors[i] for i ain counts.keys()]
hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
rgb_colors = [ordered_colors[i] for i in counts.keys()]

#MEMBUAT DAN MENYIMPAN GRAFIK
plt.figure(figsize = (8, 6))
plt.title("Nomor 2 Chart Sebelum Emboss")
plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)
plt.savefig('nomor_2_chart_sebelum.png')


# In[48]:


#MEMBUKA GAMBAR SEBELUM FILTER UNTUK DIANALISIS
image = cv2.imread('nomor_2_18218024.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#JUMLAH GAMBAR DALAM PIE CHART
number_of_colors = 8

#KONFIGURASI GAMBAR
modified_image = image.reshape(image.shape[0]*image.shape[1], 3)

clf = KMeans(n_clusters = number_of_colors)
labels = clf.fit_predict(modified_image)

counts = Counter(labels)

center_colors = clf.cluster_centers_

#MENDAPATKAN URUTAN GAMBAR DENGAN ITERASI WARNA PADA GAMBAR 
ordered_colors = [center_colors[i] for i in counts.keys()]
hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
rgb_colors = [ordered_colors[i] for i in counts.keys()]

#MEMBUAT DAN MENYIMPAN GRAFIK
plt.figure(figsize = (8, 6))
plt.title("Nomor 2 Chart Sesudah Emboss")
plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)
plt.savefig('nomor_2_chart_sesudah.png')


# In[78]:


#NOMOR TIGA


#MEMBUAT GAMBAR RUMAH DENGAN KETERANGAN NAMA DSB
#KONFIGURASI GAMBAR YANG AKAN DIGUNAKAN
img1 = Image.open("Foto_Rumah_18218024.png")
img2 = Image.open("addedimage.png")

#KONFIGURASI UKURAN GAMBAR YANG AKAN DIGUNAKAN 
x1 = 0
y1 = 0
w1, h1 = img1.size

x2 = 300
y2 = 350
w2, h2 = img2.size

#MEMBUAT GAMBAR BARU YANG BERISIKAN TEMPELAN DARI DUA GAMBAR (PEMANDANGAN DAN TULISAN)
result = Image.new("RGB", (w1, h1))
result.paste(img1, (x1, y1, x1 + w1, y1 + h1))
result.paste(img2, (x2, y2, x2 + w2, y2 + h2))

result.save(os.path.expanduser('nomor_3_1_18218024.png'))

#KONFIGURASI GAMBAR YANG AKAN DIGUNAKAN
img3 = Image.open("18218024_Yonatan Jori Saputro.png")
img4 = Image.open("nomor_3_1_18218024.png")


#KONFIGURASI KOMPOSISI ALPHA CHANNEL
#KOMPOSISI SATU (gambar saya 20%)
img3copy1 = img3.copy()
img3copy1.putalpha(51) #~20%

#KOMPOSISI DUA (gambar saya 50%)
img3copy2 = img3.copy()
img3copy2.putalpha(128) #~50%

#KOMPOSISI TIGA (gambar saya 80%)
img3copy3 = img3.copy()
img3copy3.putalpha(204) #~80%


#MEMBUAT DAN MENYIMPAN GAMBAR-GAMBAR BARU YANG TERDIRI DARI 3 KOMPOSISI ALPHA CHANNEL BERBEDA
#KOMPOSISI SATU
img4.paste(img3copy1, (0, 0), img3copy1.convert('RGBA'))
img4.save(os.path.expanduser('nomor_3a_18218024.png'))

#KOMPOSISI DUA
img4.paste(img3copy2, (0, 0), img3copy1.convert('RGBA'))
img4.save(os.path.expanduser('nomor_3b_18218024.png'))

#KOMPOSISI TIGA
img4.paste(img3copy3, (0, 0), img3copy1.convert('RGBA'))
img4.save(os.path.expanduser('nomor_3c_18218024.png'))


# In[85]:


#NOMOR EMPAT


#MENCACAH VIDEO DAN MENGAMBIL SATU BUAH FRAME
vidFrame = cv2.VideoCapture('Video_No 4_18218024.mp4')
success,image = vidFrame.read()
count = 0
while success:
    if count==20:
      cv2.imwrite("No 4_Frame_Diambil_18218024.png", image)     # save frame as JPEG file      
    success,image = vidFrame.read()
    count += 1

#MENAMBAHKAN GAMBAR TEKS PADA GAMBAR FRAME YANG DIAMBIL
#MEMBUAT GAMBAR CAPTURED FRAME DENGAN KETERANGAN NAMA DSB
#KONFIGURASI GAMBAR YANG AKAN DIGUNAKAN
img1 = Image.open("No 4_Frame_Diambil_18218024.png")
img2 = Image.open("addedimage.png")

#KONFIGURASI UKURAN GAMBAR YANG AKAN DIGUNAKAN 
x1 = 0
y1 = 0
w1, h1 = img1.size

x2 = 300
y2 = 350
w2, h2 = img2.size

#MEMBUAT GAMBAR BARU YANG BERISIKAN TEMPELAN DARI DUA GAMBAR (CAPTURED FRAME DAN TULISAN)
result = Image.new("RGB", (w1, h1))
result.paste(img1, (x1, y1, x1 + w1, y1 + h1))
result.paste(img2, (x2, y2, x2 + w2, y2 + h2))

#MENYIMPAN GAMBAR HASIL
result.save(os.path.expanduser('nomor_4_18218024.png'))

