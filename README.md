# vpoc
Virtual Pack of Cards

# Guidelines

* A pack of cards belong to an user.
* A pack of cards can be created from a standar set of cards or to demand.
* In a game all participants can operate over a pack of cards.
* There are public operations and private operations over the pack of cards.

# Api resources tree

/api
    /users
        POST: Sign-in a new user.
    /users/login
        POST: Create a new user space to create o participate in a game.
    /users/logoff
        POST: Destroy an user space.
    /packofcards
        GET: Enquire the list of cards into a pack.
        POST: Create a pack of Cards form a list of cards.
    /packofcards/createspainx50
        POST: Create a standar Spain pack of 50 cards.
    /packofcards/createspainx40
        POST: Create a standar Spain pack of 40 cards (without eights, nines or jokers).
    /packofcards/createpoker
        POST: Create a standar poker pack of cards.



