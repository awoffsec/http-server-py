import argparse
from server.server import StartServer

def main(args):
    err = StartServer(args)
    print(err)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int)
    args = parser.parse_args()
    main(args)
