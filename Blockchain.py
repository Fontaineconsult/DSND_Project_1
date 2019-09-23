import hashlib
import time


class BlockChain():

    def __init__(self):

        self.genesisblock = self._create_gen_block()
        self.tail = None

    def _create_gen_block(self):
        return Block(time.time(), '', None)

    def add_block(self, data):

        if self.tail:

            new_block = Block(time.time(), data, self.tail.hash)
            self.tail = new_block

        else:
            new_block = Block(time.time(), data, self.genesisblock.hash)
            self.tail = new_block

    def get_recent_block(self):
        return self.tail


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()


if __name__ == '__main__':

    new_chain = BlockChain()

    new_chain.add_block("This is the genesisblock")
    newest = new_chain.get_recent_block()
    print(newest.data, newest.hash, newest.previous_hash)
    print("\n")

    new_chain.add_block("This is the block that comes after the gen block, ")
    newest = new_chain.get_recent_block()
    print(newest.data, "My hash: ", newest.hash, "Previous Hash ", newest.previous_hash)
    print("\n")
    new_chain.add_block("I am also a block, ")
    newest = new_chain.get_recent_block()
    print(newest.data, "My hash: ", newest.hash, "Previous Hash ", newest.previous_hash)
    print("\n")
    new_chain.add_block("So am I!, ")
    newest = new_chain.get_recent_block()
    print(newest.data, "My hash: ", newest.hash, "Previous Hash ", newest.previous_hash)
    print("\n")
    new_chain.add_block("I'm the last block and the tail node., ")
    newest = new_chain.get_recent_block()
    print(newest.data, "My hash: ", newest.hash, "Previous Hash ", newest.previous_hash)
    print("\n")


