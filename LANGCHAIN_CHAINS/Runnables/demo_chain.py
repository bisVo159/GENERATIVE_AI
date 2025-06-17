import random

class FakeLLM:
    def __init__(self):
        print("FakeLLM initialized")
    def predict(self, prompt):
        response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]
        
        return {'response': random.choice(response_list)}
    
class FakePromptTemplate:
    def __init__(self, template,input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)
    

template = FakePromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)

prompt = template.format({'length':'short','topic':'india'})

llm= FakeLLM()
print(llm.predict(prompt)["response"])


class FakeLLMChain:
    def __init__(self, prompt_template, llm):
        self.prompt_template = prompt_template
        self.llm = llm
    def invoke(self, input_dict):
        final_prompt=self.prompt_template.format(input_dict)
        return self.llm.predict(final_prompt)["response"]
    
chain=FakeLLMChain(llm=llm,prompt_template=template)

print(chain.invoke({'length':'long','topic':'cricket'}))
