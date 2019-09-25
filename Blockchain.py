import hashlib
import time
from datetime import datetime

class BlockChain():

    def __init__(self):

        self.genesisblock = self._create_gen_block()
        self.tail = None

    def _create_gen_block(self):
        print("Creating A New Block")
        return Block(time.time(), '', None)

    def add_block(self, data):

        if len(data) == 0:
            print("Can't create a block with no data \n")
        else:

            if self.tail:

                new_block = Block(time.time(), data, self.tail.hash)
                self.tail = new_block

            else:
                new_block = Block(time.time(), data, self.genesisblock.hash)
                self.tail = new_block

    def get_recent_block(self):
        if self.tail is None:
            return "Blockchain is empty \n"
        else:
            return "---Block--- \n Data: {}, \n Hash: {},\n Previous Hash: {},\n Date: {}".format(self.tail.data,
                                                                                     self.tail.hash,
                                                                                     self.tail.previous_hash,
                                                                                     datetime.fromtimestamp(self.tail.timestamp))


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def get_previous(self):
        return self

    def calc_hash(self):

        sha = hashlib.sha256()

        if self.previous_hash is not None:
            concat_string = self.data + str(self.timestamp) + self.previous_hash
            sha.update(concat_string.encode('utf-8'))
        else:
            concat_string = self.data + str(self.timestamp)
            sha.update(concat_string.encode('utf-8'))
        return sha.hexdigest()


if __name__ == '__main__':

    new_chain = BlockChain()
    print(new_chain.get_recent_block())

    new_chain.add_block("This is the block that comes after the gen block")
    newest = new_chain.get_recent_block()
    print(newest)
    print("\n")
    new_chain.add_block("I am also a block")
    newest = new_chain.get_recent_block()
    print(newest)
    print("\n")
    new_chain.add_block("So am I!")
    newest = new_chain.get_recent_block()
    print(newest)
    print("\n")
    new_chain.add_block("I'm the last block and the tail node")
    newest = new_chain.get_recent_block()
    print(newest)
    print("\n")
    print("Adding 0 length block")
    new_chain.add_block("")
    newest = new_chain.get_recent_block()
    print(newest)
    print("\n")
    print("Making a new empty blockchain")
    empty_chain = BlockChain()
    print(empty_chain.get_recent_block())