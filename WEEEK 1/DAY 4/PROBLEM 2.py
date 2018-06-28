dict1={}
class Trie(object):

   def add_word(self, word):
       global dict1
       current = dict1
       entry = False
       # print("----am current",current)
       for i in word:
           if i not in current:
               entry = True
               current.update({i:{}})
               # print(current)
           current= current[i]
           # print(current,"*************")
       if "End Of Word" not in current:
           entry = True
           current.update({"End Of Word":{}})

       return entry
