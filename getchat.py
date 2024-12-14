from pyrogram import Client

api_id = '27982348'  # Замените на ваш api_id
api_hash = 'b8046e9be94c4b6c90829dbb0dae1af7'  # Замените на ваш api_hash
chat_identifier = -1001725160790  # Замените на ID или имя пользователя чата

app = Client("my_account", api_id=api_id, api_hash=api_hash)

async def get_chat_info(chat_id):
    async with app:
        chat = await app.get_chat(chat_id)
        print(chat)
        return chat

def main():
    chat_info = app.run(get_chat_info(chat_identifier))
    # print(f"Название чата: {chat_info.title}")
    print(f"ID чата: {chat_info.id}")
    print(f"Тип чата: {chat_info.type}")
    print(f"Участники: {chat_info.members_count}")

if __name__ == "__main__":
    main()
