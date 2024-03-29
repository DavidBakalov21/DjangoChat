from channels.consumer import AsyncConsumer
import json

class YourConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({"type": "websocket.accept"})
        await self.send({
            "type": "websocket.send",
            "text": "You have joined the chat."
        })

    async def websocket_receive(self, text_data):
        data = json.loads(text_data['text'])
        message = data['text']
        room = data['room']
        await self.send_group(room, message)

    async def websocket_disconnect(self, event):
        user = self.scope['user']
        room_name = f"chat_{user.id}"
        await self.channel_layer.group_discard(room_name, self.channel_name)



    async def chat_message(self, event):
        print(event)
        message = event['text']
        print(message)
        await self.send({
            "type": "websocket.send",
            "text": message
        })


    async def send_group(self, group_name, message):
        await self.channel_layer.group_add(group_name, self.channel_name)
        await self.channel_layer.group_send(
            group_name,
            {
                'type': 'chat.message',
                'text': message,
            }
        )