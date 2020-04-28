# vpoc
Virtual Pack of Cards

# Guidelines

* A pack of cards belong to an user.
* A pack of cards can be created from a standar set of cards or to demand.
* In a game all participants can operate over a pack of cards.
* There are public operations and private operations over the pack of cards.

# Implemented api resources tree

/api
    /v1
        /suits
            GET: List of all card suits.
        /suits/<id>
            POST: Create a new card suit.
            PUT: Update card suit information.
            DELETE: Erase a card suit.

# Next api resources tree

/api
    /v1
        /users
            GET: List of sign up users.
            POST: Sign-in a new user.
        /users/<id>
            PUT: Update Log in or log out user status.
            DELETE: Eliminate an existing user.
        /games
            GET: List of started games.
            POST: Create a new game.
        /games/<id>
            PUT: Update game information.
            DELETE: Finish a created game.
        /packofcards
            GET: Enquire the list of packs of cards.
            POST: Create a new pack of Cards.
        /packofcards/spain
            GET: List of cards into a pack of spain cards.
        /packofcards/spain40
            GET: List of cards into a pack of spain cards without eights, nines or jokers.
        /packofcards/poker
            GET: List of cards into a poker pack of cards.
        /cards
            GET: List of cards defined in api.
        /cards/<id>
            POST: Create a new card.
            PUT: Update card information.
            DELETE: Erase a card.

# Reference to global pack of cards

https://es.m.wikipedia.org/wiki/Palo_(naipes)


