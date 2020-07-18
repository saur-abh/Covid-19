
print("******************Information about  the Covid -19 Cases********************")
while True:      
    from covid import Covid
    covid=Covid(source="worldometers") 
    #covid=Covid()     
    print("What do You Want !!!!")    
    print("""
          Press 1 for "Get All Data."
          Press 2 for "List Countries."
          Press 3 for "Get Status By ID."
          Press 4 for "Get Status By Country Name."
          Press 5 for "Get Total Active Cases."
          Press 6 for "Get Total Confirmed Cases."
          Press 7 for "Get Total Recovered Cases."
          Press 8 for "Get Total Death Cases."
          """)
    take_input=(int(input(">>>>>   ")))       
    if (take_input==8):
         print("Total Death Cases is :", f'{covid.get_total_deaths():,}') 
    elif(take_input==7):
         print("Total Recovered Cases is :",f'{covid.get_total_recovered():,}')          
    elif(take_input==1):    
        print("Press 1' for Print all data")
        print("Press 2 for Print top 5 data")
        data_input=int(input(">>>>  "))
        if data_input==1:
            for item in covid.get_data():
                for key,value in item.items():
                    print(key,":",value)
        elif data_input==2:
             for item in covid.get_data()[:5]:
                 print("Top List")
                 for list1 in list(item.items())[1:6]:
                  print(list1)
    elif take_input==3:
        id_input=input("Enter country id:= >>>")
        for id in list(covid.get_status_by_country_id(id_input).items())[1:6]:
            print(id)        
    elif(take_input==4):
        country_name=input("Enter Country Name:= ")
        print(" Information about the ",country_name.upper()," Country Case.")
        for country in list(covid.get_status_by_country_name(country_name).items())[1:6]:
            print(country)        
    elif take_input == 2:
        print("Country List :>>>>")
        for country_list in covid.list_countries():
            print(country_list)
    elif(take_input==5):
        print("Total Active Cases around the World. !")
        print("Active Cases:= ",f'{covid.get_total_active_cases():,}')
    elif(take_input==6):
        print("Total Confirmed Cases around the World. !")
        print("Total Confirmed Cases is : ",f'{covid.get_total_confirmed_cases():,}')                       
    else:
        print("Choose Valid key !")
    ans=input("Do you want to Continue.! Press (Y) for Yes or (N) for No.").lower()
    while ans not in ('y','n'):
        print("Enter Valid Key !")
        ans=input("Do you want to Continue.! Press (Y) for Yes or (N) for No.").lower()
    if (ans =='n'):
        break      
print("################### Thanks for giving a Time.! ###################")    
        
        
        
        
    # =============================================================================
    # 
    # a_dictionary = {"name" : "John", "age" : 35, "height" : 65}
    # 
    # dict_items = a_dictionary.items()
    # 
    # first_two = list(dict_items)[:2]
    # print(first_two)
    # =============================================================================
    
    # =============================================================================
    # 
    # dict1=[{'id': '18', 'country': 'US', 'confirmed': 3432307, 'active': 2291468, 'deaths': 136463, 'recovered': 1049098, 'latitude': 40.0, 'longitude': -100.0, 'last_update': 1594820077000},
    #        {'id': '22', 'country': 'Brazil', 'confirmed': 1926824, 'active': 524156, 'deaths': 74133, 'recovered': 1328535, 'latitude': -14.235, 'longitude': -51.9253, 'last_update': 1594820077000},
    #        {'id': '27', 'country': 'India', 'confirmed': 936181, 'active': 319840, 'deaths': 24309, 'recovered': 592032, 'latitude': 20.593684, 'longitude': 78.96288, 'last_update': 1594820077000}, 
    #        {'id': '14', 'country': 'Russia', 'confirmed': 745197, 'active': 211069, 'deaths': 11753, 'recovered': 522375, 'latitude': 61.524, 'longitude': 105.3188, 'last_update': 1594820077000}, 
    #        {'id': '23', 'country': 'Peru', 'confirmed': 333867, 'active': 98377, 'deaths': 12229, 'recovered': 223261, 'latitude': -9.19, 'longitude': -75.0152, 'last_update': 1594820077000}]
    # 
    # 
    # 
    # d=dict1[:2]
    # 
    # 
    # 
    # =============================================================================
    # =============================================================================
    # 
    #     
    # 
    # 
    # 
    # country_cases=covid.get_status_by_country_name("india")
    # 
    # for key,value in country_cases.items():
    #     print(key,":",value)
    # print(country_cases)
    # 
    # print("Active Cases:= ",covid.get_total_active_cases())
    # 
    # print("Total Deaths:= ",covid.get_total_deaths())
    # 
    # print("Total Confirmed Cases:= ",covid.get_total_confirmed_cases())
    # =============================================================================




























