import openai

openai.api_key = '=========key========'


class chatbot():
    memory_size = 5
    gpt_standard_messages = [ {"role": "system", "content": "You are a helpful assistant. Your name is BTS. The structure of the conversation should be highly visible in the main points of the conversation / summary and examples (3 types) - to each explanation / concluding conclusion.]"} ]  
    
    
    def set_memory_size(self, memory_size ) :
        self.memory_size = memory_size
        
    
    def gpt_send_msg(self, question:str ) : 
        # 메시지 설정하기
        print( "사용자 : ", question )
        self.gpt_standard_messages.append( {"role": "user", "content": question} )

        # ChatGPT API 호출하기
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.gpt_standard_messages,
             temperature=0.8  # 원하는 temperature 값으로 설정 (기본값은 0.8)
        )
        
        print
        answer = response['choices'][0]['message']['content']
        self.gpt_standard_messages.append( {"role": "assistant", "content": answer}  )
        if self.memory_size*2 < len( self.gpt_standard_messages ): 
            self.gpt_standard_messages.pop(1)
            self.gpt_standard_messages.pop(1)
            
        print( "GPT : ", answer)