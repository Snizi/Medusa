import argparse


def parseArgs():

    parser = argparse.ArgumentParser()
    parser.add_argument('--domain', type=str, help="The domain that you want scan")
    parser.add_argument('--roots', type=str, help="A file containing all the root domains")
    parser.add_argument('--name', type=str, help="The name of the company that you're testing the assets")


    args = parser.parse_args()


    if args.domain:
        return args.name + '/', [args.domain]
    else:
        with open(args.roots, "r") as f:
            roots = [roots.strip("\n") for roots in f.readlines()]
            return args.name + '/', roots
            