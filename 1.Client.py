#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
2. Розробіть сокет сервер з використанням бібліотеки азупсіо. Сервер
повинен приймати два числа і проводити над ними прості арифметичні
функції - додавання, віднімання та множення - з використанням
користувацьких функцій, які працюватимуть у асинхронному режимі.
'''
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
mynum = [8,4]
sock.send(bytes(mynum))
print(mynum)
data = sock.recv(1024)
print(data)
sock.close()


# In[ ]:




