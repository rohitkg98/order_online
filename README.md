+App flow:-
 LoginApp:
    ->SignUp:
        ->Restaurant
        ->Client
    ->Login:
        ->Redirect to Order Portal if Client
        ->Redirect to Restaurant Portal if Restaurant
    ->InvalidLogin:
        ->Keep retrying
 Order Portal:
    ->Select Restaurant:
        ->Select Items:
            ->Finalize Order:
                ->Payment
    ->View Orders   #yet to implement
 Restaurant Portal:
    ->Add Item
    ->View Items    #yet to implement

+Models in Apps:-
 Login:
    Client extends User
    Restaurant extends User
 Order:
    Order
 Restaurant:
    Items

