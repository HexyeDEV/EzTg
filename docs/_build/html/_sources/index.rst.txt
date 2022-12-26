.. EzTg documentation master file, created by
   sphinx-quickstart on Mon Dec 26 23:10:21 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to EzTg's documentation!
================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Quick Start
===========
This is a quick start guide to get you started with EzTg.::

   from EzTg import EzTg
   import asyncio

   bot = EzTg("TOKEN")

   async def on_message(update):
      message = update["message"]
      if message["text"] == "/start":
         await bot.sendMessage(chat_id=smessage["chat"]["id"], text="Hello World!")
   
   async def main()
      await bot.start_polling(on_message)
   
   if __name__ == "__main__":
      asyncio.run(main())

How to use the send method
--------------------------
Here is a little example of using the send method.::

   from EzTg import EzTg
   import asyncio

   bot = EzTg("TOKEN")

   async def on_message(update):
      message = update["message"]
      if message["text"] == "/start":
         await bot.send("sendMessage", chat_id=smessage["chat"]["id"], text="Hello World!")
   
   async def main()
      await bot.start_polling(on_message)
   
   if __name__ == "__main__":
      asyncio.run(main())s

Here the send method has been used tho send a message. You can use the send method for any method of the telegram api and can be useful for example if such method is not yet implemented in EzTg.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
