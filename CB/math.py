import speech_handler as sphnd
while True:
     request = input("Enter what you want to do: ")

     if request == 'quit':
          break
     
     request = request.split(' ')

     i = 0

     request_d = {}

     for req in request:
          request_d[i] = req
          i = i+1

     try:
         
      for key, value in request_d.items():
               if '+' in value:
                    position = value.index('+')
                    if len(value) == 1:
                         print(" Result for " + str(request_d[key -1]) + " " + str(request_d[key]) + " " + str(request_d[key + 1]) + " is " + str(int(request_d[key-1]) + int(request_d[key + 1])) + ".") 
                    else:
                         if value[0] == '+':
                              print(" Result for " + str(request_d[key-1]) + " " + value + " is " + str(int(request_d[key-1]) + int(value[1:])) + ".")
                         elif value[len(value)-1] == '+':
                              print("Result for " + str(value) + " " + str(request_d[key+1]) + " is " + str(int(value[:len(value)-1]) + int(request_d[key+1])) + ".")
                         else:
                              print("Result for " + str(value) + "  is " + str( int(value[0:position]) + int((value[position+1:]))) + ".")

                  
               elif '-' in value:
                    position = value.index('-')
                    if len(value) == 1:
                        print(" Result for " + str(request_d[key -1]) + " " + str(request_d[key]) + " " + str(request_d[key + 1]) + " is " + str(int(request_d[key-1]) - int(request_d[key + 1])) + ".") 
                    else:
                         if value[0] == '-':
                              print(" Result for " + str(request_d[key-1]) + " " + value + " is " + str(int(request_d[key-1]) - int(value[1:])) + ".")
                         elif value[len(value)-1] == '-':
                              print("Result for " + str(value) + " " + str(request_d[key+1]) + " is " + str(int(value[:len(value)-1]) - int(request_d[key+1])) + ".")
                         else:
                              print("Result for " + str(value) + "  is " + str( int(value[0:position]) - int(value[position+1:])) + ".")

               elif '*' in value:
                    position = value.index('*')
                    if len(value) == 1:
                        print(" Result for " + str(request_d[key -1]) + " " + str(request_d[key]) + " " + str(request_d[key + 1]) + " is " + str(int(request_d[key-1]) * int(request_d[key + 1])) + ".") 
                    else:
                         if value[0] == '*':
                              print(" Result for " + str(request_d[key-1]) + " " + value + " is " + str(int(request_d[key-1]) * int(value[1:])) + ".")
                         elif value[len(value)-1] == '*':
                              print("Result for " + str(value) + " " + str(request_d[key+1]) + " is " + str(int(value[:len(value)-1]) * int(request_d[key+1])) + ".")
                         else:
                              print("Result for " + str(value) + "  is " + str( int(value[0:position]) * int(value[position+1:])) + ".")
                   

               if '/' in value:
                    position = value.index('/')
                    if len(value) == 1:
                        print(" Result for " + str(request_d[key -1]) + " " + str(request_d[key]) + " " + str(request_d[key + 1]) + " is " + str(int(request_d[key-1]) / int(request_d[key + 1])) + ".") 
                    else:
                         if value[0] == '/':
                              print(" Result for " + str(request_d[key-1]) + " " + value + " is " + str(int(request_d[key-1]) / int(value[1:])) + ".")
                         elif value[len(value)-1] == '/':
                              print("Result for " + str(value) + " " + str(request_d[key+1]) + " is " + str(int(value[:len(value)-1]) / int(request_d[key+1])) + ".")
                         else:
                              print("Result for " + str(value) + "  is " + str( int(value[0:position]) / int(value[position+1:])) + ".")
                        
     except:
          print("Sorry, worng input.")
