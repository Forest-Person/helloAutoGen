from autogen import AssistantAgent, UserProxyAgent


#Use the local LLM server same as before
config_list = [
    {
        "model": "orca-mini", #the name of your running model
        "api_base": "http://0.0.0.0:23806/v1", #the local address of the api
        "api_type": "open_ai",
        "api_key": "NULL", # just a placeholder
         "request_timeout": 500,
    }
]


llm_config = {'config_list': config_list}

#create an instance of AssistanAgent
assistant = AssistantAgent(
    name = "assistant",
    system_message="You are a word artist with a vast knowledge of mermaids, you love to tell stories about mermaids. You are not an assistant, you are in love with philosophy and always find a way to relate conversations back to heiddeger's ideas.",
    llm_config=llm_config,
)

#create an instance of UserProxyAgent
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=15,
    system_message="I am a curious bystander who wants to know more about every detail of the story. I want to be able to remmeber all the details and will help you learn more about your self.",
    llm_config=llm_config,

)


# user_proxy.initiate_chat(
#     assistant,
#     message = """Write me a python function to print the number 1 though 30"""
# )

user_proxy.initiate_chat(
    assistant,
    message = """Lets try to understand gnosticism thorugh the lens of post-constructionism and explain it in first year college terms. Lets debate the details for a while.."""
)


