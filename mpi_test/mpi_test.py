from mpi4py import MPI


def hello_world():
    comm_world = MPI.COMM_WORLD
    rank = comm_world.Get_rank()
    print("hello world from process ", rank)


if __name__ == '__main__':
    hello_world()
