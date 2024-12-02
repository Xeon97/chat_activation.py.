from .. import loader, utils

@loader.tds
class ChatActivationMod(loader.Module):
    """
    Модуль для активации команды и вывода ID чата
    """
    strings = {"name": "ChatActivation"}

    async def botcmd(self, message):
        """
        .bot - активация команды с выводом ID чата
        """
        chat_id = utils.get_chat_id(message)  # Определяем ID текущего чата
        response = f"this is the command activated for this chat this is the command activated for this chat -id {chat_id}"
        await utils.answer(message, response)  # Отправляем сообщение в чат
