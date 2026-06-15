# v2.5 Final Complete Version
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class InteractionHub(gl.Contract):
    interactions: TreeMap[Address, u256]
    scores: TreeMap[Address, u256]        # Reputation
    balances: TreeMap[Address, u256]      # Token

    def __init__(self):
        pass

    @gl.public.write
    def record_interaction(self) -> None:
        user = gl.message.sender_address

        # Record interaction
        current_int = self.interactions.get(user, u256(0))
        self.interactions[user] = current_int + u256(1)

        # Increase Reputation
        current_score = self.scores.get(user, u256(0))
        self.scores[user] = current_score + u256(10)

        # Mint Token
        current_balance = self.balances.get(user, u256(0))
        self.balances[user] = current_balance + u256(5)

    @gl.public.view
    def my_interactions(self) -> u256:
        user = gl.message.sender_address
        return self.interactions.get(user, u256(0))

    @gl.public.view
    def my_score(self) -> u256:
        user = gl.message.sender_address
        return self.scores.get(user, u256(0))

    @gl.public.view
    def my_balance(self) -> u256:
        user = gl.message.sender_address
        return self.balances.get(user, u256(0))
