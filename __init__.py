from mycroft import MycroftSkill, intent_file_handler


class Raspunsuri(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('raspunsuri.intent')
    def handle_raspunsuri(self, message):
        persoana = message.data.get('persoana')

        self.speak_dialog('raspunsuri', data={
            'persoana': persoana
        })


def create_skill():
    return Raspunsuri()

