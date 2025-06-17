from abc import ABC, abstractmethod
import random

class Runnable(ABC):
    @abstractmethod
    def invoke(self, input_data):
        pass

class FakeLLM(Runnable):
    def __init__(self):
        print("FakeLLM initialized")
    def invoke(self, prompt):
        response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]
        return {'response': random.choice(response_list)}
    
    def predict(self, prompt):
        response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]
        
        return {'response': random.choice(response_list)}
    
class FakePromptTemplate(Runnable):
    def __init__(self, template,input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        return self.template.format(**input_dict)
    
    def format(self, input_dict):
        return self.template.format(**input_dict)
    
class FakeStrOutputParser(Runnable):
    def __init__(self):
        pass

    def invoke(self, input_data):
        return input_data.get('response', '')
    
class RunnableConnector(Runnable):
    def __init__(self, *runnables):
        self.runnables = runnables

    def invoke(self, input_data):
        for runnable in self.runnables:
            input_data = runnable.invoke(input_data)
        return input_data
    
# Example usage
template = FakePromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)   
llm = FakeLLM()
parser = FakeStrOutputParser()
chain = RunnableConnector(template, llm, parser)
input_data = {'length': 'short', 'topic': 'india'}  
response = chain.invoke(input_data)
print(response)  


template1 = FakePromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
template2 = FakePromptTemplate(
    template='Explain the following joke {response}',
    input_variables=['response']
)
chain1 = RunnableConnector(template1, llm)
chain2 = RunnableConnector(template2, llm, parser)
input_data1 = {'topic': 'cricket'}
final_chain = RunnableConnector(chain1, chain2)
print(final_chain.invoke(input_data1))



# runnables types
# 1. task specific -> These are core LC components that have been converted into runnables so that they can be used in pipelines
# Example: ChatOpenAi, PromptTemplate, OutputParser, etc.

# 2. primitive runnables -> These are fundamental building blocks for structuring execution logic in Ai wokflows.
# Example: RunnableLambda, RunnablePassthrough, RunnableParallel, RunnableSequence, etc.

