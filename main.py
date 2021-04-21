from telethon import TelegramClient, sync
import time
import params


class Storage:
    @staticmethod
    def save_dialog_users_to_file(users_id, filename='target1.txt'):
        with open(filename, 'a') as file:
            users_id_str = [str(user) + "\n" for user in users_id]
            file.writelines(users_id_str)

    @staticmethod
    def get_dialog_users_from_file(filename="target.txt"):
        with open(filename, 'r') as file:
            users = file.readlines()
        return [int(user) for user in users]


class Bot:
    def __init__(self):
        pass

    def get_dialog_id(self, dialog_name):
        pass

    def get_dialog_users(self, dialog_id):
        pass

    def send_message_to_participants(self, users, text_message):
        pass

    def send_individual_message(self, entities, text_message):
        pass

    def __del__(self):
        pass


class TelegramBot(Bot):
    def __init__(self):
        api_id = params.API_ID
        api_hash = params.API_HASH
        phone_number = params.PHONE_NUMBER
        PASS = params.PASS
        self.client = TelegramClient('new1', api_id, api_hash)
        self.client.connect()
        if not self.client.is_user_authorized():
            self.client.start(phone=phone_number, password=PASS)

    def get_dialog_id(self, dialog_name):
        dialogs = self.client.get_dialogs()
        for dialog in dialogs:
            if dialog.name == dialog_name:
                return dialog.entity.id

    def get_dialog_users(self, dialog_id):
        users = self.client.get_participants(dialog_id)
        users_id = [user.id for user in users]
        return users_id

    def send_message_to_participants(self, users, text_message):
        i = 0
        for user in users:
            self.client.send_message(user, text_message)
            print("Message was sent")
            time.sleep(1)
            i += 1
        print("Message was sent to {} members".format(i))

    def send_individual_message(self, entities, text_message):
        for entity in entities:
            self.client.send_message(entity, text_message)
        print("Done")

    def __del__(self):
        self.client.disconnect()
        print("Bot was disconnected")


if __name__ == "__main__":
    message = "Добрый день! Увидела Вас в чате, @mamapapa_chat, эта статья меня просто поразила. Оказывается солнцезащитный крем так влияет на наше здоровье, и здоровье наших детей. \n https://www.instagram.com/p/CNpFfRLL5Z2/"
    client = TelegramBot()
    dialog_id = client.get_dialog_id("CRM")
    users = client.get_dialog_users(dialog_id)

    client.send_individual_message(['me'], message)
    #client.send_message_to_participants(users, message)

    # t = client.get_dialog_users_from_file('target1.txt')
    # print(t)
    # client.get_dialog_users("https://t.me/mamapapa_chat", to_txt=True)
    # client.get_dialog_users("https://t.me/stroginomam_chat1", to_txt=True)
    # client.save_dialog_users_to_file(client.get_dialog_users(client.get_dialog_id("CRM")))
    # crm_users = client.get_dialog_users(client.get_dialog_id("CRM"))
    # client.send_message_to_participants("514730215", message)

    # client.send_individual_message([client.get_dialog_id("CRM")], message)
    # client.send_message_to_participants(client.get_dialog_users(client.get_dialog_id("CRM")), message)
