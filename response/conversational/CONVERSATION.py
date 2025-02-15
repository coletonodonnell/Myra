from characterai import aiocai, sendCode, authUser
from execution.building.main_config import USER_NAME
from audio.AUDIO import Take_Command
from response.RESPONSE import RESPONSE_SYSTEM

import asyncio

CAI_TOKEN = 'TOKEN'

def Run_Conversation():
    
    asyncio.run(Authenticate_CAI())
    asyncio.run(Main_Line())
    
    pass


async def Main_Line():
    
    char = 'b2wN6Mi0D4B6FkeS1DvaM9YJBnwE1Ohdyq_UXvVW4gk'
    client = aiocai.Client(CAI_TOKEN)
    
    me = await client.get_me()
    
    async with await client.connect() as chat:
        new, answer = await chat.new_chat(
            char, me.id
        )
        print('---------------------------------')
        
        RESPONSE_SYSTEM.Custom_Response(f'{answer.text}')
        
        while True:
            #text = input(f'{USER_NAME}: ')
            text = Take_Command()
            
            if text == 'NONE':
                continue
            
            message = await chat.send_message(
                char, new.chat_id, text
            )

            # Say the response
            RESPONSE_SYSTEM.Custom_Response(message.text)
            
    
    pass



async def Authenticate_CAI():
    email = input('YOUR EMAIL: ')

    code = sendCode(email)

    link = input('CODE IN MAIL: ')

    token = authUser(link, email)

    global CAI_TOKEN
    CAI_TOKEN = token
    print(f'YOUR TOKEN: {token}')

    pass