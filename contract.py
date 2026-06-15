# v2.0
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class InteractionHub(gl.Contract):
    interactions: TreeMap[Address, u256]
    
    reputation_address: Address
    token_address: Address

    def __init__(self):
        # Hardcoded addresses for v2
        self.reputation_address = Address("0x77f86b0D8A0230BD612F41F9c638d682f6aBc476")
        self.token_address = Address("0x698c060E742D37E4742aEf4d790ba1543325C15b")

    @gl.public.write
    def record_interaction(self) -> None:
        user = gl.message.sender_address

        # Record interaction
        current = self.interactions.get(user, u256(0))
        self.interactions[user] = current + u256(1)

        # Auto reward Reputation
        try:
            rep = gl.contract(self.reputation_address)
            rep.record_action(u256(10))
        except:
            pass

        # Auto reward Token
        try:
            token = gl.contract(self.token_address)
            token.mint(u256(5))
        except:
            pass

    @gl.public.view
    def my_interactions(self) -> u256:
        user = gl.message.sender_address
        return self.interactions.get(user, u256(0))
