from langchain.callbacks.base import BaseCallbackHandler
from pyboxen import boxen


def boxen_print(*args, **kwargs):
    print(boxen(*args, **kwargs))


colors = {
    "system": "yellow",
    "human": "green",
    "function_call": "cyan",
    "ai": "blue",
    "function": "purple",


}


class ChatModelStartHandler(BaseCallbackHandler):
    def on_chat_model_start(
        self,
        serialized,
        messages,
        **kwargs,
    ):
        print("\n\n ~~~~~~~~~~ Sending messages ~~~~~~~~~~\n\n")
        for message in messages[0]:
            if message.type == "ai" and "function_call" in message.additional_kwargs:
                call = message.additional_kwargs["function_call"]
                boxen_print(f"Running tool {call['name']} with args {call['arguments']}",
                            title=message.type,
                            color=colors["function_call"]
                            )
            else:
                boxen_print(message.content, title=message.type, color=colors[message.type])
