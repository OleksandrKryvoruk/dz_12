#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
2. Розробіть сокет сервер з використанням бібліотеки азупсіо. Сервер
повинен приймати два числа і проводити над ними прості арифметичні
функції - додавання, віднімання та множення - з використанням
користувацьких функцій, які працюватимуть у асинхронному режимі.
'''

import socket
import asyncio
import nest_asyncio
nest_asyncio.apply()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    answer1 = data[0]
    answer2 = data[1]
   
    async def plus():
        sum1 = answer1 + answer2
        await asyncio.sleep(3)
        print("plus called")
        return sum1
        
    async def minus():
        sum2 = answer1 - answer2
        await asyncio.sleep(3)
        print("minus called")
        return sum2
        
    async def multiple():
        sum3 = answer1 * answer2
        await asyncio.sleep(3)
        print("multiple called")
        return sum3
      
    async def answer():
        print("answer called")
        await asyncio.sleep(3)
        conn.send(bytes(f"Server: You sent {answer1} and {answer2}: {answer1} + {answer2} = {await plus()} -> {answer1} - {answer2} = {await minus()} -> {answer1} * {answer2} = {await multiple()}", encoding='UTF-8'))                
        print("answer sent")
        
    loop = asyncio.new_event_loop()
    loop.run_until_complete(answer())


# In[ ]:




