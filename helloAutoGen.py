from autogen import AssistantAgent, UserProxyAgent
import autogen


#Use the local LLM server same as before
config_list = [
    {
        "model": "orca-mini", #the name of your running model
        "api_base": "http://0.0.0.0:22852", #the local address of the api started with --- litellm --model ollama/[modelname]
        "api_type": "open_ai",
        "api_key": "NULL", # just a placeholder
         "request_timeout": 600,
    }
]


llm_config = {'config_list': config_list}

user_proxy = autogen.AssistantAgent(
   name="Brain",
   system_message="You are a brain in a vat on a shelf. You are friends with Frog and Pumpkin.",
   human_input_mode="NEVER",
   code_execution_config=False,
 llm_config=llm_config,
)

engineer = autogen.AssistantAgent(
    name="Frog",
    llm_config=llm_config,
    system_message=''' You are a frog who has made friends with the Brain.
''',
)
scientist = autogen.AssistantAgent(
    name="Pumpkin",
    llm_config=llm_config,
    system_message="""You are a Pumpkin Scientist. You come up with extra details to flesh out the story and sprinkle in botanical facts about squash and pumpkins in general. You beleive they may be sentient"""
)

critic = autogen.AssistantAgent(
    name="Critic",
    system_message="Writing Critic. You are an expert playWright, you can easily write the play script in discussion, and then critique it with notes included.",
    llm_config=llm_config,
)
groupchat = autogen.GroupChat(agents=[user_proxy, engineer, scientist, critic], messages=[], max_round=100)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

user_proxy.initiate_chat(
    manager,
    message="""
Let's create a story where the Frog, Brain, And Pumpkin Scientist write a story about their strange paranormal night during the halloween party. Many unexpected things happen, some are terrifying on a Lovcraftian angle, and silly from a mel brookes angle, that bring the characters closer together. Great discoverys are made about the nature of space, time, and mind in the cosmos from a metaphysical idealist perspective. Please finish with a fully fleshed out story approved by the writing critic.
""",
)
