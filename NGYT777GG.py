import time
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# Your bot API details
api_id = 20284828   # Your API ID
api_hash = 'a980ba25306901d5c9b899414d6a9ab7'  # Your API Hash
bot_token = '8060132352:AAFWgHhvHPBU5n_OM-_uixBl-q0qm4l4_zk' #Bot Token
channel_username = 'HMT_guri'  # Replace with your Target channel username
# BOT MADE BY @NGYT777GG

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

async def remove_all_members():
    try:
        
        channel = await client.get_entity(channel_username)

        
        participants = await client(GetParticipantsRequest(
            channel=channel,
            filter=ChannelParticipantsSearch(''),
            offset=0,
            limit=1000000,  
            hash=0
        ))

        for member in participants.participants:
            
            if hasattr(member, 'admin_rights'):
                print(f"Skipping {member.user_id} (Owner/Admin)")
                continue

            try:
                
                await client.kick_participant(channel, member.user_id)
                print(f"Removed {member.user_id} from the channel")
                time.sleep(1)  
            except Exception as e:
                print(f"Failed to remove {member.user_id}: {e}")

    except Exception as e:
        print(f"Error fetching members: {e}")


with client:
    client.loop.run_until_complete(remove_all_members())
