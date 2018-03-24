+App flow:-


1.LoginApp:


    1.SignUp:
    
    
        * Restaurant
        
        
        * Client
        
        
    2.Login:
    
    
        * Redirect to Order Portal if Client
        * Redirect to Restaurant Portal if Restaurant
    3.InvalidLogin:
        * Link to login page
2.Order Portal:
    1.Select Restaurant:
        * Select Items:
            * Finalize Order:
                * Payment
    * View Orders   #yet to implement
3.Restaurant Portal:
    * Add Item
    * View Items    #yet to implement

+Models in Apps:-
 1.Login:
    * Client extends User
    * Restaurant extends User
 2.Order:
    * Order
 3.Restaurant:
    * Items

