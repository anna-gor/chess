
# coding: utf-8

# In[3]:


n = 1000 #размер датасета
path_cropped ='/home/ann/Documents/chess/cropped/' # путь к папке, где находятся фрагменты,из которых создается изображение
path_saved_txt = "/home/ann/Documents/chess/txt/" # путь к папке, куда записываются созданные текстовые файлы с разметкой
path_saved_png = "/home/ann/Documents/chess/png/" # путь к папке, где хранятся созданные изображения


# In[4]:


from PIL import Image
import random


# In[5]:


d = {1: 0, 2:0,
     3:1, 4: 1,
     5:2,6:2, 
     7:3,8:3,
     9:4,10:4,
     11:5,12:5,
     13:6,14:6,
     15:7,16:7,
     17:8,18:8,
     19:9,20:9,
     21:10,22:10,
     23:11,24:11,
     25:12,26:12     
}


# In[6]:


img = Image.new('RGB', (256, 256), 'white')
for glob in range(n):
    f = open(path_saved_txt+str(glob)+".txt", 'w')

    for j in range(8):
        l=[]
        for k in range(8):
            l.append(random.randint(1,26))            
 
        for i in range(8):
            img.paste(Image.open(adr+str(l[i])+'.png'),(i*32,j*32))
            
            f.write(str(d[l[i]]) + '\t')
        f.write('\n')    
    img.save(path_saved_png+str(glob)+".png")
    f.close()

