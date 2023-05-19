from mythic_container.MythicCommandBase import *
import json

class WhoamiArguments(TaskArguments):

    def __init__(self, command_line, **kwargs):
        super().__init__(command_line, **kwargs)
        self.args = []

    async def parse_arguments(self):
        if len(self.command_line) > 0:
            raise Exception("Exit takes no arguments.")

class WhoAmI(CommandBase):
    cmd = "whoami"
    needs_admin = False
    help_cmd = "whoami"
    description = "Get the username associated with your current process token"
    version = 1
    author = "@ThePurpleTux"
    argument_class = WhoamiArguments
    attackmapping = ["T1033"]


    async def create_go_tasking(self, taskData: PTTaskMessageAllData) -> PTTaskCreateTaskingMessageResponse:
        response = PTTaskCreateTaskingMessageResponse(
            TaskID=taskData.Task.ID,
            Success=True,
        )
        return response
    
    async def process_response(self, task: PTTaskMessageAllData, response: any) -> PTTaskProcessResponseMessageResponse:
        resp = PTTaskProcessResponseMessageResponse(TaskID=task.Task.ID, Success=True)
        return resp