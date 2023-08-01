import asyncio

from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup

from bot_filters import ReplyStatusFilter, KeyWorldFilter
from bot_utils import send_message_to_discord


router: Router = Router()



class FsmForm(StatesGroup):
    message_id = State()
    reply_status = State()


@router.message(KeyWorldFilter())
async def take_message(message: Message, state: FSMContext):
    print('active false status')
    await state.update_data(message_id=message.message_id)
    await state.update_data(reply_status=False)
    await asyncio.sleep(10)
    data = await state.get_data()
    reply_status = data['reply_status']
    if not reply_status:
        await send_message_to_discord(f'{message.chat.title} {message.from_user.username}\n'
                                      f'{message.text}')


@router.message(ReplyStatusFilter())
async def reply_status_change(state: FSMContext):
    await state.update_data(reply_status=True)


