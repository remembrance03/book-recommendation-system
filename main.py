from src.services.recommendation import recommend_books

###
#executing...
###
while True:
    print("write \"exit\" if u do not want any recommendations")
    print("\n")
    query = input("what kind of books do you want to read?")
    recommendations = recommend_books(query) #passes the query and fetches recommended books
    if query.lower() == "exit":
        break
      
    print("---------------------------------------------------------------")
    print("\nthese are some books you might enjoy reading :) \n")
    for result in recommendations:
        print ("-", result,"\n")
        
    print("happy reading!!!")
    print("-----------------------------------------------------------------")
