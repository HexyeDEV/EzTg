.. EzTg documentation master file, created by
   sphinx-quickstart on Mon Dec 26 23:10:21 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

InlineKeyboard Quick Start
==========================

Here is a quick example of how to use EzTg.InlineKeyboard::

    from EzTg import TelegramClient, InlineKeyboard
    import asyncio

    bot = TelegramClient("TOKEN")

    async def on_message(update):
        message = update.message
        if message.text == "/start":
            keyboard = InlineKeyboard()
            keyboard.url("Google", "https://google.com")
            keyboard.callback("Click me", "click1")
            keyboard.url_new_row("GitHub", "https://github.com")
            keyboard.callback_new_row("Click me", "click2")
            await bot.send_message(message.chat.id, "Hello World!", reply_markup=keyboard)
    
    async def on_callback(update):
        callback = update.callback_query
        if callback.data == "click1":
            await bot.send("answerCallbackQuery", callback_query_id=callback.id, text="You clicked the first button!")
        elif callback.data == "click2":
            await bot.send("answerCallbackQuery", callback_query_id=callback.id, text="You clicked the second button!", show_alert=True)
    
    async def main()
        await bot.start_polling(on_message, on_callback)
    
    asyncio.run(main())