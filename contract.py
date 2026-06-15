# Interaction Hub v2.0
# Central Connected Hub for SocialFi Ecosystem

from genlayer import *

class InteractionHub(gl.Contract):
    interactions: TreeMap[Address, u256]
    
    reputation_address: Address
    token_address: Address

    def __init__(self, reputation_addr: Address, token_addr: Address):
        self.reputation_address = reputation_addr
        self.token_address = token_addr

    @gl.public.write
    def record_interaction(self) -> None:
        """Record interaction and automatically distribute rewards"""
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
        """Get my interaction count"""
        return self.interactions.get(gl.message.sender_address, u256(0))
