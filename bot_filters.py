from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot_data import keyword_list



class ReplyStatusFilter(BaseFilter):

    async def __call__(self, message: Message, state: FSMContext) -> bool:
        datafsm = await state.get_data()
        try:
            if 'message_id' in datafsm and message.reply_to_message.message_id == datafsm['message_id']:
                return True
            else:
                return False
        except AttributeError:
            return False




class KeyWorldFilter(BaseFilter):

    async def __call__(self, message: Message) -> bool:
        test_str = message.text.split()
        result = list(set(keyword_list) & set(test_str))
        if result:
            return True
        else:
            return False